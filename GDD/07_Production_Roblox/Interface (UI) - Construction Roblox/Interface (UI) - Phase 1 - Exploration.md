---
tags:
  - production
  - roblox
  - ui
---
# 🧭 Phase 1 — exploration (20 oct. 2026)

> [[Interface (UI) - Phase 0 - Fondations|← Phase 0]] · [[Interface (UI) - Construction Roblox|Sommaire de l'interface]] · [[Interface (UI) - Phase 2 - Menu principal et sous-menus|Phase 2 →]] · [[Interface (UI) - Pièges Roblox|Pièges Roblox]]

| Élément | Emplacement | Rôle |
| :--- | :--- | :--- |
| `HUD` | `ReplicatedStorage.UI.HUD` | Objectif en haut à gauche (quête principale), TFD en haut à droite, bouton MENU en bas à droite avec la touche (M au clavier, Y à la manette, cachée en tactile). Tout glisse hors de l'écran pendant un menu ou un dialogue. |
| Bandeau de zone | `HUD` + `ReplicatedStorage.UI.Zones` | À l'entrée d'un lieu : bande biseautée qui traverse l'écran, région en sous-titre, trait cyan qui se dessine. Il faut rester 0,8 s dans le lieu ; un même lieu ne s'annonce pas plus d'une fois toutes les 25 s. 17 petits lieux (cercles) puis 7 régions (rectangles), dans l'ordre de priorité. |
| `Dialogue` | `ReplicatedStorage.UI.Dialogue` | Boîte de dialogue : nom dans une étiquette biseautée, portrait rond, texte qui s'écrit lettre par lettre, compteur 1 / 3, indicateur SUITE qui oscille. E / Entrée / Espace / A / clic pour continuer (un premier appui termine la ligne), Échap / B pour fermer. 3 styles : PNJ (terracotta), dresseur (magenta, choix COMBATTRE / PLUS TARD), découverte (cyan, losange). |
| `Invites` | `ReplicatedStorage.UI.Invites` | Remplace l'affichage par défaut des ProximityPrompt : touche dans un biseau blanc, action sur une barre terracotta, nom de l'objet au-dessus, barre cyan de maintien ; apparition avec rebond ; utilisable au clic et au tactile. |
| Secrets | `UI_Client` | Une découverte ouvre la boîte « DÉCOUVERTE » ; la première fois, une notification « SECRET TROUVÉ — zone : n / total ». |
| Onglets et liste | `Kit.tabs`, `Kit.list` | Onglets biseautés avec repère cyan qui glisse (Q / E ou LB / RB) ; liste défilante de cartes qui entrent l'une après l'autre. Écran de test `Ecrans.Galerie` (aperçu du sac). |

- L'ancienne bulle de dialogue et la carte de secret de `BourgAzur_Client` sont désactivées quand la nouvelle interface tourne (attribut `UI_Azzursal` du joueur) ; les portes animées de ce script continuent de fonctionner.
- Pendant un menu ou un dialogue : personnage bloqué, invites coupées, HUD caché.

## 🧪 Tests faits en jeu (phase 1)
- HUD, bandeau de zone, dialogue d'un dresseur avec choix, dialogue d'un vrai PNJ (la Voyageuse en manteau gris) et aperçu du sac : vérifiés en capture.
- Fermeture du dialogue : personnage et invites rétablis. Changement d'onglet : la liste se reconstruit (2 éléments dans Nourriture). 0 erreur dans la console.
- **Non vérifié en image :** les invites d'action. Elles sont bien créées au bon endroit, mais la capture d'écran de Studio n'affiche aucun BillboardGui (même un carré rouge de test). À regarder en jeu.
- Commandes de test : `dialogue:pnj`, `dialogue:dresseur`, `dialogue:decouverte`, `suite`, `fermer`, `parler` (PNJ le plus proche), `zone:Nom|Région`, `open:Galerie`, `onglet:1`.
