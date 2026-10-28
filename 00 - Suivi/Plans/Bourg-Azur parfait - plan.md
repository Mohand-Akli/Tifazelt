# Bourg-Azur parfait : audit et plan en étapes

Pour reprendre dans une nouvelle conversation, dire : « passons à l'étape N » (N = numéro ci-dessous). Claude lit ce fichier, annonce l'étape et le modèle conseillé, puis attend ton « oui ».

## Demande de Mohand (27 oct. 2026, nuit)
« Il y a beaucoup de problèmes à Bourg-Azur : des problèmes de texture, des chemins mal placés… Vérifie tout Bourg-Azur, que tout est bien mis. Carte blanche pour rajouter des trucs tant que c'est pertinent. C'est la première ville où arrive le joueur : il ne doit pas rester un seul problème. »

## Comment l'audit a été fait (28 oct. 2026)
- **Contrôles par les données**, sur toute la ville (`Workspace.Map.CityPlots.BourgAzur`, `Extensions.Bourg_*`, `Littoral_*`, `Zone1_PeripherieBourg`) et sur `Workspace.Interieurs` :
  - faces qui scintillent : deux faces dans le même plan et le même sens qui se recouvrent, en ne gardant que les zones réellement visibles ;
  - objets posés sur les chemins ;
  - murs qui coupent les chemins ;
  - bâtiments qui se chevauchent ;
  - objets qui flottent ou s'enfoncent (géométrie réelle des pièces) ;
  - pieds des PNJ par rapport au sol ;
  - textures des PNJ (toutes chargées).
- **Tour visuel** : vues du dessus de toute la ville, vues obliques et vues à hauteur de joueur.
- **Carte de la ville** tirée des données : matériau du terrain, chemins, bâtiments, clôtures, portes, PNJ (`2026-10-28_00h29_bourg-azur-carte-chemins.jpg`).
- Captures de l'audit : `10 - Captures/Images/2026-10-28_00h18` à `00h29` (section « Bourg-Azur — audit avant corrections » de l'historique).

## Problèmes trouvés

### A. Textures qui scintillent (« problèmes de texture »)
Deux pièces ont une face au même endroit : l'image tremble quand la caméra bouge.

Comptage du détecteur `11 - Développement/Outils du vault/Bourg-Azur - détecteurs.lua` (refait le 28 oct. 2026 après l'étape 1) :
- seules les zones visibles sont comptées : ni cachées par une autre pièce, ni sous le terrain ;
- seulement entre pièces d'aspect différent ;
- par prudence, deux pièces de même couleur mais d'une matière texturée (bois, métal, tissu, herbe) sont aussi comptées : leurs textures peuvent se décaler.

Le premier comptage de l'audit (357 et 243) ignorait le terrain et comptait les pièces identiques : il est remplacé par ces chiffres.

- **Extérieur : 802 paires.**

  | Zone | Paires | Dont même couleur (texture) |
  |---|---|---|
  | Magasin de vélos : jantes et paniers des vélos exposés. Ça vient du modèle de vélo `Joueur.Velos`, donc le vélo du joueur est touché aussi | 249 | 200 |
  | Rues : bordures et chaussées (Grand-Rue, Promenade, rue de la Mer) | 196 | 0 |
  | Maisons : murs et socles, encadrements, caisses, bougainvillées | 110 | 0 |
  | Plage : laisse de mer (algues, coquillages, sable humide) | 93 | 30 |
  | Périphérie : bancs | 59 | 15 |
  | Espaces publics : poteaux du Pâturage… | 24 | 2 |
  | Quartier agricole | 15 | 11 |
  | Mobilier urbain : panneaux | 15 | 13 |
  | Ruelles | 14 | 0 |
  | Décor : bancs | 12 | 12 |
  | Place centrale : dalles usées, étals | 11 | 3 |
  | Débarcadère | 3 | 1 |
  | Végétation | 1 | 0 |

- **Intérieurs : 181 paires**, dont 108 de même couleur.

  | Intérieur | Paires |
  |---|---|
  | Guilde | 67 |
  | Infirmerie | 34 |
  | Bazar | 32 |
  | Café | 19 |
  | Maison du joueur | 16 |
  | Fleuriste | 13 |

  Ce sont surtout des moulures, des plinthes, des cadres de fenêtres, des étagères, des tapis, des couronnes et des emblèmes.
- 4 plaques de sable humide sont au ras du terrain : elles scintillent avec le sable.
- 32 autres plaques sont enterrées : elles sont invisibles et sans danger, je n'y touche pas.

### B. Chemins mal placés
1. ~~**Arrivée de la Route 1** : le sentier contourne l'arche~~ : fausse alerte (vérifié à l'étape 5). L'arche est en biais et le sentier passe bien dessous : on arrive face à l'enseigne (capture `2026-10-28_04h38_bourg-azur-arrivee-par-l-arche`). La vue oblique de l'audit trompait.
2. ~~**Oliveraie**~~ : fausse alerte (vérifiée à l'étape 5). Le sentier passe entre la maison 112 et sa voisine, dans un passage que les toits cachaient sur la vue du dessus, et rejoint la Ronde au panneau. Les deux ouvertures du mur sont naturelles au sol (capture `04h40_bourg-azur-sentier-oliveraie`). Constat de l'audit :
   - le sentier qui sort de l'oliveraie (≈ 1955, 1441) part vers l'est et bute contre le coin d'une maison (≈ 1999, 1451) ;
   - il ne rejoint pas la Ronde, où se trouve le panneau « Oliveraie » (2016, 1488) ;
   - le mur est de l'oliveraie a deux trous, avec un morceau de mur isolé entre les deux. (Capture `00h22_bourg-azur-oliveraie-chemin`.)
3. **Rue des Jardins** (sud) : elle mène bien au portail du Pâturage, mais la clôture était décalée de 4 studs par rapport au portail, avec un piquet au milieu de l'entrée. **Corrigé à l'étape 5.**
4. **Placette nord** : sept sentiers en éventail vers les champs. Jugé à l'étape 5 depuis la placette : une esplanade de terre qui se divise vers les champs et le moulin, c'est naturel. Gardé.
5. ~~**Place centrale** : l'ardoise déborde~~ : fausse alerte (vérifiée à l'étape 5). Aucune case d'ardoise n'est visible ; elle est sous les disques du dallage.
6. **Raccords des rues** : vérifiés à l'étape 5. Le bout arrondi de la Grand-Rue a la largeur de la route et passe sous la place ; la marche de 0,23 vers le Belvédère est voulue (plateforme surélevée). Gardés.
7. **Trouvé à l'étape 5 — ruelles barrées** : dans les quatre ruelles (Figuiers, Bougainvillées, Impasse du Levant, Chemin des Pêcheurs), les 29 « raccords » étaient des disques de 7 studs dressés sur la tranche, des demi-disques solides de 3 studs en travers du passage. Les fontaines des quatre placettes étaient cassées de la même façon : perche à la place du dallage, bûche à la place de la vasque. Cause : le générateur `Passe3.Remplissage` tournait ses cylindres une fois de trop et inversait diamètre et hauteur. **Corrigé à l'étape 5**, dans le jeu et dans le générateur. C'est sans doute ce que Mohand avait vu comme « chemins mal placés ». L'audit l'avait manqué : ces pièces portent le nom « Raccord », que mes contrôles prenaient pour une surface de chemin.

### C. Objets mal posés
1. **Sur les chemins** :
   - ~~12 bancs posés sur la Promenade, en travers du passage~~ : fausse alerte (vérifié à l'étape 4). La promenade fait 14 de large ; chaque banc est au bord côté mer, tourné vers la mer, et laisse 9 studs de passage ;
   - 1 buisson au milieu de la rue des Jardins (2136, 1890) ;
   - 2 lampadaires sur la Ronde, en pleine chaussée : (1940, 1711) et (2281, 1810) ;
   - le panneau « Oliveraie » au milieu de la Ronde (2016, 1488) ;
   - 5 touffes d'herbe (« Prairie ») posées sur les chaussées.
2. **Laisse de mer de la plage du bourg** (trouvé à l'étape 2, capture `2026-10-28_01h34_bourg-azur-laisse-de-mer-sur-l-eau.jpg`) :
   - 156 plaques de sable humide, avec leurs algues, coquillages et bois flotté (`Extensions.Littoral_LaisseDeMer.CoteBourg`), sont posées à plat à une hauteur fixe ;
   - la plage est en pente : entre deux coins d'une même plaque, le sable varie de 1 à 4 studs ;
   - une partie flotte sur la mer au bord du rivage, une autre est à moitié enterrée ;
   - à reposer une par une sur le sable sec, dans la pente, ou à rapprocher du rivage ;
   - les mêmes plaques existent sur d'autres côtes hors du bourg (x ≈ 170 à 430, z ≈ 3 100 à 3 600 ; x ≈ -300 à -200, z ≈ 3 580) : hors chantier, à voir plus tard.
3. **Qui flottent** :
   - buisson à 6,1 studs du sol (2297, 1370) : son feuillage traverse aussi la porte d'une maison du Chemin des Pêcheurs ;
   - olivier millénaire à 2,4 studs du sol (1608, 1498) ;
   - barque du débarcadère à 2,2 studs au-dessus de l'eau (2646, 1927) ;
   - prairie à 0,8 (1869, 1377), panneau « Champ » à 0,4 (1998, 1809), olivier à 0,36 (1918, 1393), charrette à 0,5 près du moulin (2177, 1186).
4. **Enterrés** :
   - fleurs à 2,9 studs sous la roche (2043, 1005) ;
   - ~~lampadaires de la ruelle des Bougainvillées et de l'impasse du Levant, 2,1 studs dans le sol~~ : fausse alerte (vérifié à l'étape 4). Leur pied est au sol ; leur bras passe au-dessus d'un banc, que le rayon a pris pour le sol.
5. **Bâtiments** :
   - une table de pique-nique est posée sur le toit de la maison 085 (2016, 27, 1830) ;
   - ~~la maison 111 touche en biais l'angle de la maison du joueur~~ : fausse alerte (vérifié à l'étape 4). Elle est à 2,75 studs ; c'est la perspective de la capture `00h28` qui les montrait collées.
6. **PNJ** :
   - Romain, garde : pieds 0,6 stud dans le socle de l'arche ;
   - Zéphir : 0,6 stud au-dessus du sol ;
   - Victor et Kaël : 0,2 stud au-dessus du sol.
7. **Placettes au bout des ruelles** : vérifiées à l'étape 4. Chacune est au bout de sa ruelle (place d'arrivée avec fontaine, bancs, olivier) : rien n'est bloqué. La maison 3 de la ruelle des Bougainvillées, posée sur la fin de la ruelle, est traitée avec les chemins (étape 5).

### D. Visible depuis la ville
- **Étiquettes d'édition dans le ciel** : « PortSaphir (Ø 720) », « Cascade (Ø 680) », « RepaireGlacitech (Ø 680) »…
  - Ce sont 7 étiquettes du dossier `Workspace.Map.EditorLabels`, visibles en jeu jusqu'à 9 000 studs.
  - Le générateur les note : « supprimer ce dossier avant publication ». (Capture `00h25_bourg-azur-etiquettes-ciel`.)

### Écarté après vérification (pas des problèmes)
- **PNJ « gris » (Ayla)** : c'est un délai d'affichage des vêtements dans Studio. Elle s'affiche correctement après quelques secondes. Les 55 textures des 27 PNJ de la ville sont chargées.
- **Réverbères de la place centrale** : bien posés (fausse alerte due à leur boîte tournée).
- **Grande zone invisible `Zone_BourgAzur`** : sans collision, sans requête, sans contact.
- **Traînée de petits cubes près du soleil** : elle fait partie de l'image du ciel (`Ciel_Route1`), ce n'est pas un objet.
- **Chaussées principales** : aucune n'est coupée par un mur ou un bâtiment, et aucune grande rue ne finit dans le vide.

## Étapes

| # | Étape | Modèle conseillé | Statut |
|---|---|---|---|
| 1 | Étiquettes d'édition : déplacer `Workspace.Map.EditorLabels` dans `ServerStorage` (sauvegarde, plus visibles en jeu) ; créer le dossier de sauvegarde du chantier | Haiku | Fait le 28 oct. 2026 (vérifié dans Studio, voir journal) |
| 2 | Scintillements à l'extérieur (A) : écart de 0,02 à 0,05 stud sur la pièce de décor, ou bordures relevées de 0,04 ; vélos corrigés à la source (`Joueur.Velos`, jantes et panier), puis vitrine du magasin refaite (vérifier d'abord ce que reconstruit son générateur) ; sauvegarde des pièces touchées ; relancer le détecteur jusqu'à 0 paire visible | Sonnet | Fait le 28 oct. 2026 (vérifié par le détecteur, voir journal) |
| 3 | Scintillements dans les six intérieurs (A), même méthode ; contrôle des meubles qui flottent | Sonnet | Fait le 28 oct. 2026 (vérifié par le détecteur et à l'image, voir journal) |
| 4 | Objets mal posés (C) : bancs au bord de la Promenade côté mer, buisson, lampadaires, panneau, herbe hors des chaussées, laisse de mer reposée sur le sable de la plage, objets qui flottent ou s'enfoncent, table du toit, maison 111 écartée, PNJ remis au sol, placettes vérifiées | Sonnet | Fait le 28 oct. 2026 (vérifié par les détecteurs et à l'image, voir journal) |
| 5 | Chemins (B) : sauvegarde du terrain (`TerrainRegion`), entrée par l'arche, sentier de l'oliveraie jusqu'à la Ronde et mur avec une vraie ouverture, fin de la rue des Jardins, ardoise autour de la place, raccords ; éventail nord jugé en jeu | Opus | Fait le 28 oct. 2026 (vérifié à l'image et par les détecteurs, voir journal) |
| 6 | Ajouts pertinents (carte blanche, PROVISOIRES) : 2 ou 3 descentes vers la plage depuis la Promenade (aujourd'hui le seul accès est le ponton) et bancs face à la mer ; autres idées proposées avant d'être faites | Opus | À faire |
| 7 | Contrôle final : tous les détecteurs relancés, captures avant/après, tour en Play (Route 1 → arche → Grand-Rue → place → maison du joueur → Promenade → plage et ponton → potager et Pâturage), liste de vérifications pour Mohand, vault, audit, Ctrl+S | Sonnet | À faire |

## Règles du chantier
- **Sauvegarde avant chaque modification** : copie des pièces touchées dans `ServerStorage.BourgAzur_Sauvegarde_Parfait.<étape>` ; copie du terrain dans un `TerrainRegion` avant de repeindre.
- **Corrections à la main, pièce par pièce.** Aucun générateur relancé (les générateurs effaceraient les corrections passées). Aucune fonction qui écrit le terrain. Jamais `BourgAzur B.Coast`.
- **La ville ne bouge pas.** Seuls quelques objets de décor sont déplacés de quelques studs.
- **Val Palmeraie** est hors du chantier (gelé).
- Chaque correction est vérifiée par un détecteur relancé. Tout ce qui n'a été vu que par les données est marqué « non vérifié en jeu ».

## Questions pour Mohand (n'empêchent pas de commencer)
- ~~Étiquettes d'édition : `ServerStorage` ou cachées en jeu ?~~ Réponse de Mohand (28 oct. 2026) : les ranger dans `ServerStorage`. Fait à l'étape 1.
- Le ciel `Ciel_Route1` montre une traînée de cubes près du soleil peint. On le garde ?

## Journal
- 28 oct. 2026 (nuit) : audit fait (avec Opus) ; problèmes et plan ci-dessus. Rien n'a encore été modifié dans Studio (seuls des essais d'affichage sur Ayla, remis à l'identique).
- 28 oct. 2026 (nuit) : **étape 1 faite** (Mohand : « range les étiquettes d'édition dans ServerStorage » ; fait avec Opus).
  - **Avant** : seuls les générateurs de carte nomment ces étiquettes (`MapGeneration.LumeridiaEst.Builder`, `BourgAzur.Builder`, `Route1.Passe5.Collines`, `Extensions.Relief`), toujours avec une vérification de présence. Aucun script du jeu ne s'en sert. Les autres textes affichés dans le monde sont de vrais panneaux et enseignes : rien d'autre à retirer.
  - **Fait** : création de `ServerStorage.BourgAzur_Sauvegarde_Parfait`, le dossier des sauvegardes du chantier. `Workspace.Map.EditorLabels` (7 étiquettes : Cascade, CiteOcre, HameauDore, PortSaphir, PresquileMarine, RepaireGlacitech, ValPalmeraie) est déplacé dans `BourgAzur_Sauvegarde_Parfait.Etape1_EtiquettesEdition`, avec l'attribut `Origine = Workspace.Map`. C'est une seule étape d'annulation dans Studio (Ctrl+Z possible). Pour les revoir dans Studio : glisser `EditorLabels` dans `Workspace.Map`.
  - **Vérifié** dans Studio, par les données et par l'image :
    - plus de dossier `EditorLabels` dans le Workspace ;
    - aucune étiquette « Ø » restante ;
    - les 7 étiquettes sont présentes dans la sauvegarde ;
    - le ciel est dégagé depuis la placette nord (capture `2026-10-28_01h14_bourg-azur-ciel-sans-etiquettes.jpg`, même vue que `00h25_bourg-azur-etiquettes-ciel`).
  - **Pas de Play lancé** : en jeu, le contenu de `ServerStorage` n'est jamais envoyé aux joueurs.
- 28 oct. 2026 (nuit) : **détecteurs enregistrés** dans `11 - Développement/Outils du vault/Bourg-Azur - détecteurs.lua`. On colle le fichier tel quel dans `execute_luau` (contexte Edit). Il définit `_G.BA_Detecteurs`, puis lance quatre contrôles : scintillements dehors et dedans, objets sur les chemins, objets qui flottent, PNJ au sol.
  - Le fichier a été lancé dans Studio et fonctionne.
  - En le préparant, j'ai rendu le test des scintillements plus juste : le terrain cache désormais les faces posées dessus, et deux pièces identiques ne comptent plus.
  - Nouveaux chiffres de départ : **802** paires dehors et **181** dedans (section A) ; 48 objets sur les chemins. Ce sont ceux de la section C (bancs, buisson, lampadaires, panneau, herbe), la maison 3 de la ruelle des Bougainvillées et une placette du Chemin des Pêcheurs à regarder, plus les raccords de l'entrée et les accessoires du débarcadère (planches, caisses, tonneaux, cordages, filet), qui sont voulus ; 8 objets qui flottent ou s'enfoncent ; 5 PNJ mal posés.
- 28 oct. 2026 (nuit) : **étape 2 faite** (Mohand : « fais l'étape 2 » ; fait avec Opus). Dehors, plus aucune face visible ne se superpose à une autre : **802 → 0 paire**.
  - **Sauvegardes** (`ServerStorage.BourgAzur_Sauvegarde_Parfait.Etape2_Scintillements`) : module `Velos_avant_etape2`, générateur `MagasinVelos_generateur_avant_etape2`, magasin `MagasinVelos_modele_avant_etape2`. Sur la copie, les tags de Gilles sont retirés pour qu'aucun script ne la prenne pour un PNJ ; ils sont notés dans l'attribut `Tags_avant`. Chaque étape de modification est aussi une étape d'annulation de Studio.
  - **Vélos, corrigés à la source** (`ReplicatedStorage.Joueur.Velos`) : 235 superpositions sur les 5 vélos d'essai, dans les jantes, le panier, la selle de course, la manivelle et le catadioptre.
    - Jantes : segments à largeur alternée (+0,03).
    - Panier : chaque plaque dans son propre plan.
    - Selle de course : pièce arrière plus épaisse (0,15) et 0,01 plus en arrière.
    - Manivelles : 0,11 d'épaisseur au lieu de 0,09.
    - Catadioptre arrière : décollé de 0,02.
    - Résultat : 0 paire sur les 5 vélos. La soudure du vélo du joueur fonctionne. Le vélo du joueur est fabriqué à chaque partie à partir de ce module.
  - **Magasin de vélos** :
    - **Contrôle préalable** : le générateur, relancé tel quel, redonne exactement le magasin en place (73 pièces hors vélos identiques, Gilles identique). Aucune retouche manuelle n'est perdue.
    - **Corrections du générateur** (`MapGeneration.BourgAzur.MagasinVelos`) :
      - sol, mur du fond et linteau aux bonnes longueurs ;
      - piliers et soubassements qui dépassent légèrement du mur ;
      - vitre plus épaisse que le mur, de part et d'autre ;
      - volets posés à l'extérieur du mur (ils le traversaient) ;
      - le générateur charge maintenant une copie fraîche du module des vélos. Dans Studio, `require` garde l'ancienne version en mémoire : le premier essai avait refait la vitrine avec l'ancien vélo.
    - **Résultat** : magasin reconstruit, 1 178 pièces comme avant, 0 paire, Gilles tagué `PNJ_Bourg`. Capture `2026-10-28_01h37_bourg-azur-magasin-velos-sans-scintillement.jpg`.
  - **Le reste de la ville** (`D.corrigerScintillements`, ajouté au fichier des détecteurs) : 6 passes, 553 → 8 paires.
    - Pour chaque paire, la pièce dont la face commune est la plus petite avance de 0,04 stud vers l'extérieur. 515 pièces ont bougé, la plupart de 0,04 et quelques-unes jusqu'à 0,12 (déplacées plusieurs fois).
    - Pièces les plus touchées : bordures de rue 194, algues 64, assises de bancs 38, pièces de maisons 36, poteaux 21, bougainvillées 19, socles 15, panneaux 14, dossiers 13, coquillages 13, encadrements 12.
    - Chaque pièce déplacée porte l'attribut `Etape2_Decalage` (Vector3). Pour annuler : `p.CFrame -= p:GetAttribute("Etape2_Decalage")`.
  - **Les 8 dernières paires** : des algues posées sur des plaques de sable humide, sur lesquelles la correction automatique oscillait. 6 algues ont été étagées à la main (+0,02, +0,04).
  - **Coïncidence avec le terrain** (le détecteur ne la voit pas) : contrôle à part de toutes les pièces plates de la ville. La nappe du pique-nique du Pré du Dimanche (4 carreaux) est remontée de 0,04. Hors chantier et non corrigé : une planche d'épave de la Crique secrète, à (1023 ; 0,75 ; 2752).
  - **Pièces « sensibles » déplacées** : 4 portes de décor de maisons, sans invite ni tag, et la plateforme du bout du ponton (+0,04, avec son invite « Pêcher »). Aucune porte magique, aucun déclencheur, aucun siège ni aucun PNJ n'a bougé.
  - **Trouvé en route** :
    - la laisse de mer flotte sur la mer : ajoutée à la section C et à l'étape 4 ;
    - les anciennes sauvegardes d'intérieurs (`ServerStorage.Sauvegardes_Interieurs.*_avant`) gardent 6 PNJ et 6 déclencheurs de porte tagués. C'est sans danger : les portes ne cherchent leurs destinations que dans le Workspace, et les scripts des PNJ tournent côté joueur.
  - **Vérifié** : détecteurs relancés (0 scintillement dehors, 8 objets qui flottent et 5 PNJ mal posés, comme avant) ; magasin regardé à l'œil.
  - **Non vérifié en jeu** : le vélo du joueur et ses nouvelles pièces en roulant (pas de Play lancé), et le rendu à l'écran de toutes les corrections de 0,04, trop fines pour se voir sur une capture.
- 28 oct. 2026 (nuit) : **étape 3 faite** (Mohand : « fais l'étape 3 » ; fait avec Opus). Dans les six intérieurs, plus aucune face visible ne se superpose : **181 → 0 paire**.
  - **Correction automatique** (`D.corrigerScintillements`, attribut `Etape3_Decalage`) : 159 pièces ont avancé de 0,04 à 0,16 stud. Ce sont surtout des couronnes et des bras de l'emblème de la Guilde, des étagères du Bazar, des nervures de l'Infirmerie, des chaises du Café, des rideaux et des cadres. Aucun mur n'a bougé : seul le cadre de la porte de la maison du joueur touchait la structure, et c'est le cadre qui a avancé. Une liaison avec Studio a été perdue pendant la correction : j'ai vérifié l'état réel (pièces marquées) avant de continuer, sans relancer à l'aveugle.
  - **Traverses de 12 chaises** (Café et Guilde) : leur face avant était à 0,01 de celle du dossier, et la correction automatique les faisait osciller. Elles sont épaissies de 0,26 à 0,30, sans être déplacées ; la taille d'origine est notée dans `Etape3_TailleAvant`.
  - **Meubles mal posés**, contrôlés sur les 122 meubles et objets des intérieurs :
    - **étagère du fond du Bazar** : elle flottait à 0,5 stud du sol ; descendue de 0,50 avec ses 126 pièces ;
    - **tableau « Avis de missions » de la Guilde** : son titre entrait de 0,44 dans la fenêtre au-dessus ; descendu de 0,50, sans le pupitre.
    - Les 46 autres objets « pas posés » sont voulus : fenêtres, suspensions, lustres, coupole, portes, coques.
    - Les 6 PNJ des intérieurs ont les pieds au sol.
  - **Guilde, trouvé à l'image** (aucun détecteur ne le voyait) : les piliers du colombage, espacés de 7, ne suivaient pas les fenêtres, espacées de 12. Ils coupaient les trois fenêtres de chaque mur long, le tableau d'avis, l'enseigne « Coin échanges » et la vitrine « Palmarès ».
    - **Piliers des deux murs** : ils sont maintenant à z = 1206 (sous le corbeau), 1214, 1227,2 et 1239,5. Le pilier du milieu (z = 1221) est retiré des deux côtés et sauvegardé dans `ServerStorage.BourgAzur_Sauvegarde_Parfait.Etape3_Interieurs`.
    - **Le reste** : tableau et pupitre recentrés sous la fenêtre du milieu (+2) ; une plante décalée de 0,3 ; 2 coins du cadre du tableau, que le pilier ne cachait plus, corrigés.
    - **Contrôle** : aucun pilier ne traverse plus de fenêtre, de panneau ni de meuble. Captures `2026-10-28_02h25_guilde-piliers-devant-tableau` (avant), `02h29_guilde-mur-tableau-corrige` et `02h29_guilde-mur-trophees-corrige` (après).
  - **Tour visuel des cinq autres intérieurs** (maison du joueur, Café, Fleuriste, Bazar, Infirmerie) : aucun défaut. Une première vue très sombre de la maison du joueur venait du délai de calcul de la lumière : elle est claire après 3 secondes. Les six intérieurs ont des éclairages comparables. Capture `02h31_bazar-etagere-au-sol`.
  - **Non vérifié en jeu** : pas de Play lancé. Les décalages de 0,04 sont trop fins pour se juger sur une capture.
- 28 oct. 2026 (nuit) : **étape 4 faite** (Mohand : « fais l'étape 4 » ; fait avec Opus). Sauvegardes dans `ServerStorage.BourgAzur_Sauvegarde_Parfait.Etape4_ObjetsMalPoses` (objets retirés, avec l'attribut `Origine`). Chaque objet déplacé garde sa position d'origine dans `Etape4_PivotAvant` (modèle) ou `Etape4_CFrameAvant` (pièce).
  - **Chaussées dégagées** :
    - 2 lampadaires en double retirés : l'un était au milieu de la Ronde, à 4,9 studs d'un lampadaire bien placé ; l'autre à 3,7 studs d'un voisin, le bras tourné vers l'extérieur.
    - Le lampadaire seul dans la Ronde (2283, 1811) est ramené au bord, comme les autres (6,1 studs de l'axe), le bras vers la route, le pied sur le terrain.
    - Écartés de la chaussée et posés au sol : le buisson de la rue des Jardins, le panneau « Oliveraie » (il sera réajusté avec le sentier de l'oliveraie à l'étape 5), 5 touffes d'herbe (Ronde, rue des Jardins, allée du jardin des Orangers).
  - **Laisse de mer de la plage du bourg** (`Littoral_LaisseDeMer.CoteBourg`, 983 objets) :
    - **205 pièces plates** (sable humide, lignes de marée) inclinées selon la pente du sable mesurée sous chacune (plan sur 9 points), leur dessus posé juste au-dessus du sable. 114 d'entre elles, à cheval sur le rivage où le fond plonge à -30, ont d'abord été remontées sur le sable sec (3,6 studs en moyenne).
    - **742 petits objets** (algues, coquillages, branches, bois flotté) reposés sur la surface ; 23 ramenés du bord de l'eau sur le sable sec.
    - **Rochers** laissés tels quels (enfoncés, c'est voulu). Aucun objet retiré.
    - **37 superpositions recréées** par les reposes, corrigées : 0.
    - Captures `2026-10-28_03h24_bourg-azur-laisse-de-mer-reposee` (même vue que l'« avant » `01h34`).
  - **Objets qui flottaient, remis au sol** :
    - la barque du débarcadère trempe maintenant de 0,3 dans l'eau (elle était 2,2 au-dessus), son amarre est réorientée vers le ponton (capture `03h32_bourg-azur-barque-dans-l-eau`) ;
    - l'olivier millénaire (2,4), une prairie (0,8), la charrette à la roue cassée, les panneaux « Champ » et de rue, la moustache secrète, un olivier, un buisson, un cyprès, des fleurs ;
    - sur la place centrale, 9 pots de fleurs, 4 réverbères et 7 pigeons (tous 0,2 à 0,25 au-dessus du dallage) ;
    - deux tables de la terrasse du café.
  - **Retiré** : une boule de feuillage sans tronc qui flottait à 6 studs devant la porte d'une maison du Chemin des Pêcheurs.
  - **Décalé** : une bitte d'amarrage du débarcadère, traversée par deux caisses (2,6 studs).
  - **Table de pique-nique** : elle était sur le toit de la maison 085 ; posée sur la pelouse en (2021,7 ; 1873,1), à l'ombre d'un arbre (capture `03h32_bourg-azur-table-pique-nique-au-sol`).
  - **PNJ remis au sol** :
    - Romain, garde : sorti du socle du pilier de l'arche ;
    - Zéphir : descendu de 0,62 ;
    - Victor et Kaël : descendus de 0,2 ;
    - Ernest, ancien guetteur du sémaphore : remonté de 0,57, ses pieds étaient dans la plateforme.
  - **Fausses alertes de l'audit** : les 12 bancs, la maison 111, les lampadaires « enterrés » des ruelles, les placettes (section C corrigée). Fleurs du nord (2043, 1005) entièrement enfouies dans un rocher : invisibles, laissées.
  - **Erreur rattrapée en route** : la recherche du sol par rayon traverse les pièces `CanQuery = false`. Romain avait d'abord été enfoncé de 0,6 dans le pavé de l'entrée. J'ai ajouté au fichier des détecteurs une recherche du sol réel (`D.solSous`, section 6), qui tient compte de toutes les pièces et des disques de la place. Tous les objets déplacés et tous les PNJ ont été revérifiés avec elle : bien posés.
  - **Vérifié** : 0 scintillement dans la ville après l'étape ; il reste 40 objets sur des chemins, tous voulus (bancs, accessoires du ponton, raccords, placette) plus la maison de la ruelle (étape 5).
  - **Non vérifié en jeu** : pas de Play lancé.
- 28 oct. 2026 (nuit) : **étape 5 faite** (Mohand : « fais l'étape 5 » ; fait avec Opus). Studio a été relancé pendant l'étape. Toutes les corrections des étapes 1 à 4 étaient bien enregistrées ; seuls les détecteurs gardés en mémoire ont été rechargés, depuis le fichier. Sauvegardes dans `ServerStorage.BourgAzur_Sauvegarde_Parfait.Etape5_Chemins` : générateurs `Remplissage_avant_etape5` et `Deco_avant_etape5`, piquets retirés. Les pièces modifiées gardent `Etape5_CFrameAvant` et `Etape5_TailleAvant`. **Aucun terrain modifié**, donc pas de `TerrainRegion` nécessaire.
  - **Vérifié au sol, pas de défaut** : l'arrivée par l'arche, le sentier de l'oliveraie, la maison 3 de la ruelle des Bougainvillées (elle donne sur la ruelle : perron, jardinières et boîte aux lettres empiètent d'1 à 1,6 stud), l'ardoise de la place, les raccords de la Grand-Rue et du Belvédère, l'éventail nord.
  - **Ruelles et placettes** (défaut principal de l'étape) :
    - 29 raccords couchés, dessus 0,02 au-dessus des dalles ;
    - fontaines des 4 placettes refaites avec les tailles voulues : dallage rond de 18, vasque de 6, eau de 4,8, colonne de 0,9 sur 3,2 ;
    - générateur `MapGeneration.BourgAzur.Passe3.Remplissage` corrigé (rotation en trop retirée, paramètres remis dans l'ordre diamètre puis hauteur) : il redonnerait la même chose.
    - Captures `04h44_bourg-azur-ruelle-demi-disques` (avant), `04h46_bourg-azur-ruelle-a-plat` et `04h46_bourg-azur-placette-fontaine` (après).
  - **Même erreur ailleurs** : les 3 assiettes du pique-nique du Pré du Dimanche étaient sur la tranche ; couchées, et générateur `Extensions.Deco` corrigé. Une recherche dans toute la ville n'a trouvé aucune autre pièce dressée ou couchée par erreur. Les autres disques debout sont des oculus de façade et l'emblème de l'Infirmerie, voulus.
  - **Portail du Pâturage** : 2 piquets retirés, l'un au milieu de l'entrée ; les lisses ouest prolongées jusqu'au poteau, les lisses est raccourcies (captures `04h40_bourg-azur-portail-paturage-avant` et `04h50_..._apres`).
  - **Dernière superposition corrigée** : une perche de clôture en zigzag sur un piquet, au quartier agricole.
  - **Contrôles** :
    - toutes les surfaces de chemin sont à plat (aucune plus haute que 1,6 stud, hors un repère de navigation invisible) ;
    - 0 scintillement dans la ville ;
    - 40 objets sur des chemins, tous voulus ;
    - les 13 repères de navigation sont invisibles et sans collision.
  - **Fichier des détecteurs** : nouvelle option `_G.BA_ChargerSeulement = true` (charger sans tout lancer, pour ne pas dépasser le délai de Studio).
  - **Non vérifié en jeu** : pas de Play lancé (marcher dans les ruelles et passer le portail).
