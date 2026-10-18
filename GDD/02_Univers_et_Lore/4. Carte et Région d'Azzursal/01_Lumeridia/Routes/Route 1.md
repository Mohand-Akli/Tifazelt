---
tags:
  - monde
  - route
  - lumeridia
  - route-1
aliases:
  - Route 1
  - Route-1
---
# 🛤️ Route 1

* **Province :** [[00_Province_Lumeridia|Luméridia Est]]
* **Départ (Est) :** [[Bourg-Azur]]
* **Arrivée (Ouest / Sud-Ouest) :** [[Val Palmeraie]]
* **Environnement majeur :** Littoral méditerranéen en pente douce, vastes plaines verdoyantes et petit bosquet labyrinthique.

## 🌅 Rôle et Ambiance
* **Rôle dans l'aventure :** Première voie terrestre que le joueur emprunte au début du jeu. C'est la zone du tutoriel naturel : le joueur y apprend les déplacements, les premières captures de Tifazelts dans les herbes hautes, et les mécaniques de combat contre des dresseurs PNJ débutants. Elle sert aussi de décor à l'événement scénaristique central de la Bague.
* **Ambiance :** Une route joyeuse, lumineuse et encourageante, baignée par la douce brise de la mer au départ, avant de s'enfoncer lentement dans la verdure plus dense de la province.
* **Taille (version Roblox) :** Un long chemin asymétrique divisé en trois sections naturelles distinctes, séparées par des collines basses et des clôtures en bois.

## 🗺️ Découpage du Tracé (Les 3 Parties)

### 🌊 Partie 1 : Le Sentier Côtier
* **Description :** Juste à la sortie de la porte de Bourg-Azur. Un chemin de terre claire longeant une petite falaise avec vue sur la mer.
* **Particularité :** Pas de hautes herbes ni d'ennemis. Zone sûre permettant au joueur de s'habituer aux contrôles, de ramasser son premier objet au sol et d'admirer le paysage. Un PNJ "guide" y donne souvent de premiers conseils d'exploration.

### 🌾 Partie 2 : La Plaine Herbeuse
* **Description :** Le chemin s'éloigne de la côte et s'élargit. Des parcelles d'herbes hautes luxuriantes bordent le chemin tracé.
* **Particularité :** Le vrai début de l'aventure. C'est ici que le joueur rencontre ses premiers Tifazelts sauvages aléatoires (niveaux 2 à 4) et se fait défier par de jeunes dresseurs enthousiastes. On y trouve de petits dénivelés permettant de sauter par-dessus de petits talus (raccourcis de retour).

### 🌳 Partie 3 : Le Bosquet des Égarés (Événement Scénarisé)
* **Description :** En approchant de Val Palmeraie, la route se rétrécit et s'enfonce dans un petit bois de chênes-lièges et d'oliviers denses. La lumière y est plus tamisée, parfois voilée d'une brume légère.
* **Événement de la Bague :** Le chemin semble se perdre et former un petit labyrinthe. C'est ici, au centre d'une petite clairière isolée (ou devant un vieil autel de pierre), que le joueur reçoit mystérieusement (ou découvre) la [[14. Objets#Bague (Nom à définir)|Bague]] mystique, avant que la brume ne se lève et ne révèle la sortie vers Val Palmeraie.

## 🐾 Tifazelts Sauvages (Spawns)
*Zone d'apparition principale : Les hautes herbes de la Partie 2.*

| Tifazelt (Nom temp.) | Type | Niveau | Taux d'apparition | Moment de la journée |
| :--- | :--- | :--- | :--- | :--- |
| *Oiseau de base* | [[9. Table des types#Vent|Vent]] | 2 - 4 | 40% | Matin / Jour |
| *Rongeur de base* | [[9. Table des types#Terre|Terre]] | 2 - 3 | 40% | Matin / Jour / Nuit |
| *Insecte (Chenille/Larve)* | [[9. Table des types|Insecte]] | 2 - 3 | 15% | Jour / Nuit |
| *Espèce rare du bosquet* | [[9. Table des types|Plante]] ou [[9. Table des types|Fée]] | 4 - 5 | 5% | Nuit uniquement |

*(Note : Tableaux à ajuster une fois la liste des 150 Tifazelts validée)*

## ⚔️ Dresseurs à affronter (PNJ)
Les dresseurs de la Route 1 possèdent 1 ou 2 Tifazelts de très bas niveau pour introduire le combat en douceur. L'affrontement se déclenche si le joueur croise leur ligne de vue.

* **Gamin Léo :** *"Mon Tifazelt et moi, on court partout dans les herbes !"* (Équipe : 1x Rongeur Niv. 3)
* **Pique-Niqueuse Sara :** *"Un petit combat avant le goûter ?"* (Équipe : 1x Oiseau Niv. 3)
* **Scout des Plaines Théo :** Placé à l'entrée du bosquet, il donne un indice sur la brume. (Équipe : 1x Insecte Niv. 4)

## 🎒 Objets et Loot (À ramasser)
* 2x **[[1. Menus Et Interfaces#Tiflask|Tiflask simple]]** (Pokéball de base) : Souvent laissés en évidence dans des coins herbeux pour inciter à la capture.
* 1x **[[1. Menus Et Interfaces#Médicaments|Potion basique]]** : Cachée derrière un arbre dans la Partie 2.

## ⚙️ Technique & Level Design (Roblox)
* **Obstacles directionnels :** De petits murets ou talus (les fameux "rebords" de Pokémon) permettent de descendre facilement en revenant vers Bourg-Azur, mais obligent à traverser les hautes herbes en allant vers Val Palmeraie.
* **Atmosphère (Lighting) :** Transition fluide : éclairage clair (`Brightness` élevée) dans la partie 1 et 2, puis le script modifie progressivement le `Fog` (brouillard) en blanc translucide dès l'entrée dans le Bosquet de la Partie 3.
* **Bande-son :** Mélodie enjouée, tempo allant, cuivres doux et guitare folk. Dans la Partie 3, la musique ralentit légèrement et devient plus mystique (cloches tubulaires, cordes) jusqu'à la résolution de l'événement.

* **État Roblox Studio (oct. 2026, passe 2 de finition) :** décor généré par `ServerStorage.MapGeneration.Route1` (mode d'emploi : module `LISEZMOI`) dans `Workspace.Map.Routes.Route1`. Sentier sinueux à largeur variable et lisières naturelles ; falaise côtière à strates avec blocs et aiguilles marines, maquis méditerranéen bas (lavande, ciste, genêt, agaves) et belvédère face à la mer ; plaine avec hautes herbes aux formes organiques, arbres en lisière, lieux repères (arbre solitaire, souche fleurie, petite clairière, vieille clôture) ; corniche à sens unique en strates (testée : infranchissable depuis le bas) ; bosquet sans grille, couloirs qui se resserrent, culs-de-sac fermés par des arbres tombés, haies à collision continue ; clairière de la Bague avec autel de pierre, pierres dressées et rayons de lumière doux. Seul script actif : `Route1_Ambiance` (client) pour la brume locale du bosquet et les papillons. PNJ, rencontres, objets et Bague restent des **repères** sans système de jeu.
* **Passe 3 (oct. 2026) :** colorimétrie plus chaude et cartoon (lumière ambiante chaude, étalonnage, ciel à nuages dessinés, couleurs du terrain ; réglages d'origine gardés dans `ServerStorage.Eclairage_AvantPasse3`) ; vent visible dans les Parties 1 et 2 (traînées blanches, pétales, hautes herbes qui ondulent, `GlobalWind`) ; 16 points d'intérêt (arche de sortie du Bourg, passage entre rochers, halte du Guide avec puits, marches de pierre, crique, tour de guet en ruine, col avec portillon, champs avec bottes de foin, ruisseau et passerelle, piquets des hautes herbes obligatoires, arbre à balançoire de Léo, rocher du Tiflask, mare de Sara, camp de Théo avec feu de camp). Les bords de la falaise côtière sont maintenant en pente douce (ils dessinaient un grand rectangle vu du ciel).
* **Passe 4 (oct. 2026) :** paysage enrichi sans changer le relief. Arbres, buissons et rochers « en cubes » remplacés par des modèles low poly à facettes (mêmes positions). Compositions dans les zones vides : lisières d'arbres en arrière-plan, bosquets, groupes de rochers, tapis de fleurs, pinèdes côtières, zones de végétation sèche, murets de pierre sèche, abords du sentier fleuris. Lieux secondaires : oliveraie sauvage, grand olivier remarquable, vieille charrette, petit sanctuaire de pierre, arche rocheuse au-dessus du sentier côtier, prairie fleurie avec amandier. Points d'intérêt complétés (dallage du puits, échelle de la tour, berges du ruisseau, couverture de pique-nique de Sara, tente et marmite de Théo). Bosquet des Égarés : parois de buissons, arbres qui dépassent des haies, sous-bois, troncs moussus, cadre de la clairière. Vie : libellules près de l'eau, oiseaux en vol, papillons supplémentaires.
* **Passe 5 (oct. 2026) :** la route devient un vrai couloir d'aventure. **Rivière de la Plaine** : l'ancien ruisseau est élargi (~26 studs) et relie désormais l'Asif-Safi à la mer ; un **grand pont de pierre** (54 studs, refuge avec banc, repères réservés à une future scène avec le rival) est le passage obligatoire entre la Plaine basse et le plateau. On ne traverse plus à la nage : dans la région de Bourg-Azur et de la Route 1, le **courant** ramène sur la rive au-delà de 12 studs dans l'eau. **Muraille** (corniche) : face continue sans prise, rebord à sens unique conservé, prolongée en pierre sèche de l'Asif-Safi jusqu'à la mer ; trou au pied de la rampe comblé. **Bosquet des Égarés** : la bordure verte extérieure est remplacée par une lisière d'arbres et de buissons, barrière en bois de la sortie retirée, lisières infranchissables jusqu'à l'eau au nord et au sud, trous des haies bouchés, buissons flottants recalés ; **3 nouveaux couloirs** (Sentier des Mousses, Allée du Grand Chêne, Passage des Racines) menant à une clairière aux champignons, un chêne géant servant de repère et des ruines avec une stèle. **Campagne** : Mas des Moissons, **grand moulin** aux ailes animées, champ de blé avec épouvantail, potager, enclos de Tifazelts (silhouettes provisoires) ; **4 cabanes de pêcheurs** avec pontons et barques, sentiers des berges jusqu'à l'embouchure. **18 PNJ R6** (dont Léo, Sara, Théo, le Guide, 2 nouveaux dresseurs débutants, agriculteurs, pêcheurs, une voyageuse mystérieuse, un randonneur égaré) et **8 secrets**. Les dresseurs ont leurs données (équipe, ligne de vue) mais aucun combat n'est encore codé.

## 🚧 À développer
* Coder le script déclenchant la brume et l'obtention de la Bague (cinématique ou boîte de dialogue PNJ mystérieux).
* Valider les noms finaux des premiers Tifazelts sauvages peuplant cette route.