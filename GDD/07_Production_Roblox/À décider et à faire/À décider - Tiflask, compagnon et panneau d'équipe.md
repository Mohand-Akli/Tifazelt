---
tags:
  - production
  - roblox
  - suivi
---
# Tiflask, Tifazelt compagnon et panneau d'équipe (26 oct. 2026) — PROVISOIRE

> [[À décider et à faire|Sommaire : à décider et à faire]]

## Portraits et Tiflask (26 oct. 2026) — PROVISOIRE
- **Portraits** des Tifazelts qui ont un modèle (Cramosaur, Cramoraptor, Cramorex) : buste rendu dans Blender dans le cercle de `Kit.portrait` (tous les écrans). Les autres gardent l'initiale.
- **Tiflask** : forme reprise de l'icône 2D du jeu (le vault ne décrit pas son apparence). Couleurs des liquides à valider : simple rouge-orangé, écume turquoise avec bulles, amitié rose. La Tiflask d'Amitié a une image et un modèle mais n'est ni en vente ni dans les règles du combat (bonus de capture et 250 de bonheur à brancher).
- **Base des systèmes** : `ReplicatedStorage.Tiflasks.Lancer` (lancer, ouverture, sortie et retour d'un Tifazelt). Branchée le 26 oct. 2026 sur la sortie d'un Tifazelt dans le monde (section suivante). Reste à décider : capture dans le monde (lancer sur un Tifazelt sauvage ?).
- **À vérifier avec de vrais clics** : pendant les tests pilotés par commandes, les menus restaient parfois bloqués (gestionnaire « occupé » : titre qui ne se ferme pas, inventaire qui ne s'ouvre pas). Probablement dû au pilotage de Studio, mais à confirmer en jouant normalement.

## Tifazelt qui accompagne le joueur (26 oct. 2026) — PROVISOIRE
Le vault ne dit rien d'un Tifazelt qui suit le joueur hors combat. Détail : [[Sortie du Tifazelt - plan]].
- **Commandes** : touche **R** (PC), **croix bas** (manette), bouton rond **SORTIR / RENTRER** (mobile, au-dessus de COURIR) pour sortir le leader ou rentrer celui qui est dehors ; bouton « Sortir » / « Rentrer » dans la **Fiche** de chaque membre (le menu se ferme pour qu'on voie le lancer). Aide à l'écran au-dessus du bouton MENU (« R · Sortir Cramosaur », croix dessinée à la manette), cachée sur mobile, en intérieur et quand le leader ne peut pas sortir. À valider : touches, emplacement du bouton mobile et de l'aide.
- **À surveiller** : en fin de séance du 26 oct. 2026, Studio déconnectait le client de test du serveur à chaque Play (« readRegionRemoval error total time exceeded »), même avec les anciennes versions des scripts. Un redémarrage de Studio a réglé le problème ; si ça revient, regarder le streaming du terrain.
- **Scène** : Tiflask lancée depuis la main, Tifazelt qui grandit depuis la fiole, suivi derrière le joueur et un peu à droite, regard vers le joueur à l'arrêt ; rentrée dans une Tiflask qui apparaît dans la main.
- **Geste et sons (26 oct. 2026, soir)** : geste de lancer par-dessus la tête et geste de rappel (bras tendu), procéduraux, vus par tous les joueurs (`Joueur.Gestes`). Sons Pro Sound Effects placés dans le monde : souffle, tintements, pop du bouchon, « pouf » et scintillement, aspiration (détail dans [[Animations, déplacements et audio]]). **À valider** : le geste à l'œil, chaque son à l'écoute (choisis sur leur titre et sur leur volume mesuré, pas écoutés).
- **Apparence** : modèle 3D avec la texture retouchée (`SA_Retouche`), pas les images du combat. Le Tifazelt traverse les obstacles (aucune collision).
- **Règles** : seules les espèces avec un modèle 3D peuvent sortir (lignée Cramosaur pour l'instant ; les autres : « ne peut pas encore sortir de sa Tiflask »). Refus si K.O. ou en intérieur. Rentre tout seul s'il tombe K.O., s'il quitte l'équipe ou à la mort du personnage ; en intérieur il rentre et ressort tout seul à la sortie ; après une évolution, la nouvelle forme ressort. Sur le vélo il suit plus vite et réapparaît près du joueur s'il est à plus de 50 studs.
- **Tiflask de sortie** : celle de la capture (champ `tiflask` posé par le moteur de combat) ; starter et Tifazelts plus anciens : Tiflask simple. À décider : Tiflask propre au starter ?
- **Bug corrigé en route** : à l'évolution, `Combat.Moteur.evoluer` changeait le nom mais pas le champ `espece` (les Tifazelts créés par `Especes.creer` en ont un). Les images de combat et le portrait de la forme évoluée auraient montré l'ancienne forme. Sauvegarde : `Sauvegardes_UI.Moteur_avant_compagnon`.

## Panneau d'équipe en exploration (26 oct. 2026) — PROVISOIRE
Demande de Mohand d'après une capture de Cobblemon. Le vault ne décrit pas de panneau d'équipe dans le HUD. Détail : [[Panneau d'équipe - plan]].
- **Place** : bord gauche, centré en hauteur. Six cartes biseautées : numéro de touche, portrait, nom, niveau, PV, Tiflask (ouverte si le Tifazelt est dehors). Choisie : la carte avance, liseré terracotta. Dehors : liseré cyan, étiquette « DEHORS ». K.O. : grisée.
- **Commandes** : touches 1 à 6, croix gauche / droite, clic. R / croix bas / bouton mobile agissent sur le Tifazelt choisi (et non plus sur le leader).
- **À valider** : place et taille du panneau, toujours affiché (ou à replier ?), touches 1 à 6 (à vérifier avec le sac de Roblox s'il est actif), croix gauche / droite.
- **Testé en Play le 26 oct. 2026** (touches 1 à 6, croix, clic, R, K.O., intérieur, menus). Non testé : affichage manette et tactile.
