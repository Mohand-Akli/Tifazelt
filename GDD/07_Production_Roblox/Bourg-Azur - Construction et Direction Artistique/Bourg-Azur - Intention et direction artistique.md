---
tags:
  - production
  - roblox
  - bourg-azur
  - direction-artistique
---
# 🎨 Bourg-Azur — intention et direction artistique

> [[Bourg-Azur - Construction et Direction Artistique|Sommaire de la construction de Bourg-Azur]] · [[Bourg-Azur - Portes et intérieurs|Portes et intérieurs →]]

## 🧭 1. Intention générale

Bourg-Azur est le **village natal** du joueur : c'est le premier lieu qu'il voit et celui où il revient. La passe 2 avait trois objectifs :

1. **Rendre le village habitable** : des intérieurs dans lesquels on entre vraiment, des bancs où l'on s'assoit, des habitants à qui l'on parle.
2. **Rendre le village crédible** : corriger ce qui trahissait la construction (balcons enfoncés, murs qui brillaient de l'intérieur, objets qui flottaient, enseignes cachées, chemins qui ne menaient nulle part).
3. **Rendre le village agréable à parcourir** : remplir les espaces verts sans encombrer les rues, ajouter de petites surprises pour les joueurs curieux.

**Ambiance visée :** un bourg côtier méditerranéen (Algérie, Grèce, sud de l'Italie) en *low poly* stylisé. Chaux blanche adoucie, volets bleu azur, bougainvillées magenta, terracotta, oliviers et palmiers. La lumière est chaude et lisible, sans éblouir.

---

## 🎨 2. Direction artistique

### 2.1 Principes
- **Formes simples, aplats de couleur.** Aucune texture réaliste ajoutée. Seuls les matériaux Roblox de base sont utilisés pour donner du grain : bois, planches, tissu, ardoise, herbe, verre et métal.
- **Lisibilité avant détail.** Les rues principales, la place et les entrées restent dégagées. Le détail se concentre près des façades, des commerces et des points d'intérêt. Les espaces verts gardent de l'air.
- **Pas de néon éblouissant.** Les lanternes des lampadaires sont passées du néon blanc à un verre chaud mat. La seule lueur volontaire est celle des portes magiques, limitée et progressive.
- **Pas de blanc pur.** Le blanc de chaux éblouissait sous le soleil de Luméridia. Les 459 surfaces blanc pur sont devenues un blanc cassé chaud.
- **Variété sans chaos.** Tailles, orientations et groupements varient, mais chaque groupe suit la même palette.

### 2.2 Palette de la ville

| Usage | Couleur (RVB) | Remarque |
|---|---|---|
| Chaux des façades (blanc adouci) | 240, 235, 224 | remplace le blanc pur (255) |
| Bleu azur des volets et des portes | 36, 74, 140 / 60, 110, 170 | identité de Bourg-Azur |
| Turquoise du Café des Embruns | 36, 140, 150 | enseigne, porte, comptoir |
| Vert du Fleuriste | 70, 130, 80 | enseigne, porte |
| Terracotta (pots, toits, jardinières) | 186–190, 104–106, 74–76 | proche du Terracotta de la charte (#C18358) |
| Pierre claire de la fontaine | 226, 214, 190 / 240, 232, 214 | margelle et vasques |
| Eau | 70, 170, 198 | verre semi-transparent |
| Feuillages | 66–104, 124–160, 66–84 | quatre verts mélangés |
| Fleurs | rose 240,90,120 · jaune 250,210,80 · lilas 160,110,220 · blanc 250,250,240 · orange 240,130,60 | massifs et prairies |
| Bois (bancs, mobilier) | 150, 108, 74 / 110, 78, 56 | deux tons, clair et foncé |
| Lueur des portes | 255, 190, 120 (dehors) / 214, 236, 255 (dedans) | chaude en entrant, « lumière du jour » en sortant |

### 2.3 Lumière
- **Extérieur :** les réglages globaux de Luméridia sont conservés (étalonnage de la Route 1, Atmosphere, Bloom léger). Les **52 lampadaires** ont une lumière plus douce (luminosité 0,8, portée 24, sans ombres).
- **Murs « éclairés de l'intérieur » :** les plafonniers des anciens intérieurs (luminosité 1,6, portée 22) traversaient les murs. Leur suppression a réglé le problème.
- **Intérieurs :** au plus 2 à 3 points lumineux chauds par pièce (luminosité 0,3, portée 24 ; 0,36 et 28 dans la Guilde), sans ombres. Le reste vient de la lumière ambiante. Les fenêtres intérieures sont des vitres « jour diffus » qui n'émettent aucune lumière.
- **Ambiance intérieure (20 oct.) :** dès que le joueur est dans un intérieur, le script client `Interieurs_Ambiance` coupe la brume extérieure (Atmosphere), retire les rayons du soleil, renforce un peu la lumière ambiante et ajoute un léger étalonnage chaud. Tout revient en 0,35 s quand il sort.
- **Enveloppes :** chaque intérieur est entouré de blocs épais, invisibles pour le joueur. Sans eux, la lumière turquoise du ciel traversait les murs et plafonds de 1 stud (l'éclairage de Roblox travaille par cases de 4 studs) et donnait une teinte verte aux pièces.
