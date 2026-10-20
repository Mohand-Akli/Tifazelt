---
tags:
  - production
  - roblox
  - route-1
aliases:
  - Route 1 Roblox
---
# 🛤️ Route 1 — Construction Roblox

> Fiche de lore et de game design : [[Route 1]]. Index de la production : [[00. Production Roblox]].
> Générateurs : `ServerStorage.MapGeneration.Route1` (`Builder`, mode d'emploi `LISEZMOI`, module `Passe4`, dossier `Passe5`) puis `ServerStorage.MapGeneration.Extensions`. Sortie : `Workspace.Map.Routes.Route1` et `Workspace.Map.Extensions`.

## 📜 Passes 2 à 5 (octobre 2026)
- **État Roblox Studio (oct. 2026, passe 2 de finition) :** décor généré par `ServerStorage.MapGeneration.Route1` (mode d'emploi : module `LISEZMOI`) dans `Workspace.Map.Routes.Route1`. Sentier sinueux à largeur variable et lisières naturelles ; falaise côtière à strates avec blocs et aiguilles marines, maquis méditerranéen bas (lavande, ciste, genêt, agaves) et belvédère face à la mer ; plaine avec hautes herbes aux formes organiques, arbres en lisière, lieux repères (arbre solitaire, souche fleurie, petite clairière, vieille clôture) ; corniche à sens unique en strates (testée : infranchissable depuis le bas) ; bosquet sans grille, couloirs qui se resserrent, culs-de-sac fermés par des arbres tombés, haies à collision continue ; clairière de la Bague avec autel de pierre, pierres dressées et rayons de lumière doux. Seul script actif : `Route1_Ambiance` (client) pour la brume locale du bosquet et les papillons. PNJ, rencontres, objets et Bague restent des **repères** sans système de jeu.
- **Passe 3 (oct. 2026) :** colorimétrie plus chaude et cartoon (lumière ambiante chaude, étalonnage, ciel à nuages dessinés, couleurs du terrain ; réglages d'origine gardés dans `ServerStorage.Eclairage_AvantPasse3`) ; vent visible dans les Parties 1 et 2 (traînées blanches, pétales, hautes herbes qui ondulent, `GlobalWind`) ; 16 points d'intérêt (arche de sortie du Bourg, passage entre rochers, halte du Guide avec puits, marches de pierre, crique, tour de guet en ruine, col avec portillon, champs avec bottes de foin, ruisseau et passerelle, piquets des hautes herbes obligatoires, arbre à balançoire de Léo, rocher du Tiflask, mare de Sara, camp de Théo avec feu de camp). Les bords de la falaise côtière sont maintenant en pente douce (ils dessinaient un grand rectangle vu du ciel).
- **Passe 4 (oct. 2026) :** paysage enrichi sans changer le relief. Arbres, buissons et rochers « en cubes » remplacés par des modèles low poly à facettes (mêmes positions). Compositions dans les zones vides : lisières d'arbres en arrière-plan, bosquets, groupes de rochers, tapis de fleurs, pinèdes côtières, zones de végétation sèche, murets de pierre sèche, abords du sentier fleuris. Lieux secondaires : oliveraie sauvage, grand olivier remarquable, vieille charrette, petit sanctuaire de pierre, arche rocheuse au-dessus du sentier côtier, prairie fleurie avec amandier. Points d'intérêt complétés (dallage du puits, échelle de la tour, berges du ruisseau, couverture de pique-nique de Sara, tente et marmite de Théo). Bosquet des Égarés : parois de buissons, arbres qui dépassent des haies, sous-bois, troncs moussus, cadre de la clairière. Vie : libellules près de l'eau, oiseaux en vol, papillons supplémentaires.
- **Passe 5 (oct. 2026) :** la route devient un vrai couloir d'aventure. **Rivière de la Plaine** : l'ancien ruisseau est élargi (~26 studs) et relie désormais l'Asif-Safi à la mer ; un **grand pont de pierre** (54 studs, refuge avec banc, repères réservés à une future scène avec le rival) est le passage obligatoire entre la Plaine basse et le plateau. On ne traverse plus à la nage : dans la région de Bourg-Azur et de la Route 1, le **courant** ramène sur la rive au-delà de 12 studs dans l'eau. **Muraille** (corniche) : face continue sans prise, rebord à sens unique conservé, prolongée en pierre sèche de l'Asif-Safi jusqu'à la mer ; trou au pied de la rampe comblé. **Bosquet des Égarés** : la bordure verte extérieure est remplacée par une lisière d'arbres et de buissons, barrière en bois de la sortie retirée, lisières infranchissables jusqu'à l'eau au nord et au sud, trous des haies bouchés, buissons flottants recalés ; **3 nouveaux couloirs** (Sentier des Mousses, Allée du Grand Chêne, Passage des Racines) menant à une clairière aux champignons, un chêne géant servant de repère et des ruines avec une stèle. **Campagne** : Mas des Moissons, **grand moulin** aux ailes animées, champ de blé avec épouvantail, potager, enclos de Tifazelts (silhouettes provisoires) ; **4 cabanes de pêcheurs** avec pontons et barques, sentiers des berges jusqu'à l'embouchure. **18 PNJ R6** (dont Léo, Sara, Théo, le Guide, 2 nouveaux dresseurs débutants, agriculteurs, pêcheurs, une voyageuse mystérieuse, un randonneur égaré) et **8 secrets**. Les dresseurs ont leurs données (équipe, ligne de vue) mais aucun combat n'est encore codé.

## 🧱 Passe 6 (18 oct. 2026) — zones 1 à 6
- **Zone 1** : abords de [[Bourg-Azur]].
- **Zone 2** : 4 quartiers de Bourg-Azur (`CityPlots.BourgAzur.Passe3`). ⚠️ 4 PNJ ajoutés à la main seraient perdus si on régénère.
- **Zone 3** : Tour du Guet (1060, 2358), Failles du Berger, Cercle des Vents (300, 1932).
- **Zone 4** : Plage de l'Estuaire, Crique des Oliviers.
- **Zone 5** : labyrinthe et récompenses du bosquet.
- **Zone 6** : Vestiges de la Garde Ancienne (-333, 2362), avec un sanctuaire et une porte scellée.

## 🌲 Forêt centrale — le Bosquet des Égarés
### Mission du 19 oct. (v1)
- Toutes les haies vertes retirées (dont 464 invisibles) ; 4 rampes douces vers les plateaux ; 9 clairières ; repères : Arbre Mort tordu, Cinq Pins, Dents du Bosquet.
- Limites naturelles : 582 grands rochers, sans collision invisible.
- Découvertes et 5 secrets ; repères de rencontres dans `SpawnZones.Foret`.

### Forêt v2 (19 oct.)
> Module `Foret2`.
- Tout le sol est au même niveau (plateaux abaissés à y ≈ 11–13) ; un seul type d'arbre (3 887 arbres) ; grand chêne, arche d'entrée et limite est retirés : **on entre par où on veut** depuis la Route 1.
- Clairière de la Bague remise comme à l'origine, avec une **Bague tournante** visible (tag `Foret_BagueTournante`).
- Limite ouest prolongée à travers l'[[Asif-Safi]]. ⚠️ Deux contournements possibles à la nage aux extrémités, en principe bloqués par la règle du courant (non vérifié à la nage).

### Forêt v3 (19 oct., corrections à la main)
- **Plus aucun buisson** dans la forêt : 1 938 buissons et haies de maquis retirés (sauvegarde `Extensions_Sauvegarde.Foret3_Buissons`). Il reste arbres, rochers, fougères et branches tombées.
- **Arbres redressés** : 3 959 troncs remis à la verticale et posés au sol ; 13 arbres collés aux falaises et 20 arbres « parasol » retirés (`Foret3_ArbresRetires`).
- **Rayons de soleil doux** (Beams) à la place des blocs transparents, visibles seulement à moins de 65 studs (blocs d'origine dans `Foret3_RayonsBlocs`).
- **Lucioles guides** : voir [[Systèmes de jeu Roblox#✨ Lucioles guides (forêt)|Lucioles guides]].

## 🌾 Plaine ouest (19 oct.)
> Module `PlaineOuest`.
Trois lieux entre la muraille et la rivière, chacun sur une légère butte, avec un PNJ, un panneau et un secret. Ils sont reliés aux chemins existants par 3 chemins de terre.
| Lieu | Position | Contenu | PNJ | Secret |
| :--- | :--- | :--- | :--- | :--- |
| **Séchoirs du Passeur** | (334, 3088) | 3 perches à poissons, tonneaux, sac de sel, barque retournée, cadre à filets | Lise, ravaudeuse de filets | Coquille nacrée sous la barque |
| **Verger de l'Ancien Puits** | (296, 2592) | 19 amandiers en fleurs, puits, muret de pierre sèche, échelle, paniers | Odette | Boîte sous le plus vieil amandier |
| **Pâture des Laineux** | (307, 2163) | Enclos en pierre sèche, capitelle, 4 Laineux (silhouettes provisoires), abreuvoir | Aurèle, berger | Sonnaille gravée d'une spirale (renvoie au Cercle des Vents) |

- Correction du 19 oct. : les taches de roche et de terre peintes par le relief (qui ressemblaient à une route abîmée, vers (349, 3069)) ont été repeintes en herbe.

## 🧪 Tests réellement faits en jeu (passe 6 et forêt)
- Pathfinding serveur : lisière est → Bague, nord → Bague, sortie vers [[Val Palmeraie]] : réussis.
- Lucioles : suivent le sentier à moins de 3 studs ; hors sentier, restent visibles en marchant dans les 4 directions ; tournent autour de la Bague.
- Rayons : allumés près de la Bague, éteints de loin (capture à ~110 studs sans bloc visible).
- Crique : aller-retour OK ; bout du ponton OK ; ailes du moulin qui tournent.
- Non testé : contournement à la nage des extrémités de la limite ouest.

## 🚧 À décider / à faire
- Le « pont basique » : le seul pont sur le fleuve est le Pont de la Plaine, en pierre.
- Tracer un sentier dans le nord-est de la forêt (aucun sentier à moins de 180 studs de la lisière est).
- Remplacer les silhouettes provisoires de Tifazelts (Laineux, Picoreurs).
- Coder la brume scénarisée et l'obtention de la Bague.
