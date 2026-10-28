---
tags:
  - production
  - roblox
  - suivi
---
# Bugs relevés en Play (26 oct. 2026) — tous traités le 26 oct. 2026

> [[À décider et à faire|Sommaire : à décider et à faire]]

> Archive : tous ces bugs ont été traités le 26 oct. 2026. Restent à valider par Mohand : la formule des stats par niveau (1, PROVISOIRE), la défaite sans perte contre Zéphir et le retour à l'infirmerie (2), les répliques selon l'avancement (3), l'affiche et la carte de la chambre et les jambes pliées au repos (6), le bandeau du titre (7) ; à revoir quand Studio affiche la 3D : le cadre « Apparence » vide (9).

Sauvegardes avant correction : `ServerStorage.Sauvegardes_UI.*_avant_bugs_2026-10-26` (Kit, Panneaux, Combat, UI_Client, Starter, Regles, NouvellePartie), `Vue_avant_correctif_ColorMap`, et `ServerStorage.Sauvegardes_PNJ.Bugs_2026-10-26_avant` (affiche, carte, répliques du Professeur, de Maman et de Zéphir).

1. ~~**Combat d'apprentissage injouable.**~~ Corrigé (voir [[À décider - Starter, Zéphir et combat d'apprentissage]]).
   - **Formule des stats par niveau (PROVISOIRE, le vault ne la donne pas)** : `Regles.statsNiveau` multiplie maintenant les stats par (niveau + 10) / (ancien niveau + 10), base au niveau 30 (`R.DECALAGE_NIVEAU = 10`). Niveau 5 : 37,5 % des stats du niveau 30 (Pyrofennec 34 PV au lieu de 93) ; niveau 1 : 27,5 % ; niveau 60 : 175 % (avant 200 %). Une montée de niveau donne toujours au moins +1. Touche aussi les bébés du Pâturage (niveau 1) et les Tifazelts au-dessus du niveau 30.
2. ~~**Perdre le combat d'apprentissage coûte 150 TFD.**~~ Corrigé (PROVISOIRE) : contre Zéphir, la défaite ne coûte rien, l'équipe est soignée et le joueur reste sur place (« Continuer »). Les autres défaites ramènent maintenant vraiment **devant le comptoir de l'infirmière de Bourg-Azur** (3180, 903, 1211 ; attribut de workspace `RetourInfirmerie` pour déplacer ce point) au lieu du point d'apparition. **Testé en Play** : 3 000 TFD gardés contre Zéphir ; contre un dresseur, −150 TFD et arrivée à l'infirmerie.
3. ~~**Dialogue du Professeur après la défaite.**~~ Corrigé (PROVISOIRE) : répliques selon l'avancement (`UI_Client.lignesStarter`). Après une défaite : « Zéphir ne t'a pas fait de cadeau… » + bouton « Revanche contre Zéphir ». Après la victoire : réplique vers la Route 1, sans bouton. Zéphir aussi (« Tu veux ta revanche ? » / « On se revoit sur la Route 1 »). **Testé en Play.**
4. ~~**Interface.**~~ Corrigé : nom d'attaque long réduit automatiquement (« Avalanche Torrentielle » tient, testé) ; les toasts longs passent sur 2 ou 3 lignes au lieu de sortir de l'écran (`Kit.toast`, testé, y compris « Maman t'a donné 3 000 TFD… » qui débordait aussi) ; signe moins remplacé par un tiret moyen « – » (le tiret simple se collait au chiffre avec le contour ; testé : « –4 »).
5. ~~**Vocabulaire de laboratoire.**~~ Corrigé : « Tiflasks de départ » au lieu de « Plateau stérile » à Bourg-Azur ; Professeur : « Je suis venu jusqu'à Bourg-Azur avec trois Tiflasks » ; Maman : « venu exprès pour toi ». Gardé : Céleste, Romain et Ayla parlent de Val Palmeraie et du laboratoire (lore, pas l'écran du starter).
6. **Chambre** : le carré bleu était une affiche vide (`MaisonJoueur.Affiche`) et la carte claire à côté aussi (`CarteDresseur`). Elles ont maintenant un dessin (PROVISOIRE) : affiche « Luméridia — Bourg-Azur » (ciel, soleil, mer, collines) et carte de dresseur épinglée, chacune dans un cadre en bois. **Non vérifié à l'écran** (Studio n'affichait plus la 3D pendant le test). Jambes pliées : le personnage joue la pose de repos du pack Cartoony (choisi le 20 oct.), qui a les genoux fléchis ; état « Running », bien posé au sol. Pas de changement : à confirmer par Mohand.
7. ~~**Titre « AZZURSAL »**~~ : Mohand a choisi « Tifazelt » (26 oct. 2026). L'écran titre affiche TIFAZELT, avec le bandeau « La région d'Azzursal » (PROVISOIRE, remplace « Le monde des Tifazelts »). Non vu à l'écran.
8. **Nouveau bug trouvé et corrigé : combat bloqué dès que le starter a un modèle 3D.** `Tifazelts.Vue` (style « dessin ») écrivait `SurfaceAppearance.ColorMap` pendant le jeu, ce qui est interdit hors plugin : erreur, puis le combat restait figé sur « À toi, Pyrofennec ! ». Correctif : une SurfaceAppearance `SA_Dessin` préparée dans chaque modèle de `Tifazelts.Modeles`, que la Vue clone à la place de l'originale. **Testé en Play** : le combat se déroule, aucune erreur. Aspect du modèle non vu (3D non affichée).
9. **Remarque** : sur l'écran « Nouveau dresseur », le cadre « Apparence » était vide pendant le test (sans doute la même absence de rendu 3D que plus haut). À revoir quand Studio affiche la 3D.
