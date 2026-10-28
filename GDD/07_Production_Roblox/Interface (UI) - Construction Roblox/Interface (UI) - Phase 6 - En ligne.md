---
tags:
  - production
  - roblox
  - ui
---
# 🌐 Phase 6 — en ligne (20 oct. 2026)

> [[Interface (UI) - Phase 5 - Début de partie|← Phase 5]] · [[Interface (UI) - Construction Roblox|Sommaire de l'interface]] · [[Interface (UI) - Phase 7 - Mini-jeux et énigmes|Phase 7 →]] · [[Interface (UI) - Pièges Roblox|Pièges Roblox]]

*Mise à jour (relecture, 28 oct. 2026) : les Tifazelts de test cités ici (Voltaneau, Florelin, Aqualune) ont été retirés du jeu le 27 oct. 2026 et remplacés par les 20 Tifazelts nommés par Mohand : voir [[À décider - Dresseurs, vélos et remplaçants (27 oct. 2026)]]. Les tests datés ci-dessous restent tels qu'ils ont été faits.*

Le serveur fait l'arbitre : `ServerScriptService.EnLigne_Serveur` (un seul RemoteEvent, `ReplicatedStorage.Reseau.EnLigne`). Côté joueur : `UI.Reseau` (messages, profil public, combat distant).

| Écran | Module | Contenu |
| :--- | :--- | :--- |
| 6.1 En ligne | `Ecrans.EnLigne` | Ouvert depuis le bandeau EN LIGNE du menu. Onglets À proximité (≤ 250 studs), Amis (amis Roblox), Boss de raid. Fiche du dresseur choisi : grade, classe, captures, équipe ; boutons COMBAT, ÉCHANGE, CARTE DE DRESSEUR. Liste rafraîchie toutes les 3 s. |
| 6.2 Demande de combat | fenêtre de `UI_Client` + `Ecrans.Combat` | Invitation avec les règles (accepter / refuser ; l'envoyeur peut annuler ; sans réponse en 30 s elle expire). Refus automatique si le joueur est déjà en combat, en échange ou dans un dialogue. Le combat se joue dans l'écran Combat habituel : chaque tour est calculé par le serveur quand les deux dresseurs ont choisi. FUITE devient ABANDON, SAC grisé. |
| 6.3 Échange | `Ecrans.Echange` | Deux colonnes (je propose / je reçois), fiche complète du Tifazelt proposé en face, PRÊT des deux côtés. Changer d'offre annule les validations. Le Tifazelt reçu entre dans l'équipe et la Tifalistre. |
| 6.4 Carte d'un autre joueur | `Ecrans.CarteDresseur` (`lecture = true`) | Même carte que la sienne, ses TFD restent privés. |
| 6.5 Boss de raid | `Ecrans.Raid` | Salle d'attente (rejoindre / quitter / lancer). Chaque dresseur affronte le boss avec son équipe ; les PV du boss sont partagés et se mettent à jour chez tous. Victoire : TFD + un objet rare pour chaque dresseur qui l'a touché. La salle rouvre 20 s après. |

Moteur de combat : `Combat.Moteur` accepte `deuxJoueurs = true` (le camp A est joué par un second dresseur : action choisie, remplaçant choisi, abandon) ; pas d'XP ni de bonheur dans les combats en ligne. Sauvegarde de l'ancien moteur et de l'ancien écran Combat dans `ServerStorage.Sauvegardes_UI`.

Joueur test (Studio seulement) : un faux dresseur « Joueur test » apparaît dans la liste pour essayer seul. Il accepte les invitations, propose un Tifazelt, valide après toi, joue ses tours et tape aussi le boss de raid. Attribut de workspace `EnLigne_JoueurTest` = false pour l'enlever. Il n'existe jamais dans le jeu publié.

## Ce qui suit le vault
- Menu En ligne : combat, échange, carte des autres joueurs (1. Menus Et Interfaces).
- PvP : victoire = PC, +1 PC par victoire de suite ; défaite = 0 PC et série brisée (3. Mécanique).
- Échange : aucune évolution ne demande d'échange (rien n'en dépend).
- Boss de raid : seul ou à plusieurs, par région (façon Pokémon GO).

## ⚠️ Provisoire / à trancher dans le GDD
- **PC par victoire : 10** (+1 par victoire de suite). Le vault ne chiffre pas la base.
- **Règles PvP** : équipes soignées pour le combat, pas d'objets, abandon = défaite, choix automatique après 60 s sans réponse, l'équipe ne garde ni dégâts ni XP.
- **Échange** : Tifazelts seulement (le vault parle aussi d'objets).
- **Raid** : boss Voltaneau niveau 35 pour Bourg-Azur, PV = 6 fois + 1 par dresseur, 5 minutes, récompense = TFD d'un combat de boss + un objet rare ; accès par le menu En ligne (pas encore de lieu dans le monde).
- **Proximité** : 250 studs.
- **Données venues du joueur** : sans sauvegarde, équipes et profils sont envoyés par le joueur ; le serveur les nettoie et les borne (types, attaques, stats, longueurs, limite de messages). À rendre sûr quand les données seront gardées par le serveur.

## 🧪 Tests faits en jeu (phase 6, avec le Joueur test)
- Menu : bandeau EN LIGNE ouvre l'écran. Liste : Joueur test « Ami », « À 4 m ». Carte de dresseur en lecture seule (TFD « Privé », 40 PC, 2 cristaux).
- Échange : invitation acceptée, son offre affichée (Florelin), j'ai proposé Aqualune, validé, Florelin reçu, toasts.
- Combat en ligne : invitation acceptée, combat complet avec remplacements et statuts, victoire : 320 → 330 PC, série de 1.
- Raid : salle avec 2 dresseurs, lancement, PV partagés qui baissent avec les coups des deux, boss vaincu : +2 800 TFD, la salle rouvre.
- Demande de combat reçue : fenêtre ACCEPTER / REFUSER avec les règles.
- 0 erreur de nos scripts.
- **Non vérifié :** deux vrais joueurs en même temps (Studio ne lance ici qu'un joueur ; à tester avec Test > Clients et serveurs, 2 joueurs), déconnexion pendant un combat, délai de 60 s, onglet Amis avec de vrais amis Roblox, les vrais clics et la manette.
- Commandes de test : `open:EnLigne`, `t:onglet|raid`, `t:combat`, `t:echange`, `t:carte`, `t:proposer|2`, `t:valider`, `open:Raid`, `t:rejoindre`, `t:lancer`.

Captures de cette phase : [[Captures 2026-10-20#Interface — phase 6 (en ligne)]].
