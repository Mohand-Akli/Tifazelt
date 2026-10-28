# Masque des motifs lumineux (spirales roses / violet vif) : blanc = lumineux. Usage : python3 motifs.py <Textures> <sortie>
import sys, os
from PIL import Image, ImageChops, ImageFilter
src, dst = sys.argv[1], sys.argv[2]
for n in ("Dauphimyst", "Dauphiclos", "Dauphiracle"):
    im = Image.open(os.path.join(src, n + "_cuit_couleur.png")).convert("RGB").resize((1024, 1024), Image.LANCZOS)
    h, s, v = im.convert("HSV").split()
    # rose / magenta (teinte 0-255 : environ 190 à 245), saturé, assez clair
    mh = h.point(lambda x: 255 if 205 <= x <= 240 else 0)
    ms = s.point(lambda x: 0 if x < 60 else min(255, (x - 60) * 4))
    mv = v.point(lambda x: 0 if x < 170 else min(255, (x - 170) * 5))
    m = ImageChops.multiply(ImageChops.multiply(mh, ms), mv).filter(ImageFilter.GaussianBlur(1.2))
    m.save(os.path.join(dst, n + "_motifs.png")); print(n, sum(m.histogram()[128:]) / (1024 * 1024))
