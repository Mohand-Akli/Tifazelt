---
tags:
  - production
  - roblox
  - bourg-azur
---
# 🏘️ Bourg-Azur — corrections dans la ville et extensions du 19 oct.

> [[Bourg-Azur - Portes et intérieurs|← Portes et intérieurs]] · [[Bourg-Azur - Construction et Direction Artistique|Sommaire de la construction de Bourg-Azur]] · [[Bourg-Azur - Fontaine, paysage et mobilier|Fontaine, paysage et mobilier →]]

## 🏘️ 4. Corrections dans la ville

| Problème | Correction |
|---|---|
| Plante qui gênait l'entrée de la maison | supprimée |
| Murs et plafonds qui semblaient éclairés de l'intérieur | plafonniers intérieurs supprimés, blanc pur adouci |
| Spawn devant la maison | spawn dans la chambre du joueur, posé au sol, sans meuble autour |
| Balcons enfoncés dans les façades (84) | réalignés sous leur porte-fenêtre et décollés du mur de 0,12 stud ; 83 appuis de fenêtre qui se superposaient retirés |
| Fleurs de façade collées au mur et qui scintillaient (144) | décollées du mur avec un léger décalage aléatoire contre le scintillement, sans collision |
| Enseigne du Café des Embruns | refaite (fond turquoise, cadre en bois, texte face à la rue, tasse de café à côté) |
| Enseigne du Fleuriste cachée par le balcon | redescendue au-dessus de l'auvent, dégagée du balcon ; même correction pour l'Épicerie, la Librairie et le Tisserand |
| Chaises et parasols du café qui flottaient | 12 objets reposés au sol, objet par objet |
| Phare hors sujet, trop petit et trop loin | retiré ; le bout du ponton devient un **ponton de pêche** (banc face à la mer, casiers, bitte d'amarrage) |
| Sortie vers la Route 1 asymétrique | portique réaligné sur l'axe du sentier de la Route 1, massifs symétriques, dallage de transition avec bord en pente douce ; passage testé dans les deux sens |
| Anneau de terre géométrique autour de la ville, qui ne menait nulle part | repeint en herbe (les vraies routes ne sont pas touchées) |
| Pas d'accès au champ ni à l'oliveraie | deux chemins de terre au tracé courbe, bordés de pierres et de touffes d'herbe, avec un panneau au départ ; deux murets de l'oliveraie ouverts |
| Lampadaires trop petits | **+35 %** de hauteur, base recalée au sol, style conservé |

---

## 🧭 13. Mission du 19 oct. 2026 (place, moulin, littoral)
> Modules `ServerStorage.MapGeneration.Extensions.Bourg`, `.Littoral` et `.Campagne`. Sorties : `Workspace.Map.Extensions.Bourg_*`, `Littoral_*`, `Campagne_*`. Sauvegardes : `Extensions_Sauvegarde.{Bourg, Littoral}`.

- **Place centrale** : pavés usés, herbe entre les dalles, dalles abîmées ; 6 étals à auvents rayés, 4 réverbères en fer forgé, 4 bancs, pots et détails du quotidien.
- **Nord agricole** : grand moulin en bois sur le Petit Mamelon (ailes animées), 6 champs, clôtures en zigzag, épouvantail, charrette à roue cassée, outils, chemins ; 76 arbres isolés retirés, 479 éléments ajoutés au pied des groupes.
- **Débarcadère** (2658, 1948) : ponton élargi de 9 à 14 studs, plancher usé, bittes, caisses, tonneaux, cordages, filet, barque amarrée, cabane de pêcheur.
- **Laisse de mer** sur la côte du Bourg, la Plage de l'Estuaire et la Crique des Oliviers : bois flotté, algues, coquillages, rochers enfouis, sable humide.
- **Crique secrète** sous les falaises (x 978–1088, z 2740–2765) : plage, descente cachée de 7 marches rocheuses, vieux feu, coffre à demi enfoui (secret), restes d'épave.
- **Berges du fleuve** : 8 anses, boue et sable, 223 roseaux, 48 nénuphars.
- **Campagne** : Mas des Moissons (596, 2332) habillé, versants des collines, ornières et flaques sur la Route 1, 5 panneaux rustiques, 7 micro-points d'intérêt.
- **Presqu'île** : arbre mort monumental avec un creux (secret), enceinte en ruine, socle ancien, pierres gravées.
- Tests en jeu : aller-retour de la crique, bout du ponton, ailes du moulin qui tournent.
- Liste des secrets : [[Secrets d'exploration]]. Journal : [[Journal de construction de la carte]].
