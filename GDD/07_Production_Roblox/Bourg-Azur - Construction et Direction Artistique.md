---
tags:
  - production
  - roblox
  - monde
  - ville
  - lumeridia
  - bourg-azur
  - direction-artistique
  - roblox
aliases:
  - DA Bourg-Azur
  - Construction Bourg-Azur
---
# 🎨 Bourg-Azur — Construction et Direction Artistique

> Compte rendu détaillé de la **passe 2** de Bourg-Azur dans Roblox Studio (octobre 2026), réalisée par Claude.
> Fiche de lore et plan général : [[Bourg-Azur]]. Charte des interfaces : [[15. Charte Graphique]].
> Ce document décrit ce qui a **réellement** été construit et testé, et les intentions artistiques derrière chaque choix.

---

## 🧭 1. Intention générale

Bourg-Azur est le **village natal** du joueur : c'est le premier lieu qu'il voit et celui où il revient. La passe 2 avait trois objectifs :

1. **Rendre le village habitable** : des intérieurs dans lesquels on entre vraiment, des bancs où l'on s'assoit, des habitants à qui l'on parle.
2. **Rendre le village crédible** : corriger ce qui trahissait la construction (balcons enfoncés, murs qui brillaient de l'intérieur, objets qui flottaient, enseignes cachées, chemins qui ne menaient nulle part).
3. **Rendre le village agréable à parcourir** : remplir les espaces verts sans encombrer les rues, ajouter de petites surprises pour les joueurs curieux.

**Ambiance visée :** un bourg côtier méditerranéen (Algérie, Grèce, sud de l'Italie) en *low poly* stylisé. Chaux blanche adoucie, volets bleu azur, bougainvillées magenta, terracotta, oliviers et palmiers. La lumière est chaude et lisible, sans éblouir.

---

## 🎨 2. Direction artistique

### 2.1 Principes
- **Formes simples, aplats de couleur.** Aucune texture réaliste ajoutée. Seuls les matériaux Roblox de base sont utilisés pour donner du grain : bois, planches, tissu, ardoise, herbe, verre et métal.
- **Lisibilité avant détail.** Les rues principales, la place et les entrées restent dégagées. Le détail se concentre près des façades, des commerces et des points d'intérêt. Les espaces verts gardent de l'air.
- **Pas de néon éblouissant.** Les lanternes des lampadaires sont passées du néon blanc à un verre chaud mat. La seule lueur volontaire est celle des portes magiques, limitée et progressive.
- **Pas de blanc pur.** Le blanc de chaux éblouissait sous le soleil de Luméridia. Les 459 surfaces blanc pur sont devenues un blanc cassé chaud.
- **Variété sans chaos.** Tailles, orientations et groupements varient, mais chaque groupe suit la même palette.

### 2.2 Palette de la ville

| Usage | Couleur (RVB) | Remarque |
|---|---|---|
| Chaux des façades (blanc adouci) | 240, 235, 224 | remplace le blanc pur (255) |
| Bleu azur des volets et des portes | 36, 74, 140 / 60, 110, 170 | identité de Bourg-Azur |
| Turquoise du Café des Embruns | 36, 140, 150 | enseigne, porte, comptoir |
| Vert du Fleuriste | 70, 130, 80 | enseigne, porte |
| Terracotta (pots, toits, jardinières) | 186–190, 104–106, 74–76 | proche du Terracotta de la charte (#C18358) |
| Pierre claire de la fontaine | 226, 214, 190 / 240, 232, 214 | margelle et vasques |
| Eau | 70, 170, 198 | verre semi-transparent |
| Feuillages | 66–104, 124–160, 66–84 | quatre verts mélangés |
| Fleurs | rose 240,90,120 · jaune 250,210,80 · lilas 160,110,220 · blanc 250,250,240 · orange 240,130,60 | massifs et prairies |
| Bois (bancs, mobilier) | 150, 108, 74 / 110, 78, 56 | deux tons, clair et foncé |
| Lueur des portes | 255, 190, 120 (dehors) / 214, 236, 255 (dedans) | chaude en entrant, « lumière du jour » en sortant |

### 2.3 Lumière
- **Extérieur :** les réglages globaux de Luméridia sont conservés (étalonnage de la Route 1, Atmosphere, Bloom léger). Les **52 lampadaires** ont une lumière plus douce (luminosité 0,8, portée 24, sans ombres).
- **Murs « éclairés de l'intérieur » :** les plafonniers des anciens intérieurs (luminosité 1,6, portée 22) traversaient les murs. Leur suppression a réglé le problème.
- **Intérieurs :** au plus 2 à 3 points lumineux chauds par pièce (luminosité 0,3, portée 24 ; 0,36 et 28 dans la Guilde), sans ombres. Le reste vient de la lumière ambiante. Les fenêtres intérieures sont des vitres « jour diffus » qui n'émettent aucune lumière.
- **Ambiance intérieure (20 oct.) :** dès que le joueur est dans un intérieur, le script client `Interieurs_Ambiance` coupe la brume extérieure (Atmosphere), retire les rayons du soleil, renforce un peu la lumière ambiante et ajoute un léger étalonnage chaud. Tout revient en 0,35 s quand il sort.
- **Enveloppes :** chaque intérieur est entouré de blocs épais, invisibles pour le joueur. Sans eux, la lumière turquoise du ciel traversait les murs et plafonds de 1 stud (l'éclairage de Roblox travaille par cases de 4 studs) et donnait une teinte verte aux pièces.

---

## 🚪 3. Le système de portes et d'intérieurs (façon Pokémon)

### 3.1 Principe
Le bâtiment visible dans la rue ne sert que de façade. L'**intérieur jouable** est une pièce séparée, plus grande que ce que l'extérieur laisse imaginer, placée hors de vue au-dessus de la carte (dossier `Workspace.Interieurs`, à 900 studs d'altitude).

### 3.2 Ce que voit le joueur
1. Il s'approche d'une porte : à environ 11 studs, le **battant s'entrouvre** (rotation de 38°, poignée comprise).
2. Une **lueur chaude** apparaît dans l'ouverture, comme une pièce éclairée derrière. C'est un simple panneau lumineux qui apparaît en fondu : ce n'est pas une vraie lampe.
3. Il franchit le **seuil** : il est téléporté devant la porte intérieure, tourné vers la pièce.
4. Pour sortir, il revient vers la porte intérieure, qui s'ouvre sur une lueur « lumière du jour ». Il réapparaît **7,5 studs devant la façade**, tourné vers la rue.

### 3.3 Façades
- L'ancien intérieur visible a été retiré (74 pièces dans la maison, 40 à l'infirmerie, 46 au café…).
- Un **volume sombre** ferme la vue derrière les fenêtres. On ne voit plus de pièce vide par les vitres.
- Les portes ouvertes d'origine ont été remplacées par de vrais battants en bois. Les entrées larges, comme l'Infirmerie et la Guilde, ont des **portes doubles**.

### 3.4 Fiabilité (technique)
- Un seul script serveur gère toutes les portes (`BourgAzur_Portes`) et un seul script client gère les animations (`BourgAzur_Client`) : pas de script par porte.
- C'est le serveur qui décide de la téléportation. Il vérifie que le personnage est vivant, qu'il n'est pas assis, qu'il se trouve vraiment sur le seuil et que la destination existe. Il charge la zone d'arrivée avant de déplacer le joueur.
- **Anti-boucle :** un délai par joueur empêche les téléportations répétées, et un nouvel essai automatique se lance si le joueur reste sur le seuil. Chaque joueur est géré séparément, donc le système fonctionne en multijoueur.

### 3.5 Les six intérieurs

| Bâtiment | Taille (studs) | Ce qu'on y trouve |
|---|---|---|
| **Maison du joueur** | 44 × 36 | Salon (canapé, table basse, meuble TV, bibliothèque, lampadaire, tapis), cuisine et salle à manger (plan de travail, frigo, évier, plaques, placards, table et 4 chaises), **chambre du joueur** (lit, chevet, bureau et ordinateur, armoire, affiche), **chambre de la mère** (lit double, deux chevets, commode avec miroir, photo), entrée (porte-manteau, meuble à chaussures). C'est ici que **le joueur apparaît** au début de la partie. |
| **Infirmerie Tifazelt** | 48 × 38 | *Refaite le 20 oct.* **Coupole** polygonale (16 × 5 panneaux, nervures dorées, oculus) au-dessus de l'entrée, tapis d'accueil, comptoir en arc (marbre, bandeau rouge, écran « Fiches dresseurs », registre, sonnette, bouquet), infirmière sur une estrade, **station de soin** (6 fioles de couleur dans leurs alvéoles sous un dôme de verre, écran « Soins 6/6 prêts »), enseigne « Infirmerie Tifazelt » avec croix verte, deux armoires à pharmacie vitrées, chariot de soins. Salle d'attente : deux bancs face à face avec coussins, table basse (magazines, bouquet), fontaine à eau, deux affiches, plantes. Espace médical : 3 lits avec chevets, séparés par des rideaux sur tringles, perfusion. |
| **Guilde des Dresseurs** | 56 × 42 | *Refaite le 20 oct.* Charpente apparente (poutres, corbeaux, piliers), fenêtres hautes, tapis bleu et or, **terrain d'entraînement** tracé au sol, comptoir bleu et or sur une estrade (registre, plume, sonnette), grand emblème or et bleu, ruban « Guilde des Dresseurs », 2 bannières, 2 étagères de rouleaux, **tableau « Avis de missions »** avec pupitre, **coin Échanges** (panneau, table ronde, 2 chaises), **salle commune** (grande table avec la carte de la région, 2 bancs de 4 places), vitrine des trophées (coupes, médailles, plaque « Palmarès »), caisses et tonneau, 3 lustres en bois. *Corrigé le 28 oct. 2026* : piliers des deux murs longs déplacés entre les fenêtres (z = 1206, 1214, 1227,2 et 1239,5 ; celui du milieu retiré et sauvegardé), car ils coupaient les fenêtres, le tableau, l'enseigne et la vitrine ; tableau et pupitre recentrés sous la fenêtre du milieu. |
| **Café des Embruns** | 44 × 34 | *Refait le 20 oct.* Sol en tomettes, soubassement turquoise, poutres. Bar turquoise à lattes avec repose-pied en laiton, **vitrine de pâtisseries** (brioches, tartelettes, croissants), 5 tabourets, 3 suspensions au-dessus du bar. Arrière-bar : **machine à café en cuivre** (dôme, groupes, manomètre), moulin, théière, étagères de bocaux, bouteilles et tasses, **ardoise « Thé des marins · Café salé · Brioche de l'Azur »**. Salle : 5 tables rondes (10 chaises) sous des suspensions en cuivre. Décor marin : filet et flotteurs, bouée, rames croisées, coquillages, tableau de la mer. |
| **Fleuriste** | 34 × 28 | *Refaite le 20 oct.* Tomettes, soubassement vert, poutres claires. **Gradins de pots** à 3 marches (mur gauche) et 2 marches (mur droit), table centrale avec 4 seaux de bouquets et étiquette, **comptoir avec rouleaux de ruban**, papier kraft, ciseaux, bouquet prêt, **arrosoir**, 3 **paniers de lierre suspendus**, **bougainvillée** sur treillage, jardinière à la fenêtre. |
| **Bazar de l'Azur** | 40 × 30 | *Refait le 20 oct.* Comptoir avec **caisse enregistreuse**, balance et bocal de bonbons ; enseigne suspendue « Bazar de l'Azur » ; étagère derrière Léon (potions, fioles, bocaux, boîtes) ; **grande étagère à 4 rayons** étiquetés Soins / Tiflasks / Vivres / Outils ; banc à paniers de fruits et objets suspendus (lanternes, cordes) ; table d'exposition (paniers de baies, fioles, ardoise « Promo du jour ») ; caisses et tonneaux. La **peluche Tiflask** (secret) est sur le rayon Outils, en hauteur. |
---

## 🏘️ 4. Corrections dans la ville

| Problème | Correction |
|---|---|
| Plante qui gênait l'entrée de la maison | supprimée |
| Murs et plafonds qui semblaient éclairés de l'intérieur | plafonniers intérieurs supprimés, blanc pur adouci |
| Spawn devant la maison | spawn dans la chambre du joueur, posé au sol, sans meuble autour |
| Balcons enfoncés dans les façades (84) | réalignés sous leur porte-fenêtre et décollés du mur de 0,12 stud ; 83 appuis de fenêtre qui se superposaient retirés |
| Fleurs de façade collées au mur et qui scintillaient (144) | décollées du mur avec un léger décalage aléatoire contre le scintillement, sans collision |
| Enseigne du Café des Embruns | refaite (fond turquoise, cadre en bois, texte face à la rue, tasse de café à côté) |
| Enseigne du Fleuriste cachée par le balcon | redescendue au-dessus de l'auvent, dégagée du balcon ; même correction pour l'Épicerie, la Librairie et le Tisserand |
| Chaises et parasols du café qui flottaient | 12 objets reposés au sol, objet par objet |
| Phare hors sujet, trop petit et trop loin | retiré ; le bout du ponton devient un **ponton de pêche** (banc face à la mer, casiers, bitte d'amarrage) |
| Sortie vers la Route 1 asymétrique | portique réaligné sur l'axe du sentier de la Route 1, massifs symétriques, dallage de transition avec bord en pente douce ; passage testé dans les deux sens |
| Anneau de terre géométrique autour de la ville, qui ne menait nulle part | repeint en herbe (les vraies routes ne sont pas touchées) |
| Pas d'accès au champ ni à l'oliveraie | deux chemins de terre au tracé courbe, bordés de pierres et de touffes d'herbe, avec un panneau au départ ; deux murets de l'oliveraie ouverts |
| Lampadaires trop petits | **+35 %** de hauteur, base recalée au sol, style conservé |

---

## ⛲ 5. La fontaine de la place

L'ancienne fontaine (bassin, colonne, vasque) était trop petite pour la place. La nouvelle est pensée comme le **cœur visuel** du village :
- **Bassin octogonal de 21 studs** en pierre claire, avec une margelle couronnée sur laquelle **on peut s'asseoir** (4 places).
- **Deux vasques superposées** sur une colonne, surmontées d'une pomme bleu azur.
- **Eau animée par des particules** légères : un jet au sommet, une nappe qui déborde de chaque vasque et une fine brume à la surface du bassin, soit 4 émetteurs au total.
- **Secret :** quelques pièces dorées au fond du bassin, côté nord, et une inscription presque effacée sur la margelle.

---

## 🌳 6. Paysage et mobilier : remplir sans encombrer

**Règle de placement :** tout ajout est contrôlé par une vérification d'espace libre. Rien n'est posé sur une route, contre une porte ou dans une maison. Les groupes sont espacés d'au moins 20 studs pour garder de l'air.

- **Abords des commerces :** chaque boutique a un décor à son image, de chaque côté de la porte et jamais devant.
  - Épicerie : cageots de fruits et tonneau.
  - Boulangerie : ardoise « Pain chaud ! » et jardinière.
  - Potier : amphores et cageot.
  - Librairie : chariot de livres.
  - Fleuriste : seaux de fleurs.
  - Tisserand : rouleaux de tissu.
  - Bazar : tonneaux et cageot.
  - Café : ardoise du menu.
  - Infirmerie : jardinières.
  - Guilde : mâts à fanions bleus.
- **Espaces verts :**
  - environ 130 **bosquets** (arbres ronds, agrumes chargés de fruits, cyprès) ;
  - environ 170 **prairies fleuries** ;
  - environ 50 groupes de **rochers** ;
  - 34 compositions plus anciennes de la passe 2a.
- **14 coins repos :** un banc tourné vers le centre du village, un arbre d'ombre et un pot fleuri.
- **8 jardinets** clos de petites barrières blanches, avec des rangs de légumes.
- **Une balançoire** près de la placette nord.
- **Une table de pique-nique** au départ du chemin du champ.
- **Bord de mer :** une barque retournée sur le sable et un séchoir à filets.
- **Assises :**
  - où l'on peut s'asseoir : les 26 bancs de rue, la fontaine, la balançoire, le pique-nique, les coins repos, le ponton et les chaises, canapés et bancs des intérieurs ;
  - comment : l'invite « S'asseoir » assoit le joueur dans le bon sens, et il se relève en sautant. On ne s'assoit pas par accident en marchant.

---

## 👥 7. Les habitants (24 PNJ R6)

De **vrais personnages Roblox R6** (Humanoid, HumanoidRootPart et les 6 parties du corps), avec des coiffures, des chapeaux et des visages variés, et des tenues en aplats de couleur. Ils sont **immobiles** et sans script, donc sans coût permanent. Ils sont posés au sol (vérifié pour les 24). Ils ne bloquent ni les portes ni les rues. Une invite **« Parler »** affiche une bulle avec une réplique courte, en alternant 2 à 3 phrases.

| Lieu | Personnages |
|---|---|
| Grand-Rue (commerces) | Margot la boulangère, Hugo l'épicier, Anselme le potier, Céleste la libraire, Nadia la tisserande |
| Place et bâtiments publics | Rosalie et les enfants Théo et Lina près de la fontaine ; Kaël devant la Guilde ; Mamie Odile devant l'Infirmerie ; Victor, habitué du café |
| Porte de la ville | Romain le garde, Ayla la dresseuse qui part pour Val Palmeraie |
| Bord de mer | Gaspard le vieux marin au belvédère, Mila la pêcheuse au bout du ponton, Léa la promeneuse sur la promenade |
| Champ et oliveraie | Paulin le jardinier, Ondine la rêveuse |
| Intérieurs | Maman (maison), l'Infirmière Tifazelt, la Réceptionniste de la Guilde, Lou le barista, Inès la fleuriste, Léon le marchand du Bazar |
| Magasin de vélos (27 oct. 2026, PROVISOIRE) | Gilles, marchand de vélos, derrière le comptoir de « Vélos de l'Azur » (boutique ouverte au sud de la place de l'entrée, côté Route 1 ; générateur `MapGeneration.BourgAzur.MagasinVelos`, corrigé le 28 oct. 2026 : plus aucune face superposée, volets posés à l'extérieur du mur) |

Les dialogues orientent le joueur (vers le champ, l'oliveraie, le belvédère, Val Palmeraie, l'infirmerie avant la Route 1) et glissent quelques indices vers les secrets.

---

## ✨ 8. Les secrets (8)

Ce sont des secrets discrets, sans récompense, à découvrir en explorant. Une petite carte « Secret trouvé (n/8) » s'affiche à chaque découverte. Le compteur n'est pas sauvegardé.

1. **Le mot sur le frigo**, dans la maison.
2. **La carte dessinée** dans la chambre, qui renvoie vers la fontaine.
3. **L'inscription et les pièces** derrière le bassin de la fontaine.
4. **Le coffret** caché derrière le plus gros rocher de l'oliveraie. Ondine donne un indice.
5. **La pierre gravée** du belvédère.
6. **Le message dans une bouteille** sur la plage, qui renvoie vers Gaspard.
7. **Moustache, le chat du café** : il réagit différemment à chaque caresse.
8. **La peluche de Tiflask** du Bazar, « pas à vendre ».

---

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

---

## 🛠️ 12. Où trouver quoi (Roblox Studio)

| Élément | Emplacement |
|---|---|
| Générateur de la passe 2 | `ServerStorage.MapGeneration.BourgAzur.Passe2` et `Passe2b` (mode d'emploi `LISEZMOI_Passe2`) |
| Sauvegarde des éléments modifiés | `ServerStorage.BourgAzur_Sauvegarde_Passe2` |
| Intérieurs | `Workspace.Interieurs.<MaisonJoueur / Infirmerie / Guilde / Cafe / Fleuriste / Bazar>` |
| Générateur des intérieurs (refonte du 20 oct.) | `ServerStorage.MapGeneration.BourgAzur.Passe3_Interieurs` (Kit + une pièce par module, mode d'emploi `LISEZMOI`) |
| Sauvegarde des anciens intérieurs | `ServerStorage.Sauvegardes_Interieurs.<Nom>_avant` |
| Générateur des ruelles (Figuiers, Bougainvillées, Impasse du Levant, Chemin des Pêcheurs) | `ServerStorage.MapGeneration.BourgAzur.Passe3.Remplissage`, corrigé le 28 oct. 2026 : il dressait les raccords des ruelles et cassait les fontaines des placettes (rotation en trop, diamètre et hauteur inversés) |
| Chantier « Bourg-Azur parfait » (28 oct. 2026) | Plan et journal : [[Bourg-Azur parfait - plan]] ; détecteurs : `Claude outputs/outils/Bourg-Azur - détecteurs.lua` ; sauvegardes : `ServerStorage.BourgAzur_Sauvegarde_Parfait` |
| Ambiance intérieure (client) | `StarterPlayerScripts.Interieurs_Ambiance` |
| Portes et assises (serveur) | `ServerScriptService.BourgAzur_Portes` |
| Animations, bulles, secrets (client) | `StarterPlayerScripts.BourgAzur_Client` |
| PNJ | `Workspace.Map.CityPlots.BourgAzur.PNJ` (et dans chaque intérieur) |
| Décor ajouté | `BourgAzur.DecorPasse2`, `BourgAzur.DecorPasse2b`, `BourgAzur.Secrets`, `PublicSpaces.Acces` |

## 🧭 13. Mission du 19 oct. 2026 (place, moulin, littoral)
> Modules `ServerStorage.MapGeneration.Extensions.Bourg`, `.Littoral` et `.Campagne`. Sorties : `Workspace.Map.Extensions.Bourg_*`, `Littoral_*`, `Campagne_*`. Sauvegardes : `Extensions_Sauvegarde.{Bourg, Littoral}`.

- **Place centrale** : pavés usés, herbe entre les dalles, dalles abîmées ; 6 étals à auvents rayés, 4 réverbères en fer forgé, 4 bancs, pots et détails du quotidien.
- **Nord agricole** : grand moulin en bois sur le Petit Mamelon (ailes animées), 6 champs, clôtures en zigzag, épouvantail, charrette à roue cassée, outils, chemins ; 76 arbres isolés retirés, 479 éléments ajoutés au pied des groupes.
- **Débarcadère** (2658, 1948) : ponton élargi de 9 à 14 studs, plancher usé, bittes, caisses, tonneaux, cordages, filet, barque amarrée, cabane de pêcheur.
- **Laisse de mer** sur la côte du Bourg, la Plage de l'Estuaire et la Crique des Oliviers : bois flotté, algues, coquillages, rochers enfouis, sable humide.
- **Crique secrète** sous les falaises (x 978–1088, z 2740–2765) : plage, descente cachée de 7 marches rocheuses, vieux feu, coffre à demi enfoui (secret), restes d'épave.
- **Berges du fleuve** : 8 anses, boue et sable, 223 roseaux, 48 nénuphars.
- **Campagne** : Mas des Moissons (596, 2332) habillé, versants des collines, ornières et flaques sur la Route 1, 5 panneaux rustiques, 7 micro-points d'intérêt.
- **Presqu'île** : arbre mort monumental avec un creux (secret), enceinte en ruine, socle ancien, pierres gravées.
- Tests en jeu : aller-retour de la crique, bout du ponton, ailes du moulin qui tournent.
- Liste des secrets : [[Secrets d'exploration]]. Journal : [[Journal de construction de la carte]].

## 🏛️ 14. Refonte des intérieurs (20 oct. 2026)
> Générateur `ServerStorage.MapGeneration.BourgAzur.Passe3_Interieurs`. Anciens intérieurs sauvegardés dans `ServerStorage.Sauvegardes_Interieurs`. Captures avant/après : [[Historique des captures]] (section « refonte des intérieurs »).

- **Pièces refaites :** Guilde, Infirmerie, Café, Bazar et Fleuriste (détail au § 3.5). Chaque pièce garde sa porte magique, son point d'arrivée, son PNJ (avec ses répliques et son service) et ses secrets. La Maison du joueur n'a pas été refaite : elle a seulement reçu l'enveloppe qui corrige sa teinte.
- **Règles respectées :** 2 à 3 lumières chaudes sans ombres par pièce, vitres non émissives, aucune collision invisible. Les assises sont des sièges sans collision avec l'invite « S'asseoir » habituelle : on passe de 33 à 40 places. La zone d'arrivée devant la porte reste dégagée.
- **Bugs corrigés :**
  - la teinte verdâtre et la brume dans les pièces ;
  - les PNJ cachés derrière des comptoirs trop hauts : les comptoirs sont plus bas et les PNJ sont sur une estrade ;
  - Léon, qui était posé sur le point d'arrivée du Bazar ;
  - la caméra bloquée derrière la lueur de la porte à l'arrivée : l'écran devenait gris ;
  - les traînées de vent de la Route 1 qui apparaissaient à l'intérieur.
- **Choix à valider (PROVISOIRE) :**
  - les croix de soin de l'Infirmerie sont **vertes**, pour éviter l'emblème de la croix rouge, qui est protégé ;
  - l'arène de la Guilde est un **terrain rectangulaire**, pour éviter un motif de type Poké Ball ;
  - les textes « Coin Échanges », « Palmarès de la Guilde », « Promo du jour » et « Bouquets du jour », ainsi que ceux des deux affiches de l'Infirmerie.
- **Testé en jeu (Play) :**
  - entrée par la porte (Guilde, Infirmerie, Café, Bazar, Fleuriste, Maison) et sortie (Infirmerie) ;
  - brume coupée à l'intérieur puis rétablie à la sortie ;
  - s'asseoir sur un banc de la salle commune ;
  - dialogue avec la réceptionniste et avec l'infirmière, jusqu'au choix « Soigner l'équipe » ;
  - aucune erreur dans la console.
- **Limite observée :** à la toute première entrée dans une pièce, la teinte peut rester verte 1 à 3 secondes, le temps que Roblox recalcule l'éclairage.
- **Non vérifié :**
  - les services ouverts jusqu'au bout depuis le Café et le Bazar ;
  - le jeu sur mobile ;
  - le multijoueur ;
  - les performances sur un appareil modeste (environ 470 à 650 pièces par intérieur).
