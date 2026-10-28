# Restructuration du vault : plan en étapes

Demande de Mohand (28 oct. 2026), après le rangement : revoir la **structure globale** du vault (hiérarchie, noms des dossiers et des notes), découper les notes trop longues en petites notes, pour que Claude et Mohand naviguent facilement et retrouvent vite une information.

Pour reprendre dans une nouvelle conversation : « passons à l'étape N ».

**Plan validé par Mohand le 28 oct. 2026, avec toutes les recommandations (R1 à R9). Pour R2, la condition « Cowork » est à confirmer au début de l'étape 2.**

## Diagnostic (28 oct. 2026, lecture seule)
- **Trop de niveaux** : une ville est à 5 niveaux de profondeur (« GDD/02_Univers_et_Lore/4. Carte et Région d'Azzursal/01_Lumeridia/Villes/ »).
- **Numérotation incohérente** : quatre styles mélangés (`01_…`, `4. …`, `00. …`, `00_…`). Les numéros des notes (1. à 16.) viennent du document d'origine et ne suivent pas les dossiers (`8. Attaques` est dans `03`, `4. Carte…` dans `02`). Noms en anglais ou avec des tirets bas (`Game_Design_Core`), noms flous (`2. Economie Et Formules Et Reste`, `00. Définition`, « Claude outputs »).
- **Notes fourre-tout** :
  - `00. Définition` : 8 sujets ; ses propres alias les listent déjà (Types, Statuts, Statistiques, Brillants, Starters, Légendaires, Évolutions, Accouplement) ;
  - `3. Mécanique` : 8 sujets (raids, météo, bonheur, jour et nuit, énigmes, réactions, échanges, PvP) ;
  - `9. Capacités des Tifazelts` : 6 sujets ;
  - `6. Personnages` : 5 sujets (ses alias citent Zéphir, Professeur Arid, Team Glacitech) ;
  - `1. Menus Et Interfaces` : mélange des menus et des définitions d'objets (Médicaments, Tiflask… : 48 liens pointent vers ces sections) ;
  - `Animations, déplacements et audio` (2 354 mots), `Habillage des PNJ` (2 052), `Route 1 - Construction Roblox` (1 469).
- **Suivi dispersé** : ce qui reste à faire (« GDD/07_Production_Roblox/À décider et à faire/ ») et les plans (« Claude outputs/Passation Cowork/ ») sont à deux endroits sans rapport.
- **Images loin de leur usage** : la carte et les maquettes sont dans « assets/ ».
- **Outil** : `audit.py` accepte les liens écrits vers un alias, alors qu'Obsidian ne les résout pas (aucun lien de ce type aujourd'hui, vérifié). Les découpages devront réécrire les liens section par section (180 liens vers `10. Table des types`, 84 vers `00. Définition`, 54 vers `1. Menus Et Interfaces`) : il faut un outil qui le fasse et le vérifie.

## Arborescence visée (avec les recommandations)

```text
Accueil.md · Glossaire.md · CLAUDE.md · README.md · LICENSE
00 - Suivi/                    Suivi.md (sommaire)
    À décider et à faire/      À décider et à faire.md + ses 9 notes
    Plans/                     plans en cours ; Terminés/
01 - Règles du jeu/            Règles du jeu.md
    Combat/                    Combat.md · Table des types · Types élémentaires · Statuts · Statistiques · Coups critiques · Météo · Réactions élémentaires · Formules de combat
    En ligne/                  Échanges · PvP · Boss de raid
    Monnaies (TFD et PC) · Bonheur · Cycle jour et nuit · Énigmes
02 - Tifazelts/                Tifazelts.md
    Noms et lignées (propositions) · Starters · Légendaires · Brillants · Évolution · Reproduction · Talents · Natures · Courbes d'expérience · Surnoms
    Attaques/                  Attaques.md (système d'attaques) · Liste des attaques.base · les 283 fiches
03 - Monde/                    Monde.md
    Région d'Azzursal · Bâtiments communs
    Luméridia Est/             Luméridia Est.md · carte
        Villes/ (7) · Routes/ (6) · Lieux et reliefs/ (4)
04 - Histoire et personnages/  Histoire et personnages.md
    Trame principale · Quêtes de l'aventure · Team Glacitech
    Personnages/               Zéphir Célestin · Mère du joueur · Professeur Arid Acanthus
05 - Joueur et dresseurs/      Joueur et dresseurs.md
    Classes du joueur · Grades · Dresseurs (PNJ) · Sanctuaires et Ligue
06 - Objets/                   Objets.md
    Objets clés · Objets spéciaux · Objets uniques · Médicaments · Nourriture · Objets tenus · Tiflask · Livre de compétences
07 - Interface et menus/       Interface et menus.md
    Menus du jeu · Liste des écrans
08 - Direction artistique/     Direction artistique.md
    Charte graphique · Direction artistique des menus · Système de design (proposition) · Maquettes/
09 - Production Roblox/        Production Roblox.md
    Journal de construction · Systèmes de jeu · Secrets d'exploration
    Bourg-Azur - Construction/ (sommaire + 6) · Route 1 - Construction/ (sommaire + 3) · Interface - Construction/ (sommaire + 9)
    PNJ/ (Habillage des PNJ : règles, Bourg-Azur, Route 1 ; Animations des PNJ) · Joueur/ (animations, course, vélo, gestes) · Audio/ (Musiques · Sons de l'interface)
10 - Captures/                 Captures.md (sommaire, ex « Historique des captures ») · Jours/ · Images/
11 - Développement/            Développement.md (ex « Claude outputs », voir R2)
    Modèles 3D/ · Textures Roblox/ · Outils/ · Illustrations/ · Images de l'interface/ · Sauvegardes Roblox/ · Archives/
gemini-scribe/                 dossier du module Obsidian (laissé)
```

## Conventions (écrites ensuite dans `CLAUDE.md`)
- **Dossiers** : premier niveau numéroté sur deux chiffres (`03 - Monde`) pour un ordre fixe ; en dessous, noms simples en français, avec accents, sans numéro.
- **Notes** : le nom dit le sujet (« Starters », « Table des types », « Professeur Arid Acanthus »), en français, sans numéro ni emoji (les emojis restent dans les titres internes) ; chaque nom est unique dans tout le vault (Obsidian lie par nom). Une note = un sujet ; au-delà d'environ 1 000 mots ou de plusieurs sujets, on découpe.
- **Sommaires** : chaque dossier a une note-sommaire **à l'intérieur**, au nom du dossier sans numéro (`03 - Monde/Monde.md`, `Luméridia Est/Luméridia Est.md`) : ce qu'il contient, une ligne par note.
- **Liens** : toujours par nom de note, jamais par chemin ; les anciens noms deviennent des alias (utiles pour la recherche, mais un lien doit viser le vrai nom).
- **Propriété `type`** dans l'en-tête de chaque note (règle, tifazelt, attaque, lieu, personnage, objet, interface, direction-artistique, production, suivi, plan, capture, sommaire) : pour filtrer dans Obsidian (Bases) et pour Claude.

## Décisions à prendre par Mohand (avant l'étape 1)

| # | Question | Recommandation |
|---|---|---|
| R1 | Dossiers de premier niveau numérotés **à la racine** (le dossier « GDD/ » disparaît, son contenu est réparti dans `01` à `10`) ? | Oui |
| R2 | Renommer `Claude outputs` en `11 - Développement` et `Modeles 3D` en `Modèles 3D`. Cela demande de rendre **relatifs** les chemins de 6 fichiers `.blend` (Blender en arrière-plan, copie avant, chemins relus après) et de corriger 3 scripts du Dauphin. **À éviter** si Claude Cowork écrit encore par défaut dans un dossier « Claude outputs » (il le recréerait). | Oui, si tu n'utilises plus Cowork pour ce projet ; sinon garder `Claude outputs` |
| R3 | Un dossier `00 - Suivi` qui regroupe « À décider et à faire » et les plans (ex `Passation Cowork`, renommé `Plans`) ? | Oui |
| R4 | Noms de notes sans numéros (« Table des types » au lieu de « 10. Table des types »), anciens noms gardés en alias ? | Oui |
| R5 | Sommaire de chaque dossier à l'intérieur du dossier ; les sommaires déjà faits (Interface, Bourg-Azur, À décider, Captures) y passent aussi. En option, le module Obsidian « Folder notes » ouvre le sommaire quand on clique sur le dossier (à installer par toi). | Oui ; module à ton choix |
| R6 | Découpages de la liste ci-dessous. Restent entiers : `Table des types` (grille de référence), `Liste des écrans` (tableau de production), les fiches de villes, routes et lieux (un lieu = une note), `Bâtiments communs`, `Sanctuaires et Ligue`, `Dresseurs (PNJ)`, `Charte graphique`, les plans (journaux), et `Val Palmeraie` (gelé : déplacé avec les autres villes, contenu non touché). | Oui |
| R7 | Captures : notes du jour dans `10 - Captures/Jours/`, images dans `10 - Captures/Images/` (la règle de `CLAUDE.md` change). | Oui |
| R8 | Images de « assets/ » rangées près de leur usage : carte dans `03 - Monde/Luméridia Est/`, maquettes dans `08 - Direction artistique/Maquettes/` ; « assets/ » disparaît. | Oui |
| R9 | Propriété `type` dans chaque note et une note `Glossaire` à la racine (TFD, PC, EM, Tiflask, Tifalistre, Gardien, Ligue, starters…). | Oui |

## Découpages prévus (R6)
| Note actuelle | Devient |
|---|---|
| `00. Définition` | Types élémentaires, Statuts, Statistiques (dans `01 - Règles du jeu/Combat/`) ; Brillants, Starters, Légendaires, Évolution, Reproduction (dans `02 - Tifazelts/`) ; l'introduction va dans le sommaire `Tifazelts` |
| `3. Mécanique` | Boss de raid, Échanges, PvP (dans `En ligne/`) ; Météo, Réactions élémentaires (dans `Combat/`) ; Bonheur, Cycle jour et nuit, Énigmes |
| `2. Economie Et Formules Et Reste` | Monnaies (TFD et PC) ; Formules de combat (dans `Combat/`) |
| `9. Capacités des Tifazelts` | Talents, Natures, Courbes d'expérience, Surnoms (dans `02 - Tifazelts/`) ; Attaques (sommaire du dossier `Attaques/`) ; Coups critiques (dans `Combat/`) |
| `12. Joueur` | Classes du joueur, Grades |
| `6. Personnages` | Zéphir Célestin, Mère du joueur, Professeur Arid Acanthus, Team Glacitech, Trame principale |
| `14. Objets` | Objets clés, Objets spéciaux, Objets uniques |
| `1. Menus Et Interfaces` | Menus du jeu (menu principal, carte de dresseur, en ligne, quêtes, interfaces) ; Médicaments, Nourriture, Objets tenus, Tiflask, Livre de compétences (dans `06 - Objets/`) |
| `16. Direction Artistique des Menus` | Direction artistique des menus (§ 1 à 5) ; Système de design (proposition) (§ 6, proposition Claude à valider) |
| `Animations, déplacements et audio` | Animations des PNJ ; Joueur : animations, course, vélo et gestes ; Musiques ; Sons de l'interface ; « où trouver quoi » dans le sommaire |
| `Habillage des PNJ` | sommaire (règles, corrections, PROVISOIRE) ; Habillage - Bourg-Azur ; Habillage - Route 1 |
| `Route 1 - Construction Roblox` | sommaire (passes 2 à 6, tests, à faire) ; Route 1 - Forêt (Bosquet des Égarés) ; Route 1 - Plaine ouest |

Environ 55 nouvelles notes et 15 sommaires. Chaque lien vers une section est réécrit vers la note qui la contient désormais ; un lien vers une note découpée mène à son sommaire.

## Règles
- **Aucun texte perdu ni modifié** hors liens, titres de note et en-têtes : contrôle par script à chaque étape (le texte d'origine doit se retrouver ligne pour ligne).
- **Commit avant et après chaque étape** ; déplacements avec `git mv` ; copie complète d'avant le rangement toujours dans `~/Documents/Tifazelt - sauvegardes/`.
- **Audit sans erreur à la fin de chaque étape** : 0 lien cassé, 0 ancre cassée, 0 lien par alias, 0 nom en double, 0 chemin introuvable.
- **Obsidian fermé** pendant les étapes 2 à 7 (il réécrit ses réglages et suit les déplacements à sa façon) ; **aucune autre conversation** ne travaille dans le vault pendant ces étapes.
- **Roblox Studio non touché.** Val Palmeraie : déplacée avec les villes, contenu non touché.
- Les plans terminés gardent leurs chemins d'origine (journal) ; une ligne en tête dit où les choses sont maintenant.

## Étapes

| # | Étape | Modèle conseillé | Statut |
|---|---|---|---|
| 0 | Diagnostic et plan | Opus (décisions d'architecture) | Fait le 28 oct. 2026 |
| 1 | Outil `restructurer.py` : déplacer, renommer et découper des notes en réécrivant liens, sections, alias et chemins écrits en dur ; mode essai ; contrôle « aucun texte perdu ». `audit.py` : liens par alias signalés. Essai complet sur une copie du vault dans le dossier temporaire de Claude | Sonnet (Opus si l'essai révèle des cas difficiles) | Fait le 28 oct. 2026 |
| 2 | Arborescence de premier niveau (dossiers seulement, aucune note renommée) ; R2 si validé (chemins des `.blend` rendus relatifs, relus avant et après) ; Obsidian (graphe, exclusions, signets, `.base`), `CLAUDE.md`, mémoire de Claude, note pour les autres sessions | Sonnet | Fait le 28 oct. 2026 |
| 3 | Renommage des notes (R4) ; sommaires déjà faits déplacés dans leurs dossiers (R5) | Sonnet | À faire |
| 4 | Découpage des règles et des Tifazelts : `00. Définition`, `3. Mécanique`, `2. Economie…`, `9. Capacités…` | Sonnet | À faire |
| 5 | Découpage histoire, joueur, objets, menus, DA : `6. Personnages`, `12. Joueur`, `14. Objets`, `1. Menus Et Interfaces`, `16. Direction Artistique des Menus` | Sonnet | À faire |
| 6 | Découpage de la production : `Animations, déplacements et audio`, `Habillage des PNJ`, `Route 1 - Construction Roblox` | Sonnet | À faire |
| 7 | Sommaires de chaque dossier, `Glossaire`, propriété `type` (R9) ; `Accueil`, `README`, `CLAUDE.md` (« carte du vault » et conventions) | Sonnet (rédaction structurée) | À faire |
| 8 | Vérification finale (audit, texte identique, aucun fichier perdu, `.blend`) ; commit ; envoi sur GitHub si Mohand le veut ; Mohand ouvre Obsidian (Accueil, explorateur, graphe) | Haiku | À faire |

## Journal
- 28 oct. 2026 : diagnostic fait (lecture seule) et plan écrit. Les 12 commits du rangement sont sur GitHub (`f4ed403..0473975`) ; GitHub signale 3 `.blend` de plus de 50 Mo (taille conseillée, la limite est de 100 Mo). En attente de la validation de Mohand et des réponses R1 à R9.
- 28 oct. 2026 : plan validé par Mohand (« tout recommandé »).
- 28 oct. 2026 : étape 1 faite.
  - **`11 - Développement/Outils du vault/restructurer.py`** : lit une liste d'opérations JSON (`deplacer`, `renommer`, `decouper`, `chemins`) et réécrit tous les liens Obsidian (vers une note, vers une section, avec texte affiché, images intégrées, liens internes vers une section de la même note, forme avec barre oblique des tableaux), les alias (l'ancien nom devient un alias), les chemins écrits entre accents graves dans les notes (sauf plans archivés et ce plan, dont le diagnostic cite volontairement les anciens chemins) et les chemins des réglages d'Obsidian (graphe, signets, exclusions, fichiers `.base`). Un lien vers une section devenue une note entière vise la note sans ancre ; un lien vers une note découpée mène à son sommaire.
  - **Mode essai** (par défaut) : tout est appliqué sur une copie instantanée du vault (hors `.git`, sans espace disque en plus), l'audit est lancé sur la copie, puis la copie est effacée. `--appliquer` agit sur le vault avec `git mv`.
  - **Contrôle intégré** : pour chaque découpage, chaque ligne d'origine (hors en-tête, liens et marques de titre) doit se retrouver ; les titres remplacés et les lignes ajoutées sont listés ; pour chaque note dont seuls les liens ou chemins changent, le reste du texte doit être identique.
  - `audit.py` : signale les liens écrits vers un alias (Obsidian ne les suit pas ; aucun aujourd'hui) ; accepte la forme avec barre oblique des liens dans les tableaux.
  - **Essai** (sur la copie puis en mode essai sur le vrai vault) : 2 dossiers déplacés, `10. Table des types` renommée et déplacée, `00. Définition` découpée en 8 notes + sommaire, `1. Menus Et Interfaces` découpée en 5 notes + sommaire ; 318 liens réécrits dans 43 notes, graphe mis à jour ; contrôles OK, audit de la copie : 0 lien cassé, 0 ancre cassée, 0 lien par alias, 0 chemin introuvable. Défauts trouvés et corrigés pendant l'essai : ancres vers une section devenue une note entière (39), barre oblique des tableaux, tags hérités à tort par les nouvelles notes, alias resté sur le sommaire à cause d'une majuscule, séparateur `---` en fin de partie, lignes vides en double.
  - Le vrai vault n'a pas changé à cette étape (à part l'outil, l'audit et ce plan).
- 28 oct. 2026 : étape 2 faite (Mohand n'utilise plus Cowork : R2 appliqué ; demande de Mohand : renommer les gros dossiers et refaire le graphe).
  - **7 fichiers `.blend` passés en chemins relatifs** avant le renommage (Blender 5.2.3 en arrière-plan, `make_paths_relative`, enregistrés compressés) : plus aucun chemin absolu vers des textures. Après déplacement : 96 fichiers lus sur 107 trouvés ; les 11 absents sont ceux de `Dauphin/Sauvegardes/Sauvegarde_avant_rig/Lignee_Dauphin.blend`, déjà absents avant.
  - **473 déplacements** (`restructurer.py`, `git mv`) : la racine ne contient plus que `00 - Suivi` à `11 - Développement`, `Accueil.md`, `CLAUDE.md`, `README.md`, `LICENSE`. « GDD », « assets », « Claude outputs » et « gemini-scribe » ont disparu : contenu réparti selon l'arborescence visée ; `Passation Cowork` → `00 - Suivi/Plans` ; `outils` → `Outils du vault` (le nom « Outils » seul est impossible : il ne diffère que par la majuscule) ; `Modeles 3D` → `Modèles 3D` ; images des captures dans `10 - Captures/Images/`, notes du jour dans `10 - Captures/Jours/` ; carte dans `03 - Monde/Luméridia Est/`, maquettes dans `08 - Direction artistique/Maquettes/` ; Gemini Scribe dans `11 - Développement/Gemini Scribe` (réglage du module mis à jour).
  - Liens : aucun à réécrire (liens par nom) ; chemins écrits en dur réécrits dans 11 notes (dont `CLAUDE.md`) ; réglages d'Obsidian (signets, exclusions, fichier `.base`) mis à jour par l'outil. Scripts du Dauphin, détecteurs Bourg-Azur, `audit.py`, `restructurer.py`, mémoire de Claude : chemins corrigés.
  - **Graphe refait** : une couleur douce par dossier (16 groupes), fiches d'attaques et plans terminés masqués, images et tags masqués, réglages d'espacement revus ; légende de l'Accueil réécrite. `CLAUDE.md` : nouvelle « carte du vault ». README : arborescence à jour.
  - Pas encore fait (étapes 3 à 8) : noms des notes (numéros), sommaires dans les dossiers, découpages, glossaire, propriété `type`. Notes encore aux anciens noms : `00. Définition`, `10. Table des types`, etc.
  - Non vérifié dans Obsidian (fermé ou à relancer par Mohand).
- 28 oct. 2026 : Obsidian, ouvert pendant l'étape 2, avait réécrit le graphe avec ses anciens réglages (pièces jointes visibles : scripts, tenues, visages). Réglages réécrits Obsidian fermé (commit `e92d400`) ; `11 - Développement/` entièrement exclu d'Obsidian (graphe et recherche) ; le prompt de Garenbois, seule note de ce dossier, est passé dans `08 - Direction artistique/Illustrations/`. À vérifier par Mohand à la réouverture d'Obsidian. **Règle** : ne jamais modifier `.obsidian/` pendant qu'Obsidian tourne.
