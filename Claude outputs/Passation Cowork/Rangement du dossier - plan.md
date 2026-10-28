# Rangement du dossier : plan en étapes

Demande de Mohand (28 oct. 2026) : ranger tout le dossier `Tifazelt` (vault Obsidian et partie développement, modèles 3D compris) ; vérifier toutes les notes (liens cassés, doublons, contradictions, notes vides) ; découper les notes trop remplies en plusieurs notes rangées dans un dossier ; finir avec un vault complet, bien structuré, et une note d'index qui dit où se trouve chaque chose.

Pour reprendre dans une nouvelle conversation : « passons à l'étape N ».

**Plan validé par Mohand le 28 oct. 2026, avec toutes les recommandations (D1 à D8).**

## État des lieux (28 oct. 2026, lecture des fichiers, rien n'a été modifié)

### Tailles
| Dossier | Taille | Remarque |
|---|---|---|
| Total | 3,0 Go | dont `.git` 528 Mo |
| `Claude outputs/Modeles 3D/` | 2,3 Go | Cramosaur 1,1 Go (dont `V04/` 956 Mo), Dauphin 1,2 Go, Tiflask 9 Mo |
| `GDD/` | 121 Mo | dont `08_Captures/` 118 Mo (436 images) |
| `.obsidian/` | 14 Mo | modules Gemini Scribe, Importer, Git, Note Linker |
| `Roblox_Textures/` | 11 Mo | vêtements des PNJ, générateur, `test.png` |
| `src/` | 5,5 Mo | `Backup1.rbxl` (16 oct.) |
| `assets/` | 1,7 Mo | carte, maquettes d'interface ; `icons/` vide |

Fichiers de travail (rendus bruts, essais, variantes refusées) : **environ 1,16 Go**
- Dauphin : `Sprites/brut` 191 Mo, `brut45` 358 Mo, `brut_B_sat13` 98 Mo, `24_images_B_sat13` 31 Mo (saturation 1,3 refusée) ; `Rendus/var_A` à `var_D` 16 Mo, `var2_E` à `var2_G` 6 Mo, `sprites_test` 25 Mo.
- Cramosaur V04 : `Sprites/brut45` 379 Mo, `test45` 3 Mo, `test45b` 8 Mo, `45_images_essai_decentre` 28 Mo.
- Cramosaur (v03) : `Sprites/Version_brillante_abandonnee` 7 Mo, `Version_mate_contour_blender` 6 Mo.
- En plus : 6 fichiers `.blend1` (copies automatiques de Blender, 157 Mo) et 3 dossiers `Sauvegarde_*` (162 Mo).

### Git
- Dernier commit : 27 oct. 2026 à 00:50 (identique à GitHub). Depuis : 25 fichiers modifiés et **2 378 fichiers jamais suivis (2,0 Go)**, dont tout le dossier `Dauphin/`. Un déplacement de ces fichiers n'a aujourd'hui aucune copie de secours.
- `.tmp.driveupload/` : les 11 fichiers temporaires sont déjà effacés du disque ; l'effacement n'est pas encore enregistré dans git (ils restent récupérables dans l'historique).
- Suivis par erreur malgré `.gitignore` : 3 `.DS_Store`, `.obsidian/workspace.json`. Non ignorés : `__pycache__/`, `*.blend1`.

### Notes
- 346 notes : 63 notes de contenu et 283 fiches d'attaques (propriétés seules, c'est normal, lues par `8. Liste des attaques.base`).
- Audit (`audit.py`) : 0 conflit, 0 note vide, 0 lien cassé, 0 ancre cassée, aucun doublon de nom de note.
- Tous les liens Obsidian sont écrits par nom de note, jamais par chemin : une note déplacée garde ses liens tant que son nom reste unique.
- Notes jamais liées : les 11 plans de `Passation Cowork`, `Animations, déplacements et audio.md`, le prompt Garenbois.
- Notes les plus longues : `Historique des captures` (7 579 mots, 1 518 lignes, 436 images), `Interface (UI) - Construction Roblox` (5 584), `À décider et à faire` (4 687), `Bourg-Azur - Construction et Direction Artistique` (3 778), `Val Palmeraie` (2 419, gelée), `00. Définition` (1 557, huit sujets différents). Les plans de passation font 1 000 à 5 000 mots (ce sont des journaux, ils restent entiers).

### Problèmes relevés dans les notes
1. **Accueil** : la légende des couleurs du graphe ne correspond à rien (aucun groupe de couleurs dans `.obsidian/graph.json`, jamais enregistré dans git) ; les fiches d'attaques ne sont pas masquées du graphe comme annoncé. Manquent : `À décider et à faire`, `Habillage des PNJ`, `Historique des captures`, `Noms des Tifazelts (propositions)`, toute la partie `Claude outputs`.
2. **README** : l'arborescence date du 19 oct. (ni `Claude outputs`, ni `Roblox_Textures`, ni `08_Captures`).
3. **Historique des captures** : annonce « 372 captures du 15 au 20 oct. », il y en a 436 jusqu'au 28 oct. ; les sections du 26 au 28 oct. sont rangées sous le titre « 2026-10-20 ».
4. **CLAUDE.md** : « Chantier en cours (au 26 oct.) » est dépassé.
5. **Contradictions repérées** (échantillon ; relecture complète à l'étape 8) :
   - Starter : six notes de lore le font remettre au Laboratoire Arid de **Val Palmeraie** ; dans le jeu il est à **Bourg-Azur** (PROVISOIRE, Val Palmeraie gelé). À trancher par Mohand.
   - `Interface (UI) - Construction Roblox` cite encore Pyrofennec, Aqualune, Florépine, retirés le 26 oct.
   - `Noms des Tifazelts (propositions)` donne Cramosaur « Feu / Obscurité » au stade 1, puis dit plus bas que le double type n'arrive qu'à la forme finale.
   - Nombre de PNJ à vérifier : 24 à Bourg-Azur (note de construction), 25 (Habillage des PNJ), 68 (CLAUDE.md), 25 + 44 = 69 (Habillage).
6. **Recoupements** : quatre notes parlent des menus (`1. Menus Et Interfaces`, `Liste des Menus et Écrans`, `16. Direction Artistique des Menus`, `Interface (UI) - Construction Roblox`) ; les notes de lore `Bourg-Azur` et `Route 1` ont chacune une section « Construction Roblox » qui double les notes de production.

### Partie développement
- **Chemins absolus dans les fichiers Blender** (lus dans les fichiers, Blender non ouvert) :
  - `Cramosaur/V04/Lignee_Cramosaur_v04.blend` et `Rendu_Sprites_v04.blend` chargent `.../Modeles 3D/Cramosaur/V04/Textures/...` en chemin absolu.
  - `Dauphin/Rendu_Sprites_Dauphin.blend` charge `Cramosaur/V04/Lignee_Cramosaur_v04.blend` et les textures v04 (y compris `Textures/Variantes/`) en absolu, et ses propres textures en relatif (`//Textures/`).
  - `Dauphin/Lignee_Dauphin.blend` : textures en relatif (`//Textures/`).
  - Les anciens `.blend` Cramosaur (v03) pointent vers des fichiers temporaires déjà disparus (`/private/tmp/...`).
  - Conséquence : `Modeles 3D/`, `Cramosaur/V04/`, `Dauphin/` et leurs `Textures/` ne doivent pas changer de place ni de nom.
- Scripts : `Dauphin/Scripts/construire_rendu_sprites.py` (`RACINE`), `rendre_sprites.py` et `rendre_portraits.py` (`sys.path`) ont des chemins absolus vers `Modeles 3D/`. Les autres scripts reçoivent leurs dossiers en arguments.
- Racine de `Claude outputs` : 6 captures sans heure du 16 oct. (`1_vue_aerienne.jpg` à `6_fleuriste.jpg`), citées nulle part.
- `Cramosaur/` mélange les versions v01 à v03 (racine) et `V04/`.
- La partie développement est dispersée à la racine : `Roblox_Textures/`, `src/`, `Claude outputs/`. `gemini-scribe/` est le dossier de travail du module Gemini Scribe (vide).
- `assets/ui/Tableau des caracteres.png` n'est cité nulle part.

## Décisions à prendre par Mohand (avant l'étape 1)

| # | Question | Recommandation |
|---|---|---|
| D1 | Copie complète du dossier (environ 3 Go, 750 Go libres) **hors du vault**, dans `~/Documents/Tifazelt - sauvegardes/2026-10-28 avant rangement/` ? Hors du vault pour qu'Obsidian ne voie pas les notes en double. | Oui |
| D2 | Git et gros fichiers. **A** : ignorer `_Travail/`, `*.blend1`, `__pycache__/` et enregistrer le reste (estimé à 0,5 Go ; 0,92 Go en réalité, voir le journal) ; **B** : tout enregistrer (2 Go de plus, envoi sur GitHub lourd) ; **C** : n'enregistrer que notes et scripts. Aucun envoi sur GitHub sans ta demande. | A |
| D3 | Captures. **A** : les images restent à plat dans `GDD/08_Captures` (règle de CLAUDE.md inchangée), seule la note est découpée par jour ; **B** : un sous-dossier d'images par jour (règle de CLAUDE.md à changer). | A |
| D4 | Garder les noms `Claude outputs`, `Modeles 3D`, `Passation Cowork`, `V04` (chemins absolus dans les `.blend`, scripts, plans, mémoire de Claude) ? | Oui, garder |
| D5 | Regrouper toute la partie développement sous `Claude outputs` : `Roblox_Textures/` → `Claude outputs/Textures Roblox/`, `src/Backup1.rbxl` → `Claude outputs/Sauvegardes Roblox/`. `assets/` reste (images du GDD). `gemini-scribe/` : laisser, ou désactiver le module si tu ne t'en sers pas. | Oui ; laisser `gemini-scribe` |
| D6 | Découpage : les 4 grosses notes. Pour chacune, le sommaire garde **son nom et sa place** (aucun chemin ni lien à changer, CLAUDE.md compris) et les parties vont dans un dossier du même nom juste à côté. En option : `00. Définition` et `3. Mécanique`. Les plans de passation restent entiers. `Val Palmeraie` n'est pas touchée (gel). | Les 4 ; options à ton choix |
| D7 | Obsidian : recréer les couleurs du graphe décrites dans l'Accueil (ou retirer la légende) ; exclure `Claude outputs/Modeles 3D` de la recherche et du graphe (environ 2 300 images). | Recréer ; exclure |
| D8 | Cramosaur v01 à v03 : les ranger dans `Cramosaur/Anciennes versions (v01-v03)/` (le jeu utilise la v04, à confirmer). | Oui |

## Arborescence visée (avec les recommandations)

```text
Tifazelt/
├── Accueil.md                 index : où se trouve chaque chose (vault et développement)
├── CLAUDE.md · README.md · LICENSE
├── assets/                    images du GDD (carte, maquettes)
├── GDD/
│   ├── 01 à 06                (mêmes dossiers ; contenus relus à l'étape 8)
│   ├── 07_Production_Roblox/
│   │   ├── À décider et à faire.md        sommaire (même place)
│   │   ├── À décider et à faire/          décisions par thème, reste à faire, chantiers PROVISOIRES, points réglés
│   │   ├── Interface (UI) - Construction Roblox.md   sommaire
│   │   ├── Interface (UI) - Construction Roblox/     phases 0 à 7, pièges Roblox
│   │   ├── Bourg-Azur - Construction et Direction Artistique.md   sommaire
│   │   ├── Bourg-Azur - Construction et Direction Artistique/     DA, intérieurs, paysage, habitants, secrets, technique
│   │   ├── Animations, déplacements et audio.md   (venue de Claude outputs)
│   │   └── 00. Production Roblox, Route 1, Systèmes, Secrets, Habillage, Journal
│   └── 08_Captures/
│       ├── Historique des captures.md     sommaire : tableau par thème, une ligne par jour
│       ├── Historique des captures/       une note par jour (2026-10-15 à 2026-10-28)
│       └── *.jpg
└── Claude outputs/
    ├── Passation Cowork/      plans en cours ; Terminés/
    ├── outils/                audit.py, détecteurs Bourg-Azur, habillage_pnj.json
    ├── Illustrations Tifazelts/ · Interface/   (inchangés)
    ├── Modeles 3D/
    │   ├── Cramosaur/  V04/ (ne bouge pas : .blend et Textures) · Anciennes versions (v01-v03)/ · Scripts/ · _Travail/
    │   ├── Dauphin/    .blend et Textures ne bougent pas · Sauvegardes/ · _Travail/
    │   ├── Tiflask/
    │   └── identifiants_roblox_sprites_45_images.json
    ├── Textures Roblox/       (ex-Roblox_Textures)
    ├── Sauvegardes Roblox/    (ex-src)
    └── Archives/              captures sans heure du 16 oct., test.png
```

## Règles
- Rien n'est effacé : on déplace. Copie complète (D1) et commit git avant le premier déplacement. Fichiers suivis déplacés avec `git mv` (l'historique suit).
- Ne bougent pas : les `.blend` en service et leurs `Textures/` (`Cramosaur/V04/`, `Dauphin/`), `Claude outputs/outils/audit.py`, le dossier `Passation Cowork`, les sommaires des notes découpées.
- Roblox Studio n'est pas touché. `Val Palmeraie` (note et jeu) n'est pas touchée : ses contradictions sont seulement signalées.
- Contradictions : les erreurs de fait (dates, comptes, noms retirés) sont corrigées ; les choix de conception ne sont jamais tranchés à la place de Mohand, ils vont dans `À décider et à faire`.
- Obsidian fermé (ou laissé sans y écrire) pendant les étapes qui déplacent des fichiers (4 à 7, 9, 10), pour éviter un commit automatique au milieu.
- Chantiers ouverts en parallèle : `Lignée Dauphin` (étape 9) et `Bourg-Azur parfait` (étapes 6 et 7). Les étapes 6, 7 et 10 touchent leurs fichiers : à faire quand aucune conversation ne travaille sur ces chantiers.
- Ne jamais dire testé ce qui ne l'est pas : séparer « vérifié » et « non vérifié ».

## Étapes

| # | Étape | Modèle conseillé | Statut |
|---|---|---|---|
| 0 | État des lieux et plan | Opus (vue d'ensemble, décisions d'organisation) | Fait le 28 oct. 2026 |
| 1 | Sauvegarde complète hors du vault (D1), contrôle du nombre de fichiers et de la taille ; git : `.gitignore` (D2), retrait de git des `.DS_Store`, `workspace.json` et `.blend1`, commit « avant rangement » (sans envoi) | Haiku (mécanique) | Fait le 28 oct. 2026 (commit `8ce99bf`) |
| 2 | Petit nettoyage sans risque : ~~effacement de `.tmp.driveupload` enregistré~~ (fait à l'étape 1) ; `__pycache__` ; `assets/icons` vide ; 6 captures sans heure et `test.png` → `Claude outputs/Archives/` | Haiku (mécanique) | Fait le 28 oct. 2026 |
| 3 | Chemins de notes écrits en dur (`` `Claude outputs/Passation Cowork/...md` `` dans À décider, Habillage, Bourg-Azur, Noms des Tifazelts, plans) remplacés par des liens Obsidian, qui suivent les déplacements ; liste des chemins de fichiers (non-notes) à mettre à jour aux étapes 9 et 10 | Sonnet (remplacements par script, vérifiés) | Fait le 28 oct. 2026 |
| 4 | `Historique des captures` : une note par jour, sommaire corrigé (436 captures du 15 au 28 oct., tableau par thème recompté), sections mal datées remises au bon jour ; images selon D3 | Sonnet (découpage par script) | Fait le 28 oct. 2026 |
| 5 | `Interface (UI) - Construction Roblox` : sommaire + Phase 0 à Phase 7 + Pièges Roblox ; liens vers une section réécrits vers la bonne partie | Sonnet | Fait le 28 oct. 2026 |
| 6 | `Bourg-Azur - Construction et Direction Artistique` : sommaire + environ 6 parties (intention et DA, portes et intérieurs, corrections et missions, fontaine et paysage, habitants et secrets, technique et où trouver quoi) | Sonnet | Fait le 28 oct. 2026 |
| 7 | `À décider et à faire` : sommaire (point d'entrée de CLAUDE.md, même place) + décisions par thème, reste à faire, chantiers PROVISOIRES, points réglés (archive) | Opus (trier ce qui est réglé, dépassé ou encore ouvert) | Fait le 28 oct. 2026 |
| 8 | Relecture de fond des 63 notes de contenu : contradictions, doublons, informations dépassées ; corrections de fait ; liste des choix pour Mohand dans `À décider et à faire` ; découpages en option (D6) ; les sections « Construction Roblox » des notes de lore renvoient aux notes de production | Opus (lecture croisée d'environ 100 000 mots, jugement) | Fait le 28 oct. 2026 |
| 9 | Développement hors modèles 3D : plans terminés → `Passation Cowork/Terminés/` (statut vérifié avec Mohand) ; `Animations, déplacements et audio.md` → `07_Production_Roblox` ; `Roblox_Textures/` et `src/` selon D5 ; chemins mis à jour | Haiku (Sonnet si un chemin résiste) | Fait le 28 oct. 2026 |
| 10 | Modèles 3D : `_Travail/` (bruts, essais, variantes refusées), `Sauvegardes/`, `Anciennes versions (v01-v03)/` (D8) ; chemins des `.blend` relus avant et après (ils doivent être identiques) ; chemins des plans et scripts mis à jour | Sonnet (vérification des fichiers Blender) | Fait le 28 oct. 2026 |
| 11 | Index : `Accueil.md` réécrit (où se trouve chaque chose, vault et développement) ; graphe et fichiers exclus (D7) ; signets ; README (arborescence) ; CLAUDE.md (chantier en cours) ; mémoire de Claude si un chemin a changé | Sonnet (rédaction structurée) | Fait le 28 oct. 2026 |
| 12 | Vérification finale : audit (0 conflit, 0 note vide, 0 lien cassé) ; contrôle élargi (chaque lien et chaque image intégrée trouvés, noms uniques, chemins écrits en dur existants, fichiers lus par les `.blend` présents) ; `audit.py` allégé (il affiche aujourd'hui 265 Ko de doublons de fichiers 3D sans intérêt) ; commit ; Mohand ouvre Obsidian et regarde l'Accueil et le graphe | Haiku (Sonnet pour `audit.py`) | À faire |

## Chemins à mettre à jour aux étapes 9 à 11 (relevé de l'étape 3)
Seuls les chemins vers des dossiers ou fichiers qui vont bouger sont listés. Les plans terminés gardent leurs chemins tels quels (journal historique) ; on ajoute seulement une ligne qui renvoie au nouvel emplacement si nécessaire.

| Fichier qui cite le chemin | Chemin cité | Étape |
|---|---|---|
| `CLAUDE.md` | `Claude outputs/Passation Cowork/Vêtements PNJ et suite.md` (section « Chantier en cours ») | 11 |
| `GDD/07_Production_Roblox/00. Production Roblox.md` | `src/Backup1.rbxl` | 9 |
| `README.md` | `src/`, `assets/icons/`, arborescence entière | 11 |
| `Vêtements PNJ et suite.md` | `Roblox_Textures/Vetements_PNJ/` | 9 |
| `Starters - plan.md` | `Cramosaur/Rendu_Sprites.blend`, `Cramosaur/Rig/`, `Cramosaur/Sources/`, `Version_brillante_abandonnee`, `Version_mate_contour_blender` | 10 |
| `Portraits et Tiflask - plan.md` | `Cramosaur/Portraits/` | 10 |
| `Lignée Cramosaur v04 - plan.md` | `V04/Sauvegarde_avant_trous/` | 10 |
| `Lignée Dauphin - plan.md` | `Sauvegarde_avant_rig/`, `Sauvegarde_Dauphiracle_sans_texture/`, `brut_B_sat13/`, `24_images_B_sat13/`, `45_images_essai_decentre/` | 10 |
| `Dauphin/Scripts/construire_rendu_sprites.py`, `rendre_sprites.py`, `rendre_portraits.py` | chemins absolus vers `Modeles 3D/Cramosaur/V04/` et `Modeles 3D/Dauphin/` (ne bougent pas : rien à changer si D4 et D8 sont respectés) | 10 (contrôle) |

Les liens vers des notes (plans, `Animations, déplacements et audio`, `Noms des Tifazelts (propositions)`, etc.) sont maintenant des liens Obsidian : ils suivent les déplacements sans rien changer.

## Journal
- 28 oct. 2026 : état des lieux fait (lecture seule, aucun fichier déplacé ni modifié en dehors de ce plan). Plan écrit. En attente de la validation de Mohand et des réponses D1 à D8.
- 28 oct. 2026 : plan validé par Mohand avec toutes les recommandations (D1 à D8).
- 28 oct. 2026 : étape 1 faite.
  - Copie complète dans `~/Documents/Tifazelt - sauvegardes/2026-10-28 avant rangement/` (`.git` et `.obsidian` compris). Vérifiée : 6 854 fichiers et 409 dossiers des deux côtés, contenu identique (comparaison `rsync` par somme de contrôle).
  - `.gitignore` complété : `*.blend1`, `__pycache__/`, `.tmp.driveupload/`, `_Travail/`, et les dossiers de travail actuels des modèles 3D (`Sprites/brut*`, `test45*`, `45_images_essai_decentre`, `24_images_B_sat13`, `Rendus/var_*`, `var2_*`, `sprites_test`), à simplifier à l'étape 10 quand ils seront dans `_Travail/`.
  - Retirés de git (toujours sur le disque) : 3 `.DS_Store`, `.obsidian/workspace.json`, 4 `.blend1`. Les 18 fichiers `Version_brillante_abandonnee` et `Version_mate_contour_blender` (Cramosaur v03) restent suivis : à traiter à l'étape 10.
  - Commit `8ce99bf` « Avant rangement » : 689 fichiers ajoutés ou modifiés, **0,92 Go** (et non 0,5 Go comme estimé : sprites finaux, rigs, textures, `.blend` en service et dossiers `Sauvegarde_*` de V04 et du Dauphin). `.git` passe de 528 Mo à 1,2 Go. **Rien n'est envoyé sur GitHub** ; le prochain « commit-and-sync » d'obsidian-git enverra ce volume. Plus aucun fichier non suivi en dehors des fichiers ignorés.
- 28 oct. 2026 : étape 2 faite.
  - `Claude outputs/1_vue_aerienne.jpg` à `6_fleuriste.jpg` → `Claude outputs/Archives/Captures sans heure (16 oct. 2026)/` (noms inchangés, heure inconnue donc pas renommées selon la règle des captures).
  - `Roblox_Textures/test.png` → `Claude outputs/Archives/Roblox_Textures_test.png` (renommé pour garder son origine).
  - Déplacements faits avec `git mv` ; aucune note ni aucun script ne citait ces fichiers.
  - Effacés (présents dans la copie de sauvegarde, vérifiés à l'octet près) : `Dauphin/Scripts/__pycache__/` (cache Python recréé automatiquement) et le dossier vide `assets/icons/` (le README le cite encore : à corriger à l'étape 11).
- 28 oct. 2026 : étape 3 faite. 49 chemins de notes écrits en dur (entre accents graves) remplacés par des liens Obsidian dans 15 notes : 11 plans de passation et le prompt Garenbois, `À décider et à faire`, `Habillage des PNJ`, `Bourg-Azur - Construction et Direction Artistique`, `Noms des Tifazelts (propositions)`. Seul le chemin a changé (diff relu mot à mot : 49 lignes modifiées, rien d'autre). Non modifiés : `CLAUDE.md` (Claude a besoin des chemins) et ce plan. Audit : 0 lien cassé ; notes jamais liées : de 16 à 4 (README, CLAUDE.md, l'exemple Gemini Scribe, ce plan). Relevé des chemins de fichiers à mettre à jour : section ci-dessus.
- 28 oct. 2026 : étape 4 faite.
  - `GDD/08_Captures/Historique des captures.md` devient un sommaire (même nom, même place, mêmes alias) : mode d'emploi pour ajouter une capture, tableau par jour, tableau par thème recompté. Les 7 notes du jour sont dans `GDD/08_Captures/Historique des captures/` (`Captures 2026-10-15` à `Captures 2026-10-28`, liens jour précédent / suivant). Images non déplacées (D3-A).
  - Contrôle par script : 436 captures avant et après, chacune une seule fois, chacune dans la note de son vrai jour, légendes identiques ; les 436 images du dossier sont toutes citées.
  - Corrigé : 64 captures des 26, 27 et 28 oct. étaient rangées sous « 2026-10-20 » ; les 17 du 27 oct. n'avaient pas de section (glissées sous « Portraits et Tiflask (26 oct.) ») : nouvelle section « Cramosaur v04, Tifalistre, intro de combat et vélos » (titre de rangement, d'après le plan du 27 oct.) ; la date « 27 oct. 2026, » retirée de deux légendes (elle est dans le titre de la note). Le sommaire annonçait 372 captures du 15 au 20 oct. : 436 du 15 au 28 oct. Les comptes par thème jusqu'au 20 oct. retombent exactement sur l'ancien tableau (la refonte des intérieurs reste comptée avec « Bourg-Azur — intérieurs »).
  - `Interface (UI) - Construction Roblox` : les trois renvois « Captures de cette phase » pointent maintenant vers la bonne section de `Captures 2026-10-20`.
  - `CLAUDE.md` : règle des captures mise à jour (ajout dans la note du jour, puis tableaux du sommaire), pour que les autres conversations suivent la nouvelle organisation.
  - Audit : 0 conflit, 0 note vide, 0 lien cassé, 0 ancre cassée (354 notes).
- 28 oct. 2026 : étape 5 faite.
  - `GDD/07_Production_Roblox/Interface (UI) - Construction Roblox.md` devient un sommaire (même nom, même place, mêmes alias, même introduction) : où est le code, tableau des 9 parties avec leur contenu, liens vers les captures des 19 et 20 oct.
  - 9 notes dans le dossier `Interface (UI) - Construction Roblox/` : `Interface (UI) - Phase 0 - Fondations` à `Phase 7 - Mini-jeux et énigmes`, et `Interface (UI) - Pièges Roblox` (sorti de la phase 0, il vaut pour tous les écrans). Chaque note a des liens vers la phase précédente, le sommaire, la phase suivante et les pièges.
  - Contrôle par script : les 264 lignes de contenu se retrouvent toutes, dans le même ordre ; seuls les niveaux de titre (sous-sections en niveau 2) et les lignes de navigation changent. Le texte n'est pas corrigé ici (les noms de starters retirés, Pyrofennec etc., restent pour l'étape 8).
  - Aucun lien ne visait une section de cette note ; les 3 liens vers la note entière (Accueil, `Liste des Menus et Écrans`, `00. Production Roblox`) mènent au sommaire. Audit : 0 lien cassé, 0 ancre cassée, aucun doublon de nom (363 notes).
- 28 oct. 2026 : étape 6 faite (aucune conversation Claude Code ne tournait ; Mohand a donné son accord pour l'étape).
  - `GDD/07_Production_Roblox/Bourg-Azur - Construction et Direction Artistique.md` devient un sommaire (même nom, même place, mêmes alias, même introduction) : tableau des 6 notes avec leurs sections, et la section « 12. Où trouver quoi (Roblox Studio) », gardée ici parce que c'est la référence la plus consultée. Tag `roblox` en double retiré.
  - 6 notes dans le dossier `Bourg-Azur - Construction et Direction Artistique/` (numéros de section d'origine conservés) : `Bourg-Azur - Intention et direction artistique` (§ 1-2), `Portes et intérieurs` (§ 3 et 14), `Corrections et extensions` (§ 4 et 13), `Fontaine, paysage et mobilier` (§ 5-6), `Habitants et secrets` (§ 7-8), `Performance, tests et pistes` (§ 9-11). Liens précédent / sommaire / suivant.
  - Contrôle par script : les 201 lignes de contenu se retrouvent toutes, chaque section d'un seul tenant. Texte non corrigé (contradictions pour l'étape 8).
  - Liens réécrits : `Journal de construction de la carte` (lien vers le § 13 → `Bourg-Azur - Corrections et extensions`) ; renvoi « captures avant/après » du § 14 → section de `Captures 2026-10-20`. Les 5 autres liens vers la note entière mènent au sommaire. Audit : 0 lien cassé, 0 ancre cassée, aucun doublon de nom (369 notes).
- 28 oct. 2026 : étape 7 faite.
  - `GDD/07_Production_Roblox/À décider et à faire.md` reste le point d'entrée (même nom, même place, mêmes alias, bandeau Val Palmeraie) et devient un sommaire : « Où noter quoi » (tableau des 8 notes) et « Anciennes sections » (où est passée chaque ancienne section, pour les renvois écrits avant). Date de mise à jour passée au 28 oct. 2026.
  - 8 notes dans `À décider et à faire/` : `Décisions par thème` (§ 1), `Reste à faire et tests` (§ 2 et tests jamais faits), 5 chantiers PROVISOIRES (`Starter, Zéphir et combat d'apprentissage`, `Modèles 3D des Tifazelts`, `Dresseurs, vélos et remplaçants (27 oct. 2026)`, `Tiflask, compagnon et panneau d'équipe`, `Bourg-Azur parfait`) et une archive `Bugs du 26 oct. 2026 (traités)`, avec en tête la liste des validations encore ouvertes.
  - Désordre corrigé : les lignes « Vérifié sans défaut… » et la liste des tests jamais faits (saisie, invites, en ligne, jouabilité, performances) étaient tombées sous « Combat d'apprentissage et Zéphir » : remises dans « Tests jamais faits ». La section « Modèles 3D de la lignée Cramosaur » contenait aussi les vélos, les dresseurs et les remplaçants : séparés. La lignée Dauphin était collée après le rappel Ctrl+S : rangée avec les modèles 3D.
  - Points dépassés : rien n'est effacé ; une ligne « *Mise à jour (rangement, 28 oct. 2026)* » est ajoutée sous 4 points : modèles de Dauphimyst faits (starters), vêtements des PNJ faits (reste à faire), rendu « saturation 1,7 » des v03 remplacé par les v04, réglage B (1,3) du Dauphin refusé par Mohand (0,8 retenu).
  - Contrôle par script : chaque ligne non vide d'origine est placée une seule fois, aucune ligne d'origine introuvable.
  - Liens : 4 renvois internes devenus faux (« voir … ci-dessous ») remplacés par des liens ; 3 renvois « Bugs relevés en Play » des plans (`Feuille de route 26-27 oct`, `Vêtements PNJ et suite`) pointent vers la note des bugs ; `CLAUDE.md` précise que le sommaire indique la note où écrire. Audit : 0 lien cassé, 0 ancre cassée, aucun doublon de nom (377 notes).
- 28 oct. 2026 : étape 8 faite.
  - Relecture en trois lots par trois agents en lecture seule (lore et monde ; règles et design ; production contre GDD), environ 62 000 mots, puis vérification de chaque point retenu dans les fichiers. 88 points signalés, dont des doublons entre lots ; deux affirmations d'agent fausses écartées (Zéphir n'est pas dans la table d'habillage ; seuls le Professeur et 68 autres PNJ y sont).
  - **Corrigé directement (erreurs de fait, 52 modifications dans 34 notes)** : types des starters au premier stade (`Noms des Tifazelts`, `Décisions par thème`) ; « cristaux et badges » → « cristaux » (`12. Joueur`) ; « Défense Physique » → « Défense » (`3. Mécanique`) ; lien « Niveau » de la Charte vers les courbes d'expérience ; ombre douce annotée « remplacée » (Charte) ; compteur de secrets « n/31 » et lieu du starter en jeu (`Liste des Menus et Écrans`) ; Fleuriste retiré des façades inaccessibles et PNJ du starter ajoutés (`Bourg-Azur`) ; « Laineux » → « Tifazelts laineux » (`Route 1`) ; « Peluche Amicale » et « Tiflask d'Amitié » (`Route 5`) ; « retrouvailles avec Zéphir » (`00_Province_Lumeridia`) ; alias « Colline Ksar » en double retiré (`Repaire Glacitech`) ; « Chasseur de trésors » (`11. PNJ`) ; phases 0 et 1 de l'interface datées du 19 oct. (d'après les captures) ; `00. Production Roblox` (tableau des notes complété, secrets 39 + 8, interface phases 0 à 7) ; 4 lignes ajoutées au `Journal de construction de la carte` (20, 26, 27, 28 oct.) ; `Habillage des PNJ` (Zéphir et Gilles, 71 PNJ).
  - **Notes de production restées au 19-20 oct.** : une ligne « *Mise à jour (relecture, 28 oct. 2026)* » ajoutée, sans réécrire l'historique : `Systèmes de jeu Roblox`, interface phases 2, 3, 4, 5, 6, 7 (Tifazelts de test retirés, défaite à l'infirmerie, sons, portraits, début de partie), Bourg-Azur habitants et performance, `Animations, déplacements et audio` (touche K barrée, un objet clé par vélo), chantiers Tiflask, Modèles 3D, Starter et Zéphir, Décisions (bulles), Reste à faire (Val Palmeraie).
  - Copie identique de la carte (`01_Lumeridia/Carte de Luméridia Est.png`, citée nulle part) → `Claude outputs/Archives/` (vérifiée identique à `assets/cartes/Lumeridia_Est.png`).
  - **Choix laissés à Mohand** : nouvelle note [[À décider - Relecture du 28 oct. 2026]] (41 choix numérotés, 7 points à vérifier dans Studio, 5 doublons laissés tels quels), ajoutée au sommaire de `À décider et à faire`. Val Palmeraie (gelé) : rien modifié, ses contradictions sont listées (choix 18).
  - Non fait : les découpages en option de `00. Définition` et `3. Mécanique` (D6, au choix de Mohand).
  - Pour l'étape 11 : `Accueil` (titre « Azzursal », notes absentes, légende et filtre du graphe), `README` (titre, arborescence), `CLAUDE.md` (« Pas encore de vrai combat ni de capture », chantier en cours du 26 oct., « 68 PNJ »).
  - Audit : 0 conflit, 0 note vide, 0 lien cassé, 0 ancre cassée (378 notes).
- 28 oct. 2026 : étape 9 faite (classement des plans validé par Mohand).
  - 8 plans terminés → `Claude outputs/Passation Cowork/Terminés/` : Lignée Cramosaur v04 ; v04, Tifalistre, PNJ, intro de combat et vélos ; Panneau d'équipe ; Portraits et Tiflask ; Starters ; Sortie du Tifazelt ; Vêtements PNJ et suite ; Feuille de route 26-27 oct. Chacun porte en tête une ligne « Rangement (28 oct. 2026) » qui renvoie à `À décider et à faire` (leurs points encore ouverts y sont déjà suivis). Restent dans `Passation Cowork/` : Bourg-Azur parfait, Lignée Dauphin, Vérifications de Mohand - 27 oct. 2026, ce plan.
  - `Claude outputs/Animations, déplacements et audio.md` → `GDD/07_Production_Roblox/` (liens par nom, rien à changer).
  - `Roblox_Textures/` → `Claude outputs/Textures Roblox/` (92 fichiers, compte identique avant et après ; le générateur reçoit ses dossiers en argument).
  - `src/Backup1.rbxl` → `Claude outputs/Sauvegardes Roblox/Backup1.rbxl` ; dossier `src/` vide retiré.
  - Chemins mis à jour : `CLAUDE.md` (plan des vêtements dans `Terminés/`, la section entière sera refaite à l'étape 11), `00. Production Roblox` (copie de secours, datée du 16 oct.), mémoire de Claude `plans-multi-etapes` (convention `Terminés/`). Le README sera refait à l'étape 11.
  - Tous les déplacements faits avec `git mv`. Audit : 0 lien cassé, 0 ancre cassée, aucun doublon de nom (378 notes).
- 28 oct. 2026 : étape 10 faite.
  - Déplacés (1 884 fichiers, 1,49 Go ; nombre de fichiers et taille vérifiés identiques après chaque déplacement) :
    - **fichiers de travail** → `_Travail/` (même sous-dossier qu'avant) : `Dauphin/_Travail/Sprites/` (`brut`, `brut45`, `brut_B_sat13`, `24_images_B_sat13`), `Dauphin/_Travail/Rendus/` (`var_A` à `var_D`, `var2_E` à `var2_G`, `sprites_test`), `Cramosaur/V04/_Travail/Sprites/` (`brut45`, `test45`, `test45b`, `45_images_essai_decentre`) ;
    - **sauvegardes** → `Sauvegardes/` (noms de dossier gardés) : `Dauphin/Sauvegardes/Sauvegarde_avant_rig`, `Dauphin/Sauvegardes/Sauvegarde_Dauphiracle_sans_texture`, `Cramosaur/V04/Sauvegardes/Sauvegarde_avant_trous` ;
    - **Cramosaur v01 à v03** → `Cramosaur/Anciennes versions (v01-v03)/` avec leur structure (`.blend` de la racine, `Portraits`, `Rendus`, `Rig`, `Sources`, `Sprites`, `Textures`) ; variantes refusées `Version_brillante_abandonnee` et `Version_mate_contour_blender` dans son `_Travail/Sprites/`.
  - Ne bougent pas : `.blend` en service et leurs `Textures/` (`Cramosaur/V04/`, `Dauphin/`), `Cramosaur/Scripts/`, `Dauphin/Scripts/`, `Tiflask/` (dont `Rendus_bruts`, gardé : non désigné comme fichier de travail), les deux fichiers `identifiants_roblox_*.json`.
  - **Chemins des `.blend` relus avant et après (lecture des fichiers décompressés, Blender non ouvert)** : identiques pour les 10 `.blend`. En service, tout est trouvé, sauf une image de rendu absente déjà avant (`V04/Rendus/trous_Cramorex_apres.png`, lue par `Lignee_Cramosaur_v04.blend`). Les anciens `.blend` Cramosaur ne lisent aucun fichier externe. `Sauvegarde_avant_rig/Lignee_Dauphin.blend` cherchait déjà ses textures dans un `Textures/` voisin qui n'existe pas (11 sur 15 absentes, comme avant) : à relier à `Dauphin/Textures/` si on rouvre un jour cette sauvegarde.
  - Git : 159 renommages suivis ; les 18 images des deux variantes refusées v03 sortent de git (elles restent sur le disque, dans l'historique et dans la copie de sauvegarde). `.gitignore` simplifié (le bloc provisoire de l'étape 1 est retiré, `_Travail/` suffit).
  - Chemins mis à jour : ligne de rangement ajoutée dans `Lignée Dauphin - plan` (section Fichiers) et dans les bandeaux de `Starters`, `Portraits et Tiflask` et `Lignée Cramosaur v04` (dans `Terminés/`). Scripts : rien à changer (ils reçoivent leurs dossiers en argument ; les chemins absolus de `Dauphin/Scripts/` visent `V04/` et `Dauphin/`, qui n'ont pas bougé).
- 28 oct. 2026 : étape 11 faite.
  - `Accueil.md` réécrit : « Pour commencer » (à décider, production, plans en cours, CLAUDE.md), toutes les notes du GDD par rubrique (dont Noms des Tifazelts, Habillage, Animations, À décider, Historique des captures, absentes avant), règle des notes découpées, tableau du dossier `Claude outputs/` (où est chaque chose, avec l'avertissement sur les chemins absolus des `.blend`), autres dossiers (`assets/`, `gemini-scribe/`, `.obsidian/`, copie de sauvegarde), légende du graphe. Titre : « Tifazelt » (au lieu de « Azzursal (Tifazelt) »).
  - Graphe (`.obsidian/graph.json`) : 14 groupes de couleurs, du plus précis au plus général, conformes à la légende ; filtre de recherche `-path:"GDD/03_Tifazelts_et_Combats/8. Attaques"` (l'ancien visait un dossier `CSV import` qui n'existe plus).
  - Fichiers exclus (`.obsidian/app.json`) : `Claude outputs/Modeles 3D/` (D7).
  - Signets : « À décider et à faire » et « Captures » ajoutés ; les 5 signets existants pointent tous vers des fichiers présents.
  - `README.md` : titre « Tifazelt », contenu du dépôt (le code Luau vit dans Studio), arborescence à jour (plus de `src/`, ni `assets/icons`).
  - `CLAUDE.md` : renvoi à l'index `Accueil.md` ; « pas encore de vrai combat ni de capture » remplacé par l'état réel (prototype avec données de test) ; « Chantier en cours (26 oct.) » remplacé par les chantiers en cours au 28 oct. ; nouvelle section « Rangement du vault » (règle des notes découpées, dossiers à ne pas déplacer, `_Travail/`, `Sauvegardes/`, `Archives/`). Règle des captures et de `À décider` déjà mises à jour aux étapes 4 et 7.
  - **Obsidian était ouvert** pendant l'écriture des réglages : Mohand doit le quitter (Cmd+Q) et le rouvrir pour qu'il les relise ; vérification à l'étape 12 que `graph.json`, `app.json` et `bookmarks.json` n'ont pas été écrasés.
  - Audit : 0 conflit, 0 note vide, 0 lien cassé, 0 ancre cassée (378 notes).
