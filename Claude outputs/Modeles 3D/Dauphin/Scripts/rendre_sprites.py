# Rend les images de sprite des dauphins. Usage : blender -b Rendu_Sprites_Dauphin.blend --python rendre_sprites.py -- <sortie> <images> <vue|toutes> <espece|toutes> [sat] [valeur] [lave] [variante]
# Boucle de respiration = « flotte » (Animation.lua), une période en <images> images, amplitude 1,4.
import bpy, sys, os, math
sys.path.insert(0, "/Users/mohand-aklizidani/Desktop/Tifazelt/Claude outputs/Modeles 3D/Dauphin/Scripts")
import dauphin_lib as D
a = sys.argv[sys.argv.index("--") + 1:]
sortie, N, vues, especes = a[0], int(a[1]), a[2], a[3]
sat = float(a[4]) if len(a) > 4 else 1.6
val = float(a[5]) if len(a) > 5 else 1.0
lave = float(a[6]) if len(a) > 6 else 0.0
variante = a[7] if len(a) > 7 else ""      # chemin d'une image de couleur de remplacement (variante E)
AMP = 1.4
Z_PIVOT = 0.15   # les dauphins flottent plus bas dans le cadre que les Cramosaur (pieds à z = 0)
os.makedirs(sortie, exist_ok=True)
sc = bpy.data.scenes["Sprites"]; bpy.context.window.scene = sc
sc.render.resolution_x = sc.render.resolution_y = 1024
sc.render.film_transparent = True
pivot = bpy.data.objects["Sp_Pivot"]; pivot.location.z = Z_PIVOT
LISTE = ("Dauphimyst", "Dauphiclos", "Dauphiracle") if especes == "toutes" else (especes,)
for e in LISTE:
    for o in ("Dauphimyst", "Dauphiclos", "Dauphiracle"):
        bpy.data.objects[o].hide_render = (o != e); bpy.data.objects[o + "_Rig"].hide_render = (o != e)
    m = bpy.data.materials[e + "_sprite"]; nt = m.node_tree
    nt.nodes["Sp_Saturation"].inputs["Saturation"].default_value = sat
    nt.nodes["Sp_Saturation"].inputs["Value"].default_value = val
    bsdf = nt.nodes["BSDF guidée"]
    bsdf.inputs["Emission Strength"].default_value = lave
    if variante:
        nt.nodes["Tex_E"].image = bpy.data.images.load(variante.replace("{e}", e))
        nt.nodes["Sp_Base"].inputs["Factor"].default_value = 1.0
    rig = bpy.data.objects[e + "_Rig"]
    for vue in (("face", "dos") if vues == "toutes" else (vues,)):
        pivot.rotation_euler = (0, 0, 0 if vue == "dos" else math.pi)
        for i in range(N):
            w = 2 * math.pi * i / N
            D.appliquer(rig, D.pose_flotte(e, w, AMP), e)
            bpy.context.view_layer.update()
            sc.render.filepath = os.path.join(sortie, "%s_%s_%02d.png" % (e, vue, i + 1))
            bpy.ops.render.render(write_still=True)
print("FINI")
