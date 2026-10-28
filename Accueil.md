---
tags:
  - accueil
aliases:
  - Accueil
  - Sommaire
  - Index
---
# 🏠 Tifazelt — Accueil du vault

> Point de départ pour trouver n'importe quoi : le game design (GDD), ce qui est construit dans Roblox Studio, et le dossier de développement. Jeu Roblox **Tifazelt**, dans la région d'**Azzursal** ; le jeu lui-même est dans Roblox Studio. Vault rangé le 28 oct. 2026 ([[Rangement du dossier - plan]]).
> Chaque couleur du **graphe** correspond à une rubrique ci-dessous (légende en bas de page).

## 🧭 Pour commencer
- **Ce qui reste à décider ou à faire** : [[À décider et à faire]], dont les 41 choix de la relecture : [[À décider - Relecture du 28 oct. 2026]].
- **Ce qui est construit dans Studio** : [[00. Production Roblox]].
- **Plans en cours** (à reprendre avec « passons à l'étape N ») : [[Bourg-Azur parfait - plan]] · [[Lignée Dauphin - plan]] · [[Vérifications de Mohand - 27 oct. 2026]] · [[Restructuration du vault - plan]] (à valider).
- **Consignes pour Claude** : `CLAUDE.md`, à la racine du dossier.

## 🟡 Game design — `GDD/01_Game_Design_Core`
- [[1. Menus Et Interfaces]] — menus, inventaire, objets tenus, Tiflask
- [[2. Economie Et Formules Et Reste]] — Tifadinar (TFD), Points de Combat (PC), formules
- [[3. Mécanique]] — météo, bonheur, jour/nuit, PvP, raids
- [[Liste des Menus et Écrans]] — plan de production de tous les écrans (phases 0 à 7)

## 🟢 Univers et lore — `GDD/02_Univers_et_Lore`
- [[00_Region_Azzursal|Région d'Azzursal]] — les 4 provinces : Luméridia, Florédena, Cristalpina, Ardusia
- [[00_Province_Lumeridia|Province de Luméridia Est]] — progression des villes et routes, carte
- [[Bâtiments Communs]] — infirmerie, guilde, bazar, pâturage…
- [[5. Quêtes Dans L'Aventure]] · [[6. Personnages]]

### 🔴 Villes de Luméridia Est
1. [[Bourg-Azur]] → 2. [[Val Palmeraie]] (développement gelé depuis le 26 oct. 2026) → 3. [[Cité Ocre]] → 4. [[Presqu'île Marine]] → 5. [[Port-Saphir]] → 6. [[Hameau-Doré]] → 7. [[Repaire Glacitech]]

### 🟤 Routes
[[Route 1]] · [[Route 2]] · [[Route 3]] · [[Route 4]] · [[Route 5]] · [[Route 6]]

### 🩵 Lieux et reliefs
[[Asif-Safi]] · [[Colline Ksar]] · [[Grotte Inconnue]] · [[Profondeurs Sous-Marines]]

## 🟣 Tifazelts et combats — `GDD/03_Tifazelts_et_Combats`
- [[00. Définition|Tifazelts — définition, stats, starters, légendaires, évolution, reproduction]]
- [[Noms des Tifazelts (propositions)]] — les 20 noms et les lignées (PROVISOIRE)
- [[9. Capacités des Tifazelts]] · [[10. Table des types]]
- **Attaques** : une fiche par attaque dans `8. Attaques/` (283 fiches, violet clair, masquées du graphe par défaut) ; tableau filtrable dans `8. Liste des attaques.base` (vues « par type » et « par catégorie »).

## 🔵 Joueur et PNJ — `GDD/04_Joueur_et_PNJ`
- [[11. PNJ]] · [[12. Joueur]] (classes, grades) · [[13. Sanctuaire]] (gardiens, Ligue)

## 🩷 Inventaire — `GDD/05_Inventaire`
- [[14. Objets]]

## 💠 Direction artistique — `GDD/06_Direction_Artistique`
- [[15. Charte Graphique]] · [[16. Direction Artistique des Menus]] (biseaux, ombre solide, accents, mise en œuvre Roblox)

## 🟠 Production Roblox — `GDD/07_Production_Roblox`
- [[00. Production Roblox]] — index de la production : où est le code dans Studio, règles pour régénérer sans casser
- [[Journal de construction de la carte]] — chronologie des passes
- [[Route 1 - Construction Roblox]] — passes 2 à 6, forêt, plaine ouest
- [[Bourg-Azur - Construction et Direction Artistique]] — sommaire et « où trouver quoi » ; 6 notes dans le dossier du même nom
- [[Interface (UI) - Construction Roblox]] — sommaire ; phases 0 à 7 et pièges Roblox dans le dossier du même nom
- [[Systèmes de jeu Roblox]] — courant, lucioles, rayons, PNJ, secrets (état du 19 oct.)
- [[Secrets d'exploration]] — les 39 secrets de la carte
- [[Habillage des PNJ]] — tenues, visages, coiffures
- [[Animations, déplacements et audio]] — animations, course, vélo, musiques, sons
- [[À décider et à faire]] — sommaire ; décisions par thème, reste à faire, chantiers PROVISOIRES, relecture et archive des bugs dans le dossier du même nom

> Les notes découpées suivent toutes la même règle : le **sommaire** garde son nom et sa place, les **parties** sont dans le dossier du même nom, juste à côté.

## ⚪ Captures — `GDD/08_Captures`
- [[Historique des captures]] — sommaire (tableaux par jour et par thème) ; une note par jour dans `Historique des captures/` ; les images `AAAA-MM-JJ_HHhMM_sujet.jpg` sont à plat dans `GDD/08_Captures/`.

## 🛠️ Développement — `Claude outputs/`

| Dossier | Contenu |
| :--- | :--- |
| `Passation Cowork/` | Plans en étapes en cours ; les plans finis sont dans `Terminés/` |
| `outils/` | `audit.py` (audit du vault : `python3 "Claude outputs/outils/audit.py" .`), `Bourg-Azur - détecteurs.lua`, `habillage_pnj.json` |
| `Modeles 3D/Cramosaur/` | `V04/` : version en service (`.blend`, `Textures/`, `Rig/`, `Sprites/`, `Portraits/`, `Rendus/`, `Sources/`, `Sauvegardes/`) ; `Scripts/` : scripts Blender et Python ; `Anciennes versions (v01-v03)/` |
| `Modeles 3D/Dauphin/` | Lignée du Dauphin : `Lignee_Dauphin.blend`, `Rendu_Sprites_Dauphin.blend`, `Textures/`, `Rig/`, `Sprites/`, `Portraits/`, `Rendus/`, `Sources/`, `Scripts/`, `Sauvegardes/` |
| `Modeles 3D/Tiflask/` | Tiflask : modèle FBX, images, rendus |
| `Modeles 3D/…/_Travail/` | Rendus bruts, essais, variantes refusées (hors git, gardés sur le disque) |
| `Illustrations Tifazelts/` | [[Garenbois - prompt de la première illustration]] |
| `Interface/` | Images faites pour l'interface (visage fâché de Zéphir) |
| `Textures Roblox/` | Vêtements des PNJ (hauts, bas, visages, aperçus) et leur générateur Python |
| `Sauvegardes Roblox/` | `Backup1.rbxl`, copie du place du 16 oct. 2026 |
| `Archives/` | Fichiers sans usage gardés par précaution (captures sans heure du 16 oct., copies) |

> ⚠️ Ne pas déplacer ni renommer `Modeles 3D/`, `Cramosaur/V04/`, `Dauphin/` et leurs `Textures/` : des fichiers Blender et des scripts y pointent par chemin absolu.

## 📁 Autres dossiers
- `assets/` : images du GDD (carte de Luméridia Est dans `cartes/`, maquettes de menus dans `ui/`).
- `gemini-scribe/` : dossier de travail du module Obsidian Gemini Scribe (créé par lui).
- `.obsidian/` : réglages d'Obsidian. `Claude outputs/Modeles 3D` est exclu de la recherche et du graphe (Réglages > Fichiers et liens > Fichiers exclus).
- Copie complète d'avant le rangement : `~/Documents/Tifazelt - sauvegardes/2026-10-28 avant rangement/` (hors du vault).

## 🎨 Légende du graphe
| Couleur | Rubrique |
| :--- | :--- |
| ⚪ Blanc | Cette page d'accueil |
| 🟡 Jaune | Game design (menus, économie, mécaniques) |
| 🔴 Rouge | Villes |
| 🟤 Brun | Routes |
| 🩵 Turquoise | Lieux et reliefs |
| 🟢 Vert | Lore général (région, province, quêtes, personnages, bâtiments) |
| 💜 Violet clair | Fiches d'attaques (masquées par défaut) |
| 🟣 Violet | Tifazelts, capacités, types |
| 🔵 Bleu | Joueur, PNJ, sanctuaires |
| 🩷 Rose | Objets |
| 💠 Cyan | Direction artistique |
| 🟠 Orange | Production Roblox |
| 🩶 Gris | Captures |
| 🟫 Sable | Développement (`Claude outputs`) |

> Pour afficher aussi les 283 attaques dans le graphe : dans le champ de recherche du graphe, retirer `-path:"GDD/03_Tifazelts_et_Combats/8. Attaques"`.
