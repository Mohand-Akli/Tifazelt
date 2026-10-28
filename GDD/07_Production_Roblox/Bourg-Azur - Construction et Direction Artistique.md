---
tags:
  - production
  - roblox
  - monde
  - ville
  - lumeridia
  - bourg-azur
  - direction-artistique
aliases:
  - DA Bourg-Azur
  - Construction Bourg-Azur
---
# 🎨 Bourg-Azur — Construction et Direction Artistique

> Compte rendu détaillé de la **passe 2** de Bourg-Azur dans Roblox Studio (octobre 2026), réalisée par Claude.
> Fiche de lore et plan général : [[Bourg-Azur]]. Charte des interfaces : [[15. Charte Graphique]].
> Ce document décrit ce qui a **réellement** été construit et testé, et les intentions artistiques derrière chaque choix.

Le détail est rangé en six notes dans le dossier `Bourg-Azur - Construction et Direction Artistique/` (les numéros de section d'origine sont conservés) :

| Note | Sections |
| :--- | :--- |
| [[Bourg-Azur - Intention et direction artistique]] | 1. Intention générale · 2. Direction artistique |
| [[Bourg-Azur - Portes et intérieurs]] | 3. Le système de portes et d'intérieurs (façon Pokémon) · 14. Refonte des intérieurs (20 oct. 2026) |
| [[Bourg-Azur - Corrections et extensions]] | 4. Corrections dans la ville · 13. Mission du 19 oct. 2026 (place, moulin, littoral) |
| [[Bourg-Azur - Fontaine, paysage et mobilier]] | 5. La fontaine de la place · 6. Paysage et mobilier : remplir sans encombrer |
| [[Bourg-Azur - Habitants et secrets]] | 7. Les habitants (24 PNJ R6) · 8. Les secrets (8) |
| [[Bourg-Azur - Performance, tests et pistes]] | 9. Performance · 10. Tests réellement effectués (Play dans Studio) · 11. Pistes pour la suite |

## 🛠️ 12. Où trouver quoi (Roblox Studio)

| Élément | Emplacement |
|---|---|
| Générateur de la passe 2 | `ServerStorage.MapGeneration.BourgAzur.Passe2` et `Passe2b` (mode d'emploi `LISEZMOI_Passe2`) |
| Sauvegarde des éléments modifiés | `ServerStorage.BourgAzur_Sauvegarde_Passe2` |
| Intérieurs | `Workspace.Interieurs.<MaisonJoueur / Infirmerie / Guilde / Cafe / Fleuriste / Bazar>` |
| Générateur des intérieurs (refonte du 20 oct.) | `ServerStorage.MapGeneration.BourgAzur.Passe3_Interieurs` (Kit + une pièce par module, mode d'emploi `LISEZMOI`) |
| Sauvegarde des anciens intérieurs | `ServerStorage.Sauvegardes_Interieurs.<Nom>_avant` |
| Générateur des ruelles (Figuiers, Bougainvillées, Impasse du Levant, Chemin des Pêcheurs) | `ServerStorage.MapGeneration.BourgAzur.Passe3.Remplissage`, corrigé le 28 oct. 2026 : il dressait les raccords des ruelles et cassait les fontaines des placettes (rotation en trop, diamètre et hauteur inversés) |
| Chantier « Bourg-Azur parfait » (28 oct. 2026) | Plan et journal : [[Bourg-Azur parfait - plan]] ; détecteurs : `Claude outputs/outils/Bourg-Azur - détecteurs.lua` ; sauvegardes : `ServerStorage.BourgAzur_Sauvegarde_Parfait` |
| Ambiance intérieure (client) | `StarterPlayerScripts.Interieurs_Ambiance` |
| Portes et assises (serveur) | `ServerScriptService.BourgAzur_Portes` |
| Animations, bulles, secrets (client) | `StarterPlayerScripts.BourgAzur_Client` |
| PNJ | `Workspace.Map.CityPlots.BourgAzur.PNJ` (et dans chaque intérieur) |
| Décor ajouté | `BourgAzur.DecorPasse2`, `BourgAzur.DecorPasse2b`, `BourgAzur.Secrets`, `PublicSpaces.Acces` |
