# Assemble les images rendues dans Blender en planches de 1024 px pour Roblox (Tifazelts.Sprite).
# - images retournées horizontalement (l'adversaire regarde vers la gauche, l'allié vers la droite) ;
# - toutes les images d'une vue recadrées sur le même rectangle et calées en bas (les pieds ne bougent pas) ;
# - réduction en alpha prémultiplié : pas de liseré sombre sur les bords ;
# - cases carrées 512 x 512 (2 x 2 par planche), ou 1024 x 512 (1 x 2) pour une créature allongée.
# Usage : python3 planches.py <dossier des images> <dossier de sortie> <Espece> [suffixe]
import sys, glob, json, os
from PIL import Image, ImageFilter, ImageChops
dossier, sortie, espece = sys.argv[1], sys.argv[2], sys.argv[3]
suffixe = sys.argv[4] if len(sys.argv) > 4 else ""
os.makedirs(sortie, exist_ok=True)
MARGE = 10
CONTOUR = 5                      # épaisseur du contour en pixels de case (0 = aucun)
COULEUR_CONTOUR = (59, 42, 34)   # brun encre de la DA

def contourner(case):
    # contour régulier tracé en 2D : silhouette dilatée, bords adoucis, sous l'image
    if CONTOUR <= 0:
        return case
    a = case.getchannel("A")
    dil = a.point(lambda v: 255 if v > 40 else 0).filter(ImageFilter.MaxFilter(2 * CONTOUR + 1)).filter(ImageFilter.GaussianBlur(0.9))
    fond = Image.new("RGBA", case.size, COULEUR_CONTOUR + (0,))
    fond.putalpha(dil)
    fond.alpha_composite(case)
    return fond
meta = {}
for vue in ("face", "dos"):
    fichiers = sorted(glob.glob(os.path.join(dossier, vue + "_*.png")))
    ims = [Image.open(f).convert("RGBA").transpose(Image.FLIP_LEFT_RIGHT) for f in fichiers]
    bb = None
    for im in ims:
        b = im.getchannel("A").point(lambda a: 255 if a > 4 else 0).getbbox()
        bb = b if bb is None else (min(bb[0], b[0]), min(bb[1], b[1]), max(bb[2], b[2]), max(bb[3], b[3]))
    w, h = bb[2] - bb[0], bb[3] - bb[1]
    if w / h > 1.4:
        CL, CH, COLS, LIGS = 1024, 512, 1, 2
    else:
        CL, CH, COLS, LIGS = 512, 512, 2, 2
    k = min((CL - 2 * MARGE) / w, (CH - 2 * MARGE) / h)
    nw, nh = round(w * k), round(h * k)
    cases = []
    for im in ims:
        c = im.crop(bb).convert("RGBa").resize((nw, nh), Image.LANCZOS).convert("RGBA")
        case = Image.new("RGBA", (CL, CH), (0, 0, 0, 0))
        case.alpha_composite(c, ((CL - nw) // 2, CH - MARGE - nh))
        cases.append(contourner(case))
    par = COLS * LIGS
    planches = []
    for p in range(0, len(cases), par):
        pl = Image.new("RGBA", (CL * COLS, CH * LIGS), (0, 0, 0, 0))
        for j, case in enumerate(cases[p:p + par]):
            pl.alpha_composite(case, ((j % COLS) * CL, (j // COLS) * CH))
        nom = "%s_%s_%d%s.png" % (espece, vue, p // par + 1, suffixe)
        pl.save(os.path.join(sortie, nom))
        planches.append(nom)
    meta[vue] = {"planches": planches, "images": len(cases), "caseL": CL, "caseH": CH, "colonnes": COLS, "lignes": LIGS,
                 "contenuL": nw, "contenuH": nh}
    gif = []
    for case in cases:
        f = Image.new("RGBA", (CL, CH), (226, 236, 214, 255)); f.alpha_composite(case); gif.append(f.convert("RGB"))
    gif[0].save(os.path.join(sortie, "%s_%s_apercu.gif" % (espece, vue)), save_all=True, append_images=gif[1:], duration=125, loop=0)
json.dump(meta, open(os.path.join(sortie, espece + "_sprites.json"), "w"), indent=1)
print(json.dumps(meta))
