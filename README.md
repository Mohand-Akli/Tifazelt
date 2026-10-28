# 🌟 Tifazelt — RPG Roblox (région d'Azzursal)

Ce dépôt GitHub centralise la base de données complète (Game Design Document) et les fichiers de développement du jeu **Tifazelt**, qui se déroule dans la région d'Azzursal. Il s'agit d'un jeu RPG d'aventure et de capture de monstres (Tifazelts) en développement sur Roblox. 

Ce répertoire n'est pas un logiciel à installer, mais un espace de documentation et d'archivage. Vous y trouverez toute la documentation concernant le lore, les mécaniques de jeu, les systèmes économiques, et la direction artistique, ainsi que les scripts associés au développement.

<br>

<a href="https://www.linkedin.com/in/mohand-akli-zidani" target="_blank">
<img src="https://img.shields.io/badge/LinkedIn-0077B5?&style=for-the-badge&logo=linkedin&logoColor=white" alt="linkedin" style="margin-bottom: 5px;" />
</a>

## Table des Matières
- [Contenu du Dépôt](#contenu-du-dépôt)
- [Univers et Mécaniques](#univers-et-mécaniques)
- [Structure du Projet](#structure-du-projet)
- [Licence](#licence)

## Contenu du Dépôt
Ce répertoire sert d'archive et d'espace de travail principal pour la conception du jeu. Il contient :
1. **La Base de Données (GDD) :** Une collection de fichiers Markdown formatés (pensés pour Obsidian) détaillant chaque aspect conceptuel du jeu : le lore des 4 régions, les personnages, le bestiaire (Tifazelts), les objets, et les formules mathématiques.
2. **Le Développement :** modèles 3D (Blender), scripts Python, textures, plans de travail et copie de secours du place Roblox. Le code Luau du jeu vit dans Roblox Studio.

## Univers et Mécaniques
- **Monde Ouvert à 4 Biomes :** Exploration fluide entre Luméridia (Côtes), Florédena (Jungle), Cristalpina (Montagnes) et Ardusia (Désert).
- **Système de Tifazelts :** Capture, entraînement et évolution de créatures élémentaires avec un système approfondi de statistiques, de natures et de bonheur.
- **Classes de Joueur :** Personnalisation du style de jeu grâce à des classes uniques (Éleveur, Infirmier, Cuisinier, Ingénieur, Stratège, Chasseur de trésors).
- **Combats Stratégiques :** Affrontements basés sur une table des types complexe (incluant le type "Réalité"), des météos dynamiques et un système de priorité.

## Structure du Projet

```text
├── README.md · LICENSE
├── Accueil.md                      (index du vault : où se trouve chaque chose)
├── CLAUDE.md                       (consignes pour Claude Code)
├── assets/                         (carte, maquettes d'interface)
├── GDD/                            (Game Design Document — vault Obsidian)
│   ├── 01_Game_Design_Core/        (menus, économie, mécaniques, liste des écrans)
│   ├── 02_Univers_et_Lore/         (région, province, 7 villes, 6 routes, lieux, quêtes, personnages)
│   ├── 03_Tifazelts_et_Combats/    (définition, noms, capacités, types, 283 fiches d'attaques)
│   ├── 04_Joueur_et_PNJ/           (PNJ, joueur, sanctuaires)
│   ├── 05_Inventaire/              (objets)
│   ├── 06_Direction_Artistique/    (charte graphique, menus)
│   ├── 07_Production_Roblox/       (ce qui est construit dans Roblox Studio ; à décider et à faire)
│   └── 08_Captures/                (captures d'écran ; historique, une note par jour)
└── Claude outputs/                 (développement)
    ├── Passation Cowork/           (plans en étapes ; Terminés/)
    ├── outils/                     (audit du vault, détecteurs)
    ├── Modeles 3D/                 (Cramosaur, Dauphin, Tiflask : Blender, textures, rigs, sprites)
    ├── Textures Roblox/            (vêtements des PNJ et leur générateur)
    ├── Sauvegardes Roblox/         (Backup1.rbxl, copie de secours du place Roblox)
    ├── Illustrations Tifazelts/ · Interface/
    └── Archives/
```

## Licence

**Licence Hybride :**
- **Code source et scripts (Luau) :** Distribués sous licence **MIT**. Vous êtes libre d'étudier et de vous inspirer du code.
- **Univers, Scénario, Noms et Direction Artistique (Lore) :** Tous droits réservés (Copyright © Mohand-Akli Zidani). L'univers d'Azzursal, le scénario, les Tifazelts, les personnages et la base de données (Game Design Document) ne sont pas libres de droits et ne peuvent être réutilisés dans un projet tiers sans autorisation explicite.