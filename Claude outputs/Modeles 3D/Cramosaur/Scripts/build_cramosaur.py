# Cramosaur v2 : reconstruction fidele a l'image de reference (avant = -Y, Z haut, ~1 m)
import bpy, math, random
from mathutils import Vector
exec(open(LIB).read())

C = coll("Cramosaur")
clear(C)
reset_mats()
rnd = random.Random(11)
S = (1, -1)

# ---------- 1. Peau d'un seul tenant ----------
parts = []
parts.append(ell("Torse", C, (0, 0.03, 0.43), (0.21, 0.19, 0.22), rot=(-8, 0, 0)))
parts.append(ell("Ventre", C, (0, -0.03, 0.34), (0.20, 0.17, 0.15)))
parts.append(ell("Cou", C, (0, -0.02, 0.60), (0.16, 0.15, 0.12)))
parts.append(ell("Crane", C, (0, -0.05, 0.79), (0.205, 0.195, 0.175), seg=24, rings=16))
parts.append(ell("Museau", C, (0, -0.19, 0.735), (0.155, 0.13, 0.092), seg=24, rings=16))
parts.append(ell("Machoire", C, (0, -0.17, 0.668), (0.13, 0.12, 0.05)))
parts.append(tube("Queue", C, [(0, 0.15, 0.36), (0, 0.32, 0.31), (0, 0.46, 0.33), (0, 0.57, 0.39), (0, 0.63, 0.44)],
                  [0.15, 0.11, 0.075, 0.04, 0.0], seg=16))
for s in S:
    parts.append(ell(f"Cuisse{s}", C, (s * 0.15, 0.04, 0.30), (0.10, 0.15, 0.15), rot=(10, 0, 0)))
    parts.append(tube(f"Tibia{s}", C, [(s * 0.16, 0.06, 0.22), (s * 0.165, 0.03, 0.10), (s * 0.165, 0.0, 0.05)], [0.085, 0.072, 0.07], seg=12))
    parts.append(ell(f"Pied{s}", C, (s * 0.165, -0.05, 0.04), (0.08, 0.125, 0.045)))
    parts.append(tube(f"Bras{s}", C, [(s * 0.15, -0.06, 0.53), (s * 0.18, -0.13, 0.47), (s * 0.16, -0.18, 0.40)], [0.048, 0.042, 0.036], seg=10))
    parts.append(ell(f"Main{s}", C, (s * 0.155, -0.19, 0.375), (0.036, 0.034, 0.032)))
def ventre(c, n):
    # plastron clair : grand ovale sur l'avant du torse
    if 0.16 < c.z < 0.60 and n.y < -0.2 and c.y < 0.0:
        return (c.x / 0.175) ** 2 + ((c.z - 0.37) / 0.22) ** 2 < 1
    # dessous de la machoire
    if 0.6 < c.z < 0.665 and c.y < -0.06 and n.z < -0.45:
        return True
    return False
peau = fuse(parts, "Peau", C, voxel=0.008, smooth_iter=8, smooth_fac=0.5, target_tris=2300,
            paint=lambda o: assign_faces(o, "Ventre", ventre))
bv = bvh_of([peau])

# ---------- 2. Tete : yeux, narines, bouche, crocs, cornes ----------
for s in S:
    e = (s * 0.17, -0.20, 0.815)
    blob(f"OeilContour{s}", C, bv, e, (0.047, 0.056), material="Contour", jitter=0, n=16, thick=0.004, rot=0)
    blob(f"Oeil{s}", C, bv, e, (0.039, 0.048), material="Oeil", jitter=0, n=16, thick=0.004, lift=0.004)
    blob(f"Pupille{s}", C, bv, e, (0.011, 0.038), material="Pupille", jitter=0, n=10, thick=0.004, lift=0.007)
    blob(f"Reflet{s}", C, bv, (s * 0.165, -0.215, 0.835), (0.009, 0.009), material="Reflet", jitter=0, n=8, thick=0.004, lift=0.01)
    blob(f"Narine{s}", C, bv, (s * 0.045, -0.33, 0.78), (0.010, 0.016), material="Pupille", jitter=0.1, n=8, rot=30 * s)
    vein(f"Bouche{s}", C, bv, [(s * 0.0, -0.325, 0.675), (s * 0.06, -0.305, 0.672), (s * 0.12, -0.245, 0.672), (s * 0.15, -0.17, 0.68), (s * 0.16, -0.12, 0.695), (s * 0.155, -0.095, 0.715)],
         width=0.0065, material="Contour", lift=0.001, seg=4)
    for i, (x, y, L) in enumerate(((0.05, -0.31, 0.03), (0.12, -0.24, 0.018))):
        cone(f"Croc{s}{i}", C, (s * x, y, 0.675), (s * x, y - 0.004, 0.675 - L), 0.011, material="Dents", seg=6, rings=2)
    cone(f"Corne{s}", C, (s * 0.11, -0.04, 0.91), (s * 0.14, 0.01, 1.01), 0.045, material="Corne", seg=10, bend=0.22, bend_dir=(0, 1, 0), rings=6)

# ---------- 3. Pattes : griffes ----------
for s in S:
    for i, dx in enumerate((-0.05, 0.0, 0.05)):
        x = s * 0.165 + dx
        cone(f"GriffePied{s}{i}", C, (x, -0.155, 0.035), (x + dx * 0.3, -0.20, 0.008), 0.02, material="Griffes", seg=6, rings=3, bend=0.2, bend_dir=(0, 0, -1))
    for i, dx in enumerate((-0.022, 0.0, 0.022)):
        x = s * 0.155 + dx
        cone(f"GriffeMain{s}{i}", C, (x, -0.21, 0.36), (x, -0.225, 0.325), 0.009, material="Griffes", seg=5, rings=2)

# ---------- 4. Criniere de fourrure (meches larges, en couches) ----------
k = 0
for layer, (zb, R, L, w) in enumerate(((0.65, 0.14, 0.07, 0.08), (0.595, 0.155, 0.075, 0.085))):
    for a in range(-160, 161, 24):
        th = math.radians(a + (12 if layer % 2 else 0))
        d = Vector((math.sin(th), -math.cos(th), 0))
        front = max(0, math.cos(th))
        base = Vector((0, -0.03, zb)) + d * R
        tip = base + d * (0.045 + 0.02 * front) + Vector((0, 0, -L * (0.9 + 0.6 * front)))
        side = Vector((math.cos(th), math.sin(th), 0))
        tuft(f"Meche{k}", C, base, tip, w, 0.04, side=side, bend=0.3, bend_dir=tuple(d)); k += 1
# pointe en V sur la poitrine
for i, (x, z) in enumerate(((-0.06, 0.47), (0.0, 0.43), (0.06, 0.47))):
    tuft(f"MecheV{i}", C, (x * 1.3, -0.165, 0.58), (x, -0.185, z), 0.06, 0.03, side=(1, 0, 0), bend=0.15, bend_dir=(0, -1, 0))

# ---------- 5. Plaques d'obsidienne sur le dos ----------
rows = [  # (y, z, ecart lateral, rayon, direction vers l'exterieur (y, z))
    (0.10, 0.62, 0.0, 0.075, (0.6, 0.8)), (0.12, 0.58, 0.11, 0.065, (0.5, 0.6)), (0.17, 0.56, 0.0, 0.085, (0.8, 0.7)),
    (0.19, 0.50, 0.12, 0.07, (0.6, 0.5)), (0.24, 0.48, 0.0, 0.08, (0.9, 0.6)), (0.27, 0.42, 0.10, 0.065, (0.6, 0.4)),
    (0.32, 0.40, 0.0, 0.07, (0.6, 0.8)), (0.38, 0.36, 0.07, 0.055, (0.3, 0.7)), (0.43, 0.37, 0.0, 0.06, (0.2, 1.0)),
    (0.50, 0.39, 0.04, 0.045, (0.0, 1.0)), (0.55, 0.42, 0.0, 0.04, (-0.2, 1.0)),
]
n = 0
for (y, z, dx, r, (oy, oz)) in rows:
    for s in ((1, -1) if dx else (0,)):
        p = Vector((s * dx, y, z))
        out = Vector((s * (1.0 if dx else 0.0), oy, oz))
        plate(f"Plaque{n}", C, bv, p, r * 1.15, r * 0.5, seed=n, rot=rnd.uniform(0, 60), tilt=(rnd.uniform(-10, 10), rnd.uniform(-10, 10)), sink=0.5, stretch=1.15, outward=out)
        n += 1

# ---------- 6. Taches sombres polygonales ----------
taches_tete = [(0.10, -0.02, 0.94, 0.03), (0.16, 0.02, 0.86, 0.028), (0.0, 0.03, 0.96, 0.03), (0.18, -0.07, 0.90, 0.022),
               (0.08, 0.08, 0.90, 0.03), (0.06, -0.22, 0.81, 0.022), (0.13, -0.18, 0.78, 0.018), (0.20, 0.0, 0.76, 0.025)]
for i, (x, y, z, r) in enumerate(taches_tete):
    for s in S:
        if x == 0 and s < 0: continue
        blob(f"TacheT{i}{s}", C, bv, (s * x, y, z), (r, r * 0.85), material="Taches", seed=i, jitter=0.2, n=6, thick=0.0015, lift=0.0, rot=rnd.uniform(0, 60))
taches_corps = [(0.25, 0.02, 0.33, 0.035), (0.25, 0.09, 0.25, 0.03), (0.25, -0.03, 0.24, 0.026), (0.23, 0.13, 0.36, 0.024),
                (0.24, 0.06, 0.40, 0.022), (0.17, 0.0, 0.10, 0.022), (0.2, -0.02, 0.50, 0.02), (0.10, 0.45, 0.30, 0.025)]
for i, (x, y, z, r) in enumerate(taches_corps):
    for s in S:
        blob(f"TacheC{i}{s}", C, bv, (s * x, y, z), (r * 0.8, r), material="Taches", seed=20 + i, jitter=0.25, n=6, thick=0.0015, lift=0.0, rot=rnd.uniform(0, 60))

# ---------- 7. Lave : taches irregulieres et fissures ----------
lave = [(0.17, 0.08, 0.58, 0.025), (0.19, 0.14, 0.53, 0.03), (0.17, 0.20, 0.50, 0.022), (0.20, 0.24, 0.44, 0.028), (0.15, 0.29, 0.43, 0.02),
        (0.13, 0.35, 0.39, 0.024), (0.10, 0.41, 0.38, 0.02), (0.08, 0.48, 0.39, 0.018), (0.06, 0.54, 0.42, 0.014), (0.21, 0.04, 0.50, 0.018),
        (0.14, 0.15, 0.58, 0.016), (0.12, 0.30, 0.48, 0.015)]
for i, (x, y, z, r) in enumerate(lave):
    for s in S:
        blob(f"LaveT{i}{s}", C, bv, (s * x, y, z), (r * 1.4, r * 1.05), seed=40 + i, jitter=0.4, n=9, rot=rnd.uniform(0, 180))
for s in S:
    vein(f"FisV1{s}", C, bv, [(s * 0.15, -0.12, 0.50), (s * 0.13, -0.16, 0.42), (s * 0.15, -0.15, 0.34), (s * 0.12, -0.16, 0.26)], width=0.009)
    vein(f"FisV2{s}", C, bv, [(s * 0.13, -0.16, 0.42), (s * 0.07, -0.18, 0.38)], width=0.007)
    vein(f"FisV3{s}", C, bv, [(s * 0.15, -0.15, 0.34), (s * 0.20, -0.08, 0.30)], width=0.007)
    vein(f"FisV4{s}", C, bv, [(s * 0.05, -0.17, 0.30), (s * 0.08, -0.17, 0.24), (s * 0.05, -0.15, 0.19)], width=0.007)
    vein(f"FisC1{s}", C, bv, [(s * 0.22, -0.06, 0.20), (s * 0.24, 0.0, 0.17), (s * 0.24, 0.08, 0.19)], width=0.008)
    vein(f"FisC2{s}", C, bv, [(s * 0.24, 0.0, 0.17), (s * 0.23, 0.02, 0.10)], width=0.006)
    vein(f"FisQ1{s}", C, bv, [(s * 0.10, 0.28, 0.26), (s * 0.08, 0.38, 0.25), (s * 0.06, 0.47, 0.27)], width=0.008)
    vein(f"FisQ2{s}", C, bv, [(s * 0.05, 0.50, 0.30), (s * 0.04, 0.57, 0.36)], width=0.006)
    vein(f"FisP{s}", C, bv, [(s * 0.20, -0.05, 0.47), (s * 0.21, 0.0, 0.40), (s * 0.19, 0.04, 0.34)], width=0.007)

# ---------- 8. Contour facon dessin ----------
outline(peau, C, thick=0.006)

par = {}
for o in C.objects:
    for p in o.data.polygons:
        m = o.data.materials[p.material_index].name
        par[m] = par.get(m, 0) + len(p.vertices) - 2
result = {"objets": len(C.objects), "triangles": tris(C), "par_mat": par}
