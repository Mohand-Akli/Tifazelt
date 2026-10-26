# Sortie du Tifazelt dans le monde : plan en étapes

Demande de Mohand (26 oct. 2026) : « On branche la sortie de ton Tifazelt sur une action du joueur ». Suite de l'étape 6 de `Portraits et Tiflask - plan.md` et de l'étape 15 de `Starters - plan.md`.

Pour reprendre dans une nouvelle conversation : « passons à l'étape N ».

## Ce que dit le vault
Rien sur un Tifazelt qui accompagne le joueur hors combat. Tout ce qui suit est **PROVISOIRE** (noté dans `GDD/07_Production_Roblox/À décider et à faire.md`).

## Choix de travail (PROVISOIRES)
- **Action** : touche **R** (PC), **croix bas** (manette), bouton rond **SORTIR / RENTRER** (mobile, au-dessus de COURIR) : sort le leader de l'équipe, ou le rentre s'il est dehors. Dans la **Fiche** d'un Tifazelt : bouton « Sortir » / « Rentrer » pour le membre affiché.
- **Scène** : le joueur lance la Tiflask devant lui (arc, rebond), le bouchon saute, le Tifazelt grandit depuis la fiole, la Tiflask disparaît. Le Tifazelt suit ensuite le joueur (derrière, un peu sur le côté), marche quand il bouge, se tourne dans le sens de la marche, épouse le sol. Pour le rentrer : une Tiflask apparaît dans la main du joueur et le Tifazelt y est aspiré.
- **Tiflask** : celle qui a servi à la capture (nouveau champ `tiflask` du Tifazelt, posé par le moteur de combat à la capture) ; starter et anciens Tifazelts : Tiflask simple.
- **Visible par tous** : le serveur tient l'état (attributs du joueur), chaque client dessine le Tifazelt de chaque joueur. Aucune donnée joueur sauvegardée.
- **Refus** : leader K.O., espèce sans modèle 3D (pour l'instant seulement la lignée Cramosaur), en intérieur, pendant un menu ou un dialogue.
- **Rentre tout seul** : K.O. (après un combat), plus dans l'équipe, mort du personnage. **En intérieur** : il rentre et ressort tout seul quand on sort.
- **Vélo** : il suit (plus vite) ; s'il est trop loin (plus de 50 studs), il réapparaît près du joueur.

## Étapes

| # | Étape | Statut |
|---|---|---|
| 1 | Serveur : `Reseau.Compagnon` (RemoteEvent) et `ServerScriptService.Compagnon_Serveur` (validation, attributs `Compagnon`, `CompagnonTiflask`, `CompagnonNom`, `CompagnonN`, intérieurs, mort, départ) | Fait le 26 oct. 2026 |
| 2 | Client : module `Tiflasks.Compagnon` (dessine le Tifazelt de chaque joueur : lancer, sortie, suivi, rentrée) et `StarterPlayerScripts.Compagnon_Client` (touche, bouton mobile, rentrée automatique) | Fait le 26 oct. 2026 |
| 3 | Fiche : bouton « Sortir » / « Rentrer » ; moteur de combat : champ `tiflask` à la capture | Fait le 26 oct. 2026 |
| 4 | Tests en Play, captures, vault, audit, rappel Ctrl+S | Fait le 26 oct. 2026 (voir journal : testé / non testé) |
| 5 | Vrais sons et geste de lancer du personnage | Fait le 26 oct. 2026 (à valider à l'écoute et à l'œil) |
| 6 | Aide à l'écran pour la touche R (sortir / rentrer) | Fait le 26 oct. 2026 |
| 7 | Suite possible : test à deux joueurs, écoute des sons, capture dans le monde, Dauphimyst et Garenbois quand leurs modèles existeront | À décider avec Mohand |

## Journal
- 26 oct. 2026 : plan établi.
- 26 oct. 2026 : étapes 1 à 4 faites.
  - **Serveur** `Compagnon_Serveur` : demande `sortir` (espèce présente dans `Tifazelts.Modeles`, type de Tiflask connu sinon simple, nom de 24 caractères au plus, personnage vivant, pas en intérieur, une demande par demi-seconde) ou `rentrer`. Il garde le Tifazelt voulu pendant un passage en intérieur (attribut vidé en entrant, reposé en sortant, vérifié toutes les 0,5 s). Il le vide à l'apparition ou à la mort du personnage. Aucune donnée sauvegardée.
  - **Client** `Tiflasks.Compagnon` : chaque client dessine le Tifazelt de chaque joueur dans `workspace.Compagnons` (dossier local). Un changement d'attribut lance la scène : rentrée de l'ancien Tifazelt, puis lancer et sortie du nouveau. Le Tifazelt arrive sans lancer quand on rejoint un joueur déjà accompagné. Suivi image par image : cible derrière le joueur (2 studs + demi-longueur) et à droite, vitesse jusqu'à 1,25 fois celle du joueur (de 14 à 60), demi-tour par le plus court chemin, sol trouvé par rayon (surfaces qui bloquent seulement), réapparition près du joueur au-delà de 50 studs, attente dehors quand le joueur entre dans un intérieur. Animation de marche ou d'attente choisie toute seule (`Animation:Auto`), rythme de marche réglé sur la vitesse. Texture retouchée (`SA_Retouche`) posée avant l'apparition (nouveau crochet `preparer` de `Tiflasks.Lancer.sortir`).
  - **Commandes** (`Compagnon_Client`) : R / croix bas / bouton mobile ; `M.compagnon` (`estDehors`, `refus`, `basculer`) pour la Fiche (bouton « Sortir » / « Rentrer », refus affiché sans fermer la fiche). Le client fait rentrer le Tifazelt tout seul (K.O., plus dans l'équipe) et fait ressortir la nouvelle forme après une évolution.
  - **Moteur de combat** : champ `tiflask` posé à la capture ; correctif de `evoluer` (le champ `espece` suit l'évolution). Commandes de test ajoutées dans `UI_Client` : `pv:1|0` et `evoluer:1`.
  - Sauvegardes : `Sauvegardes_UI.Fiche_avant_compagnon`, `Moteur_avant_compagnon`, `UI_Client_avant_compagnon`.
  - **Testé en Play** (un joueur, R6, Route 1) : touche R (sortie de Cramosaur : Tiflask lancée depuis la main, rebond, bouchon, croissance, Tiflask qui disparaît, puis suivi) ; suivi en marchant (environ 10 studs derrière en marche, 6 à l'arrêt, au sol) ; R de nouveau (rentrée) ; bouton « Rentrer » de la Fiche (menu fermé, Tifazelt rentré) ; refus pour Dauphimyst (pas de modèle : toast, la fiche reste ouverte) ; refus avec le leader K.O. ; rentrée toute seule au K.O. avec toast ; évolution en Cramoraptor (Cramosaur rentre, Cramoraptor sort) ; passage en intérieur (rentre, attend dehors, ressort avec un lancer à la sortie). Aucune erreur de jeu dans la console. Captures `2026-10-26_21h47_*`.
  - **Non testé** : vue par un autre joueur (il faut un test à deux joueurs), bouton mobile, croix de la manette, vélo, mort du personnage, personnage R15, Cramorex en sortie (taille : la Tiflask est lancée plus loin, non vu), Tiflask d'écume ou d'Amitié à la sortie (seule la simple a servi), après une vraie capture.
- 26 oct. 2026 (soir) : étape 5 faite (demande de Mohand : « vrais sons et geste de lancer du personnage »).
  - **Geste** : nouveau module `ReplicatedStorage.Joueur.Gestes` (client), mêmes conventions qu'`Animations.GestesPNJ`, images clés interpolées, joué sur le `Motor6D.Transform` à chaque `Stepped`, fondu d'entrée et de sortie, R6 et R15. `lancer` (0,65 s, lâcher à 0,3 s : élan bras en arrière et buste tourné, bras par-dessus la tête, bras gauche en balancier). `rappel` (1,1 s, bras tendu). Pas de geste sur le vélo. `Tiflasks.Compagnon` : la Tiflask suit la main jusqu'au lâcher, puis part de là ; au rappel, la Tiflask apparaît dans la main 0,15 s après le début du geste.
  - **Sons** : 8 effets Pro Sound Effects ajoutés à `Audio.Sons` (`tiflask_lancer`, `_rebond`, `_ouvrir`, `_fermer`, `_pouf`, `_scintille`, `_aspire`, `_rappel`) et nouvelle fonction `Sons.jouerEn(nom, position)` : le son est placé dans le monde, atténué de 10 à 90 studs, avec une légère variation de hauteur, et chaque client le joue chez lui. Préchargés. Le volume de chaque candidat a été mesuré en Play par tranches de 50 ms pour choisir et caler le début : le scintillement et le rappel démarrent en cours de son pour que leur pic tombe à la fin de la croissance ou de l'aspiration. Les sons sont joués par `Tiflasks.Lancer` (anciens sons d'interface retirés de `Compagnon`).
  - Sauvegardes : `Sauvegardes_UI.Sons_avant_sons_tiflask`, `Lancer_avant_sons`, `Compagnon_avant_geste`.
  - **Testé en Play** (R15) : position de la main mesurée pendant le lancer (elle recule, passe au-dessus de la tête, finit devant, revient au repos en 0,65 s) ; la Tiflask suit la main puis part à 0,31 s ; ordre et instants des sons relevés (souffle au lâcher, tintements à 0,78, 1,03 et 1,21 s, pop d'ouverture, « pouf » et scintillement à l'apparition 0,17 s plus tard, bouchon à la fermeture ; aspiration, scintillement et pop au rappel) ; aucune erreur. Captures `2026-10-26_22h10_*`. Pendant les tests, des retards d'une seconde venaient de l'outil de pilotage de Studio (il bloque le jeu pendant ses temps d'attente), pas du jeu.
  - **Non vérifié** : l'écoute des sons (pas entendus), le geste en R6, le geste vu par un autre joueur.
- 26 oct. 2026 (soir) : étape 6 faite (demande de Mohand : aide à l'écran pour la touche R).
  - **HUD** (`UI.HUD`) : au-dessus du bouton MENU, même style que sa touche : touche « R » en biseau sombre (croix de la manette dessinée, branche du bas en cyan, si la dernière entrée vient d'une manette) et cadre blanc « SORTIR CRAMOSAUR » / « RENTRER CRAMOSAUR » (le texte rétrécit pour les noms longs, petit rebond quand il change). Glisse hors de l'écran avec le reste du HUD quand un menu s'ouvre. Cachée sur écran tactile (le bouton rond SORTIR / RENTRER la remplace), quand le leader ne peut pas sortir (K.O., pas de modèle 3D) et en intérieur. Nouvelle fonction `api.aideCompagnon(texte)`, tenue à jour toutes les 0,25 s par `Tiflasks.Compagnon`.
  - Sauvegardes : `Sauvegardes_UI.HUD_avant_aide_compagnon`, `Compagnon_avant_aide`.
  - **Testé en Play** : aide affichée (« R » et « SORTIR CRAMOSAUR », capture `2026-10-26_22h23_aide-touche-r.jpg`), passage à « RENTRER CRAMOSAUR » après R, glissement hors de l'écran à l'ouverture de l'Équipe puis retour à la fermeture. **Non testé** : cachée en intérieur (le client de test a été déconnecté avant la vérification), croix de la manette, écran tactile.
  - **Studio instable en fin de séance** : à chaque lancement du Play, le client de test était déconnecté du serveur après quelques secondes, avec l'erreur interne de streaming « readRegionRemoval error total time exceeded » côté serveur. Un essai témoin avec les versions sauvegardées du HUD et de `Compagnon` donne le même résultat : ça ne vient pas de ces modifications. À refaire après un redémarrage de Studio (Ctrl+S avant de fermer).
