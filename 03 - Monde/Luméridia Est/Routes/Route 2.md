---
tags:
  - monde
  - route
  - lumeridia
  - route-2
aliases:
  - Route 2
  - Route-2
---
# 🛤️ Route 2

* **Province :** [[00_Province_Lumeridia|Luméridia Est]]
* **Départ (Sud) :** [[Val Palmeraie]]
* **Arrivée (Nord) :** [[Cité Ocre]]
* **Connexions secondaires :** Accès aux contreforts menant à la [[Grotte Inconnue]]
* **Environnement majeur :** Transition paysagère (savane sèche, canyons argileux, sols ocre), marquant le passage d'une végétation luxuriante à un climat semi-aride.

## 🌅 Rôle et Ambiance
* **Rôle dans l'aventure :** Deuxième grande route du jeu. Elle offre un défi légèrement relevé par rapport à la Route 1, avec des dresseurs mieux préparés et l'introduction de Tifazelts capables de résister aux environnements secs et rocailleux. C'est également ici que le joueur peut trouver l'entrée secrète de son premier donjon optionnel (la Grotte Inconnue).
* **Ambiance :** Sèche, chaude et poussiéreuse, mais magnifiquement contrastée. Les palmiers cèdent la place à des broussailles épineuses et à des roches aux teintes rougeoyantes. La lumière y est plus dure, écrasante en milieu de journée.
* **Taille (version Roblox) :** Route assez longue et accidentée, avec des dénivelés naturels, des gorges étroites et des corniches.

## 🗺️ Découpage du Tracé (Les 3 Parties)

### 🌿 Partie 1 : L'Ombre Déclinante
* **Description :** En sortant de la Porte du Sirocco de Val Palmeraie, l'herbe est encore un peu verte et quelques arbres isolés offrent de l'ombre.
* **Particularité :** Les hautes herbes sont plus éparses mais plus hautes (couleur jaune/beige). Le joueur y croise les derniers Tifazelts de type Plante et Insecte de la région avant l'aridité totale.

### 🪨 Partie 2 : Le Défilé des Roches Rouges
* **Description :** La route se resserre entre deux falaises argileuses. Le sol devient rougeâtre (terre battue et graviers). De gros rochers bloquent parfois le passage direct, obligeant à slalomer ou à affronter des dresseurs postés en embuscade.
* **Embranchement (Est) :** Une faille discrète dans la falaise permet de quitter le chemin principal pour rejoindre l'entrée de la [[Grotte Inconnue]].

### 🏜️ Partie 3 : La Steppe Ocre
* **Description :** Le canyon s'ouvre sur une vaste étendue rocailleuse annonçant l'architecture de la prochaine ville. Le vent chaud (sirocco) soulève par moments de légers nuages de poussière.
* **Particularité :** La visibilité peut baisser légèrement. Au loin, on aperçoit déjà le grand arc de la Porte de la Palmeraie de la Cité Ocre.

## 🐾 Tifazelts Sauvages (Spawns)
*Zone d'apparition principale : Les herbes sèches et les zones rocailleuses.*

| Tifazelt (Nom temp.) | Type | Niveau | Taux d'apparition | Moment de la journée |
| :--- | :--- | :--- | :--- | :--- |
| *Lézard des sables* | [[10. Table des types#Terre|Terre]] | 5 - 7 | 35% | Jour |
| *Oiseau rapace* | [[10. Table des types#Vent|Vent]] | 6 - 8 | 25% | Matin / Jour |
| *Scorpion rocailleux* | [[10. Table des types|Poison]] / [[10. Table des types|Insecte]] | 5 - 7 | 20% | Nuit |
| *Petit golem d'argile* | [[10. Table des types#Terre|Terre]] | 6 - 8 | 15% | Jour / Nuit |
| *Espèce rare du défilé* | [[10. Table des types|Feu]] | 7 - 8 | 5% | Jour intense (Midi) |

*(Note : Tableaux à ajuster une fois la liste des 150 Tifazelts validée)*

## ⚔️ Dresseurs à affronter (PNJ)
Les dresseurs de la Route 2 commencent à utiliser des stratégies (attaques infligeant des statuts, objets de soin).

* **Campeur Malik :** *"Il fait chaud, mais mon équipe est brûlante d'énergie !"* (Équipe : 2x Tifazelts Terre Niv. 6)
* **Exploratrice Léa :** Postée près de l'embranchement de la Grotte Inconnue. *"Tu cherches des minerais rares ou juste la bagarre ?"* (Équipe : 1x Oiseau Niv. 8)
* **Gamin Léo (Revanche) :** *"Je me suis entraîné depuis Bourg-Azur !"* (Équipe : 1x Rongeur évolué Niv. 7, 1x Insecte Niv. 5)

## 🎒 Objets et Loot (À ramasser)
* 2x **[[1. Menus Et Interfaces#Médicaments|Potion basique]]** : Visibles sur de petites corniches rocheuses.
* 1x **[[1. Menus Et Interfaces#Tiflask|Tiflask Roc]]** (Tiflask efficace sur le type Terre) : Cachée près de l'entrée de la Grotte Inconnue.
* 1x **Anti-Brûlure** / **Anti-Poison** : Indispensable avant de défier les créatures du défilé.

## ⚙️ Technique & Level Design (Roblox)
* **Effets atmosphériques (Lighting & Particles) :** * `Brightness` très élevée et `ColorShift_Top` tirant vers l'orange pâle pour simuler la chaleur.
  * Particules de poussière (`ParticleEmitter`) activées par zones au sol pour représenter le vent chaud.
  * Un léger effet de mirage (distorsion) peut être appliqué au loin sur la Partie 3.
* **Verticalité :** Utilisation de rampes de *Terrain* en matériau *Sandstone* ou *Cracked Lava* (sans lave, juste la texture craquelée) pour donner du relief aux falaises argileuses.
* **Bande-son :** Guitare acoustique aux accents hispaniques/orientaux, percussions sèches (cajón), et parfois le cri aigu d'un rapace résonnant dans le canyon.

## 🚧 À développer
* Coder l'effet de chaleur/mirage visuel sur la dernière partie de la route.
* Créer un script bloquant temporairement l'entrée de la Grotte Inconnue si le joueur n'a pas accompli une quête spécifique à Val Palmeraie.