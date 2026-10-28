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

## 🟡 Game design — `01 - Règles du jeu` · `07 - Interface et menus`
- [[1. Menus Et Interfaces]] — menus, inventaire, objets tenus, Tiflask
- [[2. Economie Et Formules Et Reste]] — Tifadinar (TFD), Points de Combat (PC), formules
- [[3. Mécanique]] — météo, bonheur, jour/nuit, PvP, raids
- [[Liste des Menus et Écrans]] — plan de production de tous les écrans (phases 0 à 7)

## 🟢 Univers et lore — `03 - Monde` · `04 - Histoire et personnages`
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

## 🟣 Tifazelts et combats — `02 - Tifazelts`
- [[00. Définition|Tifazelts — définition, stats, starters, légendaires, évolution, reproduction]]
- [[Noms des Tifazelts (propositions)]] — les 20 noms et les lignées (PROVISOIRE)
- [[9. Capacités des Tifazelts]] · [[10. Table des types]]
- **Attaques** : une fiche par attaque dans `02 - Tifazelts/Attaques/` (283 fiches, violet clair, masquées du graphe par défaut) ; tableau filtrable dans `Liste des attaques.base` (vues « par type » et « par catégorie »).

## 🔵 Joueur et PNJ — `05 - Joueur et dresseurs`
- [[11. PNJ]] · [[12. Joueur]] (classes, grades) · [[13. Sanctuaire]] (gardiens, Ligue)

## 🩷 Inventaire — `06 - Objets`
- [[14. Objets]]

## 💠 Direction artistique — `08 - Direction artistique`
- [[15. Charte Graphique]] · [[16. Direction Artistique des Menus]] (biseaux, ombre solide, accents, mise en œuvre Roblox)

## 🟠 Production Roblox — `09 - Production Roblox`
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

## ⚪ Captures — `10 - Captures/Images`
- [[Historique des captures]] — sommaire (tableaux par jour et par thème) ; une note par jour dans `Historique des captures/` ; les images `AAAA-MM-JJ_HHhMM_sujet.jpg` sont à plat dans `10 - Captures/Images/`.

## 🛠️ Développement — `11 - Développement/`

| Dossier | Contenu |
| :--- | :--- |
| `00 - Suivi/Plans/` | Plans en étapes en cours ; les plans finis sont dans `Terminés/` |
| `Outils du vault/` | `audit.py` (audit du vault : `python3 "11 - Développement/Outils du vault/audit.py" .`), `Bourg-Azur - détecteurs.lua`, `habillage_pnj.json` |
| `Modèles 3D/Cramosaur/` | `V04/` : version en service (`.blend`, `Textures/`, `Rig/`, `Sprites/`, `Portraits/`, `Rendus/`, `Sources/`, `Sauvegardes/`) ; `Scripts/` : scripts Blender et Python ; `Anciennes versions (v01-v03)/` |
| `Modèles 3D/Dauphin/` | Lignée du Dauphin : `Lignee_Dauphin.blend`, `Rendu_Sprites_Dauphin.blend`, `Textures/`, `Rig/`, `Sprites/`, `Portraits/`, `Rendus/`, `Sources/`, `Scripts/`, `Sauvegardes/` |
| `Modèles 3D/Tiflask/` | Tiflask : modèle FBX, images, rendus |
| `Modèles 3D/…/_Travail/` | Rendus bruts, essais, variantes refusées (hors git, gardés sur le disque) |
| `Illustrations/` | [[Garenbois - prompt de la première illustration]] |
| `Images de l'interface/` | Images faites pour l'interface (visage fâché de Zéphir) |
| `Textures Roblox/` | Vêtements des PNJ (hauts, bas, visages, aperçus) et leur générateur Python |
| `Sauvegardes Roblox/` | `Backup1.rbxl`, copie du place du 16 oct. 2026 |
| `Archives/` | Fichiers sans usage gardés par précaution (captures sans heure du 16 oct., copies) |

> ⚠️ Ne pas déplacer ni renommer `Modèles 3D/`, `Cramosaur/V04/`, `Dauphin/` et leurs `Textures/` : des fichiers Blender et des scripts y pointent par chemin absolu.

## 📁 Autres dossiers
- La carte de Luméridia Est est dans `03 - Monde/Luméridia Est/`, les maquettes de menus dans `08 - Direction artistique/Maquettes/`.
- `11 - Développement/Gemini Scribe/` : dossier de travail du module Obsidian Gemini Scribe (créé par lui).
- `.obsidian/` : réglages d'Obsidian. `11 - Développement/Modèles 3D` est exclu de la recherche et du graphe (Réglages > Fichiers et liens > Fichiers exclus).
- Copie complète d'avant le rangement : `~/Documents/Tifazelt - sauvegardes/2026-10-28 avant rangement/` (hors du vault).

## 🎨 Légende du graphe
Une couleur par dossier : 🟡 or = Accueil · gris-bleu = 00 Suivi · jaune = 01 Règles du jeu · violet = 02 Tifazelts · vert = 03 Monde (rouge = villes, brun = routes, turquoise = lieux) · rose = 04 Histoire et personnages · bleu = 05 Joueur et dresseurs · pêche = 06 Objets · cyan = 07 Interface et menus · vert anis = 08 Direction artistique · orange = 09 Production Roblox · gris clair = 10 Captures · taupe = 11 Développement.

> Masqués par défaut : les 283 fiches d'attaques, les plans terminés, les images et les tags. Pour les afficher : dans le champ de recherche du graphe, retirer `-path:"02 - Tifazelts/Attaques"` ; cocher « Pièces jointes » ou « Tags » dans les filtres.
