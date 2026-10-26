# Icônes / sprites d'objet : images rendues dans Blender (même cadrage), recadrées ensemble sur le même rectangle,
# carrées, calées en bas, contour encre 2D en anneau (le verre transparent reste transparent).
# Usage : python3 icone.py <taille> <contour> <sortie1> <rendu1> [<sortie2> <rendu2> ...]
import sys
from PIL import Image, ImageFilter, ImageChops
T, CONTOUR = int(sys.argv[1]), int(sys.argv[2])
paires = list(zip(sys.argv[3::2], sys.argv[4::2]))
COUL, MARGE = (59, 42, 34), CONTOUR + 6
ims = [Image.open(src).convert("RGBA") for _, src in paires]
bb = None
for im in ims:
    b = im.getchannel("A").point(lambda a: 255 if a > 6 else 0).getbbox()
    bb = b if bb is None else (min(bb[0], b[0]), min(bb[1], b[1]), max(bb[2], b[2]), max(bb[3], b[3]))
w, h = bb[2] - bb[0], bb[3] - bb[1]
k = (T - 2 * MARGE) / max(w, h)
for (dst, _), im in zip(paires, ims):
    c = im.crop(bb).convert("RGBa").resize((round(w * k), round(h * k)), Image.LANCZOS).convert("RGBA")
    case = Image.new("RGBA", (T, T), (0, 0, 0, 0))
    case.alpha_composite(c, ((T - c.width) // 2, T - MARGE - c.height))
    dur = case.getchannel("A").point(lambda v: 255 if v > 40 else 0)
    dil = dur.filter(ImageFilter.MaxFilter(2 * CONTOUR + 1)).filter(ImageFilter.GaussianBlur(0.8))
    interieur = dur.filter(ImageFilter.MinFilter(3))
    anneau = ImageChops.subtract(dil, interieur)
    fond = Image.new("RGBA", (T, T), COUL + (0,)); fond.putalpha(anneau); fond.alpha_composite(case)
    fond.save(dst)
