# Portraits des dauphins (rendu brut, vue de face rapprochée sur la tête et les épaules, pose de repos) ; ensuite Cramosaur/Scripts/portrait.py.
# Usage : blender -b Rendu_Sprites_Dauphin.blend --python rendre_portraits.py -- <sortie> [sat] [valeur] [lave]
import bpy, sys, os, math
sys.path.insert(0, "/Users/mohand-aklizidani/Desktop/Tifazelt/11 - Développement/Modèles 3D/Dauphin/Scripts")
import dauphin_lib as D
a = sys.argv[sys.argv.index("--") + 1:]
sortie = a[0]; sat = float(a[1]) if len(a) > 1 else 1.3; val = float(a[2]) if len(a) > 2 else 1.0; lave = float(a[3]) if len(a) > 3 else 0.0
os.makedirs(sortie, exist_ok=True)
sc = bpy.data.scenes["Sprites"]; bpy.context.window.scene = sc
sc.render.resolution_x = sc.render.resolution_y = 1024
pivot = bpy.data.objects["Sp_Pivot"]
ECH = 0.55
# les lumières sont accrochées au pivot : en le réduisant, elles se rapprochent ; on compense leur puissance (carré de la distance)
for n in ("Sp_Cle", "Sp_Remplissage", "Sp_Contour1", "Sp_Contour2"):
    bpy.data.objects[n].data.energy *= ECH * ECH
CIBLE = {"Dauphimyst": (0, -0.24, 0.12), "Dauphiclos": (0, -0.26, 0.12), "Dauphiracle": (0, -0.22, 0.1)}
for e in CIBLE:
    for o in CIBLE:
        bpy.data.objects[o].hide_render = (o != e); bpy.data.objects[o + "_Rig"].hide_render = (o != e)
    nt = bpy.data.materials[e + "_sprite"].node_tree
    nt.nodes["Sp_Saturation"].inputs["Saturation"].default_value = sat
    nt.nodes["Sp_Saturation"].inputs["Value"].default_value = val
    nt.nodes["BSDF guidée"].inputs["Emission Strength"].default_value = lave
    pivot.location = CIBLE[e]; pivot.scale = (ECH, ECH, ECH); pivot.rotation_euler = (0, 0, math.pi)
    D.appliquer(bpy.data.objects[e + "_Rig"], D.pose_flotte(e, 0.0, 1.0), e)
    bpy.context.view_layer.update()
    sc.render.filepath = os.path.join(sortie, e + "_portrait_brut.png")
    bpy.ops.render.render(write_still=True)
print("FINI")
