# Tifazelt — consignes pour Claude Code

Ce dossier est le vault Obsidian du jeu Roblox **Tifazelt** (région de Luméridia). Le jeu lui-même est dans Roblox Studio (placeId 88063327881434), piloté via le serveur MCP de Studio. L'historique détaillé du travail fait dans Claude Cowork est dans `00 - Suivi/Plans/` (plans finis dans `Terminés/`). **Index du vault : `Accueil.md`** (où se trouve chaque chose).

## Carte du vault (depuis le 28 oct. 2026)
`00 - Suivi` (à décider et à faire, plans en cours et `Plans/Terminés/`) · `01 - Règles du jeu` · `02 - Tifazelts` (dont `Attaques/`) · `03 - Monde` · `04 - Histoire et personnages` · `05 - Joueur et dresseurs` · `06 - Objets` · `07 - Interface et menus` · `08 - Direction artistique` · `09 - Production Roblox` (ce qui est construit dans Studio) · `10 - Captures` (`Jours/`, `Images/`) · `11 - Développement` (modèles 3D, textures, `Outils du vault/`, sauvegardes, archives). Les `.blend` utilisent des chemins relatifs : garder ensemble les dossiers de `Modèles 3D/`.

## Règles du propriétaire (Mohand) — à respecter toujours
- Répondre en **français**, de façon concise. Pas d'emojis dans l'UI du jeu. Animations d'UI ≤ ~0,35 s.
- **Ne jamais dire qu'une chose a été testée si ce n'est pas le cas.** Séparer « testé » et « non vérifié ».
- Ne pas détruire ce qui est réussi, ne pas reconstruire depuis zéro. **Sauvegarder avant de retirer** (dossiers `ServerStorage.*Sauvegarde*`).
- Pas de collision invisible. Supprimer tous les scripts des modèles Toolbox (scripts malveillants déjà trouvés).
- Aucun code distant, aucune donnée joueur.
- Ne pas lancer `BourgAzur B.Coast`. Ne pas déplacer Bourg-Azur ni Val Palmeraie.
- Tout ce qui n'est pas défini dans le vault est **PROVISOIRE** : le signaler et le noter dans `00 - Suivi/À décider et à faire.md` (le sommaire indique la note de thème ou de chantier, dans le dossier voisin `À décider et à faire/`).
- Captures : dans `10 - Captures/Images`, nom `AAAA-MM-JJ_HHhMM_sujet.jpg` (heure de Bruxelles), ajoutées à la note du jour `10 - Captures/Jours/Captures AAAA-MM-JJ.md` (à créer sur le modèle des autres si besoin), puis comptées dans les tableaux du sommaire `Historique des captures.md`.
- Après un chantier : mettre à jour les notes du vault, lancer l'audit (`python3 "Claude outputs/outils/audit.py" .`), rappeler **Ctrl+S** dans Studio.
- Économie : préférer les vérifications par les données ; regrouper les tests en jeu à demander à Mohand.

## Roblox Studio — repères techniques
- Nord = −Z. Eau du terrain y ≈ −1/−2, plaine y ≈ 2, plateau y ≈ 11. Intérieurs de Bourg-Azur dans `Workspace.Interieurs` (y = 900).
- Générateurs : `ServerStorage.MapGeneration` (LumeridiaEst, BourgAzur, Route1, ValPalmeraie, Extensions). Chaque fonction efface puis recrée son dossier ; toujours `require` une **copie clonée** ; travaux longs dans `task.spawn`.
- ⚠️ Ne jamais relancer une fonction qui écrit le terrain sans restaurer d'abord (`Co.Terrain` sans `Co.Restaurer()`, `Foret2.Aplanir`, `PlaineOuest.Terrain`, etc.). Relancer `Foret2.Arbres`/`Clairiere` ou `Route1 R.Part1/2/3` défait des corrections manuelles.
- StreamingEnabled actif. Les décors ont `CanQuery = false`.
- PNJ : R6, HumanoidRootPart ancré, tags `PNJ_Bourg` / `PNJ_Route1` (+ `Dresseur`), invite « Parler » (E, AlwaysShow, portée 9). Les invites « S'asseoir » sont sur F / ButtonY (PROVISOIRE).
- Animations PNJ : `ReplicatedStorage.Animations.GestesPNJ` + `StarterPlayerScripts.PNJ_Animations` (Motor6D.Transform côté client).
- Course/vélo : `ReplicatedStorage.Joueur.Deplacements`, `StarterPlayerScripts.Deplacements_Client`, `ServerScriptService.Deplacements_Serveur`.
- Audio : `ReplicatedStorage.Audio.Sons`, `StarterPlayerScripts.Musique`.
- Combat, capture et menus : prototype côté client avec des données de test (voir `09 - Production Roblox/Interface (UI) - Construction Roblox.md`) ; rencontres = repères dans `Route1.SpawnZones`.

## Chantiers en cours (au 28 oct. 2026)
- `00 - Suivi/Plans/Bourg-Azur parfait - plan.md` : étapes 6 (ajouts PROVISOIRES) et 7 (contrôle final) à faire.
- `00 - Suivi/Plans/Lignée Dauphin - plan.md` : étape 9, tests en Play par Mohand.
- `00 - Suivi/Plans/Vérifications de Mohand - 27 oct. 2026.md` : tests à faire par Mohand.
- `00 - Suivi/Plans/Restructuration du vault - plan.md` : plan écrit le 28 oct. 2026, en attente de la validation de Mohand (décisions R1 à R9).
- Choix en attente : `00 - Suivi/À décider et à faire/À décider - Relecture du 28 oct. 2026.md` (41 choix numérotés).

## Rangement du vault (depuis le 28 oct. 2026)
Plan et journal du rangement : `00 - Suivi/Plans/Terminés/Rangement du dossier - plan.md`.
- Une note trop longue est découpée ainsi : le sommaire garde son nom et sa place, les parties vont dans le dossier du même nom, juste à côté. Liens Obsidian par nom de note, jamais par chemin.
- Ne pas déplacer ni renommer `11 - Développement/Modèles 3D/`, `Cramosaur/V04/`, `Dauphin/` et leurs `Textures/` : des `.blend` et des scripts y pointent par chemin absolu.
- Rendus bruts, essais et variantes refusées : dans un dossier `_Travail/` (ignoré par git). Anciennes sauvegardes de fichiers : dans `Sauvegardes/`. Fichiers sans usage : `11 - Développement/Archives/`.

## Choix du modèle à chaque étape (économie de tokens)
Avant chaque étape, annonce l'étape en une ligne et recommande le modèle, puis **attends que Mohand confirme** (il change lui-même avec `/model`) :
- **Haiku** : tâches mécaniques et répétitives (lire/lister, renommer, appliquer une liste d'ID déjà décidée, mettre à jour une note, lancer l'audit).
- **Sonnet** : la plupart du code Luau et des modifications dans Studio, tests en Play, corrections de bugs simples.
- **Opus** : conception d'un nouveau système (starter, combat, quêtes), bugs difficiles, gros remaniements, décisions d'architecture.
Format : « Étape N — <quoi>. Modèle conseillé : <Haiku/Sonnet/Opus> (<raison en quelques mots>). Je continue ? »
