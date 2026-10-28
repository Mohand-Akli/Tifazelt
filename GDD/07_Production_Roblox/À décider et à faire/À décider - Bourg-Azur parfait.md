---
tags:
  - production
  - roblox
  - suivi
---
# Bourg-Azur parfait (28 oct. 2026) — audit fait, corrections à venir

> [[À décider et à faire|Sommaire : à décider et à faire]]

Demande de Mohand : régler tous les problèmes de Bourg-Azur (textures, chemins). Liste complète et étapes : [[Bourg-Azur parfait - plan]].
- **Trouvé** :
  - 802 paires de faces qui scintillent à l'extérieur (dont 196 bordures de rue et 249 sur les vélos exposés) et 181 dans les six intérieurs (comptage refait le 28 oct. 2026 avec `Claude outputs/outils/Bourg-Azur - détecteurs.lua`) ;
  - sentier de la Route 1 qui contourne l'arche ;
  - sentier de l'oliveraie qui bute contre une maison, mur de l'oliveraie avec deux trous ;
  - bancs, buisson, lampadaires et panneau sur les chaussées ;
  - objets qui flottent (buisson à 6 studs, olivier millénaire, barque) ;
  - table de pique-nique sur un toit ;
  - maison 111 collée à la maison du joueur ;
  - PNJ légèrement enfoncés ou flottants ;
  - étiquettes d'édition (« PortSaphir (Ø 720) »…) visibles dans le ciel (réglé à l'étape 1).
  - laisse de mer de la plage (plaques de sable humide, algues, coquillages) posée à plat : une partie flotte sur la mer (à reposer à l'étape 4).
- **Avancement** : étape 1 faite (étiquettes rangées) ; étape 2 faite (plus aucun scintillement visible à l'extérieur, vélos et magasin de vélos corrigés à la source). Étape 3 faite (plus aucun scintillement dans les six intérieurs ; étagère du Bazar posée au sol ; piliers de la Guilde déplacés entre les fenêtres). Étape 4 faite (chaussées dégagées, laisse de mer reposée sur le sable, barque dans l'eau, table de pique-nique descendue du toit, PNJ au sol). Étape 5 faite (ruelles débarrassées des demi-disques, fontaines des placettes refaites, portail du Pâturage dégagé ; générateurs corrigés). Prochaine : étape 6, ajouts (descentes vers la plage).
- **À décider** :
  - ~~Étiquettes d'édition : `ServerStorage` ou cachées en jeu ?~~ Décidé par Mohand (28 oct. 2026) : rangées dans `ServerStorage.BourgAzur_Sauvegarde_Parfait.Etape1_EtiquettesEdition` (fait, étape 1).
  - Ciel `Ciel_Route1` : une traînée de cubes près du soleil peint fait partie de l'image ; le garder ?
  - Ajouts proposés (PROVISOIRES) : descentes vers la plage depuis la Promenade et bancs face à la mer.
