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

> Liste tenue à jour par Claude, à partir des sections « Provisoire », « Non vérifié » et « Pistes » des notes de production. Dernière mise à jour : 26 oct. 2026.
> **Rien de ce qui est marqué « à décider » n'est écrit dans le GDD** : ce sont des valeurs posées pour que le jeu tourne.

> ⛔ **Val Palmeraie : développement totalement arrêté (décision de Mohand, 26 oct. 2026).** Ne rien construire, modifier ni brancher à Val Palmeraie jusqu'à nouvel ordre. Les points « Val Palmeraie » ci-dessous sont gelés.

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
- **Starters :** Garenbois (Plante), Dauphimyst (Eau/Psy), Cramosaur (Feu/Obscurité), choisis par Mohand le 26 oct. 2026 (remplacent Pyrofennec, Aqualune, Florépine). Reste à faire : niveau 5, attaques, et renommer dans le jeu.
- **Cadeaux de départ :** 3 000 TFD de Maman et 5 Tiflask simples.
- **Classes :** combien on en choisit. Aujourd'hui : une principale et une secondaire.
- **Apparence :** apparence du joueur. Aujourd'hui : avatar Roblox et couleur de dresseur.
- **Combat d'apprentissage :** adversaire (Zéphir ?).
- **Lieu du starter (PROVISOIRE, 26 oct. 2026) :** le vault dit Laboratoire Arid à Val Palmeraie (gelé). En jeu : le **Professeur Arid Acanthus** attend devant la maison familiale de Bourg-Azur (`Workspace.Map.Starter_BourgAzur`) ; « Parler » → « Choisir un Tifazelt ». Ses répliques et celles de Maman sont provisoires.
- **Après la quête :** objectif suivant. Aujourd'hui (PROVISOIRE) : « Premiers pas — Explorer la Route 1 » (la Route 2 par la Porte du Sirocco est gelée avec Val Palmeraie).

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
- **PNJ manquants :** PNJ de recharge de la Bonbonne. (Le Professeur Arid est désormais à Bourg-Azur, voir « Lieu du starter ».)
- **Lieux à placer dans le monde :** sanctuaires et lieu du raid.

### Monde
- **Villes :** Cité Ocre, Hameau-Doré, Port-Saphir, Presqu'île Marine, Repaire Glacitech… (seuls Bourg-Azur et Val Palmeraie sont construits).
- **Routes et lieux :** Routes 2 à 6, Cascade, Grotte Inconnue.
- **Histoire :** scène du rival sur le pont de la Route 1, brume scénarisée et obtention de la Bague.
- **Ambiance :** cycle jour/nuit, sons d'ambiance (fontaine, mouettes, ressac, café), rafales qui couchent l'herbe.
- **PNJ :** vrais vêtements pour les PNJ, visages et animations des figurines de Val Palmeraie.
- **Habillage des PNJ (PROVISOIRE, 26 oct. 2026) :** table dans [[Habillage des PNJ]], appliquée dans Studio le 26 oct. 2026 (rendu en Play à vérifier). À valider : sexe déduit pour Céleste ×2, Réceptionniste de la Guilde, Aurèle, Lou et Nour (enfants) ; Augustin et Odette traités comme âgés ; pas de cheveux gris féminins (Dr. Smyth Hair sur Mamie Odile et Odette) ; H29 et B22 à réimporter.
- **Val Palmeraie :** enseigne « Route 2 — Cité Ocre », brancher les emplacements réservés (Professeur, Tiflasks, guilde, boutique).

### Tests jamais faits
- **Habillage et starter (testé en Play le 26 oct. 2026 par Claude, nouvelle partie complète) :** voir « Bugs relevés en Play » ci-dessous. Reste à voir : le rendu des 69 PNJ un par un (seuls le Professeur et Lina vus de près) et la victoire du combat (jamais atteinte, voir bug 1).

### Bugs relevés en Play (26 oct. 2026, à corriger)
1. ~~**Combat d'apprentissage injouable.**~~ **Corrigé le 26 oct. 2026** (voir « Combat d'apprentissage et Zéphir » ci-dessous). Reste ouvert : `Regles.statsNiveau` ne baisse jamais une stat (`math.max(v + 1, …)`), donc tout Tifazelt créé sous le niveau 30 garde les stats du niveau 30 (Aqualune niveau 5 : 93 PV). Touche tous les combats de bas niveau : **à décider** (formule de stats par niveau, le vault ne la donne pas).

### Combat d'apprentissage et Zéphir (PROVISOIRE, 26 oct. 2026)
- **Règle du vault gardée** : Zéphir prend le starter qui a l'avantage (`00. Définition`). Un rival « neutre » n'existe pas avec trois starters en triangle.
- **Tifazelt de Zéphir affaibli** (`UI.NouvellePartie.adversaireTutoriel`) : une seule attaque, la plus faible qui fait des dégâts, sans drain ni soin (Aqualune → Brume scintillante, Florépine → Forêt Enchevêtrante, Pyrofennec → Brise Ardente). PV = 3 coups moyens de la meilleure attaque du starter (`N.COUPS_TUTORIEL = 3`, soit 10 à 14 PV). Simulation : 97 à 100 % de victoire en jouant au hasard. Testé en Play avec Aqualune : victoire en 5 tours, 37/93 PV restants, +200 TFD, objectif « Premiers pas — Explorer la Route 1 ».
- **Zéphir visible sur la carte** : `Workspace.Map.Starter_BourgAzur.Zéphir Célestin` (clone de Théo, scripts retirés), dans la rue devant le portail de la maison familiale (2135, 5, 1518), tourné vers le Professeur. Tenue H16 veste zippée azur + B07 survêtement, visage V03, cheveux CoolBoyHair (bleus). Tag `PNJ_Bourg`, `Service = Rival`, « Combattre » : sans starter → « Choisis d'abord ton Tifazelt », starter sans victoire → combat d'apprentissage, après victoire → « On se revoit sur la Route 1 ». Placé à 20 studs du Professeur, parce que deux invites « Parler » en AlwaysShow à moins de 18 studs se déclenchent ensemble (le Professeur prenait la main).
- À valider par Mohand : tenue, cheveux bleus, répliques, emplacement ; Zéphir reste-t-il là après la victoire ?
- Non testé en Play : duels Pyrofennec et Florépine (seulement simulés), revanche lancée depuis Zéphir après une défaite.
2. **Perdre le combat d'apprentissage coûte 150 TFD** et dit « Tu es ramené à l'Infirmerie », mais le joueur reste devant le Professeur. À décider : pas de pénalité pour ce combat, ou vrai retour à l'infirmerie.
3. **Dialogue du Professeur après la défaite** : il répète l'accueil complet (« Ah, te voilà ! », « tu veux choisir ton premier compagnon ? ») et propose « Choisir un Tifazelt » alors que le starter est déjà pris (le bouton lance bien la revanche). Il faut une réplique de revanche.
4. **Interface** : le nom « Avalanche Torrentielle » dépasse de sa carte d'attaque ; le toast « Zéphir a gagné cette fois… » dépasse de l'écran à droite ; le signe moins devant les dégâts (-3, -4) s'affiche comme un glyphe étrange.
5. **Vocabulaire de laboratoire** resté dans l'écran du starter à Bourg-Azur (« Plateau stérile ») et dans le dialogue (« venu de mon laboratoire »).
6. **Chambre** : un carré bleu incliné sur le mur (poster ou décor provisoire ?) et le personnage a les jambes pliées à l'apparition (pose de départ à vérifier).
7. **Titre du jeu** : l'écran titre affiche « AZZURSAL » alors que le jeu s'appelle Tifazelt (à confirmer, nom provisoire ?).

Vérifié sans défaut : écran titre → Nouvelle partie → création → classes → départ dans la chambre (3 000 TFD, objectif) ; sortie par la porte magique ; invite « Parler » (E) du Professeur et dialogue ; choix du starter ; combat ouvert ; invite « S'asseoir » (F) sur un banc ; 69 PNJ conformes côté serveur (Shirt, Pants, visage, accessoire, invite, aucun script) ; aucune erreur de jeu dans la console. Limites : le streaming charge tous les PNJ mais pas toutes leurs parties à distance, rendu vérifié de près seulement sur le Professeur et Lina.
- **Saisie :** vrais clics, manette, mobile, saisie du nom au clavier.
- **Invites :** les invites (ProximityPrompt) pressées à la main ; Studio ne les simule pas.
- **En ligne :** deux vrais joueurs (Test > Clients et serveurs), déconnexion en combat, délai de 60 s, amis Roblox.
- **Jouabilité :** la pêche à la main, la descente à la nage, la remontée quand l'air manque.
- **Performances :** sur un appareil modeste.

## Modèles 3D de la lignée Cramosaur (26 oct. 2026) — PROVISOIRE
- **Tailles** choisies sans référence dans le vault : Cramosaur ≈ 1,07 m de haut ; Cramoraptor et Cramorex à fixer (proposition : ≈ 1,8 m et ≈ 3 m).
- **Pas d'armature ni d'animation** : modèles statiques. À décider : rig (et lequel) avant l'animation en jeu.
- **Découpage pour Roblox** : un objet par matériau (lave séparée pour pouvoir la mettre en Neon). Import dans Studio non testé.
- Fichiers : `Claude outputs/Modeles 3D/Cramosaur/` (`.blend`, rendus, scripts de construction).

> Rappel : penser à **Ctrl+S** dans Studio après chaque séance.
