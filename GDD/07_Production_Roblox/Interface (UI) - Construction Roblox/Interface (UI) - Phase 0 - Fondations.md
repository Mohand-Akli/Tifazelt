---
tags:
  - production
  - roblox
  - ui
---
# 🧱 Phase 0 — fondations (19 oct. 2026)

> [[Interface (UI) - Construction Roblox|Sommaire de l'interface]] · [[Interface (UI) - Phase 1 - Exploration|Phase 1 →]] · [[Interface (UI) - Pièges Roblox|Pièges Roblox]]

| Élément | Emplacement | Rôle |
| :--- | :--- | :--- |
| `Theme` | `ReplicatedStorage.UI.Theme` | Couleurs, couleurs des types, police Montserrat (Black / ExtraBold / Bold), tailles, biseau 15°, ombres 8 / 5 px, durées. **Modifier une valeur ici la change partout.** |
| `Anim` | `ReplicatedStorage.UI.Anim` | Animations communes : glissé avec léger dépassement, sortie, « pop », fondu, compteur qui défile, tremblement de refus. |
| `Kit` | `ReplicatedStorage.UI.Kit` | Briques : texte en majuscules (accents compris), parallélogramme, parallélogramme bordé, carte à ombre solide, cercle, portrait provisoire, badge de type, badge de niveau, jauge, bouton biseauté, fond à lignes diagonales, fenêtre de confirmation, notification, transition de balayage. |
| `MenuManager` | `ReplicatedStorage.UI.MenuManager` | Pile d'écrans (RETOUR), mise à l'échelle 1920×1080 sur tout écran, blocage du personnage pendant un menu, Échap / Retour arrière / B de la manette pour revenir, sélection à la manette. |
| `DonneesTest` | `ReplicatedStorage.UI.DonneesTest` | Équipe de 6 Tifazelts, TFD, joueur : données factices en attendant les vrais systèmes. |
| `Ecrans.Equipe` | `ReplicatedStorage.UI.Ecrans.Equipe` | Premier écran, d'après la maquette. |
| `UI_Client` | `StarterPlayerScripts.UI_Client` | Démarre l'interface ; touche **M** ou **Y** (manette) et bouton provisoire ÉQUIPE en bas à gauche. |

## ✨ Animations
- **Ouverture et fermeture** : trois bandes biseautées (brun, terracotta, sable) balaient l'écran ; l'écran apparaît derrière elles.
- **Entrée des éléments** : le titre glisse depuis la gauche, le grand panneau depuis la gauche avec un léger rebond, les cartes de la liste depuis la droite l'une après l'autre, la barre du bas monte ; les portraits « poppent », les jauges se remplissent, les PV et les TFD défilent jusqu'à leur valeur.
- **Fond** : les lignes diagonales dérivent très lentement.
- **Boutons** : au survol, le bouton se soulève et un reflet balaie sa surface ; à l'appui, il s'enfonce dans son ombre (effet autocollant) ; un bouton inactif tremble.
- **Cartes** : au survol ou à la sélection manette, la carte se soulève et son ombre passe en cyan.
- **Fenêtre de confirmation** : voile sombre, la fenêtre arrive avec un rebond.
- **Notifications** : elles glissent depuis la droite, s'empilent, puis repartent.
- Le portrait du leader « respire » doucement.

## 🖼️ Écran ÉQUIPE (prototype fonctionnel)
- Grand panneau du leader : portrait, nom, niveau, PV, types, expérience, nature, capacité, objet tenu, bonheur, 4 attaques aux couleurs de leur type.
- Liste des 5 autres Tifazelts ; un Tifazelt K.O. est grisé et semi-transparent, avec un badge K.O. magenta.
- Clic sur un Tifazelt → fenêtre « CHANGER DE LEADER ? » → il prend la place du leader avec une animation et une notification. Un Tifazelt K.O. refuse avec une notification.
- Barre du bas : RETOUR (fonctionne), TIFALISTRE et INVENTAIRE (notification « arrive à la phase 2 »), TFD en orange.

## 🧪 Tests faits en jeu
- Ouverture en 0,38 s, fermeture en 0,44 s ; plusieurs ouvertures et fermetures d'affilée sans blocage.
- Personnage bloqué pendant le menu (vitesse 0, saut coupé), rétabli à la fermeture.
- Changement de leader confirmé (le leader devient bien le Tifazelt choisi) ; refus pour le Tifazelt K.O.
- Notifications et fenêtre de confirmation vérifiées en capture ; 0 erreur dans la console.
- Commandes de test (Studio) : attribut `UI_Test` du joueur = `open:Equipe`, `back`, `choisir:3`, `valider`, `annuler`, `toast:texte`.
- Non testé : manette réelle, écran tactile, très petits écrans.
