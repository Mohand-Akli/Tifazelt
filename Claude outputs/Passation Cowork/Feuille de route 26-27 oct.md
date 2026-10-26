# Feuille de route du 26 au 27 oct. 2026 (14h)

Décision de Mohand (26 oct. 2026) : jusqu'au **27 oct. 2026 à 14h**, tout se fait avec Opus. Claude n'annonce plus de modèle et enchaîne les étapes.

Pour reprendre dans une nouvelle conversation : « passons à l'étape N ».

| # | Étape | Statut |
|---|---|---|
| 1 | Corriger les bugs relevés en Play (2 à 7 et la formule des stats par niveau), voir `GDD/07_Production_Roblox/À décider et à faire.md` > « Bugs relevés en Play » | Fait le 26 oct. 2026 (reste : titre Azzursal/Tifazelt à décider, affiche et pose à voir à l'écran) |
| 2 | Starter Cramosaur : finir le renommage et l'intégration (`Starters - plan.md`, étapes 1 à 5) | Fait le 26 oct. 2026 (renommage, attaques, test en Play avec Cramosaur) |
| 3 | Affichage des Tifazelts en 3D : régler ce qui les rend « moches » (accord avec la DA 2D, voir le journal de `Starters - plan.md`) | Fait le 26 oct. 2026 pour la lignée Cramosaur : images pré-rendues mates et saturées (validées par Mohand), contour 2D, ombre de contact, trois stades. Reste : portraits Tifalistre / Équipe, test d'un vrai combat avec les stades 2 et 3 |
| 4 | Les deux autres starters (Dauphimyst, Garenbois) : Mohand fournit les modèles, puis modèle 3D, rig, animations, intégration | À faire (attend Mohand) |
| 5 | Portraits (Tifalistre, Équipe) et base de la Tiflask (modèles, lancer, sortie) : voir `Portraits et Tiflask - plan.md` | Fait le 26 oct. 2026 (base) |
| 6 | Sortir / rentrer un Tifazelt dans le monde (lancer de Tiflask, suivi, visible par tous) : voir `Sortie du Tifazelt - plan.md` | Fait le 26 oct. 2026 (lignée Cramosaur) |
| 7 | Panneau d'équipe sur le bord gauche (état de l'équipe, choix du Tifazelt à sortir) : voir `Panneau d'équipe - plan.md` | Fait le 26 oct. 2026 (testé en Play) |

## Journal
- 26 oct. 2026 : feuille de route établie.
- 26 oct. 2026 : étape 1 faite. Bugs 2 à 6 corrigés, formule des stats par niveau posée (PROVISOIRE), combat d'apprentissage rééquilibré, et un bug bloquant trouvé en route : `Tifazelts.Vue` écrivait `ColorMap` en jeu, ce qui figeait tout combat avec un modèle 3D (corrigé avec `SA_Dessin`). Testé en Play par commandes de test : défaite contre Zéphir sans perte, revanche, victoire, répliques, défaite contre un dresseur avec retour à l'infirmerie, toasts, tiret des dégâts, nom d'attaque long. Non vu à l'écran : la 3D (Studio ne la rendait plus pendant le test), donc l'affiche de la chambre, la pose du personnage et les modèles en combat. Détail : `À décider et à faire.md`. Ctrl+S à faire.
- 26 oct. 2026 : titre du jeu « Tifazelt » (choix de Mohand) sur l'écran titre, bandeau « La région d'Azzursal » (au lieu de « Le monde des Tifazelts », redondant). Sauvegarde `Sauvegardes_UI.Titre_avant_titre_Tifazelt`. Étape 2 commencée : starters renommés.
- 26 oct. 2026 : étape 2 faite. Starters renommés, attaques validées et appliquées, combat contre Zéphir rééquilibré et testé en Play avec Cramosaur (le rendu 3D fonctionnait de nouveau : Cramosaur visible en combat). Prochaine : étape 3, l'affichage des Tifazelts en 3D.
- 26 oct. 2026 : étape 3 commencée. Mohand précise que le problème vient des textures (basse qualité de loin) et de la lumière (terne), pas du contour. Textures retouchées en 1024 px et lumière principale appliquées dans `Tifazelts.Vue` (détail dans le journal de `Starters - plan.md`). Comparaison des contours (variantes A à H, captures 19h39) gardée pour plus tard.
- 26 oct. 2026 : la retouche de texture n'a pas suffi (« toujours super moche »). Changement d'approche : images pré-rendues dans Blender pour le combat (`Tifazelts.Sprite`), testé en Play avec Cramosaur. Détail dans le journal de `Starters - plan.md`.
- 26 oct. 2026 : rendu mat et saturé validé par Mohand (« beaucoup mieux »). Optimisations (contour 2D régulier, alpha prémultiplié, ombre de contact) et stades 2 et 3 (Cramoraptor, Cramorex) faits, testés dans un banc de combat. Détail dans le journal de `Starters - plan.md`.
- 26 oct. 2026 : portraits et Tiflask faits (détail dans `Portraits et Tiflask - plan.md`).
- 26 oct. 2026 : étape 6 faite. Touche R, croix bas, bouton mobile et bouton de la Fiche ; serveur `Compagnon_Serveur` ; testé en Play à un joueur (détail et non testé dans `Sortie du Tifazelt - plan.md`). Bug corrigé en route : l'évolution ne mettait pas à jour le champ `espece`.
- 26 oct. 2026 (soir) : geste de lancer, sons de la Tiflask, aide de la touche R, puis panneau d'équipe (étape 7). Studio est devenu instable (le joueur n'arrive plus sur le serveur de test) : à redémarrer.
