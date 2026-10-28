---
tags:
  - production
  - roblox
  - ui
---
# ⚔️ Phase 3 — combat (20 oct. 2026)

> [[Interface (UI) - Phase 2 - Menu principal et sous-menus|← Phase 2]] · [[Interface (UI) - Construction Roblox|Sommaire de l'interface]] · [[Interface (UI) - Phase 4 - Bâtiments et services|Phase 4 →]] · [[Interface (UI) - Pièges Roblox|Pièges Roblox]]

Le combat est un écran comme les menus (`Ecrans.Combat`), mais RETOUR / Échap n'en fait pas sortir : il ferme la fenêtre ouverte ou revient aux actions. Un combat se lance avec `M.combattre({ genre, adverses, dresseur, meteo, terrain })` ; le bouton COMBATTRE des dresseurs (dialogue) le fait déjà.

| Élément | Module | Rôle |
| :--- | :--- | :--- |
| Règles | `ReplicatedStorage.Combat.Regles` | Table des types (vérifiée case par case contre le vault), natures, paliers -6 / +6, critiques, statuts, météo, courbes d'XP, bonheur, et les formules provisoires (voir plus bas). |
| Moteur | `ReplicatedStorage.Combat.Moteur` | Un tour = ordre (priorité, vitesse, Chronologie Intemporelle), précision, dégâts, effets, fin de tour (poison, météo), K.O., remplacement, capture, fuite, XP, évolution. Renvoie une liste d'événements ; l'écran les joue. |
| Espèces de test | `ReplicatedStorage.Combat.Especes` | 7 espèces de la Tifalistre de test, stats de base inventées, attaques prises dans les 283 du vault selon le type. |
| Scène | `UI.CombatUI.Scene` | Arène (déborde au-delà de 16:9), portraits sur socles, cartes de PV, effets d'attaque (élan, projectile, anneau), chiffres de dégâts, flèches de stats, ouverture, Tiflask et capture, évolution. |
| Dresseur (27 oct. 2026) | `UI.CombatUI.Dresseur` | Ouverture d'un combat de dresseur : le personnage du dresseur adverse (PNJ du monde, ou avatar du joueur en ligne) en 3D animé à droite de l'écran, geste de défi (attributs `PoseCombat`, `HumeurCombat`) ; sinon le cercle avec l'initiale. |
| Fenêtres | `UI.CombatUI.Panneaux` | Sac, équipe, surnom, fin de combat, nouvelle attaque, défaite. |

## Ce qui suit le vault
- Table des types, Réalité neutre, natures ±15 %, critique x1,5 et paliers 5 / 10 / 20 / 50 / 100 %, Ensorcelé = pas de critique, Peur = critique adverse +50 %.
- Statuts : Paralysie (vitesse / 2), Brûlure (physique / 2), Gel (magique / 2), Sommeil (pas de soutien), Empoisonnement (1/16 qui augmente de 1/16 chaque tour), Peur (DEF / 2), Ensorcelé (MAG DEF / 2), Étourdi (perd son tour s'il est plus lent).
- Météo : Pluie, Soleil Effervescent, Brouillard (adversaire caché), Tempête de sable, Tempête de neige, Chronologie Intemporelle (ordre inversé).
- Plus d'EM : Défaitisme. Bonheur : +10 au K.O. adverse, -20 au K.O., +5 par niveau, 50 à la capture. Pas de perte de TFD contre un sauvage. 1 chance sur 4 000 d'être brillant.

## ⚠️ Provisoire (à écrire dans le GDD)
- **Dégâts** : ((2 x niveau / 5 + 2) x puissance x A / D) / 50 + 2, puis multiplicateurs, tirage 85-100 %. Pas de bonus de même type.
- **Efficacité** : x2 / x0,5 / x0 (le vault ne chiffre pas).
- **Effet des paliers** : (2 + n) / 2 et 2 / (2 - n) ; précision et esquive (3 + n) / 3.
- **Effets des attaques** : déduits des descriptions par mots-clés (statut, montée / baisse de stats, soin, recul, priorité, critique). Chance de statut 30 % pour une attaque de dégâts. **Il faudrait une colonne « Effet » structurée dans `8. Attaques`.** Les attaques sans effet reconnu affichent « L'effet de cette attaque n'est pas encore programmé ».
- **Capture** : (1 - 2/3 x PV / PV max) x taux de l'espèce x Tiflask (écume x1,5 sur un type Eau) x 1,5 si statut ; 3 secousses.
- **XP** : base de l'espèce x niveau / 7, x1,5 contre un dresseur ; courbes en niveau³ (les totaux au niveau 100 sont ceux du vault).
- **Stats par niveau** : chaque stat grandit comme le niveau.
- **TFD** : victoire contre un dresseur = niveau max x 40 (x2 Gardien / Boss) ; défaite = niveau max de l'équipe x 30.
- **Fuite** : sûre si plus rapide, sinon chance qui augmente à chaque essai.

## Limites connues
- Prototype côté joueur, avec les données de test : le moteur passera côté serveur avec les vraies sauvegardes (anti-triche). Le filtre de modération des surnoms se fera alors côté serveur.
- Pas d'Infirmerie construite : après une défaite, retour au point d'apparition.
- Pas de stockage visible : un Tifazelt capturé avec une équipe pleine va dans `data.stockage`.
- Les dresseurs prennent leur équipe dans l'attribut `Equipe` du PNJ (« Ondine:30|Laineux:31 »), sinon 2 Tifazelts de test autour du niveau 30.

## 🧪 Tests faits en jeu (phase 3)
- 120 puis 150 combats simulés par le moteur seul : aucune boucle infinie, victoires, défaites, fuites, captures, remplacements.
- En Play, avec captures : ouverture sauvage, dresseur et Gardien ; HUD de combat ; choix d'attaque ; sac (médicaments, Tiflask) ; capture réussie + surnom + départ au stockage ; K.O. et remplacement forcé ; victoire contre un dresseur (+1 240 TFD, XP) ; montée de niveau avec nouvelle attaque (Croix De Feu) puis évolution (Pyrofennec en Pyrovulpe, nom de test) ; défaite contre un dresseur (-1 050 TFD, équipe soignée) ; Brouillard. 0 erreur de nos scripts.
- **Non vérifié :** vrais clics et manette (Studio ne simule pas les clics), échec de capture en image, combat lancé depuis un vrai PNJ dresseur (même fonction que le dialogue de test, mais pas cliqué).
- Commandes de test : `combat:sauvage|Ondine|30|Pluie`, `combat:dresseur`, `combat:gardien`, puis `t:choisir|attaquer`, `t:choisir|attaque|1`, `t:choisir|sac`, `t:tiflask|Tiflask simple`, `t:objet|Potion basique|2`, `t:repondre|valeur`, `t:pv|A|1`, `t:ko`.
