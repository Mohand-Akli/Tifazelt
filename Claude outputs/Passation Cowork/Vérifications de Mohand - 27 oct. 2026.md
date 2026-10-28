# Vérifications de Mohand : 27 oct. 2026

Ce que toi seul peux voir dans un Play au premier plan. Coche ce qui marche, écris « non » à côté de ce qui ne marche pas, et renvoie-moi les numéros. Plan associé : `v04, Tifalistre, PNJ, intro de combat et vélos - plan.md` (étapes 1 à 7).

## Avant de commencer
- [ ] Dans Studio : **Ctrl+S**. Rien n'est enregistré tant que tu ne le fais pas (scripts, modèles et magasin créés aujourd'hui).
- [ ] Garde la fenêtre de Studio au premier plan pendant le Play. En arrière-plan, Studio n'affiche que quelques images par seconde : la fluidité ne se juge pas.
- [ ] Lance le Play normalement, sans commandes de test. L'écran titre doit s'afficher.

## Deux chemins
- **Continuer** : reprend la partie de test (14 250 TFD, six Tifazelts). Assez de TFD pour acheter au magasin de vélos : fais les sections 3, 4, 6 et 7 ici.
- **Nouvelle partie** : Titre → Jouer → Nouvelle partie → Commencer → création du dresseur. Maman donne 3 000 TFD. Fais les sections 1 et 2 ici.

## 1. Partie neuve (Nouvelle partie)
- [ ] Le Professeur Arid Acanthus, devant la maison, affiche « PROFESSEUR ARID ACANTHUS » au-dessus de sa tête (et non « Victor »).
- [ ] Zéphir Célestin affiche « ZÉPHIR CÉLESTIN » (et non « Théo »).
- [ ] Choisis Cramosaur. Sa fiche dans la Tifalistre (Menu M > Tifalistre) montre le portrait v04 : corps sombre, lave.
- [ ] Sac > Objets clés : « Vélo Azur » (et non « Vélo ») et « Tuba de plongée ».
- [ ] Tifalistre : Cramosaur capturé, Dauphimyst aperçu, les autres « ??? ».
- [ ] Touche R : Cramosaur sort en 3D et te suit. Si tu as choisi Dauphimyst ou Garenbois, R affiche « ne peut pas encore sortir de sa Tiflask ». C'est voulu : ils n'ont pas de modèle 3D.

## 2. Combat d'apprentissage contre Zéphir (Nouvelle partie)
- [ ] Parle à Zéphir, puis Combattre. L'ouverture montre Zéphir en 3D à droite : bras croisés, visage fâché, il tape du pied.
- [ ] Le combat se joue normalement. Zéphir a l'avantage de type.
- [ ] Victoire : toast « Quête terminée » (L'Heure du Choix). Défaite : le toast te renvoie au Professeur.
- [ ] **Point principal** : la respiration du Tifazelt en combat est-elle continue, sans à-coups ?
- [ ] Texte à revoir (je peux corriger) : avant le premier combat, Zéphir et le Professeur parlent de « revanche ».

## 3. Dresseurs de la Route 1 (Continuer)
Chacun apparaît en 3D à droite pendant l'ouverture, puis le combat démarre.
- [ ] Gamin Léo : Lycombre niveau 3, poing levé vers toi.
- [ ] Gamine Inès : Vipéclair niveau 2, poing levé.
- [ ] Jeune Dresseur Bastien : Fennedune niveau 2, poing levé.
- [ ] Pique-Niqueuse Sara : Pierraiglon niveau 3, **mains sur les hanches**.
- [ ] Scout des Plaines Théo : Spectrocarte niveau 4, poing levé.

## 4. Pêche (si tu as une canne à pêche)
- [ ] Pêche au ponton : une prise lance un combat contre un Dauphimyst sauvage, de niveau proche de ton équipe. Le combat se termine normalement.

## 5. Vélos : sortie du sac (Continuer)
- [ ] Sac > Objets clés > Vélo Azur > Enfourcher, ou touche V. Le vélo sort de la hanche en grandissant, avec un petit rebond et des étincelles. La main droite plonge vers le sac puis se lève, et le personnage monte. Environ un tiers de seconde.
- [ ] Descendre, ou V : le vélo rentre vers la hanche.
- [ ] Tu ne vois jamais deux vélos à la fois.

## 6. Magasin de vélos « Vélos de l'Azur » (Continuer)
- [ ] Le magasin est au sud-est de la place d'entrée, quand on arrive de la Route 1. Il est blanc, avec un store rayé bleu et blanc et une enseigne « VÉLOS DE L'AZUR ».
- [ ] Gilles, marchand de vélos : la case affiche « GILLES, MARCHAND DE VÉLOS ». « Parler », puis « Voir les vélos ».
- [ ] Quatre vélos exposés, avec leur prix : Corail 3 500 TFD, VTT Sentier 7 500, Vélo de course Éclair 12 000, Vélo Étoile 20 000. Avec 14 250 TFD, l'Étoile est grisée.
- [ ] Achète le Corail : les TFD baissent de 3 500, le toast « Vélo Corail acheté » apparaît, et le Corail devient le vélo choisi (V le fait monter).
- [ ] Rachète le même vélo : refusé (« Tu as déjà ce vélo »).
- [ ] Onglet Vendre : les vélos n'y apparaissent pas (objets clés).
- [ ] Vitesses PROVISOIRES, à sentir en roulant : Azur 38, Corail 38, VTT 41, Éclair 46, Étoile 44.

## 7. Sac : choisir son vélo (Continuer)
- [ ] Sac > Objets clés : chaque vélo a son aperçu 3D qui tourne, sa vitesse, et « Enfourcher » (ou « Descendre » si tu roules dessus).
- [ ] Enfourcher un autre vélo pendant que tu roules : tu changes de vélo.

## 8. Choix à faire (rien à tester)
- [ ] Palmier : un palmier se trouve à environ 7 studs du coin de la terrasse du magasin, côté nord-ouest. Je le déplace ou je le garde ?
- [ ] Nom et tenue de Gilles (PROVISOIRE).
- [ ] Prix et vitesses des vélos (PROVISOIRE).
- [ ] Textes « revanche » avant le premier combat (Zéphir et le Professeur).

## Vérifié par les données (sans jouer, 27 oct. 2026)
- Les modules modifiés se chargent sans erreur : catalogue des Tifazelts, espèces, services, vélos, dresseur animé, scène de combat, invites, Tifalistre, magasin, sac.
- 20 espèces, 20 entrées dans la Tifalistre, équipe de test de 6, 5 vélos, 4 à vendre.
- Cramosaur, Cramoraptor et Cramorex ont leurs images de combat et leur portrait.
- Magasin présent avec 5 vélos exposés, un seul exemplaire chacun ; Gilles présent avec son tag et son service.
- Attributs de test remis à zéro (`VersionTifazelts`, `UI_PasserTitre`).
- Anciens noms de Tifazelts : aucun dans les scripts actifs, sauf une mention dans un commentaire d'en-tête (`Combat.Especes`) et le nom de zone « Pâture des Laineux » (voulu).

## Non vérifié du tout
- La fluidité réelle à 60 i/s (Studio en arrière-plan ne la montre pas).
- Le combat en ligne à deux joueurs (avatar de l'autre joueur dans l'ouverture).
- Les Gardiens : ouverture en cercle, pas de personnage dans le monde.
- L'évolution Cramosaur → Cramoraptor au niveau 16, à l'écran.
- Le mobile (bouton VÉLO, animations).
- Les vélos Corail, Éclair et Étoile montés en jeu : vus seulement en vitrine.
- L'approche à pied du magasin depuis la Route 1, et le vendeur animé.
