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
- **Tifalistre (27 oct. 2026) :** les 20 Tifazelts nommés par Mohand (`Noms des Tifazelts (propositions)`) sont dans le jeu ; les Tifazelts de test inventés par Claude sont retirés. **PROVISOIRE** : numéros (lignée par lignée, starters d'abord : 1 à 3 Cramo, 4 à 6 Dauphi, 7 à 9 Garen, puis 10 à 20 dans l'ordre de la liste), stats de base, taux de capture, XP, courbes, descriptions, niveaux d'évolution (starters 16 et 36 ; Vipéclair 24, Lycombre 26, Oculoroc 28, Pierraiglon 20, Spectrocarte 30), types de Dauphiclos (Eau) et Garensouche (Plante) : double type seulement à la forme finale, comme Cramorex. À décider : ordre officiel (le vault dit « chronologique » ici et « numérique » ailleurs), stats et taux officiels.

### 🏪 Économie et services
- **Prix :** prix du Magasin, menu et recettes du Restaurant, salaire du Cuisinier (250 TFD, 3 services par visite).
- **Missions de la Guilde :** missions et récompenses. Elles donnent des **TFD ou des PC** ? La Liste des écrans dit PC, l'Économie réserve les PC au PvP.
- **Grades :** bornes à fixer, le vault se chevauche. Lecture retenue : Bronze 0-2, Argent 3-4, Or 5-6, Platine 7-8.
- **Investissement :** chantiers, paliers et nom de l'entreprise (« nom à définir »).
- **Gardiens :** niveaux et équipes des 8 Gardiens.
- **Reproduction :** temps d'éclosion (60 s), ce que le petit hérite, talents cachés.

### 🌅 Début de partie
- **Starters :** Garenbois (Plante), Dauphimyst (Eau/Psy), Cramosaur (Feu/Obscurité), choisis par Mohand le 26 oct. 2026 (remplacent Pyrofennec, Aqualune, Florépine). Fait le 26 oct. 2026 : renommés dans le jeu, niveau 5, attaques validées par Mohand et appliquées (détail dans `Claude outputs/Passation Cowork/Starters - plan.md`). Reste : modèles de Dauphimyst et Garenbois (à fournir par Mohand), duel Garenbois contre Zéphir à jouer en Play.
- **Cadeaux de départ :** 3 000 TFD de Maman et 5 Tiflask simples.
- **Classes :** combien on en choisit. Aujourd'hui : une principale et une secondaire.
- **Apparence :** apparence du joueur. Aujourd'hui : avatar Roblox et couleur de dresseur.
- **Combat d'apprentissage :** contre Zéphir Célestin, en place depuis le 26 oct. 2026 (PROVISOIRE, voir « Combat d'apprentissage et Zéphir » plus bas).
- **Lieu du starter (PROVISOIRE, 26 oct. 2026) :** le vault dit Laboratoire Arid à Val Palmeraie (gelé). En jeu : le **Professeur Arid Acanthus** attend devant la maison familiale de Bourg-Azur (`Workspace.Map.Starter_BourgAzur`) ; « Parler » → « Choisir un Tifazelt ». Ses répliques et celles de Maman sont provisoires.
- **Après la quête :** objectif suivant. Aujourd'hui (PROVISOIRE) : « Premiers pas — Explorer la Route 1 » (la Route 2 par la Porte du Sirocco est gelée avec Val Palmeraie).

### 🌐 En ligne
- **PvP :** PC par victoire (10, et +1 par victoire de suite) ; règles (équipes soignées, pas d'objets, choix auto après 60 s).
- **Échanges :** échanges d'objets ou seulement de Tifazelts.
- **Raid :** boss (Cobréclair niv. 35 depuis le 27 oct. 2026, avant Voltaneau, espèce de test retirée), PV, durée, récompenses, **lieu dans le monde**.
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
  - silhouettes de Laineux et Picoreurs (formes d'attente sans espèce depuis le retrait des Tifazelts de test le 27 oct. 2026 ; à remplacer par des Tifazelts de la liste quand leurs modèles existeront ; le panneau « Pâture des Laineux » reprend le nom du lieu dans le vault) ;
  - idées de la passe 3 non validées : bocage, moulin lointain, rebords à sens unique, etc.
- **Réglages visuels :** palette des troncs du bosquet, herbe 3D du terrain, `Lighting.Technology` à vérifier.
- **Val Palmeraie :** pistes « ville vivante » à valider.

### 🎨 Direction artistique et interface
- **Menus :** système de design (couleurs, tailles, animations), proposé et pas encore validé.
- **Bulles et carte « Secret trouvé » :** à passer aux couleurs de la Charte (Blanc carte, Terracotta).
- **Portraits :** depuis le 26 oct. 2026, les Tifazelts qui ont un modèle (lignée Cramosaur) ont un buste rendu dans Blender dans le cercle (`Kit.portrait`, tous les écrans) ; les autres gardent l'initiale (PROVISOIRE) en attendant leurs modèles. À valider : cadrage des bustes.
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
7. ~~**Titre « AZZURSAL »**~~ : Mohand a choisi « Tifazelt » (26 oct. 2026). L'écran titre affiche TIFAZELT, avec le bandeau « La région d'Azzursal » (PROVISOIRE, remplace « Le monde des Tifazelts »). Non vu à l'écran.
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
- **Affichage en combat (26 oct. 2026, soir)** : images pré-rendues dans Blender (`Tifazelts.Sprite`) au lieu de la 3D temps réel, jugée floue et terne par Mohand. Rendu mat et saturé (saturation 1,7) depuis la remarque de Mohand (« ni chromé ni néons »). À valider : rendu, niveau de saturation, taille (adversaire 1,3 × d, allié 1,55 × d), vitesse de respiration (8 images/s), vue de l'allié de 3/4 arrière. Cramoraptor et Cramorex faits le 26 oct. 2026 (testés dans un banc de combat, pas dans un vrai combat). À décider : taille relative des stades à l'écran, niveaux d'évolution, stats (PROVISOIRES dans `Combat.Especes`). À faire : Dauphimyst et Garenbois quand leurs modèles existeront. (Portraits Tifalistre / Équipe faits le 26 oct. 2026.)
- **Tailles** choisies sans référence dans le vault, appliquées dans le jeu : Cramosaur ≈ 1,1 m de haut, Cramoraptor ≈ 1,8 m, Cramorex ≈ 3 m. À valider.
- **Armature et animation** : rig de 21 os fait dans Blender et importé par Mohand le 26 oct. 2026 ; animations procédurales (`Tifazelts.Animation` : attente, marche, attaque, touché, K.O., apparition), utilisées par le Tifazelt qui suit le joueur. À valider à l'écran : la marche.
- ~~**Découpage pour Roblox** (modèles faits par Claude, lave séparée)~~ : sans objet, ces modèles ont été abandonnés le 26 oct. 2026 au profit des modèles Meshy fournis par Mohand, importés dans Studio.
- Fichiers : `Claude outputs/Modeles 3D/Cramosaur/` (`.blend`, rendus, scripts de construction).
- **Remplaçants des Tifazelts de test (27 oct. 2026, PROVISOIRE)** : Gardiens du Sanctuaire avec des Tifazelts de la liste au plus proche de leur type (aucun Tifazelt Insecte ni Glace nommé : Anto Solid et Icarius Crystalheart ont des équipes d'attente) ; pêche = Dauphimyst (seul Tifazelt Eau nommé) ; dresseurs de la Route 1 : attribut `EquipeJeu` (Gamin Léo Lycombre niv. 3, Gamine Inès Vipéclair niv. 2, Bastien Fennedune niv. 2, Sara Pierraiglon niv. 3, Scout Théo Spectrocarte niv. 4), le vault ne donnant que « Rongeur de base », « Insecte », « Oiseau de base » ; joueur test en ligne et œufs de test du Pâturage avec des Tifazelts de la liste. Répliques d'Aurèle et Karim et secret de la Sonnaille : « Tifazelts laineux » au lieu de « Laineux ».
- **Ouverture des combats de dresseur (27 oct. 2026, PROVISOIRE)** : le dresseur adverse apparaît en 3D, animé, à droite (`UI.CombatUI.Dresseur`). À valider par Mohand : cadrage et lumière, durée (l'ouverture reste 0,8 s de plus quand un dresseur est affiché), gestes (Zéphir bras croisés et visage fâché dessiné par Claude ; enfants et dresseurs : poing levé puis poing tendu ; Sara : mains sur les hanches ; réglables par les attributs `PoseCombat` et `HumeurCombat` du PNJ). Les Gardiens n'ont pas encore de personnage dans le monde : cercle avec l'initiale. En ligne : avatar de l'autre joueur (non testé, il faut deux joueurs).
- **Vélo (27 oct. 2026, PROVISOIRE)** : nouveau modèle en pièces (`Joueur.Velos`, vélo de ville « Azur ») et animation de sortie du sac. À valider par Mohand : allure, couleurs, taille du panier, animation (0,35 s pour sortir, 0,25 s pour ranger). Le vault ne dit rien des vélos (sortes, prix, magasin, obtention) : tout est PROVISOIRE.
- **Vélos et magasin de vélos (27 oct. 2026, PROVISOIRE)** : cinq vélos (Azur offert par Maman, Corail 3 500 TFD, VTT Sentier 7 500 TFD, course Éclair 12 000 TFD, Étoile 20 000 TFD ; vitesses 38 à 46) et un magasin « Vélos de l'Azur » au sud de la place de l'entrée de Bourg-Azur, avec un vendeur inventé (« Gilles, marchand de vélos », tenue H18 + B12, visage V01). À décider par Mohand : sortes de vélos, noms, prix, vitesses, avantage du VTT hors des chemins (aucun pour l'instant), emplacement et nom du magasin, nom du vendeur. Comme le reste du sac, les vélos achetés ne sont pas sauvegardés (pas de données joueur) et le serveur accepte le vélo demandé par le client.
- **Vérifications en attente de Mohand (27 oct. 2026)** : liste dans `Claude outputs/Passation Cowork/Vérifications de Mohand - 27 oct. 2026.md`. Textes « revanche » avant le premier combat corrigés le 27 oct. 2026 (drapeau `partie.perdu`, non testé en Play) ; palmier à environ 7 studs du coin de la terrasse du magasin (à déplacer ou à garder ?).
- **Lignée Cramosaur : v04 retenues par Mohand (27 oct. 2026)**. Les v03 ne sont plus dans le jeu (sauvegardées dans `ServerStorage.Tifazelts_Sauvegarde_v03`) ; `Tifazelts.Modeles` contient les v04 (trous réparés, retouche « E », lave lumineuse) ; images de combat v04 (réglage P2, 24 images en fondu) ; portraits v04. **PROVISOIRE, à valider par Mohand** : couleurs dans le monde (réglage « E ») et en combat (P2), durée d'une respiration (1,5 s). Détail : `Claude outputs/Passation Cowork/Lignée Cramosaur v04 - plan.md` et `v04, Tifalistre, PNJ, intro de combat et vélos - plan.md`.

- **Garenbois, première illustration (28 oct. 2026, PROVISOIRE)** : le vault ne décrit pas son apparence. Claude a rédigé un prompt dans le style des illustrations de Cramosaur et de Dauphimyst (lapin de garenne vert mousse, plaques d'écorce, petites ramilles en bois entre les oreilles, nervures de feuille dorées). Fichier : `Claude outputs/Illustrations Tifazelts/Garenbois - prompt de la première illustration.md`. À faire par Mohand : générer l'image avec son outil habituel et valider ou corriger le design.

## Portraits et Tiflask (26 oct. 2026) — PROVISOIRE
- **Portraits** des Tifazelts qui ont un modèle (Cramosaur, Cramoraptor, Cramorex) : buste rendu dans Blender dans le cercle de `Kit.portrait` (tous les écrans). Les autres gardent l'initiale.
- **Tiflask** : forme reprise de l'icône 2D du jeu (le vault ne décrit pas son apparence). Couleurs des liquides à valider : simple rouge-orangé, écume turquoise avec bulles, amitié rose. La Tiflask d'Amitié a une image et un modèle mais n'est ni en vente ni dans les règles du combat (bonus de capture et 250 de bonheur à brancher).
- **Base des systèmes** : `ReplicatedStorage.Tiflasks.Lancer` (lancer, ouverture, sortie et retour d'un Tifazelt). Branchée le 26 oct. 2026 sur la sortie d'un Tifazelt dans le monde (section suivante). Reste à décider : capture dans le monde (lancer sur un Tifazelt sauvage ?).
- **À vérifier avec de vrais clics** : pendant les tests pilotés par commandes, les menus restaient parfois bloqués (gestionnaire « occupé » : titre qui ne se ferme pas, inventaire qui ne s'ouvre pas). Probablement dû au pilotage de Studio, mais à confirmer en jouant normalement.

## Tifazelt qui accompagne le joueur (26 oct. 2026) — PROVISOIRE
Le vault ne dit rien d'un Tifazelt qui suit le joueur hors combat. Détail : `Claude outputs/Passation Cowork/Sortie du Tifazelt - plan.md`.
- **Commandes** : touche **R** (PC), **croix bas** (manette), bouton rond **SORTIR / RENTRER** (mobile, au-dessus de COURIR) pour sortir le leader ou rentrer celui qui est dehors ; bouton « Sortir » / « Rentrer » dans la **Fiche** de chaque membre (le menu se ferme pour qu'on voie le lancer). Aide à l'écran au-dessus du bouton MENU (« R · Sortir Cramosaur », croix dessinée à la manette), cachée sur mobile, en intérieur et quand le leader ne peut pas sortir. À valider : touches, emplacement du bouton mobile et de l'aide.
- **À surveiller** : en fin de séance du 26 oct. 2026, Studio déconnectait le client de test du serveur à chaque Play (« readRegionRemoval error total time exceeded »), même avec les anciennes versions des scripts. Un redémarrage de Studio a réglé le problème ; si ça revient, regarder le streaming du terrain.
- **Scène** : Tiflask lancée depuis la main, Tifazelt qui grandit depuis la fiole, suivi derrière le joueur et un peu à droite, regard vers le joueur à l'arrêt ; rentrée dans une Tiflask qui apparaît dans la main.
- **Geste et sons (26 oct. 2026, soir)** : geste de lancer par-dessus la tête et geste de rappel (bras tendu), procéduraux, vus par tous les joueurs (`Joueur.Gestes`). Sons Pro Sound Effects placés dans le monde : souffle, tintements, pop du bouchon, « pouf » et scintillement, aspiration (détail dans `Claude outputs/Animations, déplacements et audio.md`). **À valider** : le geste à l'œil, chaque son à l'écoute (choisis sur leur titre et sur leur volume mesuré, pas écoutés).
- **Apparence** : modèle 3D avec la texture retouchée (`SA_Retouche`), pas les images du combat. Le Tifazelt traverse les obstacles (aucune collision).
- **Règles** : seules les espèces avec un modèle 3D peuvent sortir (lignée Cramosaur pour l'instant ; les autres : « ne peut pas encore sortir de sa Tiflask »). Refus si K.O. ou en intérieur. Rentre tout seul s'il tombe K.O., s'il quitte l'équipe ou à la mort du personnage ; en intérieur il rentre et ressort tout seul à la sortie ; après une évolution, la nouvelle forme ressort. Sur le vélo il suit plus vite et réapparaît près du joueur s'il est à plus de 50 studs.
- **Tiflask de sortie** : celle de la capture (champ `tiflask` posé par le moteur de combat) ; starter et Tifazelts plus anciens : Tiflask simple. À décider : Tiflask propre au starter ?
- **Bug corrigé en route** : à l'évolution, `Combat.Moteur.evoluer` changeait le nom mais pas le champ `espece` (les Tifazelts créés par `Especes.creer` en ont un). Les images de combat et le portrait de la forme évoluée auraient montré l'ancienne forme. Sauvegarde : `Sauvegardes_UI.Moteur_avant_compagnon`.


## Panneau d'équipe en exploration (26 oct. 2026) — PROVISOIRE
Demande de Mohand d'après une capture de Cobblemon. Le vault ne décrit pas de panneau d'équipe dans le HUD. Détail : `Claude outputs/Passation Cowork/Panneau d'équipe - plan.md`.
- **Place** : bord gauche, centré en hauteur. Six cartes biseautées : numéro de touche, portrait, nom, niveau, PV, Tiflask (ouverte si le Tifazelt est dehors). Choisie : la carte avance, liseré terracotta. Dehors : liseré cyan, étiquette « DEHORS ». K.O. : grisée.
- **Commandes** : touches 1 à 6, croix gauche / droite, clic. R / croix bas / bouton mobile agissent sur le Tifazelt choisi (et non plus sur le leader).
- **À valider** : place et taille du panneau, toujours affiché (ou à replier ?), touches 1 à 6 (à vérifier avec le sac de Roblox s'il est actif), croix gauche / droite.
- **Testé en Play le 26 oct. 2026** (touches 1 à 6, croix, clic, R, K.O., intérieur, menus). Non testé : affichage manette et tactile.

## Bourg-Azur parfait (28 oct. 2026) — audit fait, corrections à venir
Demande de Mohand : régler tous les problèmes de Bourg-Azur (textures, chemins). Liste complète et étapes : `Claude outputs/Passation Cowork/Bourg-Azur parfait - plan.md`.
- **Trouvé** :
  - 802 paires de faces qui scintillent à l'extérieur (dont 196 bordures de rue et 249 sur les vélos exposés) et 181 dans les six intérieurs (comptage refait le 28 oct. 2026 avec `Claude outputs/outils/Bourg-Azur - détecteurs.lua`) ;
  - sentier de la Route 1 qui contourne l'arche ;
  - sentier de l'oliveraie qui bute contre une maison, mur de l'oliveraie avec deux trous ;
  - bancs, buisson, lampadaires et panneau sur les chaussées ;
  - objets qui flottent (buisson à 6 studs, olivier millénaire, barque) ;
  - table de pique-nique sur un toit ;
  - maison 111 collée à la maison du joueur ;
  - PNJ légèrement enfoncés ou flottants ;
  - étiquettes d'édition (« PortSaphir (Ø 720) »…) visibles dans le ciel (réglé à l'étape 1).
  - laisse de mer de la plage (plaques de sable humide, algues, coquillages) posée à plat : une partie flotte sur la mer (à reposer à l'étape 4).
- **Avancement** : étape 1 faite (étiquettes rangées) ; étape 2 faite (plus aucun scintillement visible à l'extérieur, vélos et magasin de vélos corrigés à la source). Étape 3 faite (plus aucun scintillement dans les six intérieurs ; étagère du Bazar posée au sol ; piliers de la Guilde déplacés entre les fenêtres). Étape 4 faite (chaussées dégagées, laisse de mer reposée sur le sable, barque dans l'eau, table de pique-nique descendue du toit, PNJ au sol). Étape 5 faite (ruelles débarrassées des demi-disques, fontaines des placettes refaites, portail du Pâturage dégagé ; générateurs corrigés). Prochaine : étape 6, ajouts (descentes vers la plage).
- **À décider** :
  - ~~Étiquettes d'édition : `ServerStorage` ou cachées en jeu ?~~ Décidé par Mohand (28 oct. 2026) : rangées dans `ServerStorage.BourgAzur_Sauvegarde_Parfait.Etape1_EtiquettesEdition` (fait, étape 1).
  - Ciel `Ciel_Route1` : une traînée de cubes près du soleil peint fait partie de l'image ; le garder ?
  - Ajouts proposés (PROVISOIRES) : descentes vers la plage depuis la Promenade et bancs face à la mer.

> Rappel : penser à **Ctrl+S** dans Studio après chaque séance.
- **Lignée du Dauphin, modèles 3D (28 oct. 2026, PROVISOIRE)** : Dauphimyst, Dauphiclos et Dauphiracle identifiés, réparés et allégés à 10 000 triangles dans `Claude outputs/Modeles 3D/Dauphin/Lignee_Dauphin.blend` (plan : `Claude outputs/Passation Cowork/Lignée Dauphin - plan.md`, étapes 1 à 3 faites). Dauphiracle refait avec le fichier texturé fourni par Mohand (la texture provisoire inventée est abandonnée, sauvegardée). Rig fait le 28 oct. : squelette de 14 os (16 pour le Dauphiracle), noms repris des Cramosaur quand l'os existe (compatible `Tifazelts.Animation`), plus `Aileron` et, pour le Dauphiracle, `NageoireG`/`NageoireD` (PROVISOIRE). **Demande de Mohand (28 oct.)** : les trois dauphins se déplacent en **nageant dans les airs**, comme s'ils volaient : animation de flottement et de nage aérienne à faire à l'étape 4 (amplitude, hauteur de vol, vitesse : PROVISOIRES). **Étapes 4, 5, 7 et 8 faites le 28 oct. 2026 (PROVISOIRE, rien testé en Play)** : modes `flotte` et `nage` dans `Tifazelts.Animation` (amplitudes, périodes, hauteur de flottement à valider) ; couleurs : réglage **B** (saturation 1,3, sans lueur) retenu en attendant le choix de Mohand (`Dauphin/Rendus/Variantes_couleur_planche.jpg`) ; sprites de combat (24 images par vue), portraits et entrées `Tifazelts.Catalogue` faits, échelles à l'écran PROVISOIRES (taille voisine des Cramosaur, Cramoraptor, Cramorex). Couleurs refaites (saturation 0,8, proches des illustrations, à la demande de Mohand) ; étape 6 faite : modèles dans `Tifazelts.Modeles`. **PROVISOIRE** : longueurs 6,5 / 10,5 / 15 studs, échelles en combat, hauteur de vol du Tifazelt qui suit (attribut `Vol` : 2,5 / 3 / 3,5 studs). 28 oct. (soir) : dauphin écrasé corrigé (os pas agrandis), textures du monde éclaircies, combat à 45 images par vue (30 i/s + fondu, choix de Mohand) pour les 6 Tifazelts, clignotement des sprites corrigé (préchargement), équipe de test = les 6 Tifazelts modélisés (stats et attaques PROVISOIRES). Reste : tests en Play par Mohand (étape 9), mémoire sur mobile.
