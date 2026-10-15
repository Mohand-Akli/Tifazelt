---
tags:
  - monde
  - lieu
  - cours-d-eau
  - fleuve
  - lumeridia
  - asif-safi
aliases:
  - Asif-Safi
  - L'Asif-Safi
  - Asif Safi
  - Fleuve Asif-Safi
---
# 🌊 L'Asif-Safi

* **Type :** Fleuve majeur / Artère fluviale régionale
* **Province :** [[00_Province_Lumeridia|Luméridia Est]]
* **Connexions & Abords :** [[Route 3]] (Rive Ouest), [[Presqu'île Marine]] (Enclave insulaire centrale), [[Route 4]] (Rive Est), Embouchure vers [[Port-Saphir]]
* **Écosystème majeur :** Milieu aquatique d'eau douce, méandres alluviaux, ripisylve dense et zones marécageuses

## 🌅 Rôle et Présentation
* **Rôle dans l'aventure :** Élément hydrographique central et frontière naturelle de Luméridia Est. L'Asif-Safi délimite la transition entre l'aridité de la Cité Ocre et le littoral de Port-Saphir. C'est le premier grand biome aquatique d'eau douce que le joueur longe, franchit et explore.
* **Étymologie & Lore :** Son nom associe la racine berbère (*Asif*, signifiant « fleuve / rivière ») et arabe (*Safi*, signifiant « pur / limpide »). Vénéré depuis des générations, il est considéré comme le cœur battant de la province, irriguant les terres cultivables et apportant une fraîcheur salvatrice face aux vents chauds du sud.
* **Ambiance :** Un cours d'eau majestueux et puissant aux reflets bleu indigo profond. Les rives sont bordées de hautes roselières, de saules pleureurs et de bouquets de joncs. Le murmure continu des courants, le clapotis de l'eau contre les pontons et le vol rasant des Tifazelts aquatiques insufflent une atmosphère vivifiante et sauvage.

## 🗺️ Géographie et Tracé du Fleuve
* **La Source des Contreforts (Amont) :** L'Asif-Safi prend sa source dans les hauteurs rocheuses intérieures, alimenté par la fonte des neiges et de puissantes résurgences karstiques.
* **Le Méandre d'Ocre (Abords Route 3) :** Le cours ralentit et s'élargit en arrivant près des terres argileuses. Ses berges sablonneuses et marécageuses constituent des frayères naturelles pour les jeunes créatures d'eau.
* **La Boucle de la Presqu'île (Le Cœur d'Eau) :** Le fleuve se sépare en deux bras puissants pour encercler intégralement le relief accueillant la [[Presqu'île Marine]], reliée aux rives extérieures par le Pont d'Ocre et le Pont Saphir.
* **Le Chenal des Moulins (Abords Route 4) :** En aval de la boucle, le courant s'accélère le long de berges consolidées par de petits ouvrages hydrauliques solarpunk (roues à aubes silencieuses, digues filtrantes).
* **L'Estuaire de Saphir :** L'embouchure terminale où les eaux douces de l'Asif-Safi se mêlent à l'eau de mer dans la baie de [[Port-Saphir]], créant une zone saumâtre foisonnante d'espèces rares.

## 🌿 Écologie & Faune Associée
* **Flore ripisylve :** Roseaux géants, joncs d'eau, iris sauvages indigo, nénuphars épais et mousses aquatiques filtrantes.
* **Types de Tifazelts dominants :** Prédominance absolue du type [[9. Table des types|Eau]], côtoyant des créatures secondaires des types [[9. Table des types|Plante]], [[9. Table des types|Insecte]] et [[9. Table des types|Vol]].
* **Micro-climat fluvial :** L'évaporation constante maintient une ceinture de fraîcheur et d'humidité permanente le long de son lit, offrant un refuge thermique aux créatures sensibles à la chaleur environnante.

## 🎣 Activités, Mécaniques & Pêche
* **Pêche à la ligne :** Multiples spots identifiables par des remous à la surface de l'eau, permettant d'attraper des Tifazelts aquatiques exclusifs selon la canne et l'appât équipés.
* **Navigation & Franchissement :** Outre les deux ponts principaux, des plates et des barques à rames permettent de naviguer le long de certains méandres calmes (accès préalable au surf ou à une monture aquatique requis pour naviguer en plein courant).
* **Trésors des Profondeurs :** Les berges recèlent de galets polis, de coquillages d'eau douce, de perles et de parchemins scellés perdus par d'anciennes caravanes fluviales.

## ⚙️ Technique & Intégration (Roblox)
* **Configuration Terrain Water :**
  * *WaterColor :* Teinte bleu indigo soutenue (`Color3.fromRGB(30, 60, 140)`).
  * *WaterTransparency :* 0.65 à 0.70 pour garder une visibilité nette sur les fonds rocheux et les créatures aquatiques visibles sous la surface.
  * *WaveSize & WaveSpeed :* Ondulations calmes dans la boucle insulaire, plus vives et écumantes près des seuils rocheux et de l'estuaire.
* **Physique des Courants :** Utilisation de volumes de force invisibles (`VectorForce` ou `LinearVelocity`) entraînant doucement les éléments flottants et les nageurs dans le sens du courant.
* **Bande-son :** Nappe continue de clapotis et d'écoulement d'eau vive, mêlée aux coassements d'amphibiens au coucher du soleil et au bruissement du vent dans les roseaux.

## 👥 Personnages & Rencontres des Rives
* **Les Pêcheurs de l'Asif :** Dresseurs sédentaires postés sur les berges, défiant les voyageurs avec des équipes adaptées aux techniques aquatiques.
* **L'Hydrologue de terrain :** Scientifique indépendant surveillant la qualité de l'eau et notant l'impact du débit fluvial sur la faune sauvage.
* **Les Bateliers de passage :** PNJ proposant des traversées d'une rive à l'autre contre quelques [[2. Economie Et Formules Et Reste#💵 Tifadinar (TFD)|TFD]].

## 📜 Quêtes liées
* *À compléter (ex: Nettoyer des débris coincés dans les roseaux d'un méandre, repérer un banc migrateur de Tifazelts rares remontant le courant vers l'amont...)*

## 🚧 À développer
* Grille de capture complète : probabilités d'apparition des Tifazelts sauvages par pêche (Canne Simple, Canne Pro) et par navigation à la surface.
* Événements hydrologiques dynamiques (montée des eaux ouvrant des passages vers des grottes immergées).