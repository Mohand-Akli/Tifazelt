# Construit Dauphin/Rendu_Sprites_Dauphin.blend : copie de Cramosaur/V04/Rendu_Sprites_v04.blend (scène « Sprites » : lumières, caméra,
# monde, compositeur) avec les trois dauphins (maillages allégés + armatures de Lignee_Dauphin.blend) et un matériau de sprite copié
# de Cramosaur_v04_cuit (texture, normales, rugosité, variante E, masque lumineux, saturation).
# Usage : blender -b --python construire_rendu_sprites.py
import bpy, os
RACINE = "/Users/mohand-aklizidani/Desktop/Tifazelt/Claude outputs/Modeles 3D"
SRC = RACINE + "/Cramosaur/V04/Rendu_Sprites_v04.blend"
DAU = RACINE + "/Dauphin/Lignee_Dauphin.blend"
OUT = RACINE + "/Dauphin/Rendu_Sprites_Dauphin.blend"
TEX = RACINE + "/Dauphin/Textures/"
ESPECES = ("Dauphimyst", "Dauphiclos", "Dauphiracle")

bpy.ops.wm.open_mainfile(filepath=SRC)
sc = bpy.data.scenes["Sprites"]
bpy.context.window.scene = sc
# tout ce qui existe est caché au rendu (Cramosaur, Tiflask...) : on ne supprime rien
for o in sc.objects:
    if not o.name.startswith("Sp_"):
        o.hide_render = True; o.hide_viewport = True
modele = bpy.data.materials["Cramosaur_v04_cuit"]

with bpy.data.libraries.load(DAU, link=False) as (src, dst):
    dst.objects = [n for e in ESPECES for n in (e, e + "_Rig")]
col = bpy.data.collections.new("Sprites_Dauphin")
sc.collection.children.link(col)
for o in dst.objects:
    col.objects.link(o)
    o.hide_render = False; o.hide_viewport = False
for e in ESPECES:
    rig = bpy.data.objects[e + "_Rig"]
    rig.location = (0, 0, 0)
    mesh = bpy.data.objects[e]
    m = modele.copy(); m.name = e + "_sprite"
    def img(nom, fichier, cs):
        im = bpy.data.images.load(TEX + fichier); im.colorspace_settings.name = cs; m.node_tree.nodes[nom].image = im
    img("Tex_couleur", e + "_cuit_couleur.png", "sRGB")
    img("Tex_normales", e + "_cuit_normales.png", "Non-Color")
    img("Tex_rugosite", e + "_cuit_rugosite.png", "Non-Color")
    img("Tex_E", e + "_cuit_couleur.png", "sRGB")          # variante E = base tant qu'aucune variante n'est choisie
    img("Tex_lave", "Variantes/" + e + "_motifs.png", "Non-Color")
    mesh.data.materials.clear(); mesh.data.materials.append(m)
bpy.ops.wm.save_as_mainfile(filepath=OUT)
print("OK", OUT)
