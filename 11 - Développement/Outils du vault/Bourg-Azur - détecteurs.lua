-- Détecteurs du chantier « Bourg-Azur parfait » (28 oct. 2026)
-- À coller tel quel dans execute_luau (contexte Edit). Définit _G.BA_Detecteurs puis lance les contrôles.
-- Plan : 00 - Suivi/Plans/Bourg-Azur parfait - plan.md
--   scintillements(racines, boite) : faces de même sens, dans le même plan, qui se recouvrent ET restent visibles
--                                    (zone commune ni couverte par une autre pièce ni sous le terrain,
--                                     et pièces d'aspect différent : couleur, matière, texture ou décalque)
--   surChemins(racines, boite)     : objets posés sur les chaussées, places, allées et pontons
--   flottants(racines, boite)      : modèles de décor dont le point le plus bas n'est pas sur le sol
--   pnjAuSol(boite)                : pieds des PNJ par rapport au sol
--   solSous(x, z, yMax, exclure)   : sol réel sous un point (section 6, appelle d'abord D.indexerSol)
-- boite = {x0, x1, z0, z1, ymax} : seules les pièces dont le centre est dedans sont examinées.
-- Attention : flottants et pnjAuSol cherchent le sol par rayon. Un rayon traverse les pièces CanQuery = false
-- (beaucoup de décors et certains dallages) : un objet posé sur l'une d'elles paraît flotter. Avant de déplacer
-- quoi que ce soit, confirmer avec solSous (section 6), qui tient compte de toutes les pièces et des disques.
local D = {}

D.VILLE = {1600, 2800, 1100, 2200, 100}
D.INTERIEURS = {-1e6, 1e6, -1e6, 1e6, 1e6}

function D.racinesVille()
	local t = {workspace.Map.CityPlots.BourgAzur}
	for _, c in ipairs(workspace.Map.Extensions:GetChildren()) do
		if c.Name:find("^Bourg") or c.Name:find("^Littoral") or c.Name:find("^Zone1") then table.insert(t, c) end
	end
	return t
end

function D.racinesInterieurs()
	return {workspace.Interieurs}
end

local function dansBoite(pos, b)
	return pos.X > b[1] and pos.X < b[2] and pos.Z > b[3] and pos.Z < b[4] and pos.Y < b[5]
end

local function court(x)
	return (x:GetFullName():gsub("Workspace%.Map%.CityPlots%.BourgAzur%.", "BA."):gsub("Workspace%.Map%.Extensions%.", "Ext."):gsub("Workspace%.Interieurs%.", "Int."))
end
D.court = court

-- grille de recherche : cellule -> liste d'indices
local function grille(parts, pas)
	local g = {}
	for i, p in ipairs(parts) do
		local pos, r = p.Position, p.Size.Magnitude / 2
		for x = math.floor((pos.X - r) / pas), math.floor((pos.X + r) / pas) do
			for y = math.floor((pos.Y - r) / pas), math.floor((pos.Y + r) / pas) do
				for z = math.floor((pos.Z - r) / pas), math.floor((pos.Z + r) / pas) do
					local k = x .. "," .. y .. "," .. z
					g[k] = g[k] or {}
					table.insert(g[k], i)
				end
			end
		end
	end
	return g
end

-- 1. Scintillements ---------------------------------------------------------

local function faces(p)
	local cf, h = p.CFrame, p.Size / 2
	local t = {}
	for _, a in ipairs({
		{cf.RightVector, h.X, cf.UpVector, h.Y, cf.LookVector, h.Z},
		{cf.UpVector, h.Y, cf.RightVector, h.X, cf.LookVector, h.Z},
		{cf.LookVector, h.Z, cf.RightVector, h.X, cf.UpVector, h.Y},
	}) do
		for _, sg in ipairs({1, -1}) do
			table.insert(t, {n = a[1] * sg, c = cf.Position + a[1] * (sg * a[2]), u = a[3], hu = a[4], v = a[5], hv = a[6]})
		end
	end
	return t
end
D.faces = faces

-- même sens, même plan (à 0,012 près), recouvrement d'au moins 0,03 stud dans les deux directions
local function recouvre(f, g)
	if f.n:Dot(g.n) < 0.9995 then return false end
	if math.abs((g.c - f.c):Dot(f.n)) > 0.012 then return false end
	local d = g.c - f.c
	for _, axe in ipairs({f.u, f.v, g.u, g.v}) do
		local rf = math.abs(f.u:Dot(axe)) * f.hu + math.abs(f.v:Dot(axe)) * f.hv
		local rg = math.abs(g.u:Dot(axe)) * g.hu + math.abs(g.v:Dot(axe)) * g.hv
		if math.abs(d:Dot(axe)) > rf + rg - 0.03 then return false end
	end
	return true
end
D.recouvre = recouvre

local function dansRect(f, pt)
	local d = pt - f.c
	return math.abs(d:Dot(f.u)) <= f.hu + 1e-3 and math.abs(d:Dot(f.v)) <= f.hv + 1e-3
end

local function dansPart(p, pt)
	local l = p.CFrame:PointToObjectSpace(pt)
	local h = p.Size / 2
	return math.abs(l.X) < h.X and math.abs(l.Y) < h.Y and math.abs(l.Z) < h.Z
end

-- deux pièces de même couleur et de même matière sans texture donnent la même image : pas de scintillement visible
local SANS_TEXTURE = {[Enum.Material.SmoothPlastic] = true, [Enum.Material.Plastic] = true, [Enum.Material.Neon] = true, [Enum.Material.Glass] = true}

local function habillee(p)
	for _, c in ipairs(p:GetChildren()) do
		if c:IsA("Decal") or c:IsA("SurfaceGui") or c:IsA("SurfaceAppearance") then return true end
	end
	return false
end

local function memeAspect(a, b)
	if a.Material ~= b.Material or not SANS_TEXTURE[a.Material] or a.MaterialVariant ~= b.MaterialVariant then return false end
	local ca, cb = a.Color, b.Color
	if math.abs(ca.R - cb.R) > 0.004 or math.abs(ca.G - cb.G) > 0.004 or math.abs(ca.B - cb.B) > 0.004 then return false end
	if math.abs(a.Transparency - b.Transparency) > 0.01 or math.abs(a.Reflectance - b.Reflectance) > 0.01 then return false end
	return not (habillee(a) or habillee(b))
end
D.memeAspect = memeAspect

-- point sous la surface du terrain (l'eau ne cache rien)
local paramsTerrain = RaycastParams.new()
paramsTerrain.FilterType = Enum.RaycastFilterType.Include
paramsTerrain.FilterDescendantsInstances = {workspace.Terrain}
paramsTerrain.IgnoreWater = true

local function sousTerrain(q)
	local hit = workspace:Raycast(q + Vector3.new(0, 4, 0), Vector3.new(0, -4.02, 0), paramsTerrain)
	return hit ~= nil and hit.Position.Y >= q.Y - 0.01
end

-- points de la zone commune aux deux faces (échantillonnage 5 x 5 sur chacune)
local function pointsCommuns(f, g)
	local pts = {}
	for _, a in ipairs({{f, g}, {g, f}}) do
		local x, y = a[1], a[2]
		for i = -2, 2 do for j = -2, 2 do
			local pt = x.c + x.u * (x.hu * i / 2.2) + x.v * (x.hv * j / 2.2)
			if dansRect(y, pt) then table.insert(pts, pt) end
		end end
	end
	return pts
end

function D.scintillements(racines, boite)
	boite = boite or D.VILLE
	local blocs, toutes = {}, {}
	for _, r in ipairs(racines) do
		for _, p in ipairs(r:GetDescendants()) do
			if p:IsA("BasePart") and p.Transparency < 0.9 and dansBoite(p.Position, boite) then
				table.insert(toutes, p)
				if p:IsA("Part") and p.Shape == Enum.PartType.Block then table.insert(blocs, p) end
			end
		end
	end
	local F = {}
	for i, p in ipairs(blocs) do F[i] = faces(p) end
	local gB = grille(blocs, 8)
	local gT = grille(toutes, 8)
	local vus, res = {}, {}
	for _, l in pairs(gB) do
		for a = 1, #l do for b = a + 1, #l do
			local i, j = l[a], l[b]
			if i > j then i, j = j, i end
			local k = i .. ":" .. j
			if not vus[k] then
				vus[k] = true
				local A, B = blocs[i], blocs[j]
				local visible, faceVue = false, nil
				-- même aspect : rien à voir, on passe la paire
				local facesA = memeAspect(A, B) and {} or F[i]
				for _, f in ipairs(facesA) do
					for _, g in ipairs(F[j]) do
						if recouvre(f, g) then
							-- visible si un point commun, décollé de 0,04 vers l'extérieur, n'est ni sous le terrain ni dans une autre pièce
							for _, pt in ipairs(pointsCommuns(f, g)) do
								local q = pt + f.n * 0.04
								local cell = gT[math.floor(q.X / 8) .. "," .. math.floor(q.Y / 8) .. "," .. math.floor(q.Z / 8)]
								local couvert = sousTerrain(q)
								if cell and not couvert then
									for _, o in ipairs(cell) do
										local O = toutes[o]
										if O ~= A and O ~= B and dansPart(O, q) then couvert = true break end
									end
								end
								if not couvert then visible, faceVue = true, f break end
							end
						end
						if visible then break end
					end
					if visible then break end
				end
				if visible then table.insert(res, {a = A, b = B, n = faceVue.n, c = faceVue.c}) end
			end
		end end
	end
	return res
end

-- regroupe une liste de paires par dossier (2 niveaux sous la racine) et noms des pièces
function D.resumePaires(paires, max)
	local par = {}
	for _, pr in ipairs(paires) do
		local chemin = court(pr.a)
		local grp = chemin:match("^(%w+%.[%w_]+)") or chemin
		local k = grp .. " " .. pr.a.Name .. "/" .. pr.b.Name
		par[k] = (par[k] or 0) + 1
	end
	local t = {}
	for k, v in pairs(par) do table.insert(t, {k, v}) end
	table.sort(t, function(x, y) return x[2] > y[2] end)
	local out = {}
	for i = 1, math.min(#t, max or 40) do table.insert(out, t[i][2] .. "  " .. t[i][1]) end
	return table.concat(out, "\n")
end

-- 2. Objets posés sur les chemins -------------------------------------------

D.SURFACES = {Chaussee = true, Raccord = true, Dallage = true, Plateforme = true, Allee = true, Chemin = true, Ponton = true, Elargissement = true}

-- l'objet = premier ancêtre dont le parent est un dossier
local function objet(p)
	local m = p
	while m.Parent and m.Parent ~= workspace and not m.Parent:IsA("Folder") do m = m.Parent end
	return m
end

function D.surChemins(racines, boite)
	boite = boite or D.VILLE
	local surfaces, objets = {}, {}
	for _, r in ipairs(racines) do
		for _, p in ipairs(r:GetDescendants()) do
			if p:IsA("BasePart") and dansBoite(p.Position, boite) then
				if D.SURFACES[p.Name] and p.Position.Y < 20 then table.insert(surfaces, p)
				elseif p.Transparency < 0.9 then table.insert(objets, p) end
			end
		end
	end
	local hits, ordre = {}, {}
	for _, s in ipairs(surfaces) do
		local cf, sz = s.CFrame, s.Size
		local top = cf.Position.Y + sz.Y / 2
		local sobj = objet(s)
		for _, o in ipairs(objets) do
			local d = o.Position - cf.Position
			if math.abs(d.X) < sz.X + sz.Z and math.abs(d.Z) < sz.X + sz.Z then
				local l = cf:PointToObjectSpace(o.Position)
				local bas = o.Position.Y - o.Size.Y / 2
				if math.abs(l.X) < sz.X / 2 - 1.5 and math.abs(l.Z) < sz.Z / 2 - 1.5 and bas > top - 0.6 and bas < top + 4 then
					local m = objet(o)
					if m ~= sobj and not m:FindFirstChildOfClass("Humanoid") and not m:IsAncestorOf(s) then
						if not hits[m] then
							hits[m] = {surface = s, pos = o.Position, solide = false}
							table.insert(ordre, m)
						end
						if o.CanCollide then hits[m].solide = true end
					end
				end
			end
		end
	end
	local res = {}
	for _, m in ipairs(ordre) do
		local h = hits[m]
		table.insert(res, {objet = m, surface = h.surface, pos = h.pos, solide = h.solide})
	end
	return res
end

-- 3. Objets qui flottent ou s'enfoncent -------------------------------------

local function plusBas(m)
	local best, bp = math.huge, nil
	for _, p in ipairs(m:GetDescendants()) do
		if p:IsA("BasePart") and p.Transparency < 0.95 then
			local cf, s = p.CFrame, p.Size / 2
			for _, sx in ipairs({-1, 1}) do for _, sy in ipairs({-1, 1}) do for _, sz in ipairs({-1, 1}) do
				local w = cf:PointToWorldSpace(Vector3.new(sx * s.X, sy * s.Y, sz * s.Z))
				if w.Y < best then best, bp = w.Y, w end
			end end end
		end
	end
	return best, bp
end

-- seuils : flotte au-delà de +0,35 stud, enfoncé au-delà de -2,5 studs (les pieds plantés restent permis)
function D.flottants(racines, boite, haut, bas)
	boite, haut, bas = boite or D.VILLE, haut or 0.35, bas or -2.5
	local params = RaycastParams.new()
	params.FilterType = Enum.RaycastFilterType.Exclude
	params.RespectCanCollide = false
	local res = {}
	for _, r in ipairs(racines) do
		for _, m in ipairs(r:GetDescendants()) do
			if m:IsA("Model") and m:FindFirstChildWhichIsA("BasePart") and not m:FindFirstChildOfClass("Humanoid") and not m.Parent:IsA("Model") then
				local y, p = plusBas(m)
				local cf = m:GetBoundingBox()
				if p and dansBoite(cf.Position, boite) and y < 60 then
					params.FilterDescendantsInstances = {m}
					local hit = workspace:Raycast(Vector3.new(cf.X, y + 3, cf.Z), Vector3.new(0, -40, 0), params)
					if hit then
						local ecart = y - hit.Position.Y
						if ecart > haut or ecart < bas then
							table.insert(res, {objet = m, ecart = ecart, pos = Vector3.new(cf.X, y, cf.Z), sol = hit.Instance, matiere = hit.Material})
						end
					end
				end
			end
		end
	end
	table.sort(res, function(a, b) return math.abs(a.ecart) > math.abs(b.ecart) end)
	return res
end

-- 4. PNJ au sol ---------------------------------------------------------------

function D.pnjAuSol(boite)
	boite = boite or D.VILLE
	local CS = game:GetService("CollectionService")
	local params = RaycastParams.new()
	params.FilterType = Enum.RaycastFilterType.Exclude
	local res = {}
	for _, t in ipairs({"PNJ_Bourg", "PNJ_Route1"}) do
		for _, m in ipairs(CS:GetTagged(t)) do
			local ll, rl, hrp = m:FindFirstChild("Left Leg"), m:FindFirstChild("Right Leg"), m:FindFirstChild("HumanoidRootPart")
			if m:IsA("Model") and ll and rl and hrp and dansBoite(hrp.Position, boite) then
				local pied = math.min(ll.Position.Y - ll.Size.Y / 2, rl.Position.Y - rl.Size.Y / 2)
				params.FilterDescendantsInstances = {m}
				local hit = workspace:Raycast(Vector3.new(hrp.Position.X, pied + 2, hrp.Position.Z), Vector3.new(0, -20, 0), params)
				if hit and math.abs(pied - hit.Position.Y) > 0.15 then
					table.insert(res, {pnj = m, ecart = pied - hit.Position.Y, sol = hit.Instance})
				end
			end
		end
	end
	return res
end

-- 5. Correction des scintillements -------------------------------------------
-- Pour chaque paire, la pièce dont la face commune est la plus petite (bordure, cadre, décor) avance de delta
-- vers l'extérieur de la face : elle passe devant. Jamais une pièce de PNJ ni une pièce soudée (signalées à part).
-- Le décalage cumulé est noté dans un attribut (Vector3) : pour annuler, p.CFrame -= p:GetAttribute(attribut).
local function aireFace(p, n)
	local s = p.Size
	if math.abs(p.CFrame.RightVector:Dot(n)) > 0.99 then return s.Y * s.Z end
	if math.abs(p.CFrame.UpVector:Dot(n)) > 0.99 then return s.X * s.Z end
	return s.X * s.Y
end

local function intouchable(p)
	local x = p.Parent
	while x and x ~= workspace do
		if x:IsA("Model") and x:FindFirstChildOfClass("Humanoid") then return true end
		x = x.Parent
	end
	return #p:GetJoints() > 0
end

function D.decaler(paires, delta, attribut)
	delta, attribut = delta or 0.04, attribut or "Etape2_Decalage"
	local deja, n, sautees = {}, 0, {}
	for _, pr in ipairs(paires) do
		local ia, ib = intouchable(pr.a), intouchable(pr.b)
		if ia and ib then
			table.insert(sautees, pr)
		else
			local choix
			if ia then choix = pr.b elseif ib then choix = pr.a
			else choix = (aireFace(pr.a, pr.n) <= aireFace(pr.b, pr.n)) and pr.a or pr.b end
			-- une pièce ne bouge qu'une fois par passe ; la passe suivante revoit ce qui reste
			if not deja[choix] then
				deja[choix] = true
				local v = pr.n * delta
				choix.CFrame = choix.CFrame + v
				choix:SetAttribute(attribut, (choix:GetAttribute(attribut) or Vector3.zero) + v)
				n += 1
			end
		end
	end
	return n, sautees
end

-- passes successives jusqu'à zéro paire visible (ou plus aucun progrès)
function D.corrigerScintillements(racines, boite, delta, attribut, maxPasses)
	local journal = {}
	for passe = 1, maxPasses or 5 do
		local paires = D.scintillements(racines, boite)
		if #paires == 0 then table.insert(journal, ("passe %d : 0 paire"):format(passe)) return 0, journal end
		local n, sautees = D.decaler(paires, delta, attribut)
		table.insert(journal, ("passe %d : %d paires, %d pièces décalées, %d sautées"):format(passe, #paires, n, #sautees))
		if n == 0 then return #paires, journal end
	end
	local reste = D.scintillements(racines, boite)
	table.insert(journal, ("fin : %d paires"):format(#reste))
	return #reste, journal
end

-- 6. Sol réel ------------------------------------------------------------------
-- Index de toutes les pièces visibles et solides (CanQuery ignoré), par cellules de 16 studs.
local cellulesSol = {}
function D.indexerSol(racines)
	cellulesSol = {}
	for _, r in ipairs(racines) do
		for _, p in ipairs(r:GetDescendants()) do
			if p:IsA("BasePart") and p.Transparency < 0.95 and p.Name ~= "Zone_BourgAzur" then
				local e = p.Size.Magnitude / 2
				for gx = math.floor((p.Position.X - e) / 16), math.floor((p.Position.X + e) / 16) do
					for gz = math.floor((p.Position.Z - e) / 16), math.floor((p.Position.Z + e) / 16) do
						local k = gx .. "," .. gz
						cellulesSol[k] = cellulesSol[k] or {}
						table.insert(cellulesSol[k], p)
					end
				end
			end
		end
	end
end

local paramsSolTerrain = RaycastParams.new()
paramsSolTerrain.FilterType = Enum.RaycastFilterType.Include
paramsSolTerrain.FilterDescendantsInstances = {workspace.Terrain}
paramsSolTerrain.IgnoreWater = true

-- dessus d'une pièce sur la verticale (x, z) : disque réel pour un cylindre à axe vertical, sphère pour une boule, sinon boîte orientée
local function dessusSur(p, x, z)
	local cf, hs = p.CFrame, p.Size / 2
	if p:IsA("Part") and p.Shape == Enum.PartType.Cylinder and math.abs(cf.RightVector.Y) > 0.99 then
		local l = cf:PointToObjectSpace(Vector3.new(x, cf.Y, z))
		if l.Y * l.Y + l.Z * l.Z > (p.Size.Y / 2) ^ 2 then return nil end
		return cf.Y + hs.X
	end
	if p:IsA("Part") and p.Shape == Enum.PartType.Ball then
		local d2, r = (x - cf.X) ^ 2 + (z - cf.Z) ^ 2, p.Size.X / 2
		if d2 > r * r then return nil end
		return cf.Y + math.sqrt(r * r - d2)
	end
	local o = cf:PointToObjectSpace(Vector3.new(x, 0, z))
	local d = Vector3.new(cf.RightVector.Y, cf.UpVector.Y, cf.LookVector.Y)
	local tmin, tmax = -math.huge, math.huge
	for _, ax in ipairs({{o.X, d.X, hs.X}, {o.Y, d.Y, hs.Y}, {o.Z, d.Z, hs.Z}}) do
		if math.abs(ax[2]) < 1e-6 then
			if math.abs(ax[1]) > ax[3] then return nil end
		else
			local t1, t2 = (-ax[3] - ax[1]) / ax[2], (ax[3] - ax[1]) / ax[2]
			if t1 > t2 then t1, t2 = t2, t1 end
			tmin, tmax = math.max(tmin, t1), math.min(tmax, t2)
		end
	end
	if tmin > tmax then return nil end
	return tmax
end

-- sol réel sous (x, z), au plus haut à yMax : plus haute pièce solide traversée par la verticale, ou terrain (l'eau ne porte rien)
function D.solSous(x, z, yMax, exclure)
	local best, quoi = -math.huge, nil
	local h = workspace:Raycast(Vector3.new(x, yMax, z), Vector3.new(0, -200, 0), paramsSolTerrain)
	if h then best, quoi = h.Position.Y, workspace.Terrain end
	for _, p in ipairs(cellulesSol[math.floor(x / 16) .. "," .. math.floor(z / 16)] or {}) do
		if p.CanCollide and not (exclure and (p == exclure or p:IsDescendantOf(exclure))) then
			local top = dessusSur(p, x, z)
			if top and top <= yMax and top > best then best, quoi = top, p end
		end
	end
	return best, quoi
end

_G.BA_Detecteurs = D

-- Lancement : résumé des quatre contrôles sur la ville, puis scintillements des intérieurs.
-- Tout enchaîner peut dépasser le délai de réponse de Studio : avec _G.BA_ChargerSeulement = true (mis avant le collage),
-- le fichier ne fait que charger les fonctions, et chaque contrôle se lance ensuite à part.
D.indexerSol(D.racinesVille())
if _G.BA_ChargerSeulement then return "détecteurs chargés (_G.BA_Detecteurs)" end
local out = {}
local ext = D.scintillements(D.racinesVille(), D.VILLE)
table.insert(out, ("Scintillements visibles, extérieur : %d"):format(#ext))
table.insert(out, D.resumePaires(ext, 25))
local int = D.scintillements(D.racinesInterieurs(), D.INTERIEURS)
table.insert(out, ("Scintillements visibles, intérieurs : %d"):format(#int))
local parInt = {}
for _, pr in ipairs(int) do
	local top = pr.a
	while top.Parent and top.Parent ~= workspace.Interieurs do top = top.Parent end
	parInt[top.Name] = (parInt[top.Name] or 0) + 1
end
local t = {}
for k, v in pairs(parInt) do table.insert(t, k .. "=" .. v) end
table.sort(t)
table.insert(out, "  " .. table.concat(t, ", "))
local sc = D.surChemins(D.racinesVille(), D.VILLE)
table.insert(out, ("Objets sur les chemins : %d"):format(#sc))
local fl = D.flottants(D.racinesVille(), D.VILLE)
table.insert(out, ("Objets qui flottent ou s'enfoncent : %d"):format(#fl))
local pn = D.pnjAuSol(D.VILLE)
table.insert(out, ("PNJ mal posés : %d"):format(#pn))
_G.BA_Resultats = {exterieur = ext, interieurs = int, surChemins = sc, flottants = fl, pnj = pn}
return table.concat(out, "\n")
