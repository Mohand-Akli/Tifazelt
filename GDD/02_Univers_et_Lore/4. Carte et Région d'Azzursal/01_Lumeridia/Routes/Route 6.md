---
tags:
  - monde
  - route
  - lumeridia
  - route-6
aliases:
  - Route 6
  - Route-6
---
# 🛤️ Route 6

* **Province :** [[00_Province_Lumeridia|Luméridia Est]]
* **Départ (Ouest) :** [[Hameau-Doré]]
* **Arrivée (Est / Sommet) :** [[Colline Ksar]] / [[Repaire Glacitech]]
* **Connexions secondaires :** Anciennes corniches d'observation, sentiers d'éboulis
* **Environnement majeur :** Ascension montagneuse abrupte, transition brutale entre plaine agricole chaleureuse et roches givrées par des installations cryogéniques ennemies.

## 🌅 Rôle et Ambiance
* **Rôle dans l'aventure :** La Route 6 marque un tournant majeur dans l'aventure. Fini l'exploration paisible : c'est le chemin de l'affrontement. Le joueur doit gravir un sentier lourdement surveillé pour atteindre le cœur de la menace locale. C'est un véritable test de force avant le donjon du Repaire Glacitech.
* **Ambiance :** Oppressante et ascendante. On quitte la chaleur réconfortante des moissons pour un vent mordant et surnaturel. Des tuyaux crachent de l'air glacé, des barbelés bloquent les anciens sentiers, et des projecteurs magenta balaient les rochers. La musique s'accélère, signifiant le danger imminent.
* **Taille (version Roblox) :** Route très verticale. Conçue sous forme de lacets étroits et de corniches successives (switchbacks). La progression est ralentie par le terrain et les affrontements obligatoires.

## 🗺️ Découpage du Tracé (Les 3 Parties)

### 🍂 Partie 1 : Les Contreforts Dorés
* **Description :** En quittant le Haut-Douar, le chemin de terre laisse place à de gros pavés inégaux. Quelques arbres aux feuilles rousses et jaunes s'accrochent encore à la roche, mais l'herbe devient rare.
* **Particularité :** Dernier refuge des Tifazelts de la plaine. La pente est déjà raide, et le joueur peut encore faire demi-tour facilement. 

### 🚧 Partie 2 : Le Défilé de la Sentinelle
* **Description :** Un canyon étroit traversant les flancs de la colline. La Team Glacitech y a installé son premier barrage : des murs de tôle, des barricades en béton et des caisses d'équipement technique abandonnées. 
* **Particularité :** Les premiers Sbires Glacitech patrouillent ici. De petits projecteurs fixes ou mobiles (lasers de détection) obligent parfois le joueur à synchroniser ses déplacements pour éviter les embuscades ou déclencher un combat s'il est repéré.

### ❄️ Partie 3 : L'Escarpement Givré
* **Description :** Les dernières dizaines de mètres avant le sommet de la Colline Ksar. L'air y est figé par les rejets des immenses générateurs cryogéniques du donjon au-dessus. Les rochers bruns sont couverts de plaques de givre et de stalactites de glace.
* **Particularité :** La faune a totalement changé en raison de cette pollution thermique. Des flaques d'eau gelée peuvent faire glisser le joueur. À la fin de ce chemin, les imposantes portes d'acier du Repaire s'élèvent.

## 🐾 Tifazelts Sauvages (Spawns)
*Zone d'apparition principale : Les petits renfoncements rocheux et corniches des Parties 2 et 3.*

| Tifazelt (Nom temp.) | Type | Niveau | Taux d'apparition | Moment de la journée |
| :--- | :--- | :--- | :--- | :--- |
| *Boucardin des Roches* | [[9. Table des types#Terre|Terre]] | 15 - 17 | 30% | Jour |
| *Rongeur Cuirassé* | [[9. Table des types#Métal|Métal]] | 16 - 18 | 25% | Jour / Nuit |
| *Renard des Neiges (Corrompu)* | [[9. Table des types|Glace]] | 16 - 18 | 20% | Nuit / Tempête |
| *Chauve-souris Féroce* | [[9. Table des types#Vent|Vent]] / [[9. Table des types#Obscurité|Obscurité]] | 15 - 17 | 15% | Nuit |
| *Espèce rare de l'Escarpement* | [[9. Table des types|Glace]] ou [[9. Table des types#Métal|Métal]] | 17 - 19 | 10% | Brouillard / Glace |

*(Note : Tableaux à ajuster une fois la liste des 150 Tifazelts validée)*

## ⚔️ Dresseurs à affronter (PNJ)
Les dresseurs classiques laissent majoritairement la place aux membres de la Team Glacitech. Leurs Tifazelts exploitent le froid et l'acier.

* **Alpiniste Roch :** *"Même avec cette glace étrange, je grimperai !"* (Équipe : 2x Terre Niv. 16)
* **Sbire Glacitech en Patrouille :** *"Halte-là ! Zone restreinte par l'ordre Glacitech !"* (Équipe : 1x Métal Niv. 17, 1x Poison Niv. 16)
* **Sbire Glacitech Vétéran :** *"Tu ne passeras pas le barrage."* (Équipe : 1x Glace Niv. 18)
* **Ingénieur Glacitech (Mini-boss d'étape) :** Garde la porte du sommet. (Équipe : 1x Électrique Niv. 17, 1x Métal/Glace Niv. 19)

## 🎒 Objets et Loot (À ramasser)
* 2x **Anti-Gel** : Dispersés près des barricades (très utiles pour le donjon à venir).
* 1x **[[1. Menus Et Interfaces#Tiflask|Tiflask Cryo]]** : Spéciale pour capturer les Tifazelts de type Glace. Volée dans une caisse logistique ennemie.
* 1x **Rappel** : Posé dangereusement près d'une falaise dans la Partie 1.
* 1x **Corde Fuite (ou équivalent)** : Idéale pour quitter la zone si le joueur se trouve à court de ressources avant le boss.

## ⚙️ Technique & Level Design (Roblox)
* **Transition Atmosphérique Dynamique :** Un script `ColorCorrection` et `Atmosphere` doit être mis en place : au fil de la montée, les couleurs se désaturent (passage du doré au gris/bleu froid), la `Brightness` diminue, et un `Fog` blanc ou magenta léger apparaît.
* **Obstacles & Glissades :** Utilisation du matériau *Ice* de Roblox modifiant la friction (`CustomPhysicalProperties`) sur le dernier tronçon pour rendre la progression chaotique et forcer des itinéraires précis.
* **Bande-son :** Thème de route militaire. Les instruments à vent chaleureux de la Route 5 sont remplacés par des synthétiseurs agressifs, des basses lourdes (808) et des bruits mécaniques réguliers imitant les machines de la Team.

## 🚧 À développer
* Coder les "cônes de vision" dynamiques pour les patrouilles de la Team Glacitech (façon infiltration légère).
* Tester l'ajustement de la friction sur la glace pour s'assurer que l'escalade n'est pas trop punitive ni frustrante.