# Portraits et Tiflask : plan en étapes

Demande de Mohand (26 oct. 2026) : portraits de la Tifalistre et de l'Équipe à partir des rendus, puis une base de Tiflask (modèles) pour pouvoir ensuite faire le lancer de Tiflask, la sortie d'un Tifazelt de sa Tiflask, etc.

Pour reprendre dans une nouvelle conversation : « passons à l'étape N ».

## Ce que dit le vault
- Les Tiflasks capturent les Tifazelts ; il en existe plusieurs types (poche « Tiflask » du sac). Le magasin en vend. Le Professeur en remet un lot au départ.
- Types cités : Tiflask simple, Tiflask d'écume (jeu : « plus efficace près de l'eau »), Tiflask d'Amitié (vault, 3. Mécanique : le Tifazelt capturé commence à 250 de bonheur).
- Aucune description visuelle : la forme vient de l'icône 2D du jeu (`Kit.tiflask` : fiole ronde à col étroit, bouchon cuivre, liquide coloré). **PROVISOIRE**.

## Étapes

| # | Étape | Statut |
|---|---|---|
| 1 | Portraits : rendu en buste de chaque espèce qui a un modèle (Blender, même rendu mat et saturé), découpé en disque ; `Kit.portrait` affiche l'image dans le cercle à la place de l'initiale (tous les écrans en profitent : Tifalistre, Équipe, fiche, combat, infirmerie…) | Fait le 26 oct. 2026 |
| 2 | Tiflask dans Blender : un modèle (fiole, col, bouchon, bague, liquide), trois variantes (simple, écume, amitié) ; rendus pour l'interface (icône) et pour le combat (sprite) | Fait le 26 oct. 2026 |
| 3 | Tiflask 3D dans Roblox : modèle en pièces fidèle au modèle Blender (prêt tout de suite, recolorable), rangé dans `ReplicatedStorage.Tiflasks` ; export FBX du modèle Blender si on préfère un maillage | Fait le 26 oct. 2026 |
| 4 | Base des systèmes : module `Tiflasks` (types et couleurs, création du modèle, lancer en arc, ouverture, sortie d'un Tifazelt) côté client, et animation de capture du combat avec le sprite | Fait le 26 oct. 2026 (base ; pas encore branché sur une action du joueur) |
| 5 | Tests en Play, captures, mise à jour du vault, audit, rappel Ctrl+S | Fait le 26 oct. 2026 (voir journal : ce qui est testé et ce qui ne l'est pas) |
| 6 | Suite proposée : brancher le lancer sur une action du joueur (sortir / rentrer un membre de l'équipe dans le monde, étape 15 de `Starters - plan.md`), réplication serveur, son, Tiflask d'Amitié en vente et son effet (250 de bonheur) | Sortie / rentrée et réplication faites le 26 oct. 2026 (`Sortie du Tifazelt - plan.md`). Reste : vrais sons, Tiflask d'Amitié |

## Journal
- 26 oct. 2026 : plan établi.
- 26 oct. 2026 : étapes 1 à 5 faites.
  - **Portraits** : buste de 3/4 face rendu dans la scène « Sprites » de `Rendu_Sprites.blend` (cadrage sur les sommets liés à la tête et au cou, caméra réorientée sur le buste, même éclairage que les sprites), 512 px, retourné, contour encre 2D, découpé en disque (`Scripts/portrait.py`). Fichiers : `Claude outputs/Modeles 3D/Cramosaur/Portraits/`. Téléversés : Cramosaur 70721059442395, Cramoraptor 97302386996463, Cramorex 113296115553469 (`Tifazelts.Catalogue.portraitDe`). `Kit.portrait` met l'image dans le cercle (grisée si K.O.) ; sinon initiale comme avant. **Testé en Play** : Équipe (grand portrait) et Tifalistre (liste et fiche).
  - **Tiflask (Blender)** : collection `Sprites_Tiflask` de `Rendu_Sprites.blend` : panse en verre stylisé (transparent au centre, marqué sur les bords), liquide coupé à 60 %, col, lèvre, bague et chapeau en cuivre, bouchon en liège, deux reflets blancs, écume en option. Variantes PROVISOIRES : simple (rouge-orangé), écume (turquoise + bulles), amitié (rose). Images 512 px avec contour encre en anneau (`Scripts/icone.py`) : icône (sac) et fermée / ouverte (combat, même cadrage). Fichiers : `Claude outputs/Modeles 3D/Tiflask/` (`Images/`, `Rendus_bruts/`, `Tiflask_v01.fbx`).
  - **Tiflask 3D (Roblox)** : `ReplicatedStorage.Tiflasks.Modele`, en pièces fidèle au modèle Blender (verre Glass, liquide = intersection boule / bloc avec `UsePartColor`, bague, bouchon soudé à part pour sauter), environ 1,2 stud de haut, pivot au pied. `Tiflasks.Donnees` : types, couleurs, images, `get`, `iconeObjet`. `Tiflasks.Lancer` (client, effets visuels) : `creer`, `lancer` (arc, rotation, rebond), `ouvrir` / `fermer`, `eclat`, `sortir` (le Tifazelt grandit depuis la Tiflask, animation d'apparition), `rentrer`, `detruire`. Correctif en route : `ScaleTo` travaille en relatif (les modèles de Tifazelts ont une échelle d'origine de 0,056 à 0,22).
  - **Combat** : `CombatUI.Scene.tiflask` / `capture` utilisent le sprite de la Tiflask lancée (`e.tiflask` du moteur) : fermée au vol, ouverte quand le Tifazelt est aspiré puis refermée, ouverte de nouveau s'il s'échappe ; ancien dessin gardé en repli (`S.tiflaskDessin`). **Sac** : `Kit.portrait` affiche l'icône des Tiflasks connues.
  - Sauvegardes : `Sauvegardes_UI.{Kit,Catalogue}_avant_portraits`, `Sauvegardes_UI.{Scene,Combat}_avant_tiflask`.
  - **Testé en Play** : trois Tiflasks posées dans le monde (couleurs, écume) ; lancer (0,9 s) puis sortie de Cramosaur à sa taille normale, retour dans la Tiflask, suppression, aucune erreur ; capture dans le banc de combat (sprite de la Tiflask d'écume qui secoue sur le socle, échec, le Tifazelt ressort) ; icônes et portraits dans `Kit.portrait` (grand, petit, K.O.). **Non testé** : l'image « ouverte » à l'écran (affichée un quart de seconde, non capturée), une vraie capture lancée depuis le sac dans un combat, l'inventaire réel (le gestionnaire de menus restait « occupé » pendant les commandes de test : à vérifier avec de vrais clics), le lancer branché sur une action du joueur (pas encore fait).
