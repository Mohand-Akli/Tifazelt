---
tags:
  - monde
  - lieu
  - sous-marin
  - exploration
  - lumeridia
  - profondeurs-sous-marines
aliases:
  - Profondeurs Sous-Marines
  - Abysses de Saphir
  - Fonds Marins
---
# 🌊 Profondeurs Sous-Marines

* **Type :** Zone secrète subaquatique / Abysse d'exploration
* **Province :** [[00_Province_Lumeridia|Luméridia Est]]
* **Accès & Connexions :** Jetée des Plongeurs de [[Port-Saphir]]
* **Condition d'accès :** Requiert obligatoirement la possession et l'équipement de la [[14. Objets#Bonbonne d'oxygène|Bonbonne d'oxygène]].
* **Écosystème majeur :** Récifs coralliens bioluminescents, canyons sous-marins, épaves marchandes et failles abyssales froides.

## 🌅 Rôle et Présentation
* **Rôle dans l'aventure :** Zone d'exploration avancée (endgame ou mid-game tardif) de Luméridia Est. Accessible uniquement une fois l'équipement de plongée obtenu à Port-Saphir, elle regorge de Tifazelts aquatiques très rares, d'objets d'évolution enfouis et de trésors engloutis.
* **Lore & Ambiance :** Un monde sous-marin majestueux, silencieux et mystérieux. Près de la surface, la lumière du soleil filtre en de puissants rayons dorés. Plus on descend, plus l'obscurité s'installe, brisée uniquement par la bioluminescence des coraux, des anémones et des créatures pélagiques. Des ruines antiques reposent au fond, témoignant de l'histoire pré-cataclysmique d'Azzursal.

## 🗺️ Géographie et Paliers de Plongée
L'exploration de cette zone se fait de manière verticale, la pression et les dangers augmentant avec la profondeur :

* **Le Récif des Murènes (Palier Supérieur / 0 à -20m) :** Forêt de coraux multicolores très lumineuse. C'est une zone grouillante de vie où évoluent de grands bancs de petits Tifazelts d'eau au-dessus de bancs de sable blanc.
* **Le Cimetière des Galions (Palier Intermédiaire / -20 à -50m) :** La lumière commence à faiblir. On y trouve les carcasses d'anciens navires marchands échoués sur les récifs. Les joueurs peuvent s'infiltrer dans les cales béantes pour y trouver des coffres scellés.
* **La Forêt de Varech Géant :** Labyrinthe végétal sous-marin composé d'algues immenses s'étirant vers la surface. La visibilité y est fortement réduite et des courants marins inattendus peuvent faire dériver le joueur.
* **La Fosse Abyssale (Palier Profond / -50 à -100m+) :** Zone de haute pression, d'eau glaciale et sombre. Quelques fumerolles hydrothermales réchauffent des poches isolées. C'est le domaine des créatures les plus redoutables, anciennes et massives.
* **Le Temple Submergé :** Une gigantesque structure architecturale scellée reposant au fond de la faille, liée au mystère des Sanctuaires ou au repaire d'un Tifazelt légendaire des mers.

## 🌿 Écologie & Tifazelts Sauvages
* **Types dominants :** Le type [[10. Table des types|Eau]] est omniprésent, accompagné de créatures de type [[10. Table des types|Poison]] (poissons-lions et créatures coralliennes venimeuses), [[10. Table des types|Électrique]] (raies et anguilles luminescentes) et [[10. Table des types#Obscurité|Obscurité]] dans la Fosse Abyssale.
* **Comportement sauvage :** Les Tifazelts marins se déplacent en trois dimensions. Certains prédateurs s'enfouissent dans le sable ou se camouflent en rochers (mimétisme) pour surprendre les plongeurs.

## 🤿 Mécaniques de Jeu & Plongée (Gameplay)
* **Jauge d'Oxygène :** L'immersion n'est pas illimitée au début. La jauge d'air décroît progressivement. Le joueur doit remonter à la surface, utiliser des consommables ou trouver des "cheminées de bulles d'air" sous-marines pour se recharger.
* **Mouvements 3D :** Le gameplay passe en natation libre à 360°. La flottabilité neutre permet de se maintenir à une certaine profondeur, et des propulseurs peuvent être acquis plus tard pour aller à contre-courant.
* **Courants Marins :** De puissants flux d'eau (visibles par des sillages de bulles rapides) agissent comme des tapis roulants ou des ascenseurs naturels. Certains passages ne peuvent être franchis qu'en empruntant le bon courant.

## ⚙️ Technique & Intégration (Roblox)
* **Physique & Mouvements :**
  * Basculement du personnage en *Swimming State* forcé.
  * Gravité globale de la zone réduite pour donner la sensation de portance de l'eau.
* **Atmosphère visuelle (Lighting & Post-Processing) :**
  * Utilisation massive de `ColorCorrectionEffect` (teinte bleutée forte, contraste ajusté).
  * `DepthOfFieldEffect` pour flouter les objets lointains et simuler la perte de visibilité sous-marine.
  * Particules flottantes (`ParticleEmitter`) représentant du plancton lumineux et des bulles expirées par le joueur.
  * Rayons lumineux volumétriques (God Rays) visibles uniquement dans le Palier Supérieur.
* **Bande-son :** Ambiance étouffée et cotonneuse. Sons de respiration saccadée dans un détendeur, battements de cœur lors de la perte d'oxygène, chants lointains et mélancoliques de grands Tifazelts cétacés.

## 👥 Personnages & Rencontres Subaquatiques
* **L'Archéologue Sous-Marin :** Un chercheur équipé d'un scaphandre lourd étudiant les ruines du Temple Submergé, proposant de déchiffrer des tablettes trouvées au fond.
* **Les Chasseurs de Trésors :** Dresseurs rivaux explorant les cales des galions, prêts à déclencher un combat aquatique pour défendre leur butin.

## 📜 Quêtes liées
* *À compléter (ex: Remonter le journal de bord perdu d'une caravelle, sauver un dresseur imprudent coincé dans la Forêt de Varech sans oxygène, résoudre l'énigme des courants pour déverrouiller l'accès au Temple Submergé...)*

## 🚧 À développer
* Liste exacte et taux d'apparition des Tifazelts par niveau de profondeur.
* Améliorations de la combinaison de plongée (ex: Combinaison pressurisée pour accéder à la fosse abyssale sans subir de dégâts continus).