---
tags:
  - production
  - roblox
  - suivi
---
# Dresseurs, vélos et remplaçants des Tifazelts de test (27 oct. 2026) — PROVISOIRE

> [[À décider et à faire|Sommaire : à décider et à faire]]

- **Remplaçants des Tifazelts de test (27 oct. 2026, PROVISOIRE)** : Gardiens du Sanctuaire avec des Tifazelts de la liste au plus proche de leur type (aucun Tifazelt Insecte ni Glace nommé : Anto Solid et Icarius Crystalheart ont des équipes d'attente) ; pêche = Dauphimyst (seul Tifazelt Eau nommé) ; dresseurs de la Route 1 : attribut `EquipeJeu` (Gamin Léo Lycombre niv. 3, Gamine Inès Vipéclair niv. 2, Bastien Fennedune niv. 2, Sara Pierraiglon niv. 3, Scout Théo Spectrocarte niv. 4), le vault ne donnant que « Rongeur de base », « Insecte », « Oiseau de base » ; joueur test en ligne et œufs de test du Pâturage avec des Tifazelts de la liste. Répliques d'Aurèle et Karim et secret de la Sonnaille : « Tifazelts laineux » au lieu de « Laineux ».
- **Ouverture des combats de dresseur (27 oct. 2026, PROVISOIRE)** : le dresseur adverse apparaît en 3D, animé, à droite (`UI.CombatUI.Dresseur`). À valider par Mohand : cadrage et lumière, durée (l'ouverture reste 0,8 s de plus quand un dresseur est affiché), gestes (Zéphir bras croisés et visage fâché dessiné par Claude ; enfants et dresseurs : poing levé puis poing tendu ; Sara : mains sur les hanches ; réglables par les attributs `PoseCombat` et `HumeurCombat` du PNJ). Les Gardiens n'ont pas encore de personnage dans le monde : cercle avec l'initiale. En ligne : avatar de l'autre joueur (non testé, il faut deux joueurs).
- **Vélo (27 oct. 2026, PROVISOIRE)** : nouveau modèle en pièces (`Joueur.Velos`, vélo de ville « Azur ») et animation de sortie du sac. À valider par Mohand : allure, couleurs, taille du panier, animation (0,35 s pour sortir, 0,25 s pour ranger). Le vault ne dit rien des vélos (sortes, prix, magasin, obtention) : tout est PROVISOIRE.
- **Vélos et magasin de vélos (27 oct. 2026, PROVISOIRE)** : cinq vélos (Azur offert par Maman, Corail 3 500 TFD, VTT Sentier 7 500 TFD, course Éclair 12 000 TFD, Étoile 20 000 TFD ; vitesses 38 à 46) et un magasin « Vélos de l'Azur » au sud de la place de l'entrée de Bourg-Azur, avec un vendeur inventé (« Gilles, marchand de vélos », tenue H18 + B12, visage V01). À décider par Mohand : sortes de vélos, noms, prix, vitesses, avantage du VTT hors des chemins (aucun pour l'instant), emplacement et nom du magasin, nom du vendeur. Comme le reste du sac, les vélos achetés ne sont pas sauvegardés (pas de données joueur) et le serveur accepte le vélo demandé par le client.
- **Vérifications en attente de Mohand (27 oct. 2026)** : liste dans [[Vérifications de Mohand - 27 oct. 2026]]. Textes « revanche » avant le premier combat corrigés le 27 oct. 2026 (drapeau `partie.perdu`, non testé en Play) ; palmier à environ 7 studs du coin de la terrasse du magasin (à déplacer ou à garder ?).
