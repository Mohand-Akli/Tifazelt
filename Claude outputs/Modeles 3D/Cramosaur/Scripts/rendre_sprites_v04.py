# Rend les images de sprite (respiration) des Cramosaur v04 depuis V04/Rendu_Sprites_v04.blend (réglage P2 déjà en place).
# Reconstruit le 28 oct. 2026 (le code de pose du 27 oct. n'avait pas été gardé) : boucle « idle » de Tifazelts.Animation,
# une période en <images> images, amplitude 1,6, axes du modèle au repos (comme Bone.Transform dans Studio).
# Usage : blender -b V04/Rendu_Sprites_v04.blend --python rendre_sprites_v04.py -- <sortie> <images> <vue|toutes> <espece|toutes> [indices]
import bpy, sys, os, math
from mathutils import Vector, Quaternion
a = sys.argv[sys.argv.index("--") + 1:]
sortie, N, vues, especes = a[0], int(a[1]), a[2], a[3]
indices = [int(x) for x in a[4].split(",")] if len(a) > 4 else None
AMP = 1.6
os.makedirs(sortie, exist_ok=True)
sc = bpy.data.scenes["Sprites"]; bpy.context.window.scene = sc
pivot = bpy.data.objects["Sp_Pivot"]
Z_PIVOT = pivot.location.z - 0.08   # un peu plus bas qu'au 27 oct. : les pieds touchaient le bord de l'image
TOUTES = ("Cramosaur", "Cramoraptor", "Cramorex")
AVANT = Vector((0, -1, 0)); HAUT = Vector((0, 0, 1)); LAT = HAUT.cross(AVANT)

def pose_idle(w):
    p = {}
    def aj(n, pp=0.0, y=0.0, r=0.0):
        e = p.setdefault(n, [0.0, 0.0, 0.0]); e[0] += pp; e[1] += y; e[2] += r
    aj("Dos1", 0.025 * math.sin(w)); aj("Cou1", -0.03 * math.sin(w + 0.6)); aj("Tete", 0.02 * math.sin(w + 1.2))
    aj("Machoire", 0.03 + 0.02 * math.sin(w + 0.3))
    for i in range(1, 5): aj("Queue%d" % i, y=0.1 * math.sin(w - i * 0.6))
    aj("BrasG1", 0.05 * math.sin(w + 1)); aj("BrasD1", 0.05 * math.sin(w + 1))
    return {n: [v * AMP for v in e] for n, e in p.items()}

def appliquer(rig, pose):
    for pb in rig.pose.bones:
        pb.rotation_mode = "QUATERNION"
        e = pose.get(pb.name)
        if not e: pb.rotation_quaternion = Quaternion((1, 0, 0, 0)); continue
        R = Quaternion(LAT, e[0]) @ Quaternion(HAUT, e[1]) @ Quaternion(AVANT, e[2])
        Rb = pb.bone.matrix_local.to_3x3()
        pb.rotation_quaternion = (Rb.inverted() @ R.to_matrix() @ Rb).to_quaternion()

for e in (TOUTES if especes == "toutes" else (especes,)):
    for o in TOUTES:
        bpy.data.objects[o + "_v04"].hide_render = (o != e); bpy.data.objects[o + "_Rig_v04"].hide_render = (o != e)
    rig = bpy.data.objects[e + "_Rig_v04"]
    # les trois maillages sont placés à x = 0 / 1,6 / 3,2 : la caméra (pivot) est recentrée sur l'espèce, à la même hauteur
    appliquer(rig, {}); bpy.context.view_layer.update()
    ob = bpy.data.objects[e + "_v04"]
    pts = [ob.matrix_world @ Vector(c) for c in ob.bound_box]
    pivot.location = ((min(p.x for p in pts) + max(p.x for p in pts)) / 2, (min(p.y for p in pts) + max(p.y for p in pts)) / 2, Z_PIVOT)
    for vue in (("face", "dos") if vues == "toutes" else (vues,)):
        pivot.rotation_euler = (0, 0, 0 if vue == "dos" else math.pi)
        for i in (indices or range(N)):
            appliquer(rig, pose_idle(2 * math.pi * i / N))
            bpy.context.view_layer.update()
            sc.render.filepath = os.path.join(sortie, "%s_%s_%02d.png" % (e, vue, i + 1))
            bpy.ops.render.render(write_still=True)
print("FINI")
