import bpy, math, random
from mathutils import Vector
exec(open(LIB).read())

C = coll("Cramosaur")
clear(C)
reset_mats()
rnd = random.Random(7)

def sym(fn, name, *a, **k):
    """Cree la piece gauche (x>0) et son miroir."""
    out = []
    for s, tag in ((1, "G"), (-1, "D")):
        out.append(fn(f"{name}_{tag}", s))
    return out

# --- Corps ---
torse = ell("Torse", C, (0, 0.05, 0.42), (0.21, 0.24, 0.26), rot=(-12, 0, 0))
ventre_bas = ell("Bassin", C, (0, 0.04, 0.30), (0.22, 0.22, 0.19))
cou = ell("Cou", C, (0, -0.05, 0.60), (0.16, 0.16, 0.14))
tete = ell("Tete", C, (0, -0.10, 0.80), (0.22, 0.21, 0.20), seg=16, rings=10)
museau = ell("Museau", C, (0, -0.27, 0.735), (0.165, 0.15, 0.105), seg=14, rings=8)
machoire = ell("Machoire", C, (0, -0.25, 0.675), (0.14, 0.13, 0.06), material="Ventre")
plastron = ell("Plastron", C, (0, -0.09, 0.40), (0.155, 0.13, 0.20), material="Ventre", rot=(-10, 0, 0))
queue = tube("Queue", C, [(0, 0.20, 0.32), (0, 0.38, 0.23), (0, 0.55, 0.15), (0, 0.70, 0.12), (0, 0.82, 0.13)],
             [0.15, 0.115, 0.075, 0.035, 0], seg=12, scale_x=0.95)

for s, t in ((1, "G"), (-1, "D")):
    ell(f"Cuisse_{t}", C, (s * 0.15, 0.06, 0.27), (0.105, 0.14, 0.155))
    tube(f"Jambe_{t}", C, [(s * 0.16, 0.08, 0.20), (s * 0.165, 0.04, 0.10), (s * 0.165, 0.0, 0.05)], [0.08, 0.07, 0.065], seg=10)
    ell(f"Pied_{t}", C, (s * 0.165, -0.04, 0.035), (0.078, 0.115, 0.042))
    for i, dx in enumerate((-0.045, 0, 0.045)):
        x = s * 0.165 + dx
        cone(f"GriffePied_{t}{i}", C, (x, -0.13, 0.03), (x * 1.0 + dx * 0.3, -0.175, 0.012), 0.017, material="Griffes", seg=6, rings=3)
    tube(f"Bras_{t}", C, [(s * 0.14, -0.12, 0.50), (s * 0.17, -0.20, 0.44), (s * 0.15, -0.23, 0.37)], [0.05, 0.042, 0.036], seg=8)
    ell(f"Main_{t}", C, (s * 0.15, -0.235, 0.35), (0.038, 0.036, 0.035))
    for i, dx in enumerate((-0.02, 0.0, 0.02)):
        x = s * 0.15 + dx
        cone(f"GriffeMain_{t}{i}", C, (x, -0.245, 0.33), (x, -0.25, 0.295), 0.009, material="Griffes", seg=5, rings=2)
    # cornes orange
    cone(f"Corne_{t}", C, (s * 0.105, -0.07, 0.94), (s * 0.15, -0.02, 1.07), 0.042, material="Corne", seg=10, bend=0.18, bend_dir=(0, 1, 0))

# --- surfaces de reference ---
bv_tete = bvh_of([tete, museau])
bv_corps = bvh_of([torse, ventre_bas, queue])

for s, t in ((1, "G"), (-1, "D")):
    # yeux : grands, orange, pupille fendue
    patch(f"Oeil_{t}", C, bv_tete, (s * 0.12, -0.26, 0.82), (0.062, 0.072), material="Oeil", flat=0.30, rot=0)
    patch(f"Pupille_{t}", C, bv_tete, (s * 0.12, -0.26, 0.82), (0.013, 0.05), material="Pupille", flat=0.3, lift=0.016)
    patch(f"Reflet_{t}", C, bv_tete, (s * 0.10, -0.27, 0.85), (0.012, 0.012), material="Reflet", flat=0.4, lift=0.02)
    # narines, bouche
    patch(f"Narine_{t}", C, bv_tete, (s * 0.05, -0.41, 0.77), (0.012, 0.02), material="Pupille", flat=0.3, rot=30 * s)
    vein(f"Bouche_{t}", C, bv_tete, [(s * 0.02, -0.42, 0.70), (s * 0.10, -0.38, 0.69), (s * 0.15, -0.30, 0.70), (s * 0.17, -0.22, 0.715)],
         width=0.006, material="Pupille", lift=0.002)
    for i, (x, y) in enumerate(((0.06, -0.40), (0.12, -0.34))):
        cone(f"Dent_{t}{i}", C, (s * x, y, 0.70), (s * x, y - 0.005, 0.675), 0.011, material="Dents", seg=5, rings=2)

# --- collerette de fourrure ---
k = 0
for a in range(-150, 151, 20):
    th = math.radians(a)
    d = Vector((math.sin(th), -math.cos(th), 0))
    base = Vector((0, -0.05, 0.61)) + d * 0.14
    tip = base + d * 0.10 + Vector((0, 0, -0.09 - 0.05 * math.cos(th)))
    cone(f"Fourrure_{k}", C, base, tip, 0.06, material="Fourrure", seg=5, rings=3); k += 1
for i, x in enumerate((-0.06, 0.0, 0.06)):
    cone(f"Barbe_{i}", C, (x, -0.17, 0.56), (x * 0.6, -0.20, 0.42 + abs(x)), 0.055, material="Fourrure", seg=5, rings=3)

# --- plaques de roche sur le dos ---
spine = [(0, 0.02, 0.70), (0, 0.10, 0.64), (0, 0.17, 0.57), (0, 0.24, 0.48), (0, 0.32, 0.38), (0, 0.42, 0.30), (0, 0.52, 0.23), (0, 0.62, 0.19)]
n = 0
for i, p in enumerate(spine):
    sz = 0.115 * (1 - i / len(spine) * 0.55)
    for off in ((0,), (-0.09, 0.09))[i % 2 if 0 < i < len(spine) - 2 else 0]:
        q = Vector(p) + Vector((off, 0, 0))
        loc, nor = proj(bv_corps, q + Vector((0, 0.05, 0.15)))
        r = rock(f"Roche_{n}", C, (0, 0, 0), (sz * 0.9, sz * 1.15, sz * 0.55), seed=n)
        r.rotation_euler = Vector((0, 0, 1)).rotation_difference(nor).to_euler()
        r.location = loc + nor * sz * 0.3
        n += 1

# --- taches sombres ---
for i, (p, sz) in enumerate([((0.15, -0.02, 0.92), (0.035, 0.028)), ((0.19, -0.10, 0.88), (0.03, 0.025)), ((0.06, -0.06, 0.99), (0.03, 0.025)),
                             ((0.20, -0.22, 0.76), (0.022, 0.02)), ((0.0, 0.0, 1.0), (0.03, 0.03))]):
    for s in (1, -1):
        patch(f"TacheTete_{i}_{s}", C, bv_tete, (p[0] * s, p[1], p[2]), sz, material="Taches", flat=0.1, rot=rnd.uniform(0, 90))
bv_cuisse = bvh_of([o for o in C.objects if o.name.startswith("Cuisse")])
for i, (p, sz) in enumerate([((0.25, 0.04, 0.32), (0.035, 0.045)), ((0.24, 0.10, 0.22), (0.03, 0.04)), ((0.25, -0.02, 0.22), (0.025, 0.035)), ((0.23, 0.14, 0.30), (0.02, 0.025))]):
    for s in (1, -1):
        patch(f"TacheCuisse_{i}_{s}", C, bv_cuisse, (p[0] * s, p[1], p[2]), sz, material="Taches", flat=0.1, rot=rnd.uniform(0, 90))

# --- lave : taches sur les flancs, veines sur le ventre et la queue ---
lave = [((0.20, 0.16, 0.50), (0.03, 0.022)), ((0.21, 0.22, 0.43), (0.025, 0.03)), ((0.17, 0.28, 0.48), (0.03, 0.02)),
        ((0.20, 0.08, 0.56), (0.022, 0.018)), ((0.14, 0.38, 0.32), (0.025, 0.02)), ((0.11, 0.46, 0.26), (0.022, 0.016)),
        ((0.08, 0.56, 0.20), (0.018, 0.014)), ((0.21, 0.30, 0.40), (0.02, 0.015))]
for i, (p, sz) in enumerate(lave):
    for s in (1, -1):
        patch(f"LaveTache_{i}_{s}", C, bv_corps, (p[0] * s, p[1], p[2]), sz, material="Lave", flat=0.25, rot=rnd.uniform(0, 180), lift=0.002)
for s in (1, -1):
    vein(f"LaveVentre_{s}", C, bv_corps, [(s * 0.05, -0.20, 0.30), (s * 0.12, -0.16, 0.27), (s * 0.18, -0.10, 0.28), (s * 0.22, -0.02, 0.33)], width=0.012)
    vein(f"LaveVentreB_{s}", C, bv_corps, [(s * 0.12, -0.16, 0.27), (s * 0.14, -0.16, 0.36), (s * 0.12, -0.18, 0.44)], width=0.009)
    vein(f"LaveQueue_{s}", C, bv_corps, [(s * 0.08, 0.30, 0.18), (s * 0.08, 0.42, 0.14), (s * 0.06, 0.55, 0.10), (s * 0.03, 0.66, 0.09)], width=0.010)
    vein(f"LaveFlancB_{s}", C, bv_corps, [(s * 0.24, 0.10, 0.36), (s * 0.22, 0.12, 0.46), (s * 0.20, 0.08, 0.53)], width=0.009)
    vein(f"LaveFlancC_{s}", C, bv_corps, [(s * 0.23, 0.18, 0.34), (s * 0.18, 0.24, 0.22)], width=0.008)
    vein(f"LavePoitrail_{s}", C, bv_corps, [(s * 0.17, -0.10, 0.50), (s * 0.20, -0.04, 0.44), (s * 0.22, 0.02, 0.40)], width=0.009)
    vein(f"LaveFlanc_{s}", C, bv_corps, [(s * 0.22, 0.02, 0.30), (s * 0.24, 0.10, 0.36), (s * 0.23, 0.18, 0.34), (s * 0.20, 0.26, 0.28)], width=0.010)

par = {}
dg = bpy.context.evaluated_depsgraph_get()
for o in C.objects:
    m = o.data.materials[0].name
    par[m] = par.get(m, 0) + sum(len(p.vertices) - 2 for p in o.data.polygons)
result = {"objets": len(C.objects), "triangles": tris(C), "par_mat": par}
