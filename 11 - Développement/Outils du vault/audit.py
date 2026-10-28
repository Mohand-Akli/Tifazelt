import os,re,sys,json,collections,unicodedata
# Audit du vault : python3 "11 - Développement/Outils du vault/audit.py" .
# Conflits git, notes vides, doublons de nom (notes et fichiers cités), liens et ancres cassés,
# liens écrits vers un alias (Obsidian ne les suit pas), notes sans lien entrant, chemins écrits en dur (`Claude outputs/...`, `GDD/...`, `assets/...`) introuvables
# (sauf dans les plans archivés de `Passation Cowork/Terminés/`, qui gardent volontairement leurs chemins d'origine).
root=sys.argv[1]
N=lambda s: unicodedata.normalize('NFC',s)
files=[]
for dp,dn,fn in os.walk(root):
    dn[:]=[d for d in dn if not d.startswith('.')]
    for f in fn:
        if f.startswith('.'): continue
        files.append(os.path.relpath(os.path.join(dp,f),root))
md=[f for f in files if f.endswith('.md')]
byname=collections.defaultdict(list)
for f in files:
    b=N(os.path.basename(f)); byname[b[:-3] if b.endswith('.md') else b].append(f); byname[b].append(f)
heads={}
alias={}
for f in md:
    t=open(os.path.join(root,f),encoding='utf-8',errors='replace').read()
    hs=set()
    for m in re.finditer(r'^#{1,6}\s+(.*?)\s*$',t,re.M):
        h=re.sub(r'[\*\_`]','',m.group(1)).strip(); hs.add(N(h).lower())
    heads[f]=hs
    fm=re.match(r'^---\n(.*?)\n---',t,re.S)
    if fm:
        for a in re.findall(r'^\s*-\s*(.+)$',fm.group(1).split('aliases:')[-1],re.M) if 'aliases:' in fm.group(1) else []:
            alias[N(a.strip().strip('"\''))]=f
link=re.compile(r'(!?)\[\[([^\]\|#]*)(#[^\]\|]*)?(\|[^\]]*)?\]\]')
chemin=re.compile(r'`((?:Claude outputs|GDD|assets)/[^`\n]*)`')
par_alias=collections.Counter(); broken=collections.Counter(); brokenh=collections.Counter(); inlinks=collections.Counter(); where=collections.defaultdict(set)
conflicts=[]; empty=[]; cites=set(); chemins_absents=[]
def existe(p):
    for q in (N(p),unicodedata.normalize('NFD',p)):
        full=os.path.join(root,q)
        if os.path.exists(full): return True
        d,b=os.path.split(full)
        if b and os.path.isdir(d) and any(N(x).startswith(N(b)) for x in os.listdir(d)): return True
    return False
for f in md:
    t=open(os.path.join(root,f),encoding='utf-8',errors='replace').read()
    if re.search(r'^(<<<<<<<|>>>>>>>|=======$)',t,re.M): conflicts.append(f)
    if len(t.strip())==0: empty.append(f)
    for m in link.finditer(t):
        tgt=N(m.group(2).strip()).rstrip('\\').strip(); h=m.group(3)  # « \| » dans un tableau
        if tgt=='' : tf=f
        else:
            base=os.path.basename(tgt)
            c=byname.get(base) or byname.get(base+'.md')
            if not c and tgt in alias:
                # Obsidian ne suit pas un lien écrit vers un alias : il faut viser le vrai nom de la note
                par_alias[tgt]+=1; where[('A',tgt)].add(f); c=[alias[tgt]]
            if not c: broken[tgt]+=1; where[tgt].add(f); continue
            tf=c[0]
            if not tf.endswith('.md'): cites.add(N(os.path.basename(tf)))
        inlinks[tf]+=1
        if h and tf.endswith('.md'):
            hh=N(re.sub(r'[\*\_`]','',h[1:])).strip().lower().rstrip("\\").strip()
            if hh.startswith('^'): continue
            if hh not in heads.get(tf,set()): brokenh[(tf,h[1:])]+=1; where[('H',tf,h[1:])].add(f)
    if '/Terminés/' in N(f): continue
    for m in chemin.finditer(t):
        p=m.group(1).strip().rstrip('.,;:')
        if any(x in p for x in ('<','*','…','...','AAAA','{')): continue
        if not existe(p): chemins_absents.append((f,p))
dups={k:sorted(set(v)) for k,v in byname.items() if len(set(v))>1 and not k.endswith('.md')}
notes_doublons={k:v for k,v in dups.items() if all(x.endswith('.md') for x in v)}
fichiers_cites_doublons={k:v for k,v in dups.items() if k in cites}
autres=len([k for k in dups if k not in notes_doublons and k not in fichiers_cites_doublons and '.' in k])
attaques=[f for f in md if '/8. Attaques/' in f]
print('notes md',len(md),'dont fiches d\'attaques',len(attaques))
print('conflits',conflicts); print('vides',empty)
print('doublons de nom (notes)',notes_doublons)
print('doublons de nom (fichiers cités dans les notes)',fichiers_cites_doublons)
print('autres fichiers au nom en double (copies de travail, non cités)',autres)
print('liens cassés',sum(broken.values()),'cibles',len(broken))
for k,v in broken.most_common(200): print('  ',v,k,'<-',sorted(where[k])[:4])
print('liens écrits vers un alias (non suivis par Obsidian)',sum(par_alias.values()))
for k,v in par_alias.most_common(200): print('  ',v,k,'->',alias[k].split('/')[-1],'<-',sorted(where[('A',k)])[:3])
print('ancres cassées',sum(brokenh.values()))
for (tf,h),v in brokenh.most_common(200): print('  ',v,tf.split('/')[-1],'#',h,'<-',sorted(where[('H',tf,h)])[:3])
orph=[f for f in md if inlinks[f]==0 and f not in attaques]
print('orphelins hors fiches d\'attaques',orph)
print('fiches d\'attaques sans lien entrant (lues par 8. Liste des attaques.base)',sum(1 for f in attaques if inlinks[f]==0))
print('chemins écrits en dur introuvables',len(chemins_absents))
for f,p in chemins_absents: print('  ',f,'->',p)
