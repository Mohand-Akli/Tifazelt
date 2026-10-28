---
tags:
  - production
  - roblox
  - ui
---
# 🏘️ Phase 4 — bâtiments et services (20 oct. 2026)

> [[Interface (UI) - Phase 3 - Combat|← Phase 3]] · [[Interface (UI) - Construction Roblox|Sommaire de l'interface]] · [[Interface (UI) - Phase 5 - Début de partie|Phase 5 →]] · [[Interface (UI) - Pièges Roblox|Pièges Roblox]]

On entre dans un service en parlant au PNJ du bâtiment : son dialogue propose le service (attribut `Service` du PNJ, et `Service2` pour un second choix). Le Pâturage s'ouvre avec l'invite « Gérer » posée sur un poteau du portail (pas de nouvelle pièce, pas de collision ajoutée).

| Service | Écran | Où, à Bourg-Azur | Contenu |
| :--- | :--- | :--- | :--- |
| Infirmerie | `Ecrans.Infirmerie` | Infirmière Tifazelt | 6 capsules ; SOIGNER rend PV, statuts et EM. Classe Infirmier : atelier des remèdes (une Potion basique par visite). |
| Magasin | `Ecrans.Magasin` | Léon, marchand (Bazar) | Onglets Acheter / Vendre, quantité, total. Revente à 50 %, objets clés invendables. |
| Magasin de vélos (27 oct. 2026) | `Ecrans.Magasin` (catalogue `Velos`) | Gilles, marchand de vélos (« Vélos de l'Azur », Bourg-Azur) | Même écran que le Bazar : aperçu 3D du vélo qui tourne, vitesse, un seul exemplaire par vélo, le vélo acheté devient le vélo choisi. |
| Restaurant | `Ecrans.Restaurant` | Lou, barista (Café des Embruns) | 3 repas qui soignent l'équipe, parfois un objet rare. Classe Cuisinier : recettes avec les ingrédients du sac, service en salle payé. |
| Guilde | `Ecrans.Guilde` | Réceptionniste | Missions par rang (ajoutées au journal des quêtes), échanges (phase 6), tableau des grades. |
| Investissement | `Ecrans.Investissement` | Réceptionniste (2e choix) ou bouton « Chantiers du bourg » de la Guilde | 3 chantiers, paliers et récompenses. |
| Pâturage | `Ecrans.Paturage` | Portail du Pâturage | Garde (déposer / prendre, l'équipe garde au moins 1 Tifazelt), soins de l'Éleveur, reproduction et œufs. |
| Sanctuaire | `Ecrans.Sanctuaire` | Pas encore construit : commande `service:Sanctuaire|3` | 8 Gardiens, DÉFIER lance un combat « gardien » ; victoire = cristal, grade recalculé, récompense en TFD. |

Données et règles : `UI.Services` (prix, catalogue, menu, recettes, missions, chantiers, Gardiens, grades). Nouvelles espèces de test pour les Gardiens dans `Combat.Especes` : Psychelle (Psy), Florelin (Plante), Braisillon (Feu), Givrelle (Glace).

## Ce qui suit le vault
- Infirmerie : PV, statuts et EM. Classe Infirmier : activité exclusive.
- Magasin : achat en TFD, revente ; objets clés impossibles à revendre.
- Restaurant : repas qui soignent et font trouver des objets rares ; classe Cuisinier : cuisine et service contre un salaire.
- Pâturage : garde ; Éleveur jusqu'à +100 de bonheur en une fois ; reproduction : genres opposés, au moins un type commun, parents déjà évolués ou sans évolution, pas de Légendaire, petit au niveau 1, espèce 50/50 ou celle du parent qui tient la Boîte de Chocolats, 2 % de talent caché, brillant 1 / 4 000 (x2 avec le Pendentif Brillant, x10 avec la Boîte à Bijoux), 75 de bonheur à l'éclosion.
- Sanctuaires : les 8 Gardiens et leurs types (13. Sanctuaire).
- Investissement : entreprise de travaux publics au nom à définir, paliers de récompenses.

## ⚠️ Provisoire / à trancher dans le GDD
- **Tous les chiffres** : prix, menu, recettes, salaire (250 TFD, 3 services par visite), missions et récompenses, chantiers et paliers, niveaux et équipes des Gardiens, temps d'éclosion (60 s).
- **Grades** : le vault dit « Bronze 0 à 2, Argent 2 à 4… », les bornes se chevauchent. Lecture retenue : Bronze 0-2, Argent 3-4, Or 5-6, Platine 7-8.
- **Guilde** : la Liste des écrans parle de récompenses en PC, mais `2. Economie` réserve les PC au PvP et aux Ruines de Combat. Les missions donnent donc des TFD pour l'instant.
- **Reproduction** : le genre n'existait pas encore dans les données (ajouté) ; le nouveau-né reprend les stats et 2 attaques du parent ; il n'y a pas de liste de talents cachés.
- Les missions acceptées vont dans le journal, mais leur suivi (compter les dresseurs battus…) n'est pas programmé.

## 🧪 Tests faits en jeu (phase 4)
- Infirmerie : soin de l'équipe (Florépine K.O. relevée, PV pleins). Magasin : achat de 3 Super potions (-1 800 TFD, sac 2 → 5), onglet Vendre. Restaurant : Grand plat (-900), cuisine d'une Galette (classe Cuisinier de test), un service (+250). Guilde : mission acceptée, onglet Grade. Investissement : 5 000 TFD dans le kiosque (palier 1). Pâturage : équipe pleine refusée, dépôt, reproduction Laineux + Galetin, éclosion d'un Laineux niveau 1. Sanctuaire : victoire contre Aria Titania, cristal Fée, grade Argent, +2 720 TFD. Dialogue de la réceptionniste : les choix MISSIONS / CHANTIERS DU BOURG / PLUS TARD s'affichent.
- 0 erreur de nos scripts.
- **Non vérifié :** les vrais clics (choix du dialogue, boutons, invite du Pâturage) — Studio ne simule pas les clics ni les invites.
- Commandes de test : `service:Infirmerie` (et Magasin, Restaurant, Guilde, Paturage, Sanctuaire|n, Investissement), `classe:Infirmier`, puis `t:soigner`, `t:choisir|Super potion`, `t:plus|2`, `t:agir`, `t:onglet|vendre`, `t:action|3`, `t:accepter|1`, `t:investir|1|5000`, `t:choisir|stock|1`, `t:action|deposer`, `t:action|parent|1`, `t:action|confier`, `t:avancer`, `t:action|eclore1`, `t:defier`, `t:continuer`.
