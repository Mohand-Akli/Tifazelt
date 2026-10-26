# Lignée Cramosaur, nouvelles versions (v04) : plan en étapes

Demande de Mohand (26 oct. 2026) : trois nouvelles versions Meshy de la lignée des dinosaures (`~/Downloads/meshy_1793054409870.glb`, `meshy_1793054413554.glb`, `meshy_1793054447571.glb`). Tout corriger pour les importer dans le jeu, **en gardant les versions actuelles (v03) pour comparer** et choisir la meilleure.

Pour reprendre dans une nouvelle conversation : « passons à l'étape N ».

## Constat à l'inspection
- Mêmes défauts que les v02 : UV quantifiées avec une transformation de texture (Studio l'ignore) et images WebP. La correction n'est plus exactement « x16 » : il y a aussi un petit décalage, donc l'ancien `Scripts/corriger_glb.py` ne suffit plus.
- **Beaucoup plus détaillées** : 366 000, 420 000 et 614 000 triangles, contre 10 500 pour les v03 ; Roblox accepte au plus 20 000 triangles par maillage. Il faut les alléger.
- Pas d'os ni d'animation.

## Règle
Rien n'est retiré : les v03 restent dans le jeu (`ReplicatedStorage.Tifazelts.Modeles`), dans `Rendu_Sprites.blend` et dans `Rig/`. Les v04 vivent à côté (dossier `V04/`, fichiers Blender séparés, dossier Studio séparé).

## Étapes

| # | Étape | Statut |
|---|---|---|
| 1 | Identifier l'espèce de chaque fichier ; import dans un nouveau fichier Blender `V04/Lignee_Cramosaur_v04.blend` ; UV corrigées (transformation appliquée), textures en PNG | Fait le 26 oct. 2026 |
| 2 | Allègement à environ 10 000 triangles (demande de Mohand ; comme les v03, sous la limite de 20 000), contrôle des textures et des détails par rendu ; même échelle que les v03 | Fait le 26 oct. 2026 |
| 3 | Rig : même squelette de 21 os que les v03 (pour garder `Tifazelts.Animation`), poids, test de pose ; export FBX (et GLB) pour Studio | Fait le 26 oct. 2026 |
| 4 | Comparaison v03 / v04 : rendus côte à côte avec l'éclairage mat et saturé du combat (copie `Rendu_Sprites_v04.blend`) | Fait le 26 oct. 2026 (`V04/Rendus/Comparaison_v03_v04.jpg`) |
| 5 | Import dans Studio par Mohand (Accueil > Importer 3D), puis intégration par Claude dans `ReplicatedStorage.Tifazelts.Modeles_v04` (sans toucher `Modeles`) ; aperçu côte à côte dans Studio et réglage pour essayer les v04 en jeu | **Attend l'import par Mohand** des 3 `V04/Rig/*_Rig_v04.glb` |
| 6 | Si les v04 sont retenues : images de combat, portraits et icônes refaits avec elles | À décider avec Mohand |

## Journal
- 26 oct. 2026 : plan établi après inspection des trois GLB.
- 26 oct. 2026 : étapes 1 à 4 faites (Mohand a demandé en cours de route environ 10 000 triangles).
  - **Fichiers** : copies des sources dans `Claude outputs/Modeles 3D/Cramosaur/V04/Sources/` (meshy_1793054409870 = **Cramosaur**, 413554 = **Cramoraptor**, 447571 = **Cramorex**, reconnus sur des rendus de dessus et de profil). Travail dans `V04/Lignee_Cramosaur_v04.blend` (nouveau fichier ; `Lignee_Cramosaur.blend`, `Rig/Lignee_Cramosaur_Rig.blend` et `Rendu_Sprites.blend` non modifiés).
  - **UV et textures** : la transformation de texture des fichiers (échelle d'environ 16, plus un petit décalage, différents pour chaque fichier) est appliquée directement aux UV, et les nœuds de placage sont retirés. UV vérifiées entre 0 et 1, textures correctes au rendu (yeux, lave). Images WebP converties : `V04/Textures/*_v04_couleur.jpg` (réécrite depuis l'image d'origine, écart moyen inférieur à 1 niveau), `*_normales.png`, `*_metal_rugosite.png` (identiques à l'original), plus `*_metal.png` et `*_rugosite.png` séparés. Métal presque nul sur les trois : pas d'effet chromé cette fois.
  - **Allègement** : de 366 000, 420 000 et 614 000 triangles à **10 000** chacun (Decimate, réduction). Comparaison au rendu : silhouette, cornes, collerette, yeux et lave conservés ; reliefs fins un peu plus doux (`V04/Rendus/verif_allege_vs_detaille.jpg`). Les versions détaillées sont gardées, cachées, dans la collection `V04_HautePoly` (pour un éventuel report des détails en carte de normales).
  - **Repère** : même convention que les v03 : longueur 0,95 m, pieds à z = 0, tête vers -Y, gauche vers +X, placés à x = 0 / 1,6 / 3,2. Le corps du Cramorex v04 est décalé d'environ 9 cm vers +X, et sa queue se courbe sur le côté puis retombe en massue.
  - **Rig** : même squelette que les v03 (21 os, mêmes noms et même hiérarchie, donc `Tifazelts.Animation` reste valable). Os placés d'après des vues de profil et de dessus à l'échelle (1 px = 1 mm, grille), contrôlés par superposition (`V04/Rendus/os_*_controle.jpg`) ; la queue du Cramorex suit sa courbe. Poids par proximité des os : 3 influences au plus, bras et jambes limités à leur côté, rayon maximal pour les bras (4,5 cm) et les jambes (12 cm), mâchoire limitée au bas de la tête. Test de pose exagérée (tête, mâchoire, cou, queue, cuisse, jambe, bras) : déformation propre sur les trois (`V04/Rendus/v04_test_pose_gros_plan.jpg`).
  - **Exports** : `V04/Rig/*_Rig_v04.glb` (conseillé : textures PBR intégrées, UV en clair, aucune extension, 10 000 triangles, 21 os avec leurs poids, images JPEG) et `*_Rig_v04.fbx` (textures intégrées).
  - **Comparaison** : `V04/Rendu_Sprites_v04.blend` (copie de `Rendu_Sprites.blend`, collection `Sprites_v04`, même traitement mat et saturé que le combat) ; planche `V04/Rendus/Comparaison_v03_v04.jpg` (vues face et dos du combat, même cadrage par espèce). Constat : Cramosaur très proche (plus de plaques noires sur le dos) ; Cramoraptor et Cramorex v04 plus trapus, gris à taches noires comme Cramosaur (la lignée se ressemble davantage), queues en massue ; v03 plus fines et plus sombres, veines de lave plus marquées.
  - **Jeu** : `Tifazelts.Animation` et `Tiflasks.Compagnon` calculent maintenant l'avant de la créature de la hanche vers la tête (et non plus du bout de la queue vers la tête), sinon le Cramorex v04 aurait été décalé d'environ 18°. Vérifié sur les trois v03 : écart de 0°. Sauvegardes : `Sauvegardes_UI.Animation_avant_v04`, `Compagnon_avant_v04`.
  - **Non fait** : import dans Studio (Mohand), intégration dans `Tifazelts.Modeles_v04`, essai en jeu ; report des détails de la version détaillée en carte de normales (pas jugé nécessaire au vu des rendus).
