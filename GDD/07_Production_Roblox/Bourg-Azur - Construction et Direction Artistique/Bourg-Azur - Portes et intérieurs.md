---
tags:
  - production
  - roblox
  - bourg-azur
---
# 🚪 Bourg-Azur — portes et intérieurs

> [[Bourg-Azur - Intention et direction artistique|← Intention et direction artistique]] · [[Bourg-Azur - Construction et Direction Artistique|Sommaire de la construction de Bourg-Azur]] · [[Bourg-Azur - Corrections et extensions|Corrections dans la ville et extensions du 19 oct. →]]

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

## 🏛️ 14. Refonte des intérieurs (20 oct. 2026)
> Générateur `ServerStorage.MapGeneration.BourgAzur.Passe3_Interieurs`. Anciens intérieurs sauvegardés dans `ServerStorage.Sauvegardes_Interieurs`. Captures avant/après : [[Captures 2026-10-20#Bourg-Azur — refonte des intérieurs (Guilde, Infirmerie, Café, Bazar, Fleuriste)]].

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
