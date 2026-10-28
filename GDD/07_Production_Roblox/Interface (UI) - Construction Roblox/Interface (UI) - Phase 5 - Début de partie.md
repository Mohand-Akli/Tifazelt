---
tags:
  - production
  - roblox
  - ui
---
# 🌅 Phase 5 — début de partie (20 oct. 2026)

> [[Interface (UI) - Phase 4 - Bâtiments et services|← Phase 4]] · [[Interface (UI) - Construction Roblox|Sommaire de l'interface]] · [[Interface (UI) - Phase 6 - En ligne|Phase 6 →]] · [[Interface (UI) - Pièges Roblox|Pièges Roblox]]

À l'arrivée dans le jeu, l'écran titre s'ouvre (attribut de workspace `UI_PasserTitre` = true pour le sauter en développement).

| Étape | Écran | Contenu |
| :--- | :--- | :--- |
| Titre | `Ecrans.Titre` | Logo AZZURSAL, JOUER (→ CONTINUER / NOUVELLE PARTIE), PARAMÈTRES. Derrière : la caméra glisse au-dessus de Bourg-Azur, face à la mer (plan réglable : attributs `TitreCamA`, `TitreCamB`, `TitreVise`). Le personnage attend sous le décor pendant le titre (le monde est chargé par morceaux autour de lui) et revient à sa place avec CONTINUER. |
| Création | `Ecrans.CreationDresseur` | Nom (3 à 12 lettres, accents, espaces, tirets, apostrophes ; capitale ajoutée), avatar Roblox du joueur en vitrine (pose de repos, il tourne doucement), couleur de dresseur (6 pastilles), aperçu de la carte de dresseur. |
| Classe | `Ecrans.Classe` | 6 cartes (rôle + 3 avantages résumés de 12. Joueur) : une principale, une secondaire, puis confirmation. |
| Chargement | `UI.Chargement` | Deux bandes biseautées couvrent l'écran, nom du lieu, astuce, Tiflask qui remue, barre de progression. Utilisé à la fin de la création (Bourg-Azur, Maison familiale). |
| Starter | `Ecrans.Starter` | Salle des Spécimens : 3 Tiflasks (Feu, Eau, Plante). Choisir ouvre la fiole (Tifazelt, type, forme finale du vault). Après confirmation : Zéphir prend celui qui a l'avantage, le Professeur Arid Acanthus remet le Tifalistre et des Tiflask, bouton AFFRONTER ZÉPHIR (combat d'apprentissage). |

Fin de la création : partie remise à zéro (`UI.NouvellePartie`), arrivée dans la chambre de la maison familiale, objectif « L'Heure du Choix », Maman donne des TFD. Le starter s'obtient en examinant le plateau stérile du Laboratoire Arid (invite « Examiner », attribut `Service = Starter`). Victoire contre Zéphir : quête terminée, objectif suivant. Défaite : revanche en revenant au plateau.

Autres changements : la Tiflask est dessinée comme une fiole ronde à bouchon (`Kit.tiflask`, même famille que la Tiflask du combat) ; un écran qui plante à l'ouverture ne bloque plus les menus ; sans Tifazelt, Équipe et Fiche affichent un message, et les combats sont refusés ; la carte de dresseur prend la couleur choisie.

## Ce qui suit le vault
- 3 classes principales et 3 secondaires avec leurs avantages (12. Joueur).
- Starters Feu, Eau, Plante ; formes finales Feu / Obscurité, Eau / Psy, Plante / Fée ; Zéphir prend celui qui a l'avantage (00. Définition, 6. Personnages).
- Le Professeur Arid remet le starter, des Tiflask et le Tifalistre ; Salle des Spécimens et plateau stérile (Val Palmeraie).
- Quête « L'Heure du Choix » : laboratoire, starter, Tifalistre, combat d'apprentissage. Départ dans la chambre ; Maman donne des TFD.

## ⚠️ Provisoire / à trancher dans le GDD
- **Noms des starters** : Pyrofennec, Aqualune, Florépine (repris de la Tifalistre de test, le vault dit `???`). Stats, courbe, niveau 5, attaques prises automatiquement.
- **Chiffres** : 3 000 TFD de Maman, 5 Tiflask simples.
- **Une classe principale + une secondaire** : le vault ne dit pas combien on en choisit ; repris de la carte de dresseur de test.
- **Apparence** : le vault ne la décrit pas. Avatar Roblox + couleur de dresseur en attendant.
- **Adversaire du combat d'apprentissage** : Zéphir (le vault dit seulement « combat d'apprentissage »).
- **Objectif après la quête** : « Vers la Route 2, sortir par la Porte du Sirocco » (déduit de la note Val Palmeraie).
- **Professeur Arid** : pas encore de PNJ dans le laboratoire ; il parle dans l'écran du starter.
- Le nom n'est pas encore passé au filtre de Roblox (à faire côté serveur avec la sauvegarde).
- « Continuer » reprend les données de test (pas de sauvegarde pour l'instant).

## 🧪 Tests faits en jeu (phase 5)
- Titre : décor de Bourg-Azur chargé, JOUER → CONTINUER / NOUVELLE PARTIE ; CONTINUER ramène le personnage à son point de départ, caméra normale.
- Création : nom trop long refusé (« 12 lettres au maximum »), « Élise » accepté, couleurs, avatar en pose de repos.
- Classe : Éleveur + Stratège, Infirmier + Chasseur de trésors, Cuisinier + Ingénieur, confirmation.
- Fin de création : chargement « Bourg-Azur », arrivée dans la chambre, 3 000 TFD, objectif L'Heure du Choix ; carte de dresseur à jour.
- Avec l'équipe vide : Menu, Carte de dresseur, Inventaire, Tifalistre, Quêtes, Livre, Infirmerie, Pâturage, Guilde, Restaurant, Sanctuaire s'ouvrent ; Équipe, Fiche et combat refusés avec un message.
- Starter : Pyrofennec → Zéphir prend Aqualune ; Florépine → Zéphir prend Pyrofennec ; Tifalistre et Tiflask reçus ; combat contre Zéphir gagné → « Quête terminée », objectif Vers la Route 2, +200 TFD ; le plateau dit ensuite que les Tiflasks ont trouvé leurs dresseurs.
- 0 erreur de nos scripts.
- **Non vérifié :** les vrais clics et la saisie au clavier dans la case du nom, la manette, l'invite « Examiner » du laboratoire (Studio ne simule pas les invites), la marche jusqu'au laboratoire.
- Commandes de test : `titre`, `t:jouer`, `t:continuer`, `t:nouvelle`, `t:nom|Élise`, `t:couleur|3`, `t:suivant`, `t:principale|1`, `t:secondaire|2`, `t:valider`, `valider`, `service:Starter`, `t:choisir|1`, `t:confirmer`, `t:combat`, `chargement:Val Palmeraie|Laboratoire Arid|8`.

Captures de cette phase : [[Captures 2026-10-20#Interface — phase 5 (début de partie)]].
