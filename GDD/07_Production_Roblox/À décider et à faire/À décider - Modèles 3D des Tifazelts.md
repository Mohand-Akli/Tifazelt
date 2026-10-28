---
tags:
  - production
  - roblox
  - suivi
---
# Modèles 3D des Tifazelts — PROVISOIRE

> [[À décider et à faire|Sommaire : à décider et à faire]]

## Lignée Cramosaur (26 et 27 oct. 2026)

- **Affichage en combat (26 oct. 2026, soir)** : images pré-rendues dans Blender (`Tifazelts.Sprite`) au lieu de la 3D temps réel, jugée floue et terne par Mohand. Rendu mat et saturé (saturation 1,7) depuis la remarque de Mohand (« ni chromé ni néons »). À valider : rendu, niveau de saturation, taille (adversaire 1,3 × d, allié 1,55 × d), vitesse de respiration (8 images/s), vue de l'allié de 3/4 arrière. Cramoraptor et Cramorex faits le 26 oct. 2026 (testés dans un banc de combat, pas dans un vrai combat). À décider : taille relative des stades à l'écran, niveaux d'évolution, stats (PROVISOIRES dans `Combat.Especes`). À faire : Dauphimyst et Garenbois quand leurs modèles existeront. (Portraits Tifalistre / Équipe faits le 26 oct. 2026.)
  - *Mise à jour (rangement, 28 oct. 2026) : dépassé en partie : les v04 ont remplacé les v03 (réglage « E » dans le monde, « P2 » en combat, voir plus bas) et la lignée Dauphin est faite (section suivante).*
- **Tailles** choisies sans référence dans le vault, appliquées dans le jeu : Cramosaur ≈ 1,1 m de haut, Cramoraptor ≈ 1,8 m, Cramorex ≈ 3 m. À valider.
- **Armature et animation** : rig de 21 os fait dans Blender et importé par Mohand le 26 oct. 2026 ; animations procédurales (`Tifazelts.Animation` : attente, marche, attaque, touché, K.O., apparition), utilisées par le Tifazelt qui suit le joueur. À valider à l'écran : la marche.
- ~~**Découpage pour Roblox** (modèles faits par Claude, lave séparée)~~ : sans objet, ces modèles ont été abandonnés le 26 oct. 2026 au profit des modèles Meshy fournis par Mohand, importés dans Studio.
- Fichiers : `Claude outputs/Modeles 3D/Cramosaur/` (`.blend`, rendus, scripts de construction).
- **Lignée Cramosaur : v04 retenues par Mohand (27 oct. 2026)**. Les v03 ne sont plus dans le jeu (sauvegardées dans `ServerStorage.Tifazelts_Sauvegarde_v03`) ; `Tifazelts.Modeles` contient les v04 (trous réparés, retouche « E », lave lumineuse) ; images de combat v04 (réglage P2, 24 images en fondu) ; portraits v04. **PROVISOIRE, à valider par Mohand** : couleurs dans le monde (réglage « E ») et en combat (P2), durée d'une respiration (1,5 s). Détail : [[Lignée Cramosaur v04 - plan]] et [[v04, Tifalistre, PNJ, intro de combat et vélos - plan]].
  - *Mise à jour (relecture, 28 oct. 2026) : le combat est passé à 45 images par vue (30 i/s + fondu, choix de Mohand) pour les 6 Tifazelts modélisés : voir la lignée du Dauphin ci-dessous.*

## Lignée du Dauphin (28 oct. 2026)

- **Lignée du Dauphin, modèles 3D (28 oct. 2026, PROVISOIRE)** : Dauphimyst, Dauphiclos et Dauphiracle identifiés, réparés et allégés à 10 000 triangles dans `Claude outputs/Modeles 3D/Dauphin/Lignee_Dauphin.blend` (plan : [[Lignée Dauphin - plan]], étapes 1 à 3 faites). Dauphiracle refait avec le fichier texturé fourni par Mohand (la texture provisoire inventée est abandonnée, sauvegardée). Rig fait le 28 oct. : squelette de 14 os (16 pour le Dauphiracle), noms repris des Cramosaur quand l'os existe (compatible `Tifazelts.Animation`), plus `Aileron` et, pour le Dauphiracle, `NageoireG`/`NageoireD` (PROVISOIRE). **Demande de Mohand (28 oct.)** : les trois dauphins se déplacent en **nageant dans les airs**, comme s'ils volaient : animation de flottement et de nage aérienne à faire à l'étape 4 (amplitude, hauteur de vol, vitesse : PROVISOIRES). **Étapes 4, 5, 7 et 8 faites le 28 oct. 2026 (PROVISOIRE, rien testé en Play)** : modes `flotte` et `nage` dans `Tifazelts.Animation` (amplitudes, périodes, hauteur de flottement à valider) ; couleurs : réglage **B** (saturation 1,3, sans lueur) retenu en attendant le choix de Mohand (`Dauphin/Rendus/Variantes_couleur_planche.jpg`) ; sprites de combat (24 images par vue), portraits et entrées `Tifazelts.Catalogue` faits, échelles à l'écran PROVISOIRES (taille voisine des Cramosaur, Cramoraptor, Cramorex). Couleurs refaites (saturation 0,8, proches des illustrations, à la demande de Mohand) ; étape 6 faite : modèles dans `Tifazelts.Modeles`. **PROVISOIRE** : longueurs 6,5 / 10,5 / 15 studs, échelles en combat, hauteur de vol du Tifazelt qui suit (attribut `Vol` : 2,5 / 3 / 3,5 studs). 28 oct. (soir) : dauphin écrasé corrigé (os pas agrandis), textures du monde éclaircies, combat à 45 images par vue (30 i/s + fondu, choix de Mohand) pour les 6 Tifazelts, clignotement des sprites corrigé (préchargement), équipe de test = les 6 Tifazelts modélisés (stats et attaques PROVISOIRES). Reste : tests en Play par Mohand (étape 9), mémoire sur mobile.
  - *Mise à jour (rangement, 28 oct. 2026) : le réglage B (saturation 1,3) a été refusé par Mohand (« trop flashant ») ; la saturation 0,8 est retenue (voir [[Lignée Dauphin - plan]], étape 5).*

## Garenbois (28 oct. 2026)

- **Garenbois, première illustration (28 oct. 2026, PROVISOIRE)** : le vault ne décrit pas son apparence. Claude a rédigé un prompt dans le style des illustrations de Cramosaur et de Dauphimyst (lapin de garenne vert mousse, plaques d'écorce, petites ramilles en bois entre les oreilles, nervures de feuille dorées). Fichier : [[Garenbois - prompt de la première illustration]]. À faire par Mohand : générer l'image avec son outil habituel et valider ou corriger le design.
