---
tags:
  - menus
  - ui
  - production
aliases:
  - Liste des menus
  - Écrans du jeu
  - Plan UI
---
# 📋 Liste des Menus et Écrans (plan de production UI)

> Tous les écrans dont le jeu aura besoin, rangés par **phase de production** : on les génère dans Roblox Studio dans cet ordre, étape par étape, chacun **fonctionnel** (ouverture, fermeture, navigation, données réelles ou de test).
> Style : [[16. Direction Artistique des Menus]]. Description des menus du jeu : [[1. Menus Et Interfaces]].
> Statut : ☐ à faire · 🛠️ en cours · ✅ fait et testé en jeu. Construction : [[Interface (UI) - Construction Roblox]].

## 🧱 Phase 0 — Fondations (à faire avant tout écran)
| # | Élément | Rôle | Statut |
| :--- | :--- | :--- | :--- |
| 0.1 | **`UI_Theme`** | Couleurs, polices, tailles, couleurs des types (valeurs de la DA, partie 6) | ✅ |
| 0.2 | **`UI_Kit`** | Composants : Fond, Carte, BoutonBiseau, Onglet, BadgeType, BadgeNiveau, CercleIcone, Jauge, BarreNav, ListeCartes, Modale, Toast | ✅ |
| 0.3 | **Gestionnaire de menus** | Ouvrir / fermer, pile d'écrans (RETOUR), bloque les déplacements quand un menu est ouvert, souris + tactile + manette | ✅ |
| 0.4 | **Données de test** | Équipe, inventaire, TFD et quêtes factices pour tester les écrans avant que les systèmes de jeu existent | ✅ |

## 🧭 Phase 1 — Exploration (ce que le joueur voit en permanence)
| # | Écran | Contenu | Lien GDD | Statut |
| :--- | :--- | :--- | :--- | :--- |
| 1.1 | **HUD d'exploration** | Bouton MENU, monnaie (TFD), objectif actuel, raccourcis | [[5. Quêtes Dans L'Aventure#🎯 Système d'Objectif\|Objectif]] | ✅ objectif, TFD, bouton MENU (ouvre le menu principal) |
| 1.2 | **Bandeau de zone** | Nom du lieu à l'entrée (« ROUTE 1 — BOSQUET DES ÉGARÉS ») | [[00_Province_Lumeridia]] | ✅ 17 lieux et 7 régions (`UI.Zones`) |
| 1.3 | **Boîte de dialogue** | Nom du PNJ, portrait dans un cercle, texte, choix de réponse | [[11. PNJ]] | ✅ texte lettre par lettre, choix (dresseurs) ; remplace l'ancienne bulle |
| 1.4 | **Notifications (toasts)** | Secret trouvé (n/31), objet reçu, quête mise à jour | [[Secrets d'exploration]] | ✅ branché sur les 39 secrets ; invites d'action (E PARLER…) au style de la DA |
| 1.5 | **Fenêtre de confirmation** | OUI / NON, réutilisée partout | — | ✅ |

## 🎒 Phase 2 — Menu principal et ses sous-menus
| # | Écran | Contenu | Lien GDD | Statut |
| :--- | :--- | :--- | :--- | :--- |
| 2.1 | **Menu principal** | Accès : Équipe, Tifalistre, Inventaire, Carte de dresseur, Quêtes, Carte, En ligne, Paramètres | [[1. Menus Et Interfaces]] | ✅ 8 tuiles (+ « En ligne » verrouillée) ; touche M / Y et bouton MENU |
| 2.2 | **Équipe** | 6 Tifazelts : leader en grand, liste à droite, PV, types, niveau ; réordonner, faire tenir un objet, nourrir | [[1. Menus Et Interfaces#**Équipe**\|Équipe]] | ✅ leader, liste, échange, ouverture de la fiche |
| 2.3 | **Fiche détaillée d'un Tifazelt** | Statistiques, nature, capacité (passive / cachée), 4 attaques, bonheur, objet tenu, brillant | [[00. Définition]] · [[9. Capacités des Tifazelts]] | ✅ stats colorées par la nature, 4 attaques du vault, précédent / suivant, définir leader |
| 2.4 | **Inventaire** | Onglets : Médicaments, Nourriture, Objets, Tiflask, Objets clés ; grille d'icônes dans des cercles ; utiliser, donner, jeter | [[1. Menus Et Interfaces#🎒 Inventaire (Différentes Sections)\|Inventaire]] · [[14. Objets]] | ✅ 5 poches, utiliser (choix du Tifazelt), donner, jeter (confirmation) |
| 2.5 | **Livre de Compétences** | Pages d'attaques classées par chapitre de type ; pages manquantes en gris | [[1. Menus Et Interfaces#**Livre de Compétences**\|Livre]] · `8. Liste des attaques` | ✅ 15 chapitres, 283 attaques du vault, pages manquantes en gris |
| 2.6 | **Tifalistre** | Liste numérotée à gauche (capturé / aperçu / inconnu), fiche et modèle 3D à droite | [[14. Objets#Tifalistre\|Tifalistre]] | ✅ liste + fiche (sans modèle 3D pour l'instant) |
| 2.7 | **Carte de dresseur** | TFD, PC, cristaux des Gardiens, heures de jeu, grade, classe | [[1. Menus Et Interfaces#🪪 Carte de dresseur\|Carte de dresseur]] · [[12. Joueur]] | ✅ carte d'identité, 8 cristaux, progression de grade |
| 2.8 | **Journal des quêtes** | Objectif principal, quêtes annexes acceptées / terminées | [[5. Quêtes Dans L'Aventure]] | ✅ 3 onglets, SUIVRE met la quête dans l'objectif du HUD |
| 2.9 | **Carte de la région** | Carte de Luméridia Est, position du joueur, lieux découverts | [[00_Province_Lumeridia]] | ✅ relief relevé sur la carte, lieux, position en direct |
| 2.10 | **Paramètres** | Son, musique, sensibilité caméra, qualité, langue, commandes | — | ✅ musique, effets, vitesse du texte, bandeau, notifications (session seulement) |

## ⚔️ Phase 3 — Combat
| # | Écran | Contenu | Lien GDD | Statut |
| :--- | :--- | :--- | :--- | :--- |
| 3.1 | **Ouverture de combat** | Bandeau « UN TIFAZELT SAUVAGE APPARAÎT » / présentation du dresseur ; version spéciale pour Gardiens et Boss | [[1. Menus Et Interfaces#⚔️ Combats\|Combats]] | ✅ sauvage, dresseur, Gardien / Boss (version longue, écran qui tremble) |
| 3.2 | **HUD de combat** | Barres de PV fines, niveau, statut, météo ; actions : ATTAQUER, SAC, ÉQUIPE, FUITE | [[15. Charte Graphique#⚔️ Le HUD de Combat (In-game)\|HUD]] | ✅ barres de PV fines, niveau, types, statut, météo ; ATTAQUER, SAC, ÉQUIPE, FUITE |
| 3.3 | **Choix d'attaque** | 4 boutons biseautés (type, catégorie, EM restants, puissance) | [[9. Capacités des Tifazelts]] | ✅ 4 boutons biseautés (type, catégorie, puissance, EM) |
| 3.4 | **Sac en combat** | Médicaments et Tiflask utilisables | [[14. Objets]] | ✅ médicaments sur le Tifazelt choisi, Tiflask (sauvages seulement) |
| 3.5 | **Changement de Tifazelt** | Version réduite de l'Équipe | — | ✅ changement volontaire et remplacement forcé après un K.O. |
| 3.6 | **Capture** | Lancer de Tiflask, secousses, réussite / échec, surnom | [[1. Menus Et Interfaces#**Tiflask**\|Tiflask]] | ✅ lancer, 0 à 3 secousses, réussite / échec, surnom (formule provisoire) |
| 3.7 | **Fin de combat** | XP gagnée, TFD, PC, objets ; montée de niveau | [[2. Economie Et Formules Et Reste]] | ✅ XP par Tifazelt, montées de niveau et stats gagnées, TFD |
| 3.8 | **Nouvelle attaque** | Apprendre / remplacer une des 4 attaques | — | ✅ oublier une des 4 attaques ou renoncer |
| 3.9 | **Évolution** | Animation et nouvelle fiche | [[00. Définition#🔄 Méthodes d'Évolution\|Évolution]] | ✅ animation et nouvelle fiche (évolution de test) |
| 3.10 | **Défaite** | Perte de TFD, retour à l'Infirmerie | [[2. Economie Et Formules Et Reste#📉 Perte de TFD\|Perte de TFD]] | ✅ perte de TFD contre un dresseur, équipe soignée (retour au point d'apparition, pas encore d'Infirmerie) |

## 🏘️ Phase 4 — Bâtiments et services
| # | Écran | Contenu | Lien GDD | Statut |
| :--- | :--- | :--- | :--- | :--- |
| 4.1 | **Infirmerie** | Soigner l'équipe (bonus de la classe Infirmier) | [[Bâtiments Communs#🏥 Infirmerie\|Infirmerie]] | ✅ capsules, soin PV / statuts / EM ; atelier des remèdes pour la classe Infirmier |
| 4.2 | **Magasin** | Acheter / vendre, quantité, prix en TFD | [[Bâtiments Communs#🛒 Magasin\|Magasin]] | ✅ acheter / vendre, quantité, total en TFD (prix provisoires) |
| 4.3 | **Restaurant / cuisine** | Recettes, ingrédients, préparation (classe Cuisinier) | [[Bâtiments Communs#🍽️ Restaurant\|Restaurant]] | ✅ repas (soin + objet rare), cuisine et service pour la classe Cuisinier (provisoire) |
| 4.4 | **Guilde des dresseurs** | Missions, grade, récompenses en PC | [[Bâtiments Communs#🛡️ Guilde des dresseurs\|Guilde]] | ✅ missions par rang, grade ; échanges annoncés pour la phase 6 (récompenses en TFD, voir note) |
| 4.5 | **Pâturage** | Stockage des Tifazelts, reproduction (conditions, objets) | [[Bâtiments Communs#🌿 Pâturage\|Pâturage]] · [[00. Définition#🥚 Accouplement et Reproduction\|Reproduction]] | ✅ garde équipe / pâturage, soins de l'Éleveur (+100), reproduction avec les règles du vault, œufs |
| 4.6 | **Sanctuaire** | Défi du Gardien, obtention du cristal | [[13. Sanctuaire]] | ✅ 8 Gardiens, défi (combat), remise du cristal, grade (équipes provisoires, pas encore de sanctuaire dans le monde) |
| 4.7 | **Investissement** | Injecter des TFD dans un lieu | [[2. Economie Et Formules Et Reste#🏗️ Investissement (Injecter des fonds)\|Investissement]] | ✅ 3 chantiers à paliers (provisoires, entreprise « nom à définir ») |

## 🌅 Phase 5 — Début de partie
| # | Écran | Contenu | Lien GDD | Statut |
| :--- | :--- | :--- | :--- | :--- |
| 5.1 | **Écran titre** | Logo AZZURSAL, JOUER, PARAMÈTRES | — | ✅ logo AZZURSAL, JOUER (Continuer / Nouvelle partie), PARAMÈTRES ; décor de Bourg-Azur en fond |
| 5.2 | **Création du dresseur** | Nom, apparence | [[12. Joueur]] | ✅ nom (3 à 12 lettres), avatar Roblox en vitrine, couleur de dresseur (provisoire) |
| 5.3 | **Choix de la classe** | 6 classes en cartes : effets, bonus | [[12. Joueur#🛡️ Classes de Dresseur\|Classes]] | ✅ 6 cartes, une principale + une secondaire |
| 5.4 | **Choix du starter** | 3 starters au Laboratoire Arid | [[00. Définition#🌟 Starters (Tifazelt de Départ)\|Starters]] · [[Val Palmeraie]] | ✅ 3 Tiflasks, Professeur Arid, choix de Zéphir, Tifalistre + Tiflask, combat d'apprentissage (noms provisoires) |
| 5.5 | **Écrans de chargement** | Transitions, astuces | [[1. Menus Et Interfaces#⏳ Chargements & Mini-Jeux\|Chargements]] | ✅ nom du lieu, astuce du vault, Tiflask animée, barre de progression |

## 🌐 Phase 6 — En ligne
| # | Écran | Contenu | Lien GDD | Statut |
| :--- | :--- | :--- | :--- | :--- |
| 6.1 | **Menu En ligne** | Joueurs à proximité / amis | [[1. Menus Et Interfaces#🌐 En ligne\|En ligne]] | ✅ onglets À proximité / Amis / Boss de raid, fiche du dresseur, COMBAT, ÉCHANGE, CARTE |
| 6.2 | **Demande de combat (PvP)** | Invitation, acceptation, règles | [[3. Mécanique#⚔️ PvP (Joueur contre Joueur)\|PvP]] | ✅ invitation (accepter / refuser / annuler), combat calculé par le serveur, PC + série de victoires |
| 6.3 | **Échange** | Deux colonnes, validation des deux côtés | [[3. Mécanique#🔄 Échange de Tifazelt\|Échange]] | ✅ deux colonnes, validation des deux côtés, offre changée = validations annulées (Tifazelts seulement pour l'instant) |
| 6.4 | **Carte de dresseur d'un autre joueur** | Version lecture seule de 2.7 | — | ✅ même carte, TFD privés |
| 6.5 | **Boss de raid** | Salle d'attente, équipe, récompenses | [[3. Mécanique#🐉 Boss de Raid\|Raid]] | ✅ salle d'attente, PV du boss partagés, récompenses (boss et chiffres provisoires) |

## 🎣 Phase 7 — Mini-jeux et énigmes
| # | Écran | Contenu | Lien GDD | Statut |
| :--- | :--- | :--- | :--- | :--- |
| 7.1 | **Pêche** | Jauge de tension, prise | [[14. Objets#**Canne à pêche**\|Canne à pêche]] | ✅ lancer, ferrer, jauge de tension (zone verte), prise → combat contre un Tifazelt Eau ; ponton de Bourg-Azur |
| 7.2 | **Plongée** | Jauge d'oxygène (bonbonne, 5 min) | [[14. Objets#**Bonbonne d'oxygène**\|Bonbonne]] | ✅ jauge d'air dès que la tête est sous l'eau, Tuba (plus de souffle), Bonbonne 5 min, profondeur, teinte bleue et flou |
| 7.3 | **Puzzles et énigmes** | Interface selon l'énigme | [[3. Mécanique#🧩 Puzzles et Énigmes\|Puzzles]] | ✅ écran commun ; énigme des symboles (stèle, Route 1) et des dalles (Crique secrète, Chasseur de trésors seulement) |

---
**Total : 4 fondations + 45 écrans.** Les phases 0 à 2 donnent un jeu explorable avec de vrais menus ; la phase 3 demande que le système de combat soit codé en même temps.
