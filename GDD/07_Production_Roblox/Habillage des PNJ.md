# Habillage des PNJ — table (refonte du 26 oct. 2026)

Table conçue à l'étape 3 du plan « Vêtements PNJ » (voir [[Vêtements PNJ et suite]]). **Appliquée dans Studio le 26 oct. 2026** (étape 4) : `Shirt`, `Pants`, Decal `face`, accessoire de cheveux soudé à la tête et attributs `Haut`, `Bas`, `Visage`, `Coiffure`. Sauvegarde de l'habillage précédent : `ServerStorage.Sauvegardes_PNJ.Habillage_avant_refonte`. Vérifié par les données (69/69). **Rendu en Play non vérifié.** Copie machine : `Claude outputs/outils/habillage_pnj.json`.

IDs des images : voir la note de passation. H29 et B22 sont introuvables : non utilisés.

## Règles
- Uniformes de métier : garde H24+B09, infirmière H25+B10, pêcheurs H20/H21+B23, boulangère H22, jardinier/maraîchère H23, Guilde H27+B08, labo/archéologie H26, Val Palmeraie H28+B26 (Sorlin seulement).
- Enfants (10, repérés par la taille du torse < 1,9) : hauts vifs, shorts ou jupes, visages V22/V23/V05/V06/V03. Jamais de barbe.
- Personnes âgées : V19, V20, V21 ou V24 ; pulls, cardigans, velours, jupes longues.
- Barbes et moustaches (V16–V19, V21) seulement sur des hommes adultes ou âgés. Pas de jupe sur les hommes.
- Aucun couple Haut+Bas répété, sauf les uniformes (pêcheurs, gardes) ; aucune tenue complète identique.
- Cheveux : 4 coiffures féminines seulement dans `Garderobe_Classique.Cheveux` (Kate, Sideswept, Ultra-Fabulous, Lavander), réparties pour que deux voisines n'aient pas la même. Hat1 (chapeau) réservé à Gaspard, Paulin et Augustin.
- Couleur de peau (BodyColors) inchangée.

## Corrections par rapport à l'habillage actuel
- Tom (enfant) avait une barbe de trois jours (V18) ; enfants habillés en adultes (Tom, Nour, Lou, Nina).
- Professeur Arid avait le visage « Grand-mère » (V20) → V24 Sage.
- Lou le barista avait une coiffure féminine (Kate Hair) → MessyHair.
- H09+B12 sur Augustin, Firmin et Karim (identiques) → trois tenues différentes.

## Bourg-Azur (25)
| PNJ | Profil | Haut | Bas | Visage | Coiffure (AssetId) | PROVISOIRE |
|---|---|---|---|---|---|---|
| Anselme, potier | homme | H10 Chemise en jean | B12 Travail | V18 Barbe 3 jours | MessyHairBrown (323476364) |  |
| Ayla, dresseuse | femme | H16 Veste zippée azur | B25 Legging | V09 Pétillante | Sideswept Bangs Brown (20573078) |  |
| Céleste, libraire | femme | H13 Pull torsadé | B18 Jupe plissée | V14 Lunettes rondes | Kate Hair (62724852) | sexe |
| Gaspard, vieux marin | homme âgé | H06 Marinière | B11 Velours | V21 Vieux marin | Hat1 (62234425) |  |
| Hugo, épicier | homme | H08 Chemise blanche | B27 Brique | V01 Sourire | Guy Hair (12270248) |  |
| Infirmière Tifazelt | femme | H25 Tunique infirmière | B10 Blanc | V08 Regard doux | Kate Hair (62724852) |  |
| Inès, fleuriste | femme | H30 Blouse rose | B20 Jupe fleurie | V03 Rieur | Ultra-Fabulous Hair (16630147) |  |
| Kaël, dresseur | homme | H18 Blouson noir | B03 Jean noir | V05 Malicieux | CoolBoyHair (451221329) |  |
| Lina | fille | H04 T-shirt jaune | B21 Jupe en jean | V23 Enfant joyeux | Sideswept Bangs Brown (20573078) |  |
| Lou, barista | homme | H01 T-shirt blanc | B03 Jean noir | V02 Content | MessyHair (26658141) (26658141) |  |
| Léa, promeneuse | femme | H07 Polo corail | B17 Pantacourt | V02 Content | LavanderHair (451220849) |  |
| Léon, marchand | homme | H19 Gilet de marchand | B08 Costume | V16 Moustachu | BrownCharmerHair (376548738) |  |
| Maman | femme | H14 Cardigan | B04 Chino | V08 Regard doux | Sideswept Bangs Brown (20573078) |  |
| Mamie Odile | femme âgée | H13 Pull torsadé | B29 Jupe longue grise | V20 Grand-mère | Dr. Smyth Hair (62743701) | cheveux |
| Margot, boulangère | femme | H22 Tablier boulangère | B19 Jupe terracotta | V03 Rieur | Ultra-Fabulous Hair (16630147) |  |
| Mila, pêcheuse | femme | H20 Ciré jaune | B23 Ciré + bottes | V06 Rousseur | Kate Hair (62724852) |  |
| Nadia, tisserande | femme | H12 Pull bordeaux | B20 Jupe fleurie | V15 Lunettes carrées | LavanderHair (451220849) |  |
| Ondine, rêveuse | femme | H02 T-shirt azur | B21 Jupe en jean | V13 Endormi | LavanderHair (451220849) |  |
| Paulin, jardinier | homme | H23 Tablier jardinier | B28 Jardinier | V01 Sourire | Hat1 (62234425) |  |
| Professeur Arid Acanthus | homme âgé | H26 Blouse de labo | B04 Chino | V24 Sage | Dr. Smyth Hair (62743701) |  |
| Romain, garde | homme | H24 Uniforme de garde | B09 Uniforme | V10 Sérieux | Guy Hair (12270248) |  |
| Rosalie | femme | H09 Chemise à carreaux | B19 Jupe terracotta | V01 Sourire | Kate Hair (62724852) |  |
| Réceptionniste de la Guilde | femme | H27 Veston Guilde | B08 Costume | V07 Yeux bleus | Ultra-Fabulous Hair (16630147) | sexe |
| Théo | garçon | H02 T-shirt azur | B13 Short jean | V22 Enfant espiègle | BoyNormalHair1 (13477818) |  |
| Victor, habitué du café | homme | H17 Veste en jean | B04 Chino | V18 Barbe 3 jours | MessyHair (376524487) (376524487) |  |

## Route 1 (44)
| PNJ | Profil | Haut | Bas | Visage | Coiffure (AssetId) | PROVISOIRE |
|---|---|---|---|---|---|---|
| Anouar, le Guide | homme | H16 Veste zippée azur | B05 Cargo kaki | V01 Sourire | Pal Hair (63690008) |  |
| Apolline, apicultrice | femme | H08 Chemise blanche | B12 Travail | V04 Timide | Sideswept Bangs Brown (20573078) |  |
| Aubin, gardien de la tour | homme | H18 Blouson noir | B05 Cargo kaki | V10 Sérieux | Guy Hair (12270248) |  |
| Augustin, le meunier | homme âgé | H01 T-shirt blanc | B12 Travail | V16 Moustachu | Hat1 (62234425) | age |
| Aurèle, berger | homme | H10 Chemise en jean | B11 Velours | V18 Barbe 3 jours | MessyHair (26658141) (26658141) | sexe |
| Basile, retraité | homme âgé | H14 Cardigan | B11 Velours | V19 Grand-père | Dr. Smyth Hair (62743701) |  |
| Céleste, cartographe | femme | H17 Veste en jean | B05 Cargo kaki | V15 Lunettes carrées | Sideswept Bangs Brown (20573078) | sexe |
| Elias, voyageur | homme | H15 Sweat gris | B01 Jean bleu | V12 Étonné | BoyNormalHair1 (13477818) |  |
| Ernest, ancien guetteur | homme âgé | H12 Pull bordeaux | B11 Velours | V19 Grand-père | Pal Hair (63690008) |  |
| Fabienne, voisine | femme | H07 Polo corail | B19 Jupe terracotta | V02 Content | Kate Hair (62724852) |  |
| Firmin, vigneron | homme | H09 Chemise à carreaux | B27 Brique | V01 Sourire | BrownWildMonkHair (80922374) |  |
| Félix, randonneur égaré | homme | H03 Raglan | B05 Cargo kaki | V12 Étonné | NerdHair (32278814) |  |
| Gamin Léo | garçon | H04 T-shirt jaune | B14 Short cargo | V22 Enfant espiègle | BoyNormalHair1 (13477818) |  |
| Gamine Inès | fille | H30 Blouse rose | B18 Jupe plissée | V23 Enfant joyeux | Ultra-Fabulous Hair (16630147) |  |
| Garde Joris | homme | H24 Uniforme de garde | B09 Uniforme | V16 Moustachu | BrownCharmerHair (376548738) |  |
| Hélène, en pique-nique | femme | H05 Débardeur vert | B17 Pantacourt | V03 Rieur | LavanderHair (451220849) |  |
| Inaya, fleuriste en herbe | fille | H02 T-shirt azur | B30 Short rouge | V06 Rousseur | Sideswept Bangs Brown (20573078) |  |
| Ivo, voyageur | homme | H17 Veste en jean | B03 Jean noir | V10 Sérieux | CoolBoyHair (451221329) |  |
| Jeune Dresseur Bastien | garçon | H15 Sweat gris | B16 Bermuda | V05 Malicieux | MessyHair (26658141) (26658141) |  |
| Karim, éleveur | homme | H21 Veste de pêche | B12 Travail | V17 Barbu | BrownWildMonkHair (80922374) |  |
| Lina, promeneuse | femme | H16 Veste zippée azur | B02 Jean délavé | V08 Regard doux | Kate Hair (62724852) |  |
| Lise, ravaudeuse de filets | femme | H06 Marinière | B20 Jupe fleurie | V04 Timide | Sideswept Bangs Brown (20573078) |  |
| Lou | fille | H01 T-shirt blanc | B13 Short jean | V23 Enfant joyeux | LavanderHair (451220849) | sexe |
| Léonie, promeneuse | femme | H10 Chemise en jean | B02 Jean délavé | V07 Yeux bleus | Ultra-Fabulous Hair (16630147) |  |
| Marin, maître-nageur | homme | H05 Débardeur vert | B15 Short de plage | V02 Content | BrownCharmerHair (376548738) |  |
| Marius, pêcheur | homme | H20 Ciré jaune | B23 Ciré + bottes | V18 Barbe 3 jours | BrownWildMonkHair (80922374) |  |
| Maël, pêcheur à la ligne | homme | H21 Veste de pêche | B23 Ciré + bottes | V13 Endormi | BoyNormalHair1 (13477818) |  |
| Mira, pêcheuse | femme | H20 Ciré jaune | B23 Ciré + bottes | V09 Pétillante | Sideswept Bangs Brown (20573078) |  |
| Nina | fille | H03 Raglan | B18 Jupe plissée | V22 Enfant espiègle | Ultra-Fabulous Hair (16630147) |  |
| Nour | fille | H05 Débardeur vert | B30 Short rouge | V03 Rieur | Kate Hair (62724852) | sexe |
| Odette, gardienne du verger | femme âgée | H14 Cardigan | B29 Jupe longue grise | V20 Grand-mère | Dr. Smyth Hair (62743701) | age,cheveux |
| Oscar, pêcheur | homme | H21 Veste de pêche | B23 Ciré + bottes | V17 Barbu | Pal Hair (63690008) |  |
| Paulette, en vacances | femme | H11 Chemise hawaïenne | B13 Short jean | V03 Rieur | Kate Hair (62724852) |  |
| Pique-Niqueuse Sara | femme | H07 Polo corail | B21 Jupe en jean | V09 Pétillante | Ultra-Fabulous Hair (16630147) |  |
| Professeure Anir, archéologue | femme | H26 Blouse de labo | B05 Cargo kaki | V14 Lunettes rondes | Sideswept Bangs Brown (20573078) |  |
| Rosa, maraîchère | femme | H23 Tablier jardinier | B12 Travail | V06 Rousseur | LavanderHair (451220849) |  |
| Rosa, marchande de glaces | femme | H02 T-shirt azur | B17 Pantacourt | V02 Content | Ultra-Fabulous Hair (16630147) |  |
| Scout des Plaines Théo | homme | H05 Débardeur vert | B14 Short cargo | V02 Content | MessyHair (376524487) (376524487) |  |
| Sorlin, gardien des pierres | homme âgé | H28 Tunique brodée | B26 Sarouel | V24 Sage | Pal Hair (63690008) |  |
| Tom | garçon | H15 Sweat gris | B13 Short jean | V05 Malicieux | MessyHairBrown (323476364) |  |
| Vieux Joseph | homme âgé | H13 Pull torsadé | B04 Chino | V19 Grand-père | Dr. Smyth Hair (62743701) |  |
| Voyageuse en manteau gris | femme | H15 Sweat gris | B25 Legging | V13 Endormi | LavanderHair (451220849) |  |
| Yanis, passeur | homme | H06 Marinière | B05 Cargo kaki | V18 Barbe 3 jours | BrownCharmerHair (376548738) |  |
| Ysaline, égarée | femme | H01 T-shirt blanc | B19 Jupe terracotta | V04 Timide | Kate Hair (62724852) |  |

## PROVISOIRE (à valider par Mohand)
- **sexe** déduit du prénom ou du rôle : Céleste (libraire et cartographe) femmes, Réceptionniste de la Guilde femme, Aurèle homme, Lou (enfant, Route 1) fille, Nour fille. Lou le barista est un homme d'après le GDD (« Lou le barista »).
- **âge** : Augustin le meunier et Odette traités comme âgés.
- **cheveux** : aucune coiffure féminine grise dans la garde-robe ; Mamie Odile et Odette reçoivent Dr. Smyth Hair (gris). À remplacer si on importe d'autres cheveux Roblox (sans scripts).
