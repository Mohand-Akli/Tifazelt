---
tags:
  - monde
  - lieu
  - grotte
  - donjon
  - lumeridia
  - grotte-inconnue
aliases:
  - Grotte Inconnue
  - La Grotte Inconnue
  - Grotte ???
  - Caverne Mystérieuse
---
# 🕳️ La Grotte Inconnue

* **Type :** Réseau souterrain naturel / Donjon d'exploration
* **Province :** [[00_Province_Lumeridia|Luméridia Est]]
* **Connexions :** Entrée principale aux contreforts rocheux (proche de la [[Route 2]] et [[Route 3]]), galeries secondaires descendant vers des failles inexplorées
* **Écosystème majeur :** Milieu cavernicole obscur, cavités karstiques, gisements cristallins et lacs souterrains stagnants

## 🌅 Rôle et Présentation
* **Rôle dans l'aventure :** Première grande zone souterraine facultative ou semi-obligatoire de Luméridia Est. C'est un lieu propice au « grinding » (entraînement), à la découverte d'espèces cavernicoles rares et à la recherche d'objets d'évolution ou de fossiles minéraux.
* **Histoire & Lore :** Mentionnée uniquement sous le nom de « Grotte ??? » sur les vieux parchemins de voyage, cette cavité naturelle est réputée instable et chargée d'une énergie minérale résiduelle. Les anciens mineurs d'Azzursal l'évitaient en raison de résonances étranges émises par ses parois cristallines, qui réagissent curieusement à la présence des [[13. Objets#Bague (Nom à définir)|Bagues des Sanctuaires]].
* **Ambiance :** Obscure, fraîche et mystique. L'écho des gouttes d'eau tombant des stalactites brise un silence lourd. Seuls les reflets turquoise et ambrés de grappes de cristaux phosphorescents percent les ténèbres, tandis que des yeux sauvages luisent au fond des anfractuosités.

## 🗺️ Géographie et Niveaux d'Exploration
Le réseau est structuré en plusieurs salles interconnectées, demandant de l'éclairage ou des capacités de terrain pour progresser :

* **L'Entrée des Stalactites (Niveau 0) :** Vestibule éclairé par la lumière du jour filtrant depuis l'extérieur. Le sol est jonché de débris rocheux et de gravats.
* **Le Labyrinthe des Piliers (Niveau -1) :** Vaste salle encombrée de colonnes naturelles de calcaire. Sans source lumineuse (torche ou Tifazelt doté de capacités lumineuses), le champ de vision du joueur y est drastiquement réduit.
* **La Faille des Cristaux Résonants :** Une crevasse spectaculaire traversée par un pont naturel de roche. D'immenses géodes cristallines scintillent le long des parois et réagissent aux sons des combats.
* **Le Lac Englouti (Point Bas) :** Nappe d'eau souterraine d'un noir d'encre où vivent des Tifazelts aveugles ou bioluminescents. Des corniches permettent d'en faire le tour pour atteindre un cul-de-sac abritant un trésor scellé.
* **L'Éboulis Scellé :** Un passage effondré bloqué par de lourds rochers massifs, nécessitant une capacité ou un outil spécial pour être dégagé plus tard dans l'aventure.

## 🌿 Écologie & Tifazelts Sauvages
* **Faune des parois et plafonds :** Forte densité de Tifazelts des types [[9. Table des types|Roche]], [[9. Table des types|Sol]] et [[9. Table des types|Insecte]], ainsi que des créatures chiroptères (chauves-souris) de type [[9. Table des types|Vol]] / [[9. Table des types|Ténèbres]].
* **Profondeurs et failles :** Apparition occasionnelle de créatures semi-spectrales ou minérales attirées par les cristaux d'énergie.
* **Comportement sauvage :** Les créatures y sont plus territoriales : certaines tombent directement des stalactites au passage du joueur si celui-ci fait trop de bruit en courant.

## 💡 Mécaniques, Puzzles & Exploration
* **Gestion de l'obscurité :** Mécanique de visibilité restreinte. Le joueur doit s'équiper d'une torche, d'une lanterne de mineur ou faire appel à un Tifazelt apprenant une capacité produisant de la lumière pour élargir son rayon de vision.
* **Puzzles de blocs rocheux :** Présence de rochers cubiques à pousser sur des dalles de pression naturelles pour abaisser des ponts de pierre.
* **Filons d'extraction :** Dépôts minéraux scintillants que le joueur peut miner ou fouiller pour obtenir des fragments d'évolution, des pépites à revendre en [[2. Economie Et Formules Et Reste#💵 Tifadinar (TFD)|TFD]] ou des pierres brutes artisanales pour la Cité Ocre.

## ⚙️ Technique & Navigation (Roblox)
* **Configuration d'éclairage (Lighting) :**
  * *Atmosphere / OutdoorLight :* Désactivées ou occultées à l'intérieur.
  * *Ambient :* Teinte bleu nuit très sombre (`Color3.fromRGB(10, 15, 25)`).
  * *PointLight / SurfaceLight :* Lumières d'ambiance douces émanant des cristaux néon (*Neon Material* turquoise et doré).
* **Audio & Réverbération :**
  * Activation d'un effet `ReverbSoundEffect` (preset *Cave* ou *Dungeon*) pour amplifier l'écho des bruits de pas et des cris d'attaques.
  * Nappe sonore feutrée de ruissellements d'eau et de souffles d'air souterrains.

## 👥 Personnages & Rencontres des Profondeurs
* **Le Spéléologue Égaré :** Chercheur imprudent à sec de torches qui offre un objet utile au joueur en échange d'indications pour retrouver la sortie.
* **Le Prospecteur de Gemmes :** Mineur itinérant échangeant des minerais rares contre des consommables.
* **Dresseurs Aventuriers :** Jeunes explorateurs venus tester leur courage dans le noir.

## 📜 Quêtes liées
* *À compléter (ex: Secourir l'apprenti mineur coincé derrière un éboulis, prélever un éclat de cristal résonant pour le Laboratoire Arid de Val Palmeraie, capturer un spécimen rare du Lac Englouti...)*

## 🚧 À développer
* Liste et pourcentages d'apparition des Tifazelts sauvages par niveau de profondeur.
* Définition précise de la capacité ou de l'objet requis pour briser l'Éboulis Scellé ouvrant un futur raccourci vers une autre province.