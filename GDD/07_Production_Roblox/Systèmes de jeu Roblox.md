---
tags:
  - production
  - roblox
  - systemes
aliases:
  - Scripts Roblox
---
# ⚙️ Systèmes de jeu Roblox (scripts actifs)

> Ce qui tourne vraiment dans le jeu aujourd'hui. Tout le reste (combats, captures, quêtes, objets) n'est **pas encore codé** : les PNJ, dresseurs et objets sont des repères avec des attributs.
> Index : [[00. Production Roblox]].

## 🌊 Courant (nage limitée)
- Script : `StarterPlayerScripts.Route1_Passe5_Client`.
- Dans la zone x −860 à 2900, si les pieds du joueur sont dans l'eau à plus de **12 studs** de la dernière rive, il est ramené sur la rive avec un message.
- S'applique à la Rivière de la Plaine, à l'[[Asif-Safi]] et à la mer autour de [[Bourg-Azur]].
- Coupure pour les tests : `workspace.Route1_CourantActif = false`.

## ✨ Lucioles guides (forêt)
- Script : `StarterPlayerScripts.Foret_Lucioles` (anciennes versions : `Extensions_Sauvegarde.Foret_Lucioles_v1` et `_v2`).
- Réglages : attributs de `Workspace.Map.Extensions.Foret_Guidage` — `Cible` (position de la Bague), `ZoneMin` / `ZoneMax` (zone active), `Actif`, `Reseau` (réseau des sentiers).
- **Réseau des sentiers** : calculé par `Foret2.Reseau()` (463 nœuds). Pour chaque nœud : le nœud suivant vers la Bague et la distance restante par le chemin. À relancer si on retrace les sentiers.
- **Comportement** :
  - un essaim de 6 lucioles flotte à environ 13 studs devant le joueur, le long du sentier ;
  - hors sentier, il vise le sentier le plus proche (couper à travers bois coûte 6 fois plus cher), se tient à 9 studs ;
  - si la direction à suivre est derrière le joueur, il se place au bord de son champ de vision, du côté où tourner ;
  - près de la Bague (moins de 28 studs), il tourne autour d'elle ;
  - après une téléportation, il s'éteint puis réapparaît sans traînée.
- **Apparence** : petit corps sombre, ventre lumineux vert-jaune, halo rond et doux, errance naturelle (bruit de Perlin), clignotement irrégulier ; une seule lumière faible pour tout l'essaim.

## ☀️ Rayons de soleil doux
- Géré par le même script `Foret_Lucioles`, sur les pièces taguées `Foret_RayonsDoux` (clairière de la Bague, `Ring_Event_Clearing.Lumiere`, `PuitsDeLumiere_Lumineuse`).
- Rayons en Beams : pleins à moins de 38 studs de la caméra, éteints au-delà de 65.

## 💍 Bague tournante
- Modèle tagué `Foret_BagueTournante` dans la clairière : il tourne et flotte doucement (côté client).

## 💬 PNJ et bulles de dialogue
- Script : `StarterPlayerScripts.BourgAzur_Client`. Les PNJ de la Route 1 ont le tag `PNJ_Route1` ; les dresseurs ont le tag `Dresseur` avec les attributs `Equipe` et `LigneDeVue` (aucun combat codé).
- Val Palmeraie a ses propres figurines dans `ValPalmeraie_Ambiance`.

## 🔍 Secrets et compteur
- Chaque secret porte l'attribut `ZoneSecret` (`Exploration` ou `Route1`). Le compteur « Secret trouvé (n/total) » est affiché par `BourgAzur_Client` ; total d'exploration dans `workspace.SecretsTotal_Exploration`.
- Liste : [[Secrets d'exploration]].

## 🌬️ Ambiance
- `Route1_Ambiance` : brume locale du bosquet, papillons, vent visible (`GlobalWind`).
- **Moulin** : ailes taguées `Route1_AilesMoulin` (attribut `Axe`), animées côté client quand la caméra est à moins de 450 studs.
- `ValPalmeraie_Ambiance` : noria, palmiers, heure de l'arrosage toutes les 180 s.
