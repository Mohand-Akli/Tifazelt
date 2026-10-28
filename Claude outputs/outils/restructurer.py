#!/usr/bin/env python3
"""Restructurer le vault : déplacer, renommer et découper des notes en réécrivant les liens.

Usage :
    python3 restructurer.py <vault> <operations.json>               essai : tout est appliqué sur une copie
                                                                    instantanée du vault (hors .git), audit compris,
                                                                    puis la copie est effacée ; le vault n'est pas touché
    python3 restructurer.py <vault> <operations.json> --appliquer   applique (avec git mv)
    ... --appliquer --sans-git                                     applique sans git (copie de test)

Fichier d'opérations (JSON) : une liste, appliquée dans l'ordre.
    {"op": "deplacer", "de": "chemin", "vers": "chemin"}          fichier ou dossier ; les liens par nom restent bons
    {"op": "renommer", "note": "chemin.md", "nom": "Nouveau nom", "dossier": "chemin (facultatif)"}
    {"op": "decouper", "note": "chemin.md",   (tags et alias des parties : seulement ceux donnés ici)
        "sommaire": {"nom": "...", "dossier": "...", "titre": "# ... (facultatif)"},
        "parties": [{"nom": "...", "dossier": "...", "sections": ["titre exact d'une section", ...],
                     "titre": "# ... (facultatif)", "alias": ["..."], "tags": ["..."]}]}
    {"op": "chemins", "de": "préfixe", "vers": "préfixe"}            chemins écrits en dur (`...`) et réglages
Les déplacements ajoutent d'eux-mêmes leur règle « chemins ».

Ce que fait l'outil :
- liens [[note]], [[note#section]], [[note|texte]], ![[...]] : réécrits vers le nouveau nom ou vers la note
  qui contient désormais la section ; un lien vers une note découpée mène à son sommaire ;
- ancien nom d'une note renommée ou découpée ajouté à ses alias ;
- chemins écrits entre accents graves (`...`) dans les notes (sauf plans archivés dans Terminés/)
  et chemins des réglages d'Obsidian (graphe, signets, exclusions, fichiers .base) ;
- contrôle « aucun texte perdu » : hors en-têtes, liens et marques de titre, chaque ligne d'origine
  doit se retrouver ; les lignes ajoutées sont listées.
"""
import os, re, sys, json, shutil, subprocess, unicodedata, collections

N = lambda s: unicodedata.normalize('NFC', s)
LIEN = re.compile(r'(!?)\[\[([^\]\|#]*)(#[^\]\|]*)?(\|[^\]]*)?\]\]')
TITRE = re.compile(r'^(#{1,6})\s+(.*?)\s*$')
CODE = re.compile(r'`([^`\n]+)`')
REGLAGES = ['.obsidian/graph.json', '.obsidian/bookmarks.json', '.obsidian/app.json']


def norm_titre(h):
    return N(re.sub(r'[\*\_`]', '', h)).strip().lower().rstrip('\\').strip()


def lire(p):
    return open(p, encoding='utf-8').read()


def separer_entete(t):
    m = re.match(r'^---\n(.*?)\n---\n?', t, re.S)
    if not m:
        return None, t
    return m.group(1), t[m.end():]


def entete_ajouter_alias(fm, noms):
    """Ajoute des alias à un en-tête YAML simple (listes « - x »)."""
    noms = [n for n in noms if n]
    if not noms:
        return fm
    lignes = (fm or '').split('\n') if fm else []
    if not any(l.startswith('aliases:') for l in lignes):
        lignes.append('aliases:')
    i = next(k for k, l in enumerate(lignes) if l.startswith('aliases:'))
    j = i + 1
    while j < len(lignes) and lignes[j].startswith('  - '):
        j += 1
    deja = {N(l[4:].strip().strip('"\'')) for l in lignes[i + 1:j]}
    ajout = ['  - ' + n for n in noms if N(n) not in deja]
    lignes[j:j] = ajout
    return '\n'.join(lignes)


def entete_retirer_alias(fm, noms):
    if not fm:
        return fm
    cibles = {N(n).lower() for n in noms}
    return '\n'.join(l for l in fm.split('\n') if not (l.startswith('  - ') and N(l[4:].strip().strip('"\'')).lower() in cibles))


def assembler(fm, corps):
    corps = corps.lstrip('\n')
    return ('---\n' + fm + '\n---\n' if fm is not None else '') + corps.rstrip('\n') + '\n'


def sections(lignes):
    """Liste des titres : (indice, niveau, texte), hors blocs de code."""
    res, code = [], False
    for i, l in enumerate(lignes):
        if l.strip().startswith('```'):
            code = not code
            continue
        if code:
            continue
        m = TITRE.match(l)
        if m:
            res.append((i, len(m.group(1)), m.group(2)))
    return res


def bloc(lignes, titres, texte):
    """Indices [debut, fin) de la section dont le titre est `texte`."""
    trouve = [(i, n) for i, n, t in titres if norm_titre(t) == norm_titre(texte)]
    if len(trouve) != 1:
        raise SystemExit('section %r trouvée %d fois' % (texte, len(trouve)))
    i, n = trouve[0]
    fin = next((j for j, m, _ in titres if j > i and m <= n), len(lignes))
    return i, fin, n


def decaler_titres(lignes, de):
    out = []
    for l in lignes:
        m = TITRE.match(l)
        if m and de:
            niv = max(1, len(m.group(1)) - de)
            l = '#' * niv + ' ' + m.group(2)
        out.append(l)
    return out


def texte_normalise(t):
    """Pour le contrôle : sans en-tête, liens remplacés par un jeton, marques de titre retirées."""
    _, corps = separer_entete(t)
    out = []
    for l in corps.split('\n'):
        l = LIEN.sub('⟦lien⟧', l)
        if TITRE.match(l):
            l = re.sub(r'[\*\_`]', '', re.sub(r'^#{1,6}\s+', '', l))
        l = l.strip()
        if l and l != '---':
            out.append(l)
    return out


class Vault:
    def __init__(self, racine, avec_git):
        self.r = racine
        self.git = avec_git
        self.renommes = {}          # ancien nom -> nouveau nom
        self.decoupes = {}          # ancien nom -> (nom du sommaire, {titre normalisé: nom de la partie})
        self.prefixes = []          # (ancien, nouveau)
        self.ecrits = {}            # chemin relatif -> contenu (pour le contrôle)
        self.controles = []
        self.journal = []

    def p(self, rel):
        return os.path.join(self.r, rel)

    def notes(self):
        res = []
        for dp, dn, fn in os.walk(self.r):
            dn[:] = [d for d in dn if not d.startswith('.')]
            for f in fn:
                if f.endswith('.md'):
                    res.append(os.path.relpath(os.path.join(dp, f), self.r))
        return res

    def nom_existe(self, nom):
        return any(N(os.path.basename(n))[:-3] == N(nom) for n in self.notes())

    def bouger(self, de, vers, appliquer):
        assert os.path.exists(self.p(de)), ('absent', de)
        assert not os.path.exists(self.p(vers)), ('existe déjà', vers)
        if appliquer:
            os.makedirs(os.path.dirname(self.p(vers)) or self.r, exist_ok=True)
            suivi = self.git and subprocess.run(['git', '-C', self.r, 'ls-files', '--error-unmatch', de],
                                                capture_output=True).returncode == 0
            if suivi:
                subprocess.run(['git', '-C', self.r, 'mv', de, vers], check=True)
            else:
                os.rename(self.p(de), self.p(vers))

    # ---------- opérations ----------
    def deplacer(self, op, appliquer):
        self.bouger(op['de'], op['vers'], appliquer)
        self.prefixes.append((op['de'].rstrip('/'), op['vers'].rstrip('/')))
        self.journal.append('déplacé : %s -> %s' % (op['de'], op['vers']))

    def renommer(self, op, appliquer):
        de = op['note']
        ancien = os.path.basename(de)[:-3]
        dossier = op.get('dossier', os.path.dirname(de))
        vers = os.path.join(dossier, op['nom'] + '.md')
        if N(ancien) != N(op['nom']) and self.nom_existe(op['nom']):
            raise SystemExit('nom déjà pris : ' + op['nom'])
        self.bouger(de, vers, appliquer)
        if appliquer:
            fm, corps = separer_entete(lire(self.p(vers)))
            if N(ancien) != N(op['nom']):
                fm = entete_ajouter_alias(fm if fm is not None else '', [ancien])
            open(self.p(vers), 'w', encoding='utf-8').write(assembler(fm, corps))
        if N(ancien) != N(op['nom']):
            self.renommes[N(ancien)] = op['nom']
        self.prefixes.append((de, vers))
        self.journal.append('renommé : %s -> %s' % (de, vers))

    def decouper(self, op, appliquer):
        src = op['note']
        ancien = os.path.basename(src)[:-3]
        texte = lire(self.p(src))
        fm, corps = separer_entete(texte)
        lignes = corps.split('\n')
        titres = sections(lignes)
        pris = set()
        parties = []
        carte = {}
        tetes = set()
        for part in op['parties']:
            if self.nom_existe(part['nom']) and N(part['nom']) != N(ancien):
                raise SystemExit('nom déjà pris : ' + part['nom'])
            blocs = []
            for s in part['sections']:
                i, fin, niv = bloc(lignes, titres, s)
                if pris & set(range(i, fin)):
                    raise SystemExit('section prise deux fois : ' + s)
                pris |= set(range(i, fin))
                blocs.append((i, fin, niv))
                if len(part['sections']) == 1:
                    tetes.add(norm_titre(s))
                for j, _, t in titres:
                    if i <= j < fin:
                        carte[norm_titre(t)] = part['nom']
            parties.append((part, blocs))
        # internes : titre -> note qui le contient
        ou = {}
        for part, blocs in parties:
            for i, fin, _ in blocs:
                for j, _, t in titres:
                    if i <= j < fin:
                        ou[norm_titre(t)] = part['nom']
        nom_som = op['sommaire']['nom']
        for _, _, t in titres:
            ou.setdefault(norm_titre(t), nom_som)

        def liens_internes(l, ici):
            def f(m):
                if m.group(2).strip() == '' and m.group(3):
                    h = norm_titre(m.group(3)[1:])
                    cible = ou.get(h, ici)
                    if cible != ici and h in tetes:
                        return '%s[[%s%s]]' % (m.group(1), cible, m.group(4) or '')
                    if cible != ici:
                        return '%s[[%s%s%s]]' % (m.group(1), cible, m.group(3), m.group(4) or '')
                return m.group(0)
            return LIEN.sub(f, l)

        sorties = {}
        remplaces = []
        for part, blocs in parties:
            contenu = []
            if len(blocs) == 1:
                i, fin, niv = blocs[0]
                contenu = decaler_titres(lignes[i:fin], niv - 1)
                if part.get('titre'):
                    remplaces.append(texte_normalise(lignes[i])[0])
                    contenu[0] = part['titre']
            else:
                contenu = [part.get('titre') or '# ' + part['nom'], '']
                for k, (i, fin, niv) in enumerate(blocs):
                    if k:
                        contenu.append('')
                    contenu += decaler_titres(lignes[i:fin], niv - 2)
            contenu = [liens_internes(l, part['nom']) for l in contenu]
            while contenu and contenu[-1].strip() in ('', '---'):
                contenu.pop()
            tags = ['  - ' + x for x in part.get('tags', [])]
            pfm = 'tags:\n' + '\n'.join(tags) if tags else ''
            if part.get('alias'):
                pfm = entete_ajouter_alias(pfm, part['alias'])
            rel = os.path.join(part['dossier'], part['nom'] + '.md')
            sorties[rel] = assembler(pfm if pfm else None, '\n'.join(contenu))
        reste = [l for k, l in enumerate(lignes) if k not in pris]
        while reste and reste[-1].strip() in ('', '---'):
            reste.pop()
        if op['sommaire'].get('titre'):
            remplaces += [texte_normalise(l)[0] for l in reste if l.startswith('# ')]
            reste = [l for l in reste if not l.startswith('# ')]
            reste = [op['sommaire']['titre'], ''] + reste
        elif not any(l.startswith('# ') for l in reste):
            reste = ['# ' + nom_som, ''] + reste
        reste += ['', '## Notes', ''] + ['- [[%s]]' % part['nom'] for part, _ in parties]
        reste = [liens_internes(l, nom_som) for l in reste]
        reste = [l for k, l in enumerate(reste) if not (l.strip() == '' and k and reste[k - 1].strip() == '')]
        sfm = entete_retirer_alias(fm, [a for part, _ in parties for a in part.get('alias', [])] + [p['nom'] for p, _ in parties])
        sfm = entete_retirer_alias(sfm, [nom_som])
        if N(ancien) != N(nom_som):
            sfm = entete_ajouter_alias(sfm if sfm is not None else '', [ancien])
        rel_som = os.path.join(op['sommaire']['dossier'], nom_som + '.md')
        # contrôle « aucun texte perdu »
        avant = collections.Counter(texte_normalise(texte))
        apres = collections.Counter()
        for t in list(sorties.values()) + [assembler(sfm, '\n'.join(reste))]:
            apres.update(texte_normalise(t))
        perdu = avant - apres - collections.Counter(remplaces)
        ajoute = apres - avant
        if remplaces:
            self.journal.append('  titres remplacés dans %s : %s' % (src, remplaces))
        self.controles.append((src, sum(perdu.values()), list(perdu)[:5], sorted(ajoute)))
        if appliquer:
            if os.path.normpath(rel_som) != os.path.normpath(src):
                self.bouger(src, rel_som, True)
            open(self.p(rel_som), 'w', encoding='utf-8').write(assembler(sfm, '\n'.join(reste)))
            for rel, t in sorties.items():
                assert not os.path.exists(self.p(rel)), ('existe déjà', rel)
                os.makedirs(os.path.dirname(self.p(rel)), exist_ok=True)
                open(self.p(rel), 'w', encoding='utf-8').write(t)
        self.decoupes[N(ancien)] = (nom_som, carte, tetes)
        self.prefixes.append((src, rel_som))
        self.journal.append('découpé : %s -> sommaire %s + %d notes' % (src, rel_som, len(sorties)))

    # ---------- réécritures ----------
    def reecrire_lien(self, m, compteur):
        bang, cible, ancre, alias = m.group(1), m.group(2), m.group(3) or '', m.group(4) or ''
        esc = ''
        if alias and (cible.endswith('\\') or ancre.endswith('\\')):
            esc = '\\'
            cible, ancre = cible.rstrip('\\'), ancre.rstrip('\\')
        nom = N(os.path.basename(cible.strip()))
        if not nom:
            return m.group(0)
        if nom in self.renommes:
            compteur[nom] += 1
            return '%s[[%s%s%s%s]]' % (bang, self.renommes[nom], ancre, esc, alias)
        if nom in self.decoupes:
            som, carte, tetes = self.decoupes[nom]
            compteur[nom] += 1
            if ancre:
                h = norm_titre(ancre[1:])
                part = carte.get(h)
                if part and h in tetes:
                    # la section est devenue la note entière : lien sans ancre
                    return '%s[[%s%s%s]]' % (bang, part, esc, alias)
                if part:
                    return '%s[[%s%s%s%s]]' % (bang, part, ancre, esc, alias)
                return '%s[[%s%s%s%s]]' % (bang, som, ancre, esc, alias)
            return '%s[[%s%s%s]]' % (bang, som, esc, alias)
        return m.group(0)

    def reecrire_chemin(self, s):
        for de, vers in sorted(self.prefixes, key=lambda x: -len(x[0])):
            if s == de or s.startswith(de + '/'):
                return vers + s[len(de):]
        return s

    def reecrire_tout(self, appliquer):
        compteur = collections.Counter()
        modifies = 0
        for rel in self.notes():
            t = lire(self.p(rel))
            n = LIEN.sub(lambda m: self.reecrire_lien(m, compteur), t)
            t_chemins = t
            if not any(x in N(rel) for x in ('/Terminés/', 'Restructuration du vault - plan')):
                n = CODE.sub(lambda m: '`' + self.reecrire_chemin(m.group(1)) + '`', n)
                t_chemins = CODE.sub(lambda m: '`' + self.reecrire_chemin(m.group(1)) + '`', t)
            if n != t:
                modifies += 1
                if texte_normalise(n) != texte_normalise(t_chemins):
                    self.controles.append((rel, 'texte changé hors liens', [], []))
                if appliquer:
                    open(self.p(rel), 'w', encoding='utf-8').write(n)
        reglages = [f for f in REGLAGES if os.path.exists(self.p(f))]
        for dp, dn, fn in os.walk(self.r):
            dn[:] = [d for d in dn if not d.startswith('.')]
            reglages += [os.path.relpath(os.path.join(dp, f), self.r) for f in fn if f.endswith('.base')]
        for rel in reglages:
            t = lire(self.p(rel))
            n = t
            for de, vers in sorted(self.prefixes, key=lambda x: -len(x[0])):
                for fin in ('"', '\\"', '/'):
                    n = n.replace('"' + de + fin, '"' + vers + fin)
            if n != t:
                self.journal.append('réglage mis à jour : ' + rel)
                if appliquer:
                    open(self.p(rel), 'w', encoding='utf-8').write(n)
        return compteur, modifies


def copie_instantanee(racine):
    import tempfile
    tmp = tempfile.mkdtemp(prefix='essai_vault_')
    for item in os.listdir(racine):
        if item == '.git':
            continue
        r = subprocess.run(['cp', '-cR', os.path.join(racine, item), tmp], capture_output=True)
        if r.returncode != 0:
            src = os.path.join(racine, item)
            (shutil.copytree if os.path.isdir(src) else shutil.copy2)(src, os.path.join(tmp, item))
    return tmp


def main():
    racine, fichier = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2])
    if '--appliquer' not in sys.argv:
        tmp = copie_instantanee(racine)
        print('ESSAI sur une copie : %s' % tmp)
        try:
            r = subprocess.run([sys.executable, os.path.abspath(__file__), tmp, fichier, '--appliquer', '--sans-git'])
            audit = os.path.join(tmp, 'Claude outputs', 'outils', 'audit.py')
            if not os.path.exists(audit):
                audit = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'audit.py')
            print('--- audit de la copie ---')
            sortie = subprocess.run([sys.executable, audit, tmp], capture_output=True, text=True).stdout
            print('\n'.join(l[:220] for l in sortie.split('\n') if not l.startswith('fiches') and not l.startswith('autres')))
        finally:
            if '--garder' not in sys.argv:
                shutil.rmtree(tmp)
        return
    appliquer = True
    v = Vault(racine, avec_git='--sans-git' not in sys.argv)
    ops = json.load(open(fichier, encoding='utf-8'))
    for op in ops:
        if op['op'] == 'deplacer':
            v.deplacer(op, appliquer)
        elif op['op'] == 'renommer':
            v.renommer(op, appliquer)
        elif op['op'] == 'decouper':
            v.decouper(op, appliquer)
        elif op['op'] == 'chemins':
            v.prefixes.append((op['de'].rstrip('/'), op['vers'].rstrip('/')))
        else:
            raise SystemExit('opération inconnue : ' + op['op'])
    compteur, modifies = v.reecrire_tout(appliquer)
    print('\n'.join(v.journal))
    print('liens réécrits : %d (%s)' % (sum(compteur.values()), ', '.join('%s : %d' % kv for kv in compteur.most_common())))
    print('notes dont les liens ou chemins changent : %d' % modifies)
    ok = True
    for src, perdu, ex, ajoute in v.controles:
        if perdu == 'texte changé hors liens':
            ok = False
            print('ALERTE texte changé hors liens :', src)
        elif perdu:
            ok = False
            print('ALERTE %s : %d ligne(s) perdue(s), ex. %s' % (src, perdu, ex))
        else:
            print('contrôle %s : aucun texte perdu ; lignes ajoutées : %s' % (src, ajoute))
    print('RÉSULTAT : appliqué |', 'contrôles OK' if ok else 'CONTRÔLES EN ÉCHEC')
    if not ok and appliquer:
        sys.exit(1)


if __name__ == '__main__':
    main()
