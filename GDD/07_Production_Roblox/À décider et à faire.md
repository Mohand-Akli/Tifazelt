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
- **Habillage et starter (testé en Play le 26 oct. 2026 par Claude, nouvelle partie complète) :** voir « Bugs relevés en Play » ci-dessous. Reste à voir : le rendu des 69 PNJ un par un (seuls le Professeur et Lina vus de près). Victoire du combat d'apprentissage atteinte en Play (Aqualune, puis Pyrofennec le 26 oct. au soir).

### Bugs relevés en Play (26 oct. 2026) — tous traités le 26 oct. 2026
Sauvegardes avant correction : `ServerStorage.Sauvegardes_UI.*_avant_bugs_2026-10-26` (Kit, Panneaux, Combat, UI_Client, Starter, Regles, NouvellePartie), `Vue_avant_correctif_ColorMap`, et `ServerStorage.Sauvegardes_PNJ.Bugs_2026-10-26_avant` (affiche, carte, répliques du Professeur, de Maman et de Zéphir).

1. ~~**Combat d'apprentissage injouable.**~~ Corrigé (voir « Combat d'apprentissage et Zéphir » ci-dessous).
   - **Formule des stats par niveau (PROVISOIRE, le vault ne la donne pas)** : `Regles.statsNiveau` multiplie maintenant les stats par (niveau + 10) / (ancien niveau + 10), base au niveau 30 (`R.DECALAGE_NIVEAU = 10`). Niveau 5 : 37,5 % des stats du niveau 30 (Pyrofennec 34 PV au lieu de 93) ; niveau 1 : 27,5 % ; niveau 60 : 175 % (avant 200 %). Une montée de niveau donne toujours au moins +1. Touche aussi les bébés du Pâturage (niveau 1) et les Tifazelts au-dessus du niveau 30.
2. ~~**Perdre le combat d'apprentissage coûte 150 TFD.**~~ Corrigé (PROVISOIRE) : contre Zéphir, la défaite ne coûte rien, l'équipe est soignée et le joueur reste sur place (« Continuer »). Les autres défaites ramènent maintenant vraiment **devant le comptoir de l'infirmière de Bourg-Azur** (3180, 903, 1211 ; attribut de workspace `RetourInfirmerie` pour déplacer ce point) au lieu du point d'apparition. **Testé en Play** : 3 000 TFD gardés contre Zéphir ; contre un dresseur, −150 TFD et arrivée à l'infirmerie.
3. ~~**Dialogue du Professeur après la défaite.**~~ Corrigé (PROVISOIRE) : répliques selon l'avancement (`UI_Client.lignesStarter`). Après une défaite : « Zéphir ne t'a pas fait de cadeau… » + bouton « Revanche contre Zéphir ». Après la victoire : réplique vers la Route 1, sans bouton. Zéphir aussi (« Tu veux ta revanche ? » / « On se revoit sur la Route 1 »). **Testé en Play.**
4. ~~**Interface.**~~ Corrigé : nom d'attaque long réduit automatiquement (« Avalanche Torrentielle » tient, testé) ; les toasts longs passent sur 2 ou 3 lignes au lieu de sortir de l'écran (`Kit.toast`, testé, y compris « Maman t'a donné 3 000 TFD… » qui débordait aussi) ; signe moins remplacé par un tiret moyen « – » (le tiret simple se collait au chiffre avec le contour ; testé : « –4 »).
5. ~~**Vocabulaire de laboratoire.**~~ Corrigé : « Tiflasks de départ » au lieu de « Plateau stérile » à Bourg-Azur ; Professeur : « Je suis venu jusqu'à Bourg-Azur avec trois Tiflasks » ; Maman : « venu exprès pour toi ». Gardé : Céleste, Romain et Ayla parlent de Val Palmeraie et du laboratoire (lore, pas l'écran du starter).
6. **Chambre** : le carré bleu était une affiche vide (`MaisonJoueur.Affiche`) et la carte claire à côté aussi (`CarteDresseur`). Elles ont maintenant un dessin (PROVISOIRE) : affiche « Luméridia — Bourg-Azur » (ciel, soleil, mer, collines) et carte de dresseur épinglée, chacune dans un cadre en bois. **Non vérifié à l'écran** (Studio n'affichait plus la 3D pendant le test). Jambes pliées : le personnage joue la pose de repos du pack Cartoony (choisi le 20 oct.), qui a les genoux fléchis ; état « Running », bien posé au sol. Pas de changement : à confirmer par Mohand.
7. **Titre « AZZURSAL »** : pas modifié. Le vault appelle le projet « Azzursal (Tifazelt) » (README, Accueil, Charte graphique) et Azzursal est la région. **À décider par Mohand** : titre du jeu « Azzursal » ou « Tifazelt ».
8. **Nouveau bug trouvé et corrigé : combat bloqué dès que le starter a un modèle 3D.** `Tifazelts.Vue` (style « dessin ») écrivait `SurfaceAppearance.ColorMap` pendant le jeu, ce qui est interdit hors plugin : erreur, puis le combat restait figé sur « À toi, Pyrofennec ! ». Correctif : une SurfaceAppearance `SA_Dessin` préparée dans chaque modèle de `Tifazelts.Modeles`, que la Vue clone à la place de l'originale. **Testé en Play** : le combat se déroule, aucune erreur. Aspect du modèle non vu (3D non affichée).
9. **Remarque** : sur l'écran « Nouveau dresseur », le cadre « Apparence » était vide pendant le test (sans doute la même absence de rendu 3D que plus haut). À revoir quand Studio affiche la 3D.

### Combat d'apprentissage et Zéphir (PROVISOIRE, 26 oct. 2026)
- **Règle du vault gardée** : Zéphir prend le starter qui a l'avantage (`00. Définition`). Un rival « neutre » n'existe pas avec trois starters en triangle.
- **Tifazelt de Zéphir affaibli** (`UI.NouvellePartie.adversaireTutoriel`) : une seule attaque, la plus faible qui fait des dégâts, sans drain ni soin (Aqualune → Brume scintillante, Florépine → Forêt Enchevêtrante, Pyrofennec → Brise Ardente). PV = 3 coups moyens de la meilleure attaque du starter (`N.COUPS_TUTORIEL = 3`, soit 10 à 14 PV). Simulation : 97 à 100 % de victoire en jouant au hasard. Testé en Play avec Aqualune : victoire en 5 tours, 37/93 PV restants, +200 TFD, objectif « Premiers pas — Explorer la Route 1 ».
- **Zéphir visible sur la carte** : `Workspace.Map.Starter_BourgAzur.Zéphir Célestin` (clone de Théo, scripts retirés), dans la rue devant le portail de la maison familiale (2135, 5, 1518), tourné vers le Professeur. Tenue H16 veste zippée azur + B07 survêtement, visage V03, cheveux CoolBoyHair (bleus). Tag `PNJ_Bourg`, `Service = Rival`, « Combattre » : sans starter → « Choisis d'abord ton Tifazelt », starter sans victoire → combat d'apprentissage, après victoire → « On se revoit sur la Route 1 ». Placé à 20 studs du Professeur, parce que deux invites « Parler » en AlwaysShow à moins de 18 studs se déclenchent ensemble (le Professeur prenait la main).
- À valider par Mohand : tenue, cheveux bleus, répliques, emplacement ; Zéphir reste-t-il là après la victoire ?
- **Rééquilibrage du 26 oct. (soir), après la nouvelle formule des stats** : les PV du Tifazelt de Zéphir valent 3 tours moyens du starter joué au hasard (moyenne de ses 4 attaques, soutien = 0), et son attaque est plafonnée pour qu'il lui faille environ 8 coups (`N.COUPS_RIVAL = 8`). Simulation sur 1 000 combats joués au hasard : Pyrofennec 94 %, Aqualune 99,8 %, Florépine 100 %. **Testé en Play avec Pyrofennec** : défaite forcée, puis revanche gagnée en 3 coups d'Incandescence (30/34 PV), objectif « Premiers pas ».
- Non testé en Play : duel Florépine (seulement simulé), revanche lancée depuis Zéphir après une défaite.

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
