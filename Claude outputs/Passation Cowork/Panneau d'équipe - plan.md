# Panneau d'équipe en exploration : plan en étapes

Demande de Mohand (26 oct. 2026), d'après une capture de Cobblemon : un panneau de sélection des Tifazelts sur le bord gauche de l'écran, dans le style de Tifazelt, pour voir l'état de l'équipe et choisir le Tifazelt à faire sortir de sa Tiflask.

Pour reprendre dans une nouvelle conversation : « passons à l'étape N ».

## Ce que dit le vault
Rien sur un panneau d'équipe en exploration (le HUD du vault : objectif, TFD, bouton MENU). Tout ce qui suit est **PROVISOIRE** (noté dans [[À décider et à faire]]).

## Choix de travail (PROVISOIRES)
- **Place** : bord gauche, centré en hauteur, sous la carte « Objectif ». Six cartes biseautées qui débordent du bord gauche, comme les rangées de l'écran Équipe. La carte choisie avance d'un cran et prend un liseré terracotta.
- **Chaque carte** : numéro de touche (1 à 6), portrait (buste rendu ou initiale), nom (surnom sinon espèce), niveau, jauge de PV et PV, Tiflask du Tifazelt (icône). Le Tifazelt dehors : liseré cyan, Tiflask ouverte, étiquette « DEHORS ». K.O. : carte grisée, étiquette « K.O. ».
- **Choisir** : touches **1 à 6** (PC), **croix gauche / droite** (manette), clic ou toucher sur une carte. Un second clic sur la carte choisie la fait sortir ou rentrer.
- **R / croix bas / bouton mobile** : agit sur le Tifazelt choisi (et non plus toujours le leader). S'il est dehors : il rentre. Sinon, s'il peut sortir : il sort (celui qui était dehors rentre d'abord). Sinon, si un autre est dehors : celui-ci rentre. L'aide au-dessus du MENU affiche l'action correspondante.
- **Aide sous le panneau** : « 1-6 · CHOISIR » (croix dessinée à la manette), cachée sur écran tactile.
- Le panneau glisse hors de l'écran avec le reste du HUD quand un menu ou un dialogue s'ouvre ; caché sans Tifazelt.

## Étapes

| # | Étape | Statut |
|---|---|---|
| 1 | Module `UI.HUDEquipe` (cartes, sélection, aide) et intégration au HUD (`api.etatEquipe`, glissement avec le HUD, mode clavier / manette / tactile) | Fait le 26 oct. 2026 |
| 2 | `Tiflasks.Compagnon` : Tifazelt choisi, touches 1 à 6 et croix gauche / droite, R sur le Tifazelt choisi, aide au-dessus du MENU | Fait le 26 oct. 2026 |
| 3 | Tests (banc d'essai, puis Play après redémarrage de Studio), captures, vault, audit, rappel Ctrl+S | Fait le 26 oct. 2026 (voir journal) |

## Journal
- 26 oct. 2026 : plan établi.
- 26 oct. 2026 (soir) : étapes 1 et 2 codées, banc d'essai fait.
  - **`UI.HUDEquipe`** (nouveau) : cartes de 340 × 74 (unités de la maquette), espacées de 84, dans un panneau ancré à gauche et centré en hauteur (40 plus bas que le milieu). Chaque carte :
    - liseré terracotta si elle est choisie, cyan si son Tifazelt est dehors, sable sinon ;
    - bande de gauche aux couleurs du type ;
    - numéro de touche (en mode clavier) ;
    - portrait `Kit.portrait` de 58 ;
    - nom qui rétrécit s'il est long, jauge de PV, « NV. », PV ou étiquette « K.O. » ;
    - image de la Tiflask (`Tiflasks.Donnees` : icône, ou image « ouverte » s'il est dehors) et étiquette « DEHORS ».
  - Les cartes non choisies sont rentrées de 26 dans le bord ; la carte choisie avance (0,15 s). Le panneau n'est reconstruit que si quelque chose change : équipe, PV, niveau, Tiflask, choix, Tifazelt dehors, mode d'entrée.
  - Clic ou toucher : choisit la carte ; un second clic sur la carte choisie sort ou rentre le Tifazelt. Sous les cartes : « 1-6 · CHOISIR » (croix dessinée en mode manette, rien au tactile).
  - **`UI.HUD`** : crée le panneau, `api.etatEquipe(equipe, choisi, dehors)`, mode clavier / manette / tactile suivi avec la dernière entrée, glissement hors de l'écran avec le reste du HUD.
  - **`Tiflasks.Compagnon`** : Tifazelt choisi (le leader par défaut ; suit le Tifazelt si l'ordre de l'équipe change ; revient au leader s'il quitte l'équipe), touches 1 à 6 et croix gauche / droite (petit son de survol), `api.choisir`, `api.selection`. **R** : rentre le choisi s'il est dehors ; sinon le sort s'il peut (celui qui était dehors rentre d'abord) ; sinon rentre celui qui est dehors ; sinon toast du refus. L'aide au-dessus du MENU et le bouton mobile suivent la même règle. Sortir depuis la fiche choisit aussi ce Tifazelt.
  - Sauvegardes : `Sauvegardes_UI.HUD_avant_aide_compagnon` et `Compagnon_avant_aide` (avant l'aide et le panneau).
  - **Testé sur un banc d'essai** : le vrai module et les vraies données de test sont affichés dans un écran à part, côté client, sans lancer le jeu. Vérifié : affichage (Cramosaur dehors, choisi, K.O., trois sortes de Tiflask), avancée de la nouvelle carte choisie, clic qui choisit, clic sur la carte choisie qui déclenche sortir / rentrer. Capture `2026-10-26_22h41_panneau-equipe-banc.jpg`. Tout compile.
  - **Pas testé en jeu** : Studio n'accepte plus le joueur sur le serveur de test (erreur interne « readRegionRemoval error total time exceeded », même avec les anciennes versions des scripts), et le jeu côté client se fige au bout de quelques secondes. À tester après **Ctrl+S et redémarrage de Studio** : panneau dans le HUD, touches 1 à 6, R sur le Tifazelt choisi, échange quand un autre est dehors, glissement à l'ouverture d'un menu, mode manette et tactile.
- 26 oct. 2026 (soir, après redémarrage de Studio par Mohand) : **testé en Play**. Le joueur se connecte de nouveau au serveur de test ; aucune erreur côté client ni côté serveur.
  - **Affichage** : panneau dans le HUD, sous la carte « Objectif » (capture `2026-10-26_22h54_panneau-equipe-en-jeu.jpg` : Cramosaur dehors, carte « DEHORS » et Tiflask ouverte, Dauphimyst choisi).
  - **Choisir** :
    - touches 4, 1, 2 : la bonne carte avance à chaque fois ;
    - croix droite deux fois : de 2 à 4 (l'outil de test la simule comme du clavier, donc l'affichage en mode manette n'est pas vérifié) ;
    - clic sur la carte 1 : choisie ; second clic : Cramosaur sort.
  - **R** :
    - Cristalithe choisi (pas de modèle) : toast de refus, aide cachée ;
    - Cramosaur choisi : il sort, aide « RENTRER CRAMOSAUR » ;
    - Dauphimyst choisi pendant que Cramosaur est dehors : l'aide indique « RENTRER CRAMOSAUR », et R le fait rentrer.
  - **K.O.** (`pv:1|0`) : Cramosaur rentre tout seul, carte « K.O. », aide cachée ; une fois soigné, l'aide revient sur « SORTIR CRAMOSAUR ».
  - **Intérieur** : aide cachée, panneau affiché ; en ressortant, Cramosaur ressort et l'aide revient.
  - **Menus** : le panneau glisse hors de l'écran à l'ouverture de l'Équipe et revient à sa place à la fermeture.
  - **Bug trouvé et corrigé** : `Anim.slideIn` rend toujours l'élément visible. À chaque fermeture de menu, l'aide revenait donc, même cachée et avec un texte périmé. `UI.HUD` ne fait plus revenir l'aide et le panneau que s'ils ont lieu d'être (`parts` avec une condition, `HUDEquipe.aDesCartes`) ; l'entrée initiale aussi.
  - **Non testé** : l'affichage en mode manette (croix dessinée, numéros cachés), l'écran tactile, l'échange direct entre deux Tifazelts qui ont un modèle (un seul dans l'équipe de test ; même chemin que l'évolution, déjà testée).
