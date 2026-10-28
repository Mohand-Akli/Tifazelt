---
tags:
  - production
  - roblox
  - suivi
---
# Combat d'apprentissage et Zéphir (PROVISOIRE, 26 oct. 2026)

> [[À décider et à faire|Sommaire : à décider et à faire]]

- **Règle du vault gardée** : Zéphir prend le starter qui a l'avantage (`00. Définition`). Un rival « neutre » n'existe pas avec trois starters en triangle.
- **Tifazelt de Zéphir affaibli** (`UI.NouvellePartie.adversaireTutoriel`) : une seule attaque, la plus faible qui fait des dégâts, sans drain ni soin (Aqualune → Brume scintillante, Florépine → Forêt Enchevêtrante, Pyrofennec → Brise Ardente). PV = 3 coups moyens de la meilleure attaque du starter (`N.COUPS_TUTORIEL = 3`, soit 10 à 14 PV). Simulation : 97 à 100 % de victoire en jouant au hasard. Testé en Play avec Aqualune : victoire en 5 tours, 37/93 PV restants, +200 TFD, objectif « Premiers pas — Explorer la Route 1 ».
- **Zéphir visible sur la carte** : `Workspace.Map.Starter_BourgAzur.Zéphir Célestin` (clone de Théo, scripts retirés), dans la rue devant le portail de la maison familiale (2135, 5, 1518), tourné vers le Professeur. Tenue H16 veste zippée azur + B07 survêtement, visage V03, cheveux CoolBoyHair (bleus). Tag `PNJ_Bourg`, `Service = Rival`, « Combattre » : sans starter → « Choisis d'abord ton Tifazelt », starter sans victoire → combat d'apprentissage, après victoire → « On se revoit sur la Route 1 ». Placé à 20 studs du Professeur, parce que deux invites « Parler » en AlwaysShow à moins de 18 studs se déclenchent ensemble (le Professeur prenait la main).
- À valider par Mohand : tenue, cheveux bleus, répliques, emplacement ; Zéphir reste-t-il là après la victoire ?
- **Rééquilibrage du 26 oct. (soir), après la nouvelle formule des stats** : les PV du Tifazelt de Zéphir valent 3 tours moyens du starter joué au hasard (moyenne de ses 4 attaques, soutien = 0), et son attaque est plafonnée pour qu'il lui faille environ 8 coups (`N.COUPS_RIVAL = 8`). Simulation sur 1 000 combats joués au hasard : Pyrofennec 94 %, Aqualune 99,8 %, Florépine 100 %. **Testé en Play avec Pyrofennec** : défaite forcée, puis revanche gagnée en 3 coups d'Incandescence (30/34 PV), objectif « Premiers pas ».
- Non testé en Play : duel Florépine (seulement simulé), revanche lancée depuis Zéphir après une défaite.
