---
tags:
  - production
  - roblox
  - bourg-azur
---
# 🧪 Bourg-Azur — performance, tests et pistes

> [[Bourg-Azur - Habitants et secrets|← Habitants et secrets]] · [[Bourg-Azur - Construction et Direction Artistique|Sommaire de la construction de Bourg-Azur]]

## ⚙️ 9. Performance

- Toute la ville compte environ **15 600 pièces**, et les 6 intérieurs environ **1 600**. Tout est ancré, et les décors sans fonction n'ont pas de collision.
- Il n'y a ni script de surveillance par objet ni PNJ animé. Le client contrôle les portes 6 fois par seconde et ne les anime que pendant qu'elles bougent.
- Le streaming du monde, déjà actif, a été conservé. Le serveur charge la zone d'arrivée avant chaque téléportation.
- Le jeu tourne à 15 images par seconde dans Studio, en ville comme ailleurs : c'est la limite de l'environnement de test, pas une vraie mesure sur un appareil.

---

## 🧪 10. Tests réellement effectués (Play dans Studio)

- Apparition du joueur dans sa chambre : ✅
- Entrée et sortie des 6 bâtiments (bon intérieur, bon point de retour) : ✅
- Aucune nouvelle téléportation en restant devant la porte après une sortie : ✅
- S'asseoir et se relever sur un banc (testé par script) : ✅
- 24 PNJ, tous R6 complets et posés au sol : ✅
- Passage de la porte de la ville vers la Route 1, aller et retour : ✅
- Aucune erreur de script dans la console : ✅
- **Non vérifié en marchant :** les deux nouveaux chemins (champ, oliveraie), contrôlés seulement par calcul d'obstacles ; la lumière des intérieurs autres que la maison ; le rendu final de l'eau de la fontaine.

---

## 🔭 11. Pistes pour la suite

- **Harmoniser les interfaces** avec la [[15. Charte Graphique]]. Les bulles de dialogue et la carte « Secret trouvé » utilisent pour l'instant un fond bleu nuit et crème : elles devraient passer au Blanc carte, au Terracotta et aux bords en biais.
- Donner de **vrais vêtements** aux PNJ (habits du catalogue) et quelques animations d'attente simples.
- Brancher les **systèmes de jeu** sur les emplacements prêts : soins à l'infirmerie, boutique du Bazar, missions et échanges de la Guilde, Pâturage.
- Ajouter des **sons d'ambiance** : fontaine, mouettes, ressac, brouhaha du café.
- Ajouter un **cycle jour/nuit**, pour que les lampadaires et les lueurs des portes prennent tout leur sens le soir.
