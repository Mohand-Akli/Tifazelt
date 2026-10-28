# Vêtements des PNJ, corrections et suite (passation Cowork → Claude Code, 26 oct. 2026)

> *Rangement (28 oct. 2026) : plan terminé, rangé dans `Claude outputs/Passation Cowork/Terminés/`. Ce qui reste ouvert est suivi dans [[À décider et à faire]]. Le dossier `Roblox_Textures/` cité plus bas est devenu `Claude outputs/Textures Roblox/`.*

## Plan de Mohand (validé le 26 oct. 2026)
1. **Vérifier ce qui a survécu.** Je contrôle par les données, sans rien écrire :
   - l'attribut `Y_avant_correction` sur les 11 PNJ remontés ;
   - les 68 invites « Parler » (AlwaysShow, sans ligne de vue requise) ;
   - les 160 invites « S'asseoir » (F, ButtonY, OnePerButton) ;
   - `Garderobe_Classique.Cheveux` (16 accessoires) ;
   - la sauvegarde `Sauvegardes_PNJ`.
   Modèle conseillé : Haiku (lecture et listes).
2. **Refaire ce qui a été perdu.** Je rejoue les correctifs manquants, avec sauvegarde avant toute suppression. Modèle conseillé : Sonnet (modifications dans Studio).
3. **Concevoir l'habillage des 68 PNJ.** Je définis la table rôle → Haut, Bas, Visage, Coiffure, avec les règles de la passation. Les IDs H29 et B22 sont introuvables : je les évite ou je les signale. Modèle conseillé : Opus (conception du choix par rôle et de la variété).
4. **Appliquer l'habillage.** Je sauvegarde les anciens cheveux, puis j'applique les IDs choisis et j'écris les attributs `Haut`, `Bas`, `Visage`, `Coiffure`. Modèle conseillé : Haiku (liste d'IDs déjà décidée).
5. **Concevoir le starter à Bourg-Azur** (PROVISOIRE). J'étudie d'abord comment l'équipe est stockée (`DonneesTest`, `NouvellePartie`), puis je conçois l'interaction : Pyrofennec, Aqualune, Florépine au niveau 5, et le rival Zéphir qui prend le starter avantagé. Modèle conseillé : Opus (nouveau système).
6. **Implémenter le starter.** Modèle conseillé : Sonnet.
7. **Tests.** Je fais les vérifications par les données, puis je regroupe les tests en Play à te demander (habillage visuel, interaction « Parler » et « S'asseoir », starter), avec captures dans `GDD/08_Captures`. Modèle conseillé : Sonnet.
8. **Mise à jour du vault.** Je mets à jour les notes, dont « À décider et à faire » (PROVISOIRE : starter à Bourg-Azur, H29 et B22), je lance l'audit et je te rappelle de faire Ctrl+S. Modèle conseillé : Haiku.

## Où on en est (26 oct. 2026)
- **Étape 1 : faite**, lecture seule dans Studio. Tout a survécu : `Y_avant_correction` sur les 11 PNJ ; 160 invites « S'asseoir » (F, ButtonY, OnePerButton) ; 16 accessoires dans `Garderobe_Classique.Cheveux` ; `Sauvegardes_PNJ` présent (76 éléments, contenu non inspecté).
- Invites « Parler » : **69**, toutes AlwaysShow et sans ligne de vue. La passation disait 68 ; la 69e est probablement le Professeur Arid (étape 3 faite). À confirmer.
- L'attribut `Haut` est déjà présent sur **69 modèles** : l'habillage est en place.
- **Étape 2 : rien à rejouer** (aucune perte constatée). Non faite.
- **Étape 3 : bloquée** par une décision de Mohand : garder l'habillage actuel, ou le refaire. Si on le refait, la table n'existe pas encore.
- Étapes 4 à 8 : en attente.

## 1. Vérifier d'abord ce qui a survécu
La dernière session s'est coupée (Studio déconnecté). Ces changements ont été faits en Edit et sont **perdus si la place n'a pas été sauvegardée** :
- 11 PNJ enterrés remontés au niveau du terrain (attribut `Y_avant_correction` sur chacun) : Léonie, Tom, Hélène, Firmin, Nina, Sorlin, Rosa (marchande de glaces), Ysaline, Professeure Anir, Odette, Aurèle. Méthode : rayon vers le bas depuis +80 (RespectCanCollide, PNJ exclus), décalage = sol − bas de la jambe.
- Les 68 invites « Parler » : `Exclusivity = AlwaysShow`, `RequiresLineOfSight = false`.
- Les 160 invites « S'asseoir » : touche F, manette ButtonY, `OnePerButton` (avant, les tabourets du Café masquaient « Parler » de la barista). Générateurs modifiés pareil : `BourgAzur.Passe2`, `Route1.Passe5.Commun`, `BourgAzur.Passe3_Interieurs.Kit`.
- Dossier `ServerStorage.Garderobe_Classique.Cheveux` : 16 accessoires de cheveux faits par Roblox (attribut `AssetId`) : 63690008, 376548738, 451220849, 451221329, 62234425, 13477818, 62743701, 32278814, 80922374, 20573078, 323476364, 16630147, 62724852, 26658141, 12270248, 376524487.
- Ancienne garde-robe en pièces abandonnée, rangée dans `ServerStorage.Sauvegardes_PNJ.PNJ_Garderobe_Pieces_abandonne` ; Margot restaurée.
- Comptoirs mesurés : joueur à 5–6 studs des PNJ de comptoir (portée 9) → OK.

## 2. Habiller les 68 PNJ (à faire)
Textures source : `Roblox_Textures/Vetements_PNJ/` (Hauts, Bas, Visages + aperçus ; générateur Python dans `generateur/`).
Appliquer : `Shirt.ShirtTemplate` / `Pants.PantsTemplate` = `rbxassetid://<id>` ; visage = Decal `face` de la tête (Texture) ; cheveux = clone d'un accessoire de `Garderobe_Classique.Cheveux`. Retirer d'abord les anciens Accessory de cheveux (sauvegarder), garder la couleur de peau (BodyColors). Choisir par rôle (garde → H24+B09, infirmière → H25+B10, pêcheur → H20/H21+B23, boulangère → H22, jardinier → H23+B28, Guilde → H27+B08, archéologue → H26, Val Palmeraie → H28+B26, enfants → shorts/V22/V23, anciens → V19/V20/V21…), varier les autres, stocker les choix en attributs `Haut`, `Bas`, `Visage`, `Coiffure`.

ID des images :
- **Hauts** : H01 72863023580625 (T-shirt blanc), H02 81112321799052 (T-shirt azur à vague), H03 78764599213935 (raglan), H04 101861924969677 (T-shirt jaune soleil), H05 86518514448141 (débardeur vert), H06 117735281217490 (marinière), H07 70397227358313 (polo corail), H08 87033684675289 (chemise blanche), H09 74255954196541 (chemise à carreaux), H10 136029870975278 (chemise en jean), H11 124672004913636 (chemise hawaïenne), H12 100973486019051 (pull bordeaux), H13 124088420425393 (pull torsadé), H14 125888357138847 (cardigan), H15 119223121978417 (sweat à capuche), H16 124254096479649 (veste zippée azur), H17 126990513806062 (veste en jean), H18 119042952842929 (blouson noir), H19 102229264331301 (gilet de marchand), H20 119447961617976 (ciré jaune), H21 79397072058131 (veste de pêche), H22 110992828078833 (tablier de boulangère), H23 131516676648123 (tablier de jardinier), H24 113293390253786 (uniforme de garde), H25 70636899964721 (tunique d'infirmière), H26 133011804502535 (blouse de labo), H27 93618630400527 (veston de la Guilde), H28 117433356437472 (tunique brodée), H29 introuvable (à réimporter), H30 106384138019698 (blouse rose à pois).
- **Bas** : B01 113714700186995 (jean bleu), B02 105546223543018 (jean délavé), B03 128891428526716 (jean noir), B04 120017115223499 (chino), B05 104109868936899 (cargo kaki), B06 73455371638851 (jogging gris), B07 91072229784270 (survêtement), B08 76407919073277 (costume), B09 78042426282204 (uniforme), B10 104310535144498 (blanc), B11 77517389519606 (velours), B12 117832117427837 (travail), B13 73468576150028 (short jean), B14 116335954366622 (short cargo), B15 138639692401685 (short de plage), B16 123087106273050 (bermuda), B17 134580493637136 (pantacourt), B18 76815966072783 (jupe plissée), B19 119353007819333 (jupe terracotta), B20 72490843115158 (jupe longue fleurie), B21 130310467332081 (jupe en jean), B22 introuvable (à réimporter), B23 91520240799743 (ciré de pêche + bottes), B24 119044882559917 (carreaux), B25 87531215912466 (legging), B26 131929483557170 (sarouel), B27 110130845965537 (brique), B28 105017051667008 (jardinier), B29 109428689383898 (jupe longue grise), B30 82811031163128 (short rouge + chaussettes).
- **Visages** : V01 107110065772650, V02 131381226937863, V03 123285073219588, V04 120179816206383, V05 114684717604999, V06 121528492686938, V07 111245846992363, V08 83075624409709, V09 78478559337016, V10 86593856406396, V11 91501894620464, V12 134780126507455, V13 89156224820583, V14 77546636553192, V15 73351961896797, V16 130794881868550, V17 111414598869761, V18 71152692601769, V19 81124881744088, V20 126988917796776, V21 87697286000225, V22 137946979361521, V23 79495086835546, V24 117340912766139 (noms : voir `apercu_visages.jpg`).

## 3. Starter à Bourg-Azur (à faire, PROVISOIRE)
Le vault place le choix du starter au **Laboratoire Arid de Val Palmeraie** ; Mohand demande une interaction à Bourg-Azur (aussi pour les tests). Starters provisoires : Pyrofennec (Feu), Aqualune (Eau), Florépine (Plante), niveau 5. Le rival Zéphir prend le starter avantagé. Vérifier d'abord comment l'équipe est stockée (`DonneesTest`, `NouvellePartie`).

## 4. Autres chantiers récents (déjà faits et testés en Play le 20 oct.)
Course (16→26), vélo (38, objet clé « Vélo » PROVISOIRE donné par Maman), pack d'animations Cartoony, gestes des PNJ par type, musiques par zone et combat, sons d'UI et voix de dialogue. Détails : [[Animations, déplacements et audio]] et [[À décider et à faire]].

## Étape 2 faite le 26 oct. 2026 (Claude Code) : habillage des 68 PNJ
- Appliqué sur les 68 PNJ du Workspace (hors copies de `ServerStorage`) : `Shirt`, `Pants`, Decal `face` de la tête, un seul accessoire de cheveux cloné depuis `Garderobe_Classique.Cheveux`. Choix par rôle (garde, infirmière, pêcheurs, boulangère, jardinier, Guilde, archéologue, anciens, enfants…), le reste varié par une rotation.
- Attributs sur chaque PNJ : `Haut`, `Bas`, `Visage`, `Coiffure` (AssetId du cheveu).
- Sauvegarde : `ServerStorage.Sauvegardes_PNJ.Cheveux_avant_habillage` (un dossier par PNJ : anciens accessoires + attribut `Visage_avant`). Tous les anciens accessoires (cheveux, Hat1, Bandana, Robloxclassicred) ont été retirés, pas seulement les cheveux.
- Vérifié par les données : 68/68 avec un seul accessoire soudé à la tête, Shirt, Pants, visage et attributs.
- **Non vérifié** : rendu réel (les textures sont-elles bien reconnues comme Shirt/Pants ? cheveux qui traversent la tête ou le col ?), à voir en Play.
- PROVISOIRE : Val Palmeraie (H28+B26) seulement sur Sorlin ; sexe de certains PNJ déduit du prénom ; H29 et B22 introuvables, non utilisés.

## Étape 3 faite le 26 oct. 2026 (Claude Code) : starter à Bourg-Azur
- **Val Palmeraie gelé** (décision de Mohand) : plus aucun développement là-bas.
- Nouveau PNJ `Workspace.Map.Starter_BourgAzur.Professeur Arid Acanthus` (clone de Victor, scripts retirés) devant la porte de la maison familiale (2132, 5, 1498), tourné vers la porte. Tag `PNJ_Bourg`, `Service = Starter`, `ServiceLibelle = Choisir un Tifazelt`. Tenue H26 + B04, visage V20, cheveux « Dr. Smyth Hair ».
- Le système existait déjà (écran `Ecrans.Starter`, `NouvellePartie.donnerStarter`, combat d'apprentissage contre Zéphir). Modifs : en-tête « Bourg-Azur / Devant la maison familiale » et réplique d'accueil quand `lieu = Bourg-Azur` ; quête « Parler au Professeur Arid, devant la maison. » ; après victoire « Premiers pas — Explorer la Route 1 » ; toasts sans « laboratoire / Val Palmeraie » ; nouvelles répliques de Maman.
- Sauvegardes : `ServerStorage.Sauvegardes_UI.{Starter,NouvellePartie,UI_Client}_avant_starter_bourg` ; attribut `Lignes_avant_starter_bourg` sur Maman.
- **Testé en Play (par commandes de test)** : écran ouvert avec l'en-tête Bourg-Azur ; choix d'Aqualune → Zéphir prend Florépine, séquence de dialogue, bouton « Affronter Zéphir » → combat ouvert contre Florépine ; PNJ chargé, invite « Parler » active à ~7 studs, dialogue → choix « Choisir un Tifazelt / Plus tard ». Aucune erreur de jeu dans la console.
- **Non vérifié** : rendu visuel du Professeur (vêtements, cheveux), appui réel sur E, combat jusqu'au bout et objectif mis à jour, parcours complet depuis l'écran titre.

## Refonte de l'habillage : étape 3 (conception) faite le 26 oct. 2026 (Claude Code)
- Mohand a choisi de refaire l'habillage. Nouvelle table des 69 PNJ (25 Bourg-Azur, 44 Route 1) : [[Habillage des PNJ]], copie machine `Claude outputs/outils/habillage_pnj.json`.
- Contrôlée par script : aucun couple Haut+Bas répété hors uniformes, aucune barbe sur femme ou enfant, pas de jupe sur homme, H29/B22 non utilisés.
- **Rien n'a été écrit dans Studio.** Étape suivante : 4, appliquer la table (sauvegarde d'abord dans `Sauvegardes_PNJ`).

## Refonte de l'habillage : étape 4 faite le 26 oct. 2026 (Claude Code, Haiku)
- Sauvegarde d'abord : `ServerStorage.Sauvegardes_PNJ.Habillage_avant_refonte` (69 dossiers : Shirt, Pants, accessoires, attributs, `Face_avant`).
- Table appliquée aux 69 PNJ : `Shirt`, `Pants`, Decal `face`, un accessoire de cheveux cloné depuis `Garderobe_Classique.Cheveux` (`Humanoid:AddAccessory`, soudé à `Head`), attributs `Haut`, `Bas`, `Visage`, `Coiffure`. Aucune erreur.
- **Vérifié par les données** : 69/69 conformes à la table, 69 accessoires soudés à la tête, un Shirt et un Pants par PNJ.
- **Non vérifié** : rendu en Play (les vêtements s'affichent-ils, cheveux qui traversent la tête ou le col ?). Pas encore sauvegardé dans Studio : Ctrl+S à faire.
- Étape suivante à confirmer avec Mohand : les tests en Play de l'habillage (rendu, « Parler » et « S'asseoir ») et le parcours complet du starter (l'implémentation du starter est déjà faite, voir « Étape 3 faite »).

## Étape 7 (tests) : confiée à Mohand, pas faite par Claude
- Mohand fait l'étape 7 lui-même. Rien de ce qui suit n'est donc testé par Claude : rendu des 69 PNJ, « Parler » et « S'asseoir » au clavier, starter jusqu'au bout.

## Étape 8 faite le 26 oct. 2026 (Claude Code, Haiku) : mise à jour du vault
- Notes mises à jour : [[À décider et à faire]] (PNJ manquants, tests de l'habillage et du starter).
- Audit lancé (voir résultat dans la réponse de Claude). Ctrl+S dans Studio rappelé à Mohand.

## Étape 7 refaite par Claude le 26 oct. 2026 (Sonnet) : test en Play d'une nouvelle partie
- Mohand a redemandé que Claude fasse l'étape 7. Parcours joué : titre, Nouvelle partie, création, classes, chambre, porte, Professeur (E), choix d'Aqualune, combat contre Florépine (perdu deux fois), revanche, banc (F).
- **Bug majeur : le combat d'apprentissage est injouable** (Florépine drain et soin, avantage de type, dégâts de 3-4 PV). Autres défauts : pénalité de 150 TFD, dialogue du Professeur non adapté après défaite, deux textes qui débordent, vocabulaire de labo, titre « AZZURSAL ». Détail et numéros dans [[À décider - Bugs du 26 oct. 2026 (traités)]].
- Rien n'a été corrigé ni modifié dans Studio (test seulement, Play arrêté). Rendu des PNJ : Professeur et Lina vérifiés de près ; 69/69 conformes côté serveur.
- Mise à jour du paragraphe d'étape 7 ci-dessus : elle n'est plus « confiée à Mohand ».

## Bug 1 corrigé le 26 oct. 2026 (Claude Code, Opus) : combat d'apprentissage et Zéphir visible
- Sauvegardes : `ServerStorage.Sauvegardes_UI.{NouvellePartie,UI_Client}_avant_tutoriel`.
- `UI.NouvellePartie.adversaireTutoriel(starter, rival)` : rival affaibli (une attaque faible sans drain ni soin, PV = 3 coups du starter). `UI_Client.lancerTutoriel` l'utilise.
- Nouveau PNJ `Workspace.Map.Starter_BourgAzur.Zéphir Célestin` (rue devant le portail, `Service = Rival`, géré dans `UI_Client.ouvrirService`).
- Testé en Play : nouvelle partie complète avec Aqualune, victoire, objectif mis à jour ; Zéphir visible, E ouvre son dialogue, « Combattre » sans starter affiche le bon message. Détail et points à valider dans [[À décider et à faire]].
- Ctrl+S à faire dans Studio.

## Bugs 2 à 7 traités le 26 oct. 2026 (Claude Code, Opus)
- Suite du travail suivie dans [[Feuille de route 26-27 oct]]. Détail des corrections et des tests dans [[À décider - Bugs du 26 oct. 2026 (traités)]].
