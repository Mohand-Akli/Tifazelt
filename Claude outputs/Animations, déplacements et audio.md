---
tags:
  - production
  - roblox
  - animation
  - audio
aliases:
  - Animations PNJ
  - Musiques et sons
  - Course et vélo
---
# 🎬 Animations, déplacements et audio

> Construit le 20 oct. 2026. Rien ici n'est encore écrit dans le GDD : **tout est PROVISOIRE** et à valider (vitesses, choix des musiques, style des animations). Suivi : [[À décider et à faire]].

## 🧍 1. Animations des PNJ

Les PNJ sont des personnages R6. Ils sont animés **côté client**, sans fichier d'animation, par le script `StarterPlayerScripts.PNJ_Animations`. Les gestes sont dans le module `ReplicatedStorage.Animations.GestesPNJ`.

**Pour chaque PNJ :**
- il **respire** en permanence et se balance un peu ;
- il fait un **geste tiré au hasard** dans la liste de son type, avec des fondus, puis marque une pause de 2 à 7 secondes ;
- il **tourne la tête vers le joueur** quand celui-ci passe à moins de 10 studs ;
- il le **salue une fois** quand il arrive, selon son type (au plus une fois par minute) ;
- **pendant un dialogue**, il fait des gestes de conversation et hoche la tête en regardant le joueur.

Seuls les PNJ à moins de 110 studs de la caméra sont animés.

Le type est **deviné à partir du nom et du rôle** du PNJ. Pour le forcer, on pose l'attribut `TypeAnim` sur le PNJ.

### Gestes par type (poids = fréquence relative)

| Type | Qui (exemples) | Gestes |
| :--- | :--- | :--- |
| Marchand | Léon, Hugo, Margot, Inès (fleuriste), Rosa (glaces) | compter (3), présenter (2), essuyer le comptoir (2), regarder autour (2), mains sur les hanches, saluer, hocher la tête |
| Soignant | Infirmière | mains jointes (3), taper sur l'écran (2), hocher (2), saluer, regarder autour |
| Accueil | Réceptionniste de la Guilde | écrire au registre (3), présenter (2), hocher (2), mains jointes (2), regarder autour |
| Barista | Lou | essuyer une tasse (3), verser (2), présenter, hocher, regarder autour |
| Artisan | Nadia, Anselme, Lise | ouvrage des mains (4), s'étirer, s'essuyer le front, se gratter la tête, regarder autour |
| Agriculteur | Rosa (maraîchère), Karim, Augustin, Firmin, Odette, Apolline, Aurèle | ratisser (4), s'essuyer le front (2), mains sur les hanches (2), s'étirer, arroser, regarder autour |
| Jardinier | Paulin, Inaya | arroser (3), ratisser (2), front, mains sur les hanches, regarder autour |
| Pêcheur | Gaspard, Mila, Joseph, Yanis, Oscar, Marius, Mira, Maël | tenir la canne avec petites touches (5), lancer, main en visière (2), bâiller, bras croisés |
| Garde | Romain, Joris, Aubin, Ernest | mains dans le dos aux aguets (4), salut, regarder autour (2), mains sur les hanches (2) |
| Dresseur | Kaël, Ayla, Sara, Théo (scout), Inès et Léo (gamins), Bastien | poing levé (2), sautiller (2), lancer de Tiflask imaginaire (2), bras croisés (2), regarder autour (2), mains sur les hanches |
| Enfant | Lina, Théo, Tom, Nina, Nour, Lou (Route 1) | sautiller (3), balancer les bras (3), coucou des deux mains (2), regarder autour (2), se gratter la tête |
| Ancien | Mamie Odile, Victor, Basile | dos voûté (4), hocher (2), soupirer (2), se gratter la tête, regarder autour |
| Promeneur | Léa, Léonie, Elias, Ivo, Félix, Ysaline, Hélène, Paulette, Lina | lire une carte (3), regarder autour (3), main en visière (2), s'étirer, soupirer, mains sur les hanches |
| Lettré | Céleste (libraire et cartographe), Professeure Anir, Sorlin | lire un livre (4), main au menton (3), montrer du doigt, lire une carte, regarder autour |
| Rêveur | Ondine, Voyageuse en manteau gris | regarder le ciel (4), rêverie (balancement, 3), bras croisés, soupir |
| Famille | Maman, Rosalie, Fabienne | mains jointes (2), bras croisés (2), hocher (2), saluer, regarder autour (2), mains sur les hanches |
| Guide | Anouar, Marin (maître-nageur) | montrer du doigt (3), mains sur les hanches (2), main en visière (2), s'étirer, regarder autour (2) |
| Habitant | tous les autres | regarder autour (3), mains sur les hanches (2), bras croisés (2), saluer, se gratter la tête, soupirer |

**Accueil du joueur :**
- coucou des deux mains pour les enfants, poing levé pour les dresseurs, salut pour les gardes ;
- hochement de tête pour l'accueil, la barista et les anciens ;
- petit signe de la main pour tous les autres.

**Limite :** les figurines de [[Val Palmeraie]] ne sont pas des personnages Roblox et ne sont pas concernées. Elles ont leur propre animation, gérée par `ValPalmeraie_Ambiance`.

## 🏃 2. Le joueur : animations, course et vélo

- **Animations :** pack **« Cartoony »** de Roblox (repos, marche, course, saut, chute, escalade, nage), posé à chaque apparition par `ServerScriptService.Deplacements_Serveur`. Les packs « Stylish », « Rthro » et « Ninja » ont aussi été vérifiés et sont prêts en remplacement.
- **Course :**
  - commandes : maintenir **Maj** (PC), appuyer sur le **stick gauche** (manette), ou le bouton **COURIR** (mobile, il bascule) ;
  - vitesse de marche 16, de course 26 ;
  - champ de vision un peu plus large, petite poussière aux pieds ;
  - pas d'endurance pour l'instant.
- **Vélo** (objet clé « Vélo ») :
  - commandes : touche **V**, **croix haut** (manette), bouton **VÉLO** (mobile), ou Sac > Objets clés > **Enfourcher** ;
  - vitesse 38 ;
  - vélo bleu azur avec panier, sonnette et garde-boue, fabriqué par le serveur pour que **tous les joueurs le voient** ; **nouveau modèle depuis le 27 oct. 2026** (`ReplicatedStorage.Joueur.Velos`, environ 250 pièces : roues à rayons ajourées avec flancs crème, cadre « col de cygne », guidon hollandais, selle à ressorts, panier en osier, porte-bagage, phare, chaîne et carter ; plusieurs formes prévues : ville, course, VTT) ;
  - **plusieurs vélos (27 oct. 2026, PROVISOIRE)** : Vélo Azur (offert par Maman, vitesse 38), Vélo Corail (ville, 38, 3 500 TFD), VTT Sentier (41, 7 500 TFD), Vélo de course Éclair (46, 12 000 TFD), Vélo Étoile (ville ivoire et dorée, 44, 20 000 TFD) ; un objet clé par vélo ; choix dans Sac > Objets clés > Enfourcher (change de vélo si on roule déjà) ; la touche V prend le vélo choisi ; vendus au magasin « Vélos de l'Azur » de Bourg-Azur ;
  - **sortie du sac (27 oct. 2026, PROVISOIRE)** : le vélo jaillit de la hanche en grandissant avec un léger rebond (0,35 s), petit nuage d'étincelles, la main droite plonge vers le sac puis se lève, le personnage monte en même temps ; en descendant, une copie locale du vélo rétrécit vers la hanche (0,25 s) ;
  - pose de pédalage, roues et pédalier qui tournent, inclinaison dans les virages : ces effets sont visibles par le joueur lui-même, les autres le voient debout sur le vélo ;
  - on descend tout seul en entrant dans un bâtiment, dans l'eau ou en s'asseyant ;
  - il est interdit à l'intérieur ;
  - sonnette en montant ;
  - **pièces ajustées (28 oct. 2026)** pour qu'aucune face ne se superpose à une autre (scintillement) : segments de jante à largeur alternée, panier redessiné (chaque plaque dans son propre plan), pièce arrière de la selle de course plus épaisse, manivelles un peu plus épaisses, catadioptre arrière décollé du garde-boue. Aspect inchangé. Sauvegarde : `ServerStorage.BourgAzur_Sauvegarde_Parfait.Etape2_Scintillements.Velos_avant_etape2`.
- **Obtention (PROVISOIRE) :** Maman offre le vélo avec le Tuba au début d'une nouvelle partie. Il est aussi dans les données de test.

## 🎵 3. Musiques

Script `StarterPlayerScripts.Musique`, catalogue `ReplicatedStorage.Audio.Sons`.

**Fonctionnement :**
- fondus de 1,5 s entre deux musiques ;
- une musique de zone reprend là où elle s'était arrêtée ;
- volume réglé par le curseur Musique des Paramètres.

**Ordre de priorité :** combat, puis écran titre, puis sous l'eau, puis intérieur, puis zone.

Toutes les pistes viennent de la **bibliothèque sous licence de Roblox** et ont été vérifiées : elles se chargent. Elles ont été **choisies sur leur titre et leur description, sans écoute** : il faut les valider à l'oreille.

| Moment | Piste | Ce que dit le vault |
| :--- | :--- | :--- |
| Écran titre, création | « Where The Adventure Begins » (DistroKid) | — |
| Bourg-Azur | « Town Theme 1 (Day) » (DistroKid) | — (pas de bande-son décrite) |
| Route 1 | « The Adventure Begins » (APM) | Mélodie enjouée, cuivres doux, guitare folk |
| Bosquet des Égarés | « Mysterious Forest » (APM) | Partie 3 plus mystique |
| Val Palmeraie | « Middle Eastern Oud » (APM) | Flûte ney, percussions douces, kanun |
| Maison | « Peace Of Mind » (APM) | — |
| Infirmerie | « Still Water Patterns » (DistroKid) | — |
| Café des Embruns | « Swaying Tides » (DistroKid) | — |
| Bazar, Fleuriste | « Cheery Ukulele C » (APM) | — |
| Guilde | « Sun-Drenched Afternoon » (DistroKid) | — |
| Sous l'eau | « Light On The Surface » (DistroKid) | Ambiance étouffée, cotonneuse |
| Combat sauvage | « (RPG) Battle » (DistroKid) | — |
| Combat de dresseur, PvP | « The Battle Awakens » (DistroKid) | — |
| Gardien, boss, raid | « Clash of Titans » (DistroKid) | — |
| Victoire | « Victory Fanfare Sting » (APM), 10 s | — |

> À terme : remplacer par des compositions originales qui suivent les bandes-son décrites dans les fiches des lieux.

## 🔔 4. Sons de l'interface et du dialogue

Ces sons viennent du pack de sons d'interface publié par Roblox (`Roblox_UI_…`), sauf la sonnette (Pro Sound Effects). Ils passent par le curseur Effets des Paramètres.

- **Boutons :**
  - survol ou sélection à la manette : petit clic aigu ;
  - appui : clic ;
  - bouton désactivé : refus ;
  - interrupteur : bascule.
- **Menus :**
  - ouverture ou changement d'écran : balayage (en même temps que les bandes de transition) ;
  - retour : papier qui glisse ;
  - fenêtre de confirmation : « pop » ;
  - notification : signal ;
  - secret trouvé : accord.
- **Dialogue :**
  - « pop » à l'ouverture, petit clic à chaque réplique suivante, « au revoir » à la fermeture ;
  - **voix des PNJ** : un petit son toutes les deux lettres pendant que le texte s'écrit ;
  - la hauteur de la voix est propre à chaque PNJ (tirée de son nom) : plus aiguë pour les enfants, plus grave pour les anciens.
- **Déplacements :** sonnette en montant sur le vélo, souffle en descendant.
- **Tiflask dans le monde** (26 oct. 2026, PROVISOIRE, à valider à l'écoute) : sons Pro Sound Effects, joués **à l'endroit de l'action**. Les joueurs proches les entendent, de moins en moins fort avec la distance (au-delà de 90 studs, plus rien).
  - souffle au lâcher de la Tiflask ;
  - tintement de verre à l'atterrissage puis à chaque rebond, de plus en plus faible ;
  - pop de bouteille quand le bouchon saute ;
  - « pouf » quand le Tifazelt apparaît, et un scintillement qui monte jusqu'à la fin de sa croissance ;
  - au rappel : aspiration qui finit par un pop au moment où il disparaît dans la fiole, et scintillement ;
  - petit bouchon quand la Tiflask se referme.
  - Le début de chaque son a été mesuré en Play (volume par tranches de 50 ms) pour tomber sur l'action.

## 🙋 4 bis. Gestes du joueur (26 oct. 2026, PROVISOIRE)

Gestes procéduraux, sans fichier d'animation, avec les mêmes conventions que les gestes des PNJ. Chaque client les joue sur le personnage concerné : les autres joueurs voient donc aussi le geste. Ils se mêlent aux animations du personnage, avec un fondu d'entrée et de sortie. Ils marchent en R6 et en R15.
- **Lancer** (0,65 s) :
  - prise d'élan : bras droit levé en arrière, coude plié, buste tourné vers la droite, bras gauche tendu vers l'avant ;
  - puis le bras passe par-dessus la tête et le buste pivote ;
  - la Tiflask, tenue dans la main, part à 0,3 s.
- **Rappel** (1,1 s) : bras tendu devant, la Tiflask apparaît dans la main et le Tifazelt y est aspiré.
- **Pas de geste sur le vélo** : la pose de pédalage tient déjà les bras.

**Aide à l'écran** : au-dessus du bouton MENU, la touche « R » (ou la croix de la manette) et l'action en cours, « Sortir Cramosaur » ou « Rentrer Cramosaur » (`UI.HUD`, `api.aideCompagnon`).

## 🛠️ 5. Où trouver quoi (Roblox Studio)

| Élément | Emplacement |
| :--- | :--- |
| Gestes des PNJ | `ReplicatedStorage.Animations.GestesPNJ` |
| Animation des PNJ | `StarterPlayerScripts.PNJ_Animations` |
| Animations du joueur, vélo (serveur) | `ServerScriptService.Deplacements_Serveur` |
| Course et vélo (client) | `ReplicatedStorage.Joueur.Deplacements` + `StarterPlayerScripts.Deplacements_Client` |
| Demande de vélo | RemoteEvent `ReplicatedStorage.Reseau.Deplacement` |
| Catalogue des sons | `ReplicatedStorage.Audio.Sons` (`jouerEn` : son placé dans le monde) |
| Gestes du joueur (lancer, rappel) | `ReplicatedStorage.Joueur.Gestes` |
| Sons de la Tiflask | `ReplicatedStorage.Tiflasks.Lancer` (effets `tiflask_*` du catalogue) |
| Musique | `StarterPlayerScripts.Musique` |
| Sauvegardes avant modification | `ServerStorage.Sauvegardes_UI` (`Kit_avant_sons`, `Dialogue_avant_sons`, `MenuManager_avant_sons`, `UI_Client_avant_sons`, `DonneesTest_avant_velo`, `NouvellePartie_avant_velo`, `Inventaire_avant_velo`) |

**Commandes de test (en Play) :**
- attribut joueur `TestCourse` = true : courir ;
- attribut joueur `TestVelo` = true / false : monter ou descendre du vélo ;
- attribut local `_GesteForce` = nom d'un geste, posé sur un PNJ : le joue tout de suite ;
- attribut de workspace `MusiqueCoupee` = true : coupe la musique.
- touche **K** (Play dans Studio seulement) : bascule les modèles de la lignée Cramosaur entre v03 et v04 (attribut `VersionTifazelts` de ReplicatedStorage).
