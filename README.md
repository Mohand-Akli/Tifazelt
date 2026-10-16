# 🌟 Projet Azzursal (Tifazelt) — Roblox RPG

Ce dépôt GitHub centralise l'intégralité du code source ainsi que la base de données complète (Game Design Document) du projet Azzursal. Il s'agit d'un jeu RPG d'aventure et de capture de monstres (Tifazelts) en développement sur Roblox. 

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
2. **Le Code Source :** Les scripts Luau, l'architecture UI et les assets utilisés pour concrétiser le jeu sur Roblox Studio.

## Univers et Mécaniques
- **Monde Ouvert à 4 Biomes :** Exploration fluide entre Luméridia (Côtes), Florédena (Jungle), Cristalpina (Montagnes) et Ardusia (Désert).
- **Système de Tifazelts :** Capture, entraînement et évolution de créatures élémentaires avec un système approfondi de statistiques, de natures et de bonheur.
- **Classes de Joueur :** Personnalisation du style de jeu grâce à des classes uniques (Éleveur, Infirmier, Cuisinier, Ingénieur, Stratège, Chasseur de trésors).
- **Combats Stratégiques :** Affrontements basés sur une table des types complexe (incluant le type "Réalité"), des météos dynamiques et un système de priorité.

## Structure du Projet

```text
├── README.md
├── LICENSE
├── assets/
│   └── ui/                         (maquettes d'interface)
├── GDD/                            (Game Design Document — vault Obsidian)
│   ├── 01_Game_Design_Core/
│   │   ├── 1. Menus Et Interfaces.md
│   │   ├── 2. Economie Et Formules Et Reste.md
│   │   └── 3. Mécanique.md
│   ├── 02_Univers_et_Lore/
│   │   ├── 4. Carte et Région d'Azzursal/
│   │   │   ├── 00_Region_Azzursal.md
│   │   │   ├── Bâtiments Communs.md
│   │   │   └── 01_Lumeridia/
│   │   │       ├── 00_Province_Lumeridia.md
│   │   │       ├── Villes/         (7 villes)
│   │   │       ├── Routes/         (Routes 1 à 6)
│   │   │       └── Lieux_et_Reliefs/
│   │   ├── 5. Quêtes Dans L'Aventure.md
│   │   └── 6. Personnages.md
│   ├── 03_Tifazelts_et_Combats/
│   │   ├── 7. Tifazelts.md
│   │   ├── 8. Capacités des Tifazelts.md
│   │   ├── 9. Table des types.md
│   │   └── Liste des attaques/     (une fiche par attaque)
│   ├── 04_Joueur_et_PNJ/
│   │   ├── 10. PNJ.md
│   │   ├── 11. Sanctuaire.md
│   │   └── 12. Joueur.md
│   ├── 05_Inventaire/
│   │   └── 13. Objets.md
│   └── 06_Direction_Artistique/
│       └── 14. Charte Graphique.md
└── src/
    └── (Scripts Luau, modèles 3D et assets UI Roblox — à venir)
```

## Licence

**Licence Hybride :**
- **Code source et scripts (Luau) :** Distribués sous licence **MIT**. Vous êtes libre d'étudier et de vous inspirer du code.
- **Univers, Scénario, Noms et Direction Artistique (Lore) :** Tous droits réservés (Copyright © Mohand-Akli Zidani). L'univers d'Azzursal, le scénario, les Tifazelts, les personnages et la base de données (Game Design Document) ne sont pas libres de droits et ne peuvent être réutilisés dans un projet tiers sans autorisation explicite.