---
tags:
  - production
  - roblox
  - ui
---
# 🎣 Phase 7 — mini-jeux et énigmes (20 oct. 2026)

> [[Interface (UI) - Phase 6 - En ligne|← Phase 6]] · [[Interface (UI) - Construction Roblox|Sommaire de l'interface]] · [[Interface (UI) - Pièges Roblox|Pièges Roblox]]

*Mise à jour (relecture, 28 oct. 2026) : les Tifazelts de test cités ici (Ondine) ont été retirés du jeu le 27 oct. 2026 et remplacés par les 20 Tifazelts nommés par Mohand : voir [[À décider - Dresseurs, vélos et remplaçants (27 oct. 2026)]]. Les tests datés ci-dessous restent tels qu'ils ont été faits.*

| Écran | Module | Contenu |
| :--- | :--- | :--- |
| 7.1 Pêche | `Ecrans.Peche` | Invite « Pêcher » au bout du ponton de Bourg-Azur (sur la plateforme, rien d'ajouté dans l'eau). Il faut une canne à pêche dans les objets clés. LANCER, attendre que ça morde, FERRER à temps (trop tôt ou trop tard = raté), puis MOULINER : maintenir pour tirer, relâcher pour détendre, garder le curseur dans la zone verte pendant que le Tifazelt tire par à-coups. Ligne cassée si la tension est au maximum, fuite si la ligne reste molle. Prise = combat contre un Tifazelt de type Eau (nouveau décor de combat « eau »). Le décor du jeu reste visible derrière l'interface. Espace, clic, bouton A ou gâchette droite. |
| 7.2 Plongée | `UI.Plongee` (sur le HUD) | Jauge AIR dès que la tête est sous l'eau : temps restant, profondeur en mètres. Le Tuba de plongée donne plus de souffle ; la Bonbonne d'oxygène prend le relais (5 minutes, elle ne se recharge pas à la surface). La jauge passe au magenta sous 25 %. Sans air : remontée à la surface. Sous l'eau : teinte bleutée et flou au loin. |
| 7.3 Énigmes | `Ecrans.Enigme` + `UI.Enigmes` | Écran commun, interface selon l'énigme. « Symboles » : quatre creux à remplir dans l'ordre que donne l'indice (stèle du Sanctuaire de Pierre, Route 1). « Dalles » : rejouer l'ordre des lueurs, trois manches de 4, 5 puis 6 (pierre du cercle, Crique secrète). Récompense une seule fois. |

Autres changements :
- Maman donne le Tuba de plongée au début d'une nouvelle partie (vault : 14. Objets).
- Les énigmes « Chasseur de trésors » ne sont visibles que pour cette classe : attribut `ChasseurSeulement` sur l'invite.
- Invites ajoutées (attribut `Service`) : Plateforme du ponton (Peche), Stèle de la Route 1 (Enigme = stele_route1), Pierre du cercle de la Crique secrète (Enigme = pierre_crique).

## Ce qui suit le vault
- La canne permet d'affronter des Tifazelts de type Eau ; les spots de pêche (remous) et la canne améliorable sont décrits dans Asif-Safi et 14. Objets.
- Bonbonne : 5 minutes, rechargée par un PNJ de Florédena. Tuba : respirer plus longtemps. Jauge d'oxygène, ColorCorrection et DepthOfField sous l'eau (Profondeurs Sous-Marines).
- Énigmes cachées dans le monde, avec des puzzles réservés au Chasseur de trésors (3. Mécanique).

## ⚠️ Provisoire / à trancher dans le GDD
- **Pêche** :
  - réglages : zone verte, vitesse de prise, attente de 1,6 à 4,2 s, 1 s pour ferrer, « Canne pro » prévue ;
  - prises : seulement Ondine (seule espèce Eau de test) ;
  - niveau du Tifazelt pêché : autour de la moyenne de l'équipe ;
  - pas encore de remous visibles dans l'eau, pas d'appâts.
- **Plongée** :
  - souffle : 15 s sans équipement, +25 s avec le Tuba, regagné à 6 s par seconde à la surface ;
  - remontée automatique quand l'air manque ;
  - recharge de la Bonbonne : pas encore de PNJ, et le prix est `???` dans le vault.
- **Mer de Bourg-Azur** : le script existant `Route1_Passe5_Client` (le « courant ») ramène le joueur s'il nage à plus de 12 studs de la rive. On ne peut donc pas encore plonger au large de Bourg-Azur. C'est voulu pour la Route 1 ; il faudra une exception quand la Tenue de plongée existera (vault : elle permet de nager dans la mer).
- **Énigmes** : textes, solutions, emplacements et récompenses inventés pour l'exemple (1 500 TFD + 2 Super potions ; 2 500 TFD + 3 Tiflask d'écume + 1 Réveil).

## 🧪 Tests faits en jeu (phase 7)
- **Pêche** : ouverture au ponton, lancer, « Ça mord ! », ferrer, mouliner (pilote automatique), prise, combat contre une Ondine niveau 31 sur le décor « eau », fuite.
- **Plongée** :
  - jauge AIR visible sous l'eau, avec teinte bleue et flou ;
  - temps et profondeur qui bougent ;
  - la Bonbonne (orange) prend le relais quand le souffle est vide ;
  - test fait au large (x = 3 050), courant désactivé le temps du test.
- **Énigmes** :
  - stèle : mauvais ordre refusé (la pierre reste immobile), bon ordre accepté, +1 500 TFD ;
  - dalles : trois manches réussies, récompense.
- 0 erreur de nos scripts.
- **Non vérifié** :
  - la vraie prise en main de la pêche (maintenir et relâcher à la main) et son équilibre ;
  - la descente à la nage (le personnage flotte : il faut nager vers le bas) ;
  - la remontée automatique quand l'air manque (la Bonbonne de test durait 5 minutes) ;
  - l'invite cachée pour une autre classe que Chasseur de trésors ;
  - les vrais clics et la manette.
- **Commandes de test** :
  - pêche : `service:Peche`, `t:lancer`, `t:ferrer`, `t:auto`, `t:combattre` ;
  - plongée : `objet:Bonbonne d'oxygène`, `plonger:16` ;
  - énigmes : `enigme:stele_route1`, `t:poser|cercle`, `t:valider`, `enigme:pierre_crique`, `t:resoudre`.

Captures de cette phase : [[Captures 2026-10-20#Interface — phase 7 (mini-jeux et énigmes)]].
