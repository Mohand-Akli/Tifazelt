---
tags:
  - monde
  - route
  - lumeridia
  - route-3
aliases:
  - Route 3
  - Route-3
---
# 🛤️ Route 3

* **Province :** [[00_Province_Lumeridia|Luméridia Est]]
* **Départ (Ouest) :** [[Cité Ocre]]
* **Arrivée (Est) :** [[Presqu'île Marine]]
* **Connexions secondaires :** Berges ouest de l'[[Asif-Safi]]
* **Environnement majeur :** Descente argileuse, zones marécageuses, champs de roseaux et pontons de bois.

## 🌅 Rôle et Ambiance
* **Rôle dans l'aventure :** Troisième route du jeu. Elle marque une transition écologique brutale et fascinante entre la sécheresse de la Cité Ocre et l'abondance aquatique de l'Asif-Safi. C'est ici que le joueur rencontre véritablement la mécanique des milieux humides et d'eau douce, avec de nombreuses flaques de boue ralentissant la progression.
* **Ambiance :** Humide, boueuse et bruyante. Le vent chaud laisse place à une brise fraîche chargée de l'odeur de la vase et des iris d'eau. Le son strident des insectes aquatiques et le coassement des amphibiens dominent le paysage sonore.
* **Taille (version Roblox) :** Route de longueur moyenne mais sinueuse, parsemée d'obstacles naturels liés à l'eau (flaques profondes, petits ruisseaux à enjamber).

## 🗺️ Découpage du Tracé (Les 3 Parties)

### 🪨 Partie 1 : La Descente d'Argile
* **Description :** En quittant la Porte Fluviale de la Cité Ocre, le chemin descend en pente douce. La terre rougeâtre et sèche se gorge progressivement d'eau, devenant meuble et glissante.
* **Particularité :** Peu d'herbes hautes, mais des traces d'éboulements. De petits ruisseaux ruissellent sur le côté du chemin pour aller se jeter plus bas dans le marais.

### 🌾 Partie 2 : Le Marais des Joncs
* **Description :** La zone la plus vaste de la route. Le chemin disparaît presque sous la boue et les flaques d'eau peu profondes. De hautes herbes aquatiques (roseaux et joncs) remplacent l'herbe classique pour cacher les Tifazelts sauvages.
* **Particularité :** Le terrain boueux ralentit légèrement la vitesse de marche du joueur (`WalkSpeed` réduite sur certaines textures Roblox). Il y a plusieurs pontons en bois délabrés qui permettent d'éviter la boue, mais ils obligent à affronter des dresseurs.

### 🌉 Partie 3 : Les Berges du Pont d'Ocre
* **Description :** Le terrain se stabilise à l'approche de l'Asif-Safi. L'eau devient claire et profonde. De gros nénuphars flottent près de la rive. 
* **Particularité :** C'est ici que le joueur trouve ses premiers "spots de pêche" (remous dans l'eau) avant de traverser le grand pont de pierre menant à la [[Presqu'île Marine]].

## 🐾 Tifazelts Sauvages (Spawns)
*Zone d'apparition principale : Les roseaux du marais (Partie 2) et les spots de pêche (Partie 3).*

| Tifazelt (Nom temp.) | Type | Niveau | Taux d'apparition | Moment de la journée |
| :--- | :--- | :--- | :--- | :--- |
| *Crabe de boue* | [[9. Table des types|Eau]] / [[9. Table des types#Terre|Terre]] | 8 - 10 | 35% | Jour / Nuit |
| *Libellule d'eau* | [[9. Table des types|Insecte]] / [[9. Table des types|Eau]] | 8 - 11 | 30% | Jour |
| *Amphibien toxique* | [[9. Table des types|Eau]] / [[9. Table des types|Poison]] | 9 - 11 | 20% | Nuit |
| *Héron pêcheur* | [[9. Table des types#Vent|Vent]] / [[9. Table des types|Eau]] | 10 - 12 | 10% | Matin / Jour |
| *Espèce rare du marais* | [[9. Table des types|Fée]] ou [[9. Table des types|Plante]] | 11 - 12 | 5% | Brouillard / Pluie |

*(Note : Tableaux à ajuster une fois la liste des 150 Tifazelts validée)*

## ⚔️ Dresseurs à affronter (PNJ)
Les dresseurs tirent parti du terrain pour utiliser des Tifazelts infligeant des statuts (Poison, Ralentissement).

* **Pêcheur Simon :** *"La patience est la clé de la pêche... et du combat !"* (Équipe : 2x Tifazelts Eau Niv. 9)
* **Scout des Marais Chloé :** Postée sur un ponton étroit. *"Attention où tu mets les pieds !"* (Équipe : 1x Insecte/Eau Niv. 11)
* **Aventurier Marco :** *"Ma botte est coincée dans la vase, mais mes Tifazelts sont prêts !"* (Équipe : 1x Terre, 1x Poison Niv. 10)

## 🎒 Objets et Loot (À ramasser)
* 2x **Antidote** : Essentiel pour contrer les Tifazelts venimeux du marais.
* 1x **[[1. Menus Et Interfaces#Tiflask|Tiflask Écume]]** (Tiflask spécial pour les créatures de type Eau) : Cachée au bout d'un vieux ponton brisé.
* 1x **Bottes de Pêcheur (Objet de vente/Quête)** : Cachées dans une souche creuse.

## ⚙️ Technique & Level Design (Roblox)
* **Terrain Boueux :** Utilisation du matériau *Mud* de Roblox. Un script local peut détecter lorsque le joueur marche sur ce matériau pour réduire temporairement sa `Humanoid.WalkSpeed` de 16 à 12, rendant l'évitement des hautes herbes plus difficile.
* **Atmosphère (Lighting) :** Lumière plus diffuse. Un léger brouillard (`Fog` verdâtre) flotte au ras de l'eau tôt le matin et tard le soir.
* **Bande-son :** Piste musicale rythmée par des instruments à vent boisés (hautbois, flûte de pan) et des pizzicatos de cordes rappelant les sauts de grenouilles, le tout mixé avec un fond sonore de grillons et de clapotis.

## 🚧 À développer
* Mettre en place le script de ralentissement lié au matériau de la boue.
* Configurer le système de pêche basique sur les "remous" de la Partie 3 de la route.