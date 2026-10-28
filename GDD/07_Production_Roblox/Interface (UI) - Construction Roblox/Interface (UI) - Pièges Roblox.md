---
tags:
  - production
  - roblox
  - ui
---
# ⚠️ Pièges Roblox rencontrés (interface)

> [[Interface (UI) - Construction Roblox|Sommaire de l'interface]]

Relevés pendant la phase 0 (19 oct. 2026), valables pour tous les écrans.

- Un **contour UIStroke sur un cercle** se transforme en carré dans un CanvasGroup mis à l'échelle → les cercles sont faits de deux disques emboîtés.
- **Ne pas faire tourner** un élément arrondi placé dans une zone qui coupe (ClipsDescendants) : ses coins ronds disparaissent.
- Un parallélogramme doit être plus large que sa hauteur × tan(15°) ; pour les bandes hautes et étroites, utiliser un angle de 2–3°.
- Ce jeu n'a pas de `PlayerModule` : le blocage du personnage passe par `ContextActionService` et la vitesse du Humanoid.
- **Aucun émoji** dans l'interface : portraits provisoires = initiale dans un cercle teinté du type.
