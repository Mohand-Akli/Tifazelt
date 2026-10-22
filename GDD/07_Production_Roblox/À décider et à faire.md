---
tags:
  - production
  - roblox
  - suivi
aliases:
  - À décider
  - Reste à faire
---
# 🗂️ À décider et à faire

> Liste tenue à jour par Claude, à partir des sections « Provisoire », « Non vérifié » et « Pistes » des notes de production. Dernière mise à jour : 20 oct. 2026.
> **Rien de ce qui est marqué « à décider » n'est écrit dans le GDD** : ce sont des valeurs posées pour que le jeu tourne.

## 🧭 1. Décisions à prendre

### ⚔️ Combat
- **Formules :**
  - dégâts : (2 × niv / 5 + 2) × puissance × A / D / 50 + 2, tirage 85-100 %, pas de bonus de même type ;
  - efficacités : ×2, ×0,5 et ×0 ;
  - paliers de stats (−6 à +6) ;
  - capture, XP, stats par niveau ;
  - gains et pertes de TFD ;
  - fuite.
- **Effets des attaques :** il faut une colonne « Effet » structurée dans `8. Attaques`. Aujourd'hui, les effets sont devinés par mots-clés.
- **Tifalistre :** stats de base officielles et taux de capture. Les 7 espèces de test sont inventées.

### 🏪 Économie et services
- **Prix :** prix du Magasin, menu et recettes du Restaurant, salaire du Cuisinier (250 TFD, 3 services par visite).
- **Missions de la Guilde :** missions et récompenses. Elles donnent des **TFD ou des PC** ? La Liste des écrans dit PC, l'Économie réserve les PC au PvP.
- **Grades :** bornes à fixer, le vault se chevauche. Lecture retenue : Bronze 0-2, Argent 3-4, Or 5-6, Platine 7-8.
- **Investissement :** chantiers, paliers et nom de l'entreprise (« nom à définir »).
- **Gardiens :** niveaux et équipes des 8 Gardiens.
- **Reproduction :** temps d'éclosion (60 s), ce que le petit hérite, talents cachés.

### 🌅 Début de partie
- **Starters :** noms (Pyrofennec, Aqualune, Florépine, provisoires), niveau 5, attaques.
- **Cadeaux de départ :** 3 000 TFD de Maman et 5 Tiflask simples.
- **Classes :** combien on en choisit. Aujourd'hui : une principale et une secondaire.
- **Apparence :** apparence du joueur. Aujourd'hui : avatar Roblox et couleur de dresseur.
- **Combat d'apprentissage :** adversaire (Zéphir ?).
- **Après la quête :** objectif suivant (Route 2 par la Porte du Sirocco ?).

### 🌐 En ligne
- **PvP :** PC par victoire (10, et +1 par victoire de suite) ; règles (équipes soignées, pas d'objets, choix auto après 60 s).
- **Échanges :** échanges d'objets ou seulement de Tifazelts.
- **Raid :** boss (Voltaneau niv. 35), PV, durée, récompenses, **lieu dans le monde**.
- **Proximité :** distance « à proximité » (250 studs).

### 🎣 Mini-jeux
- **Pêche :** réglages (zone, attente, temps pour ferrer), prises par lieu, appâts, « Canne pro ».
- **Plongée :**
  - souffle (15 s, +25 s avec le Tuba) ;
  - prix et PNJ de recharge de la Bonbonne ;
  - exception au « courant » quand on aura la Tenue de plongée.
- **Énigmes :** textes, solutions, emplacements et récompenses (inventés pour l'exemple).

### 🗺️ Monde
- **Route 1 :**
  - le « pont basique » (seul pont = Pont de la Plaine en pierre) ;
  - sentier au nord-est de la forêt ;
  - silhouettes de Laineux et Picoreurs ;
  - idées de la passe 3 non validées : bocage, moulin lointain, rebords à sens unique, etc.
- **Réglages visuels :** palette des troncs du bosquet, herbe 3D du terrain, `Lighting.Technology` à vérifier.
- **Val Palmeraie :** pistes « ville vivante » à valider.

### 🎨 Direction artistique et interface
- **Menus :** système de design (couleurs, tailles, animations), proposé et pas encore validé.
- **Bulles et carte « Secret trouvé » :** à passer aux couleurs de la Charte (Blanc carte, Terracotta).
- **Portraits :** les portraits de Tifazelts sont provisoires (initiale dans un cercle).
- **Intérieurs (20 oct.) :**
  - croix de soin **vertes** ;
  - terrain d'entraînement **rectangulaire** dans la Guilde ;
  - textes inventés (Coin Échanges, Palmarès, Promo du jour, Bouquets du jour, affiches) ;
  - refaire ou non la **Maison du joueur**.

### 🚲 Déplacements, animations et sons (20 oct.)
- **Vélo :** comment on l'obtient et à quel moment de l'histoire. Vitesse, et où il est interdit.
- **Course :** illimitée ou avec endurance.
- **Animations :** style de celles du joueur ; liste par type de PNJ.
- **Musiques :** morceaux pris dans la bibliothèque Roblox en attendant des compositions originales, à valider à l'écoute.
- **Sons :** sons des menus et du dialogue.

## 🛠️ 2. Reste à faire

### Systèmes
- **Sauvegarde :** vraie sauvegarde côté serveur (DataStore). « Continuer » reprend aujourd'hui des données de test.
- **Sécurité :**
  - passer le moteur de combat côté serveur (anti-triche) ;
  - filtre de Roblox sur les noms et les surnoms ;
  - rendre sûres les données venues du joueur en ligne.
- **Suivi des missions :** compter les dresseurs battus, etc.
- **PNJ manquants :** Professeur Arid dans le laboratoire, PNJ de recharge de la Bonbonne.
- **Lieux à placer dans le monde :** sanctuaires et lieu du raid.

### Monde
- **Villes :** Cité Ocre, Hameau-Doré, Port-Saphir, Presqu'île Marine, Repaire Glacitech… (seuls Bourg-Azur et Val Palmeraie sont construits).
- **Routes et lieux :** Routes 2 à 6, Cascade, Grotte Inconnue.
- **Histoire :** scène du rival sur le pont de la Route 1, brume scénarisée et obtention de la Bague.
- **Ambiance :** cycle jour/nuit, sons d'ambiance (fontaine, mouettes, ressac, café), rafales qui couchent l'herbe.
- **PNJ :** vrais vêtements pour les PNJ, visages et animations des figurines de Val Palmeraie.
- **Val Palmeraie :** enseigne « Route 2 — Cité Ocre », brancher les emplacements réservés (Professeur, Tiflasks, guilde, boutique).

### Tests jamais faits
- **Saisie :** vrais clics, manette, mobile, saisie du nom au clavier.
- **Invites :** les invites (ProximityPrompt) pressées à la main ; Studio ne les simule pas.
- **En ligne :** deux vrais joueurs (Test > Clients et serveurs), déconnexion en combat, délai de 60 s, amis Roblox.
- **Jouabilité :** la pêche à la main, la descente à la nage, la remontée quand l'air manque.
- **Performances :** sur un appareil modeste.

> Rappel : penser à **Ctrl+S** dans Studio après chaque séance.
