---
tags:
  - monde
  - route
  - lumeridia
  - route-5
aliases:
  - Route 5
  - Route-5
---
# 🛤️ Route 5

* **Province :** [[00_Province_Lumeridia|Luméridia Est]]
* **Départ (Ouest) :** [[Port-Saphir]]
* **Arrivée (Est) :** [[Hameau-Doré]]
* **Connexions secondaires :** Anciennes fermes solaires, sentiers de transhumance
* **Environnement majeur :** Vastes plaines ouvertes, prairies d'élevage dorées, champs de graminées et petits bosquets ombragés.

## 🌅 Rôle et Ambiance
* **Rôle dans l'aventure :** L'avant-dernière grande route avant le donjon de la Team Glaciatech. C'est une route apaisante et bienveillante, axée sur l'élevage et l'entraînement. Les dresseurs rencontrés y sont nombreux mais proposent des affrontements justes et formateurs. C'est le lieu idéal pour faire évoluer ses Tifazelts grâce au bonheur et à l'XP abondante.
* **Ambiance :** Lumineuse, sereine et chaleureuse. En s'éloignant des côtes maritimes de Port-Saphir, l'air s'adoucit et se charge du parfum des foins coupés. La lumière y est radieuse, souvent rasante, donnant aux herbes de superbes teintes ambrées et dorées.
* **Taille (version Roblox) :** Très large et ouverte. Contrairement à d'autres routes qui forment des couloirs, la Route 5 ressemble à un vaste monde ouvert vallonné où le joueur peut chevaucher ou marcher librement.

## 🗺️ Découpage du Tracé (Les 3 Parties)

### 🌾 Partie 1 : La Lisière Océane
* **Description :** En sortant par la Porte des Plaines de Port-Saphir, le joueur monte un léger talus herbeux. Les vents portent encore quelques embruns, mais l'horizon s'ouvre sur un océan de verdure et d'herbes sèches.
* **Particularité :** Les herbes hautes sont d'un vert-jaune éclatant. On y trouve encore quelques Tifazelts influencés par le climat côtier.

### 🌳 Partie 2 : Le Val des Éleveurs
* **Description :** La zone centrale de la route. De vastes pâturages bordés de murets en pierres sèches et de clôtures en bois. De majestueux chênes solitaires offrent de grands cercles d'ombre pour se reposer.
* **Particularité :** Des PNJs éleveurs y font paître leurs créatures. C'est une zone très riche en affrontements amicaux et en loot lié au soin et au Bonheur. 

### ☀️ Partie 3 : Le Plateau Doré
* **Description :** Une plaine immense entièrement tapissée de blés et de graminées dorées. Des moulins à vent commencent à poindre à l'horizon, annonçant l'arrivée imminente au village.
* **Particularité :** Le chemin de terre batue s'élargit et devient plus clair. L'exposition au soleil est maximale. De petits points d'eau parsèment le paysage pour abreuver la faune locale.

## 🐾 Tifazelts Sauvages (Spawns)
*Zone d'apparition principale : Les immenses champs d'herbes de la Partie 2 et 3.*

| Tifazelt (Nom temp.) | Type | Niveau | Taux d'apparition | Moment de la journée |
| :--- | :--- | :--- | :--- | :--- |
| *Créature de Pâturage (Bovin/Ovin)* | [[9. Table des types|Normal]] / [[9. Table des types|Sol]] | 13 - 15 | 35% | Jour |
| *Oiseau Chanteur* | [[9. Table des types|Vol]] / [[9. Table des types|Fée]] | 12 - 14 | 25% | Matin / Jour |
| *Insecte Mielleux* | [[9. Table des types|Insecte]] / [[9. Table des types|Plante]] | 12 - 15 | 20% | Jour / Nuit |
| *Chien/Renard de Garde* | [[9. Table des types|Normal]] ou [[9. Table des types|Feu]] | 14 - 16 | 15% | Nuit |
| *Espèce rare du Plateau* | [[9. Table des types|Fée]] ou [[9. Table des types|Acier]] | 15 - 16 | 5% | Aube / Crépuscule |

*(Note : Tableaux à ajuster une fois la liste des 150 Tifazelts validée)*

## ⚔️ Dresseurs à affronter (PNJ)
Les dresseurs de cette route se spécialisent souvent dans les statistiques défensives et les attaques de soin ou de renforcement.

* **Éleveuse Clara :** *"Mes Tifazelts mangent la meilleure herbe de Luméridia !"* (Équipe : 2x Normal Niv. 14)
* **Fermier Baptiste :** Posté près d'un tracteur solarpunk. *"La récolte promet d'être bonne, voyons ce que tu vaux !"* (Équipe : 1x Plante Niv. 15, 1x Sol Niv. 14)
* **Ornithologue Robin :** *"Regarde tous ces oiseaux migrateurs..."* (Équipe : 3x Vol Niv. 13)
* **Dresseur Prometteur Yassine :** Un rival de transition cherchant à tester les badges/niveaux du joueur. *"Si tu vas au Hameau-Doré, tu dois d'abord me battre !"* (Équipe : 1x Feu Niv. 15, 1x Combat Niv. 16)

## 🎒 Objets et Loot (À ramasser)
* 2x **Super Potion** : Cachées dans les hautes herbes dorées.
* 1x **[[13. Objets#Grelot Douceur|Grelot Douceur]] (ou équivalent)** : Un objet à faire tenir qui augmente plus rapidement le Bonheur du Tifazelt. Caché au pied d'un grand chêne dans le Val des Éleveurs.
* 3x **Baies Nourrissantes** : Dans de petits buissons au bord des clôtures, excellentes pour la cuisine.
* 1x **[[1. Menus Et Interfaces#Tiflask|Tiflask Amis]]** : Une fiole qui rend le Tifazelt capturé plus amical dès le départ.

## ⚙️ Technique & Level Design (Roblox)
* **Grandes étendues (Performance) :** La zone étant vaste, utiliser du *Terrain* lisse (`Grass` et `LeafyGrass` coloré en jaune/doré) et des *Meshes* d'herbes en `Instancing` pour garder un bon framerate.
* **Atmosphère visuelle (Lighting) :** Un effet de lumière rayonnante avec des *SunRays* prononcés, et une teinte de lumière (`Ambient` et `OutdoorAmbient`) chaleureuse (RGB autour de 255, 230, 180) pour sublimer l'effet "fin d'après-midi éternelle".
* **Bande-son :** Guitare folk très entraînante, violon (fiddle), et accordéon. Une musique légère, pastorale et joyeuse rappelant un voyage à travers la campagne. 

## 🚧 À développer
* Intégrer un système de météo dynamique léger (vent qui se lève et fait onduler les champs de blé).
* Placer quelques PNJ offrant d'échanger des baies contre des ingrédients de cuisine utiles pour la classe Cuisinier.