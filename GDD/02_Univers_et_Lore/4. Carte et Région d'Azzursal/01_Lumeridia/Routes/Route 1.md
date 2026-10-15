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
* **Événement de la Bague :** Le chemin semble se perdre et former un petit labyrinthe. C'est ici, au centre d'une petite clairière isolée (ou devant un vieil autel de pierre), que le joueur reçoit mystérieusement (ou découvre) la [[13. Objets#Bague (Nom à définir)|Bague]] mystique, avant que la brume ne se lève et ne révèle la sortie vers Val Palmeraie.

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

## 🚧 À développer
* Coder le script déclenchant la brume et l'obtention de la Bague (cinématique ou boîte de dialogue PNJ mystérieux).
* Valider les noms finaux des premiers Tifazelts sauvages peuplant cette route.