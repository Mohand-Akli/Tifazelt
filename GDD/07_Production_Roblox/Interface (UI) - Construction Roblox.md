---
tags:
  - production
  - roblox
  - ui
aliases:
  - UI Roblox
  - Système de menus
---
# 🖥️ Interface (UI) — Construction Roblox

> Mise en œuvre dans Studio de la [[16. Direction Artistique des Menus]]. Plan des écrans : [[Liste des Menus et Écrans]]. Index : [[00. Production Roblox]].

## 🧱 Phase 0 — fondations (20 oct. 2026)
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

## ⚠️ Pièges Roblox rencontrés (à respecter pour les prochains écrans)
- Un **contour UIStroke sur un cercle** se transforme en carré dans un CanvasGroup mis à l'échelle → les cercles sont faits de deux disques emboîtés.
- **Ne pas faire tourner** un élément arrondi placé dans une zone qui coupe (ClipsDescendants) : ses coins ronds disparaissent.
- Un parallélogramme doit être plus large que sa hauteur × tan(15°) ; pour les bandes hautes et étroites, utiliser un angle de 2–3°.
- Ce jeu n'a pas de `PlayerModule` : le blocage du personnage passe par `ContextActionService` et la vitesse du Humanoid.
- **Aucun émoji** dans l'interface : portraits provisoires = initiale dans un cercle teinté du type.

## 🧭 Phase 1 — exploration (20 oct. 2026)
| Élément | Emplacement | Rôle |
| :--- | :--- | :--- |
| `HUD` | `ReplicatedStorage.UI.HUD` | Objectif en haut à gauche (quête principale), TFD en haut à droite, bouton MENU en bas à droite avec la touche (M au clavier, Y à la manette, cachée en tactile). Tout glisse hors de l'écran pendant un menu ou un dialogue. |
| Bandeau de zone | `HUD` + `ReplicatedStorage.UI.Zones` | À l'entrée d'un lieu : bande biseautée qui traverse l'écran, région en sous-titre, trait cyan qui se dessine. Il faut rester 0,8 s dans le lieu ; un même lieu ne s'annonce pas plus d'une fois toutes les 25 s. 17 petits lieux (cercles) puis 7 régions (rectangles), dans l'ordre de priorité. |
| `Dialogue` | `ReplicatedStorage.UI.Dialogue` | Boîte de dialogue : nom dans une étiquette biseautée, portrait rond, texte qui s'écrit lettre par lettre, compteur 1 / 3, indicateur SUITE qui oscille. E / Entrée / Espace / A / clic pour continuer (un premier appui termine la ligne), Échap / B pour fermer. 3 styles : PNJ (terracotta), dresseur (magenta, choix COMBATTRE / PLUS TARD), découverte (cyan, losange). |
| `Invites` | `ReplicatedStorage.UI.Invites` | Remplace l'affichage par défaut des ProximityPrompt : touche dans un biseau blanc, action sur une barre terracotta, nom de l'objet au-dessus, barre cyan de maintien ; apparition avec rebond ; utilisable au clic et au tactile. |
| Secrets | `UI_Client` | Une découverte ouvre la boîte « DÉCOUVERTE » ; la première fois, une notification « SECRET TROUVÉ — zone : n / total ». |
| Onglets et liste | `Kit.tabs`, `Kit.list` | Onglets biseautés avec repère cyan qui glisse (Q / E ou LB / RB) ; liste défilante de cartes qui entrent l'une après l'autre. Écran de test `Ecrans.Galerie` (aperçu du sac). |

- L'ancienne bulle de dialogue et la carte de secret de `BourgAzur_Client` sont désactivées quand la nouvelle interface tourne (attribut `UI_Azzursal` du joueur) ; les portes animées de ce script continuent de fonctionner.
- Pendant un menu ou un dialogue : personnage bloqué, invites coupées, HUD caché.

### 🧪 Tests faits en jeu (phase 1)
- HUD, bandeau de zone, dialogue d'un dresseur avec choix, dialogue d'un vrai PNJ (la Voyageuse en manteau gris) et aperçu du sac : vérifiés en capture.
- Fermeture du dialogue : personnage et invites rétablis. Changement d'onglet : la liste se reconstruit (2 éléments dans Nourriture). 0 erreur dans la console.
- **Non vérifié en image :** les invites d'action. Elles sont bien créées au bon endroit, mais la capture d'écran de Studio n'affiche aucun BillboardGui (même un carré rouge de test). À regarder en jeu.
- Commandes de test : `dialogue:pnj`, `dialogue:dresseur`, `dialogue:decouverte`, `suite`, `fermer`, `parler` (PNJ le plus proche), `zone:Nom|Région`, `open:Galerie`, `onglet:1`.

## 🎒 Phase 2 — menu principal et sous-menus (20 oct. 2026)
Tous les écrans sont dans `ReplicatedStorage.UI.Ecrans` et sont enregistrés par `UI_Client`. La touche M, le bouton Y et le bouton MENU du HUD ouvrent le **Menu** ; Échap / B / Retour arrière reviennent d'un cran.

| Écran | Module | Ce qu'il fait |
| :--- | :--- | :--- |
| Menu principal | `Ecrans.Menu` | 8 tuiles biseautées avec pictogramme et chiffre clé ; « En ligne » grisée (phase 6). |
| Équipe | `Ecrans.Equipe` | Leader en grand, 5 autres à droite ; un clic ouvre la fiche ; boutons TIFALISTRE et INVENTAIRE. |
| Fiche Tifazelt | `Ecrans.Fiche` | Statistiques (vert = stat montée par la nature, magenta = stat baissée), nature, objet, capacité, bonheur, 4 attaques avec catégorie / puissance / précision / EM et description. Précédent / Suivant (et Q / E), Définir leader. |
| Sac | `Ecrans.Inventaire` | 5 poches en onglets, liste à gauche, détail à droite. UTILISER ouvre le choix du Tifazelt (les Tifazelts à qui l'objet ne sert à rien sont grisés), DONNER fait tenir l'objet, JETER demande confirmation. |
| Livre de compétences | `Ecrans.Livre` | 15 chapitres (un par type) avec le compte possédé / total, pages possédées en détail, pages manquantes en gris. |
| Tifalistre | `Ecrans.Tifalistre` | Liste numérotée (losange vert = capturé, cyan = aperçu, gris = inconnu) et fiche à droite. Pas encore de modèle 3D. |
| Carte de dresseur | `Ecrans.CarteDresseur` | Carte façon pièce d'identité : avatar, grade, classes, TFD, PC, heures, captures, 8 cristaux des Gardiens (clic = nom du Gardien), jauge vers le grade suivant. |
| Quêtes | `Ecrans.Quetes` | Onglets Principale / Annexes / Terminées. SUIVRE met la quête dans l'objectif du HUD. |
| Carte | `Ecrans.Carte` | Carte de Luméridia Est dessinée à partir du relief, régions, lieux (orange = découvert, gris = inconnu, au survol : nom), position du joueur en direct. |
| Paramètres | `Ecrans.Parametres` | Musique, effets sonores, vitesse du texte (25 à 110 lettres / s, avec aperçu), bandeau des lieux, notifications. RÉINITIALISER avec confirmation. |

### Données
- `UI.Attaques` : les 283 attaques de `8. Attaques`, recopiées telles quelles depuis le vault (script `audit/attaques.lua` sur le PC). À l'affichage seulement, une espace est ajoutée après les virgules et les points collés, et la phrase commence par une majuscule.
- `UI.CarteDonnees` : relevé du terrain (une lettre par case de 40 studs : eau, sable, herbe, terre, roche). À refaire si la carte change.
- `UI.DonneesTest` : joueur, équipe, sac, quêtes, cristaux, Tifalistre et réglages **de test**. Les Tifazelts de la Tifalistre au-delà de l'équipe, les quantités et les effets des objets sont provisoires.

### Réglages
- Volumes : SoundGroups `Musique` et `Effets` dans SoundService (créés s'ils manquent). **Chaque son du jeu devra être rangé dans l'un des deux** pour suivre le réglage ; aujourd'hui le jeu n'a encore aucun son.
- Vitesse du texte : `Dialogue.setSpeed`. Bandeau : `HUD.bannerEnabled`. Notifications : les toasts marqués `notif = true` (secret trouvé…) sont masqués ; les retours d'action (objet utilisé, quête suivie) restent.
- Les réglages durent la session ; ils seront sauvegardés avec les données du joueur.

### 🧪 Tests faits en jeu (phase 2)
- Chaque écran ouvert en Play et vérifié en capture : Menu, Équipe, Fiche (membres 1 et 4, changement avec Q / E), Sac (fenêtre UTILISER), Livre, Tifalistre, Carte de dresseur, Quêtes (onglet Annexes), Carte, Paramètres. 0 erreur de nos scripts dans la console.
- Paramètres : curseurs et interrupteurs changent bien les volumes, la vitesse de l'aperçu et les libellés ; réinitialisation OK.
- **Non vérifié :** les clics réels (choisir un Tifazelt dans UTILISER, DONNER, cristaux, épingles de la carte) — Studio ne permet pas de simuler un clic ; la touche M elle-même (testée en phase 0, la cible a juste changé).
- Commandes de test ajoutées : `ouvrir:Ecran|n` (ex. `ouvrir:Fiche|2`) et `t:fonction|arg` (fonctions de test de l'écran du dessus, ex. `t:set|texte|1`, `t:utiliser`). Envoyer deux fois la même valeur ne relance rien : alterner `back` et `back:`.

## ⚔️ Phase 3 — combat (20 oct. 2026)
Le combat est un écran comme les menus (`Ecrans.Combat`), mais RETOUR / Échap n'en fait pas sortir : il ferme la fenêtre ouverte ou revient aux actions. Un combat se lance avec `M.combattre({ genre, adverses, dresseur, meteo, terrain })` ; le bouton COMBATTRE des dresseurs (dialogue) le fait déjà.

| Élément | Module | Rôle |
| :--- | :--- | :--- |
| Règles | `ReplicatedStorage.Combat.Regles` | Table des types (vérifiée case par case contre le vault), natures, paliers -6 / +6, critiques, statuts, météo, courbes d'XP, bonheur, et les formules provisoires (voir plus bas). |
| Moteur | `ReplicatedStorage.Combat.Moteur` | Un tour = ordre (priorité, vitesse, Chronologie Intemporelle), précision, dégâts, effets, fin de tour (poison, météo), K.O., remplacement, capture, fuite, XP, évolution. Renvoie une liste d'événements ; l'écran les joue. |
| Espèces de test | `ReplicatedStorage.Combat.Especes` | 7 espèces de la Tifalistre de test, stats de base inventées, attaques prises dans les 283 du vault selon le type. |
| Scène | `UI.CombatUI.Scene` | Arène (déborde au-delà de 16:9), portraits sur socles, cartes de PV, effets d'attaque (élan, projectile, anneau), chiffres de dégâts, flèches de stats, ouverture, Tiflask et capture, évolution. |
| Fenêtres | `UI.CombatUI.Panneaux` | Sac, équipe, surnom, fin de combat, nouvelle attaque, défaite. |

### Ce qui suit le vault
- Table des types, Réalité neutre, natures ±15 %, critique x1,5 et paliers 5 / 10 / 20 / 50 / 100 %, Ensorcelé = pas de critique, Peur = critique adverse +50 %.
- Statuts : Paralysie (vitesse / 2), Brûlure (physique / 2), Gel (magique / 2), Sommeil (pas de soutien), Empoisonnement (1/16 qui augmente de 1/16 chaque tour), Peur (DEF / 2), Ensorcelé (MAG DEF / 2), Étourdi (perd son tour s'il est plus lent).
- Météo : Pluie, Soleil Effervescent, Brouillard (adversaire caché), Tempête de sable, Tempête de neige, Chronologie Intemporelle (ordre inversé).
- Plus d'EM : Défaitisme. Bonheur : +10 au K.O. adverse, -20 au K.O., +5 par niveau, 50 à la capture. Pas de perte de TFD contre un sauvage. 1 chance sur 4 000 d'être brillant.

### ⚠️ Provisoire (à écrire dans le GDD)
- **Dégâts** : ((2 x niveau / 5 + 2) x puissance x A / D) / 50 + 2, puis multiplicateurs, tirage 85-100 %. Pas de bonus de même type.
- **Efficacité** : x2 / x0,5 / x0 (le vault ne chiffre pas).
- **Effet des paliers** : (2 + n) / 2 et 2 / (2 - n) ; précision et esquive (3 + n) / 3.
- **Effets des attaques** : déduits des descriptions par mots-clés (statut, montée / baisse de stats, soin, recul, priorité, critique). Chance de statut 30 % pour une attaque de dégâts. **Il faudrait une colonne « Effet » structurée dans `8. Attaques`.** Les attaques sans effet reconnu affichent « L'effet de cette attaque n'est pas encore programmé ».
- **Capture** : (1 - 2/3 x PV / PV max) x taux de l'espèce x Tiflask (écume x1,5 sur un type Eau) x 1,5 si statut ; 3 secousses.
- **XP** : base de l'espèce x niveau / 7, x1,5 contre un dresseur ; courbes en niveau³ (les totaux au niveau 100 sont ceux du vault).
- **Stats par niveau** : chaque stat grandit comme le niveau.
- **TFD** : victoire contre un dresseur = niveau max x 40 (x2 Gardien / Boss) ; défaite = niveau max de l'équipe x 30.
- **Fuite** : sûre si plus rapide, sinon chance qui augmente à chaque essai.

### Limites connues
- Prototype côté joueur, avec les données de test : le moteur passera côté serveur avec les vraies sauvegardes (anti-triche). Le filtre de modération des surnoms se fera alors côté serveur.
- Pas d'Infirmerie construite : après une défaite, retour au point d'apparition.
- Pas de stockage visible : un Tifazelt capturé avec une équipe pleine va dans `data.stockage`.
- Les dresseurs prennent leur équipe dans l'attribut `Equipe` du PNJ (« Ondine:30|Laineux:31 »), sinon 2 Tifazelts de test autour du niveau 30.

### 🧪 Tests faits en jeu (phase 3)
- 120 puis 150 combats simulés par le moteur seul : aucune boucle infinie, victoires, défaites, fuites, captures, remplacements.
- En Play, avec captures : ouverture sauvage, dresseur et Gardien ; HUD de combat ; choix d'attaque ; sac (médicaments, Tiflask) ; capture réussie + surnom + départ au stockage ; K.O. et remplacement forcé ; victoire contre un dresseur (+1 240 TFD, XP) ; montée de niveau avec nouvelle attaque (Croix De Feu) puis évolution (Pyrofennec en Pyrovulpe, nom de test) ; défaite contre un dresseur (-1 050 TFD, équipe soignée) ; Brouillard. 0 erreur de nos scripts.
- **Non vérifié :** vrais clics et manette (Studio ne simule pas les clics), échec de capture en image, combat lancé depuis un vrai PNJ dresseur (même fonction que le dialogue de test, mais pas cliqué).
- Commandes de test : `combat:sauvage|Ondine|30|Pluie`, `combat:dresseur`, `combat:gardien`, puis `t:choisir|attaquer`, `t:choisir|attaque|1`, `t:choisir|sac`, `t:tiflask|Tiflask simple`, `t:objet|Potion basique|2`, `t:repondre|valeur`, `t:pv|A|1`, `t:ko`.

## 🏘️ Phase 4 — bâtiments et services (20 oct. 2026)
On entre dans un service en parlant au PNJ du bâtiment : son dialogue propose le service (attribut `Service` du PNJ, et `Service2` pour un second choix). Le Pâturage s'ouvre avec l'invite « Gérer » posée sur un poteau du portail (pas de nouvelle pièce, pas de collision ajoutée).

| Service | Écran | Où, à Bourg-Azur | Contenu |
| :--- | :--- | :--- | :--- |
| Infirmerie | `Ecrans.Infirmerie` | Infirmière Tifazelt | 6 capsules ; SOIGNER rend PV, statuts et EM. Classe Infirmier : atelier des remèdes (une Potion basique par visite). |
| Magasin | `Ecrans.Magasin` | Léon, marchand (Bazar) | Onglets Acheter / Vendre, quantité, total. Revente à 50 %, objets clés invendables. |
| Restaurant | `Ecrans.Restaurant` | Lou, barista (Café des Embruns) | 3 repas qui soignent l'équipe, parfois un objet rare. Classe Cuisinier : recettes avec les ingrédients du sac, service en salle payé. |
| Guilde | `Ecrans.Guilde` | Réceptionniste | Missions par rang (ajoutées au journal des quêtes), échanges (phase 6), tableau des grades. |
| Investissement | `Ecrans.Investissement` | Réceptionniste (2e choix) ou bouton « Chantiers du bourg » de la Guilde | 3 chantiers, paliers et récompenses. |
| Pâturage | `Ecrans.Paturage` | Portail du Pâturage | Garde (déposer / prendre, l'équipe garde au moins 1 Tifazelt), soins de l'Éleveur, reproduction et œufs. |
| Sanctuaire | `Ecrans.Sanctuaire` | Pas encore construit : commande `service:Sanctuaire|3` | 8 Gardiens, DÉFIER lance un combat « gardien » ; victoire = cristal, grade recalculé, récompense en TFD. |

Données et règles : `UI.Services` (prix, catalogue, menu, recettes, missions, chantiers, Gardiens, grades). Nouvelles espèces de test pour les Gardiens dans `Combat.Especes` : Psychelle (Psy), Florelin (Plante), Braisillon (Feu), Givrelle (Glace).

### Ce qui suit le vault
- Infirmerie : PV, statuts et EM. Classe Infirmier : activité exclusive.
- Magasin : achat en TFD, revente ; objets clés impossibles à revendre.
- Restaurant : repas qui soignent et font trouver des objets rares ; classe Cuisinier : cuisine et service contre un salaire.
- Pâturage : garde ; Éleveur jusqu'à +100 de bonheur en une fois ; reproduction : genres opposés, au moins un type commun, parents déjà évolués ou sans évolution, pas de Légendaire, petit au niveau 1, espèce 50/50 ou celle du parent qui tient la Boîte de Chocolats, 2 % de talent caché, brillant 1 / 4 000 (x2 avec le Pendentif Brillant, x10 avec la Boîte à Bijoux), 75 de bonheur à l'éclosion.
- Sanctuaires : les 8 Gardiens et leurs types (13. Sanctuaire).
- Investissement : entreprise de travaux publics au nom à définir, paliers de récompenses.

### ⚠️ Provisoire / à trancher dans le GDD
- **Tous les chiffres** : prix, menu, recettes, salaire (250 TFD, 3 services par visite), missions et récompenses, chantiers et paliers, niveaux et équipes des Gardiens, temps d'éclosion (60 s).
- **Grades** : le vault dit « Bronze 0 à 2, Argent 2 à 4… », les bornes se chevauchent. Lecture retenue : Bronze 0-2, Argent 3-4, Or 5-6, Platine 7-8.
- **Guilde** : la Liste des écrans parle de récompenses en PC, mais `2. Economie` réserve les PC au PvP et aux Ruines de Combat. Les missions donnent donc des TFD pour l'instant.
- **Reproduction** : le genre n'existait pas encore dans les données (ajouté) ; le nouveau-né reprend les stats et 2 attaques du parent ; il n'y a pas de liste de talents cachés.
- Les missions acceptées vont dans le journal, mais leur suivi (compter les dresseurs battus…) n'est pas programmé.

### 🧪 Tests faits en jeu (phase 4)
- Infirmerie : soin de l'équipe (Florépine K.O. relevée, PV pleins). Magasin : achat de 3 Super potions (-1 800 TFD, sac 2 → 5), onglet Vendre. Restaurant : Grand plat (-900), cuisine d'une Galette (classe Cuisinier de test), un service (+250). Guilde : mission acceptée, onglet Grade. Investissement : 5 000 TFD dans le kiosque (palier 1). Pâturage : équipe pleine refusée, dépôt, reproduction Laineux + Galetin, éclosion d'un Laineux niveau 1. Sanctuaire : victoire contre Aria Titania, cristal Fée, grade Argent, +2 720 TFD. Dialogue de la réceptionniste : les choix MISSIONS / CHANTIERS DU BOURG / PLUS TARD s'affichent.
- 0 erreur de nos scripts.
- **Non vérifié :** les vrais clics (choix du dialogue, boutons, invite du Pâturage) — Studio ne simule pas les clics ni les invites.
- Commandes de test : `service:Infirmerie` (et Magasin, Restaurant, Guilde, Paturage, Sanctuaire|n, Investissement), `classe:Infirmier`, puis `t:soigner`, `t:choisir|Super potion`, `t:plus|2`, `t:agir`, `t:onglet|vendre`, `t:action|3`, `t:accepter|1`, `t:investir|1|5000`, `t:choisir|stock|1`, `t:action|deposer`, `t:action|parent|1`, `t:action|confier`, `t:avancer`, `t:action|eclore1`, `t:defier`, `t:continuer`.

## 🌅 Phase 5 — début de partie (20 oct. 2026)
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

### Ce qui suit le vault
- 3 classes principales et 3 secondaires avec leurs avantages (12. Joueur).
- Starters Feu, Eau, Plante ; formes finales Feu / Obscurité, Eau / Psy, Plante / Fée ; Zéphir prend celui qui a l'avantage (00. Définition, 6. Personnages).
- Le Professeur Arid remet le starter, des Tiflask et le Tifalistre ; Salle des Spécimens et plateau stérile (Val Palmeraie).
- Quête « L'Heure du Choix » : laboratoire, starter, Tifalistre, combat d'apprentissage. Départ dans la chambre ; Maman donne des TFD.

### ⚠️ Provisoire / à trancher dans le GDD
- **Noms des starters** : Pyrofennec, Aqualune, Florépine (repris de la Tifalistre de test, le vault dit `???`). Stats, courbe, niveau 5, attaques prises automatiquement.
- **Chiffres** : 3 000 TFD de Maman, 5 Tiflask simples.
- **Une classe principale + une secondaire** : le vault ne dit pas combien on en choisit ; repris de la carte de dresseur de test.
- **Apparence** : le vault ne la décrit pas. Avatar Roblox + couleur de dresseur en attendant.
- **Adversaire du combat d'apprentissage** : Zéphir (le vault dit seulement « combat d'apprentissage »).
- **Objectif après la quête** : « Vers la Route 2, sortir par la Porte du Sirocco » (déduit de la note Val Palmeraie).
- **Professeur Arid** : pas encore de PNJ dans le laboratoire ; il parle dans l'écran du starter.
- Le nom n'est pas encore passé au filtre de Roblox (à faire côté serveur avec la sauvegarde).
- « Continuer » reprend les données de test (pas de sauvegarde pour l'instant).

### 🧪 Tests faits en jeu (phase 5)
- Titre : décor de Bourg-Azur chargé, JOUER → CONTINUER / NOUVELLE PARTIE ; CONTINUER ramène le personnage à son point de départ, caméra normale.
- Création : nom trop long refusé (« 12 lettres au maximum »), « Élise » accepté, couleurs, avatar en pose de repos.
- Classe : Éleveur + Stratège, Infirmier + Chasseur de trésors, Cuisinier + Ingénieur, confirmation.
- Fin de création : chargement « Bourg-Azur », arrivée dans la chambre, 3 000 TFD, objectif L'Heure du Choix ; carte de dresseur à jour.
- Avec l'équipe vide : Menu, Carte de dresseur, Inventaire, Tifalistre, Quêtes, Livre, Infirmerie, Pâturage, Guilde, Restaurant, Sanctuaire s'ouvrent ; Équipe, Fiche et combat refusés avec un message.
- Starter : Pyrofennec → Zéphir prend Aqualune ; Florépine → Zéphir prend Pyrofennec ; Tifalistre et Tiflask reçus ; combat contre Zéphir gagné → « Quête terminée », objectif Vers la Route 2, +200 TFD ; le plateau dit ensuite que les Tiflasks ont trouvé leurs dresseurs.
- 0 erreur de nos scripts.
- **Non vérifié :** les vrais clics et la saisie au clavier dans la case du nom, la manette, l'invite « Examiner » du laboratoire (Studio ne simule pas les invites), la marche jusqu'au laboratoire.
- Commandes de test : `titre`, `t:jouer`, `t:continuer`, `t:nouvelle`, `t:nom|Élise`, `t:couleur|3`, `t:suivant`, `t:principale|1`, `t:secondaire|2`, `t:valider`, `valider`, `service:Starter`, `t:choisir|1`, `t:confirmer`, `t:combat`, `chargement:Val Palmeraie|Laboratoire Arid|8`.

Captures de cette phase : [[Historique des captures]] (section « Interface — phase 5 »).

