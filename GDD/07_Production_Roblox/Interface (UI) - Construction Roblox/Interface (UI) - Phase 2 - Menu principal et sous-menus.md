---
tags:
  - production
  - roblox
  - ui
---
# 🎒 Phase 2 — menu principal et sous-menus (20 oct. 2026)

> [[Interface (UI) - Phase 1 - Exploration|← Phase 1]] · [[Interface (UI) - Construction Roblox|Sommaire de l'interface]] · [[Interface (UI) - Phase 3 - Combat|Phase 3 →]] · [[Interface (UI) - Pièges Roblox|Pièges Roblox]]

Tous les écrans sont dans `ReplicatedStorage.UI.Ecrans` et sont enregistrés par `UI_Client`. La touche M, le bouton Y et le bouton MENU du HUD ouvrent le **Menu** ; Échap / B / Retour arrière reviennent d'un cran.

| Écran | Module | Ce qu'il fait |
| :--- | :--- | :--- |
| Menu principal | `Ecrans.Menu` | 8 tuiles biseautées avec pictogramme et chiffre clé ; « En ligne » grisée (phase 6). |
| Équipe | `Ecrans.Equipe` | Leader en grand, 5 autres à droite ; un clic ouvre la fiche ; boutons TIFALISTRE et INVENTAIRE. |
| Fiche Tifazelt | `Ecrans.Fiche` | Statistiques (vert = stat montée par la nature, magenta = stat baissée), nature, objet, capacité, bonheur, 4 attaques avec catégorie / puissance / précision / EM et description. Précédent / Suivant (et Q / E), Définir leader. |
| Sac | `Ecrans.Inventaire` | 5 poches en onglets, liste à gauche, détail à droite. UTILISER ouvre le choix du Tifazelt (les Tifazelts à qui l'objet ne sert à rien sont grisés), DONNER fait tenir l'objet, JETER demande confirmation. |
| Livre de compétences | `Ecrans.Livre` | 15 chapitres (un par type) avec le compte possédé / total, pages possédées en détail, pages manquantes en gris. |
| Tifalistre | `Ecrans.Tifalistre` | Liste numérotée (losange vert = capturé, cyan = aperçu, gris = inconnu) et fiche à droite. Pas encore de modèle 3D. *(Depuis le 26 oct. 2026 : portraits rendus dans Blender pour les Tifazelts modélisés.)* |
| Carte de dresseur | `Ecrans.CarteDresseur` | Carte façon pièce d'identité : avatar, grade, classes, TFD, PC, heures, captures, 8 cristaux des Gardiens (clic = nom du Gardien), jauge vers le grade suivant. |
| Quêtes | `Ecrans.Quetes` | Onglets Principale / Annexes / Terminées. SUIVRE met la quête dans l'objectif du HUD. |
| Carte | `Ecrans.Carte` | Carte de Luméridia Est dessinée à partir du relief, régions, lieux (orange = découvert, gris = inconnu, au survol : nom), position du joueur en direct. |
| Paramètres | `Ecrans.Parametres` | Musique, effets sonores, vitesse du texte (25 à 110 lettres / s, avec aperçu), bandeau des lieux, notifications. RÉINITIALISER avec confirmation. |

## Données
- `UI.Attaques` : les 283 attaques de `8. Attaques`, recopiées telles quelles depuis le vault (script `audit/attaques.lua` sur le PC). À l'affichage seulement, une espace est ajoutée après les virgules et les points collés, et la phrase commence par une majuscule.
- `UI.CarteDonnees` : relevé du terrain (une lettre par case de 40 studs : eau, sable, herbe, terre, roche). À refaire si la carte change.
- `UI.DonneesTest` : joueur, équipe, sac, quêtes, cristaux, Tifalistre et réglages **de test**. Les Tifazelts de la Tifalistre au-delà de l'équipe, les quantités et les effets des objets sont provisoires.

## Réglages
- Volumes : SoundGroups `Musique` et `Effets` dans SoundService (créés s'ils manquent). **Chaque son du jeu devra être rangé dans l'un des deux** pour suivre le réglage ; aujourd'hui le jeu n'a encore aucun son. *(Dépassé : musiques et sons ajoutés à partir du 20 oct. 2026, voir [[Animations, déplacements et audio]].)*
- Vitesse du texte : `Dialogue.setSpeed`. Bandeau : `HUD.bannerEnabled`. Notifications : les toasts marqués `notif = true` (secret trouvé…) sont masqués ; les retours d'action (objet utilisé, quête suivie) restent.
- Les réglages durent la session ; ils seront sauvegardés avec les données du joueur.

## 🧪 Tests faits en jeu (phase 2)
- Chaque écran ouvert en Play et vérifié en capture : Menu, Équipe, Fiche (membres 1 et 4, changement avec Q / E), Sac (fenêtre UTILISER), Livre, Tifalistre, Carte de dresseur, Quêtes (onglet Annexes), Carte, Paramètres. 0 erreur de nos scripts dans la console.
- Paramètres : curseurs et interrupteurs changent bien les volumes, la vitesse de l'aperçu et les libellés ; réinitialisation OK.
- **Non vérifié :** les clics réels (choisir un Tifazelt dans UTILISER, DONNER, cristaux, épingles de la carte) — Studio ne permet pas de simuler un clic ; la touche M elle-même (testée en phase 0, la cible a juste changé).
- Commandes de test ajoutées : `ouvrir:Ecran|n` (ex. `ouvrir:Fiche|2`) et `t:fonction|arg` (fonctions de test de l'écran du dessus, ex. `t:set|texte|1`, `t:utiliser`). Envoyer deux fois la même valeur ne relance rien : alterner `back` et `back:`.
