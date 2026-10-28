# Variantes de couleur des v04 (27 oct. 2026) pour le jeu, à partir des textures recuites.
# Usage : python3 variantes_couleur_v04.py <dossier Textures V04> <dossier de sortie>
# Sorties par espèce (1024 px) :
#   <n>_v04_var_C.png  : « Obsidienne » : corps plus sombre (proche des v03), lave avivée
#   <n>_v04_var_D.png  : « Vive » : retouche actuelle, couleurs plus saturées
#   <n>_v04_lave.png   : masque de la lave (blanc = lave), pour faire luire la lave en jeu
import sys, os
from PIL import Image, ImageChops, ImageEnhance, ImageFilter

src, dst = sys.argv[1], sys.argv[2]
os.makedirs(dst, exist_ok=True)

def masque_lave(im):
    h, s, v = im.convert("HSV").split()
    # teinte rouge-orange (0-255 : < 28 ou > 242), saturée, assez claire
    mh = h.point(lambda x: 255 if (x < 28 or x > 242) else 0)
    ms = s.point(lambda x: 0 if x < 100 else min(255, (x - 100) * 4))
    mv = v.point(lambda x: 0 if x < 80 else min(255, (x - 80) * 3))
    m = ImageChops.multiply(ImageChops.multiply(mh, ms), mv)
    return m.filter(ImageFilter.GaussianBlur(1.2))

def avec_masque(base, modifie, masque):
    return Image.composite(modifie, base, masque)

for n in ("Cramosaur", "Cramoraptor", "Cramorex"):
    couleur = Image.open(os.path.join(src, f"{n}_v04_cuit_couleur.png")).convert("RGB").resize((1024, 1024), Image.LANCZOS)
    retouche = Image.open(os.path.join(src, f"{n}_v04_cuit_retouche.png")).convert("RGB")
    lave = masque_lave(couleur)
    lave.save(os.path.join(dst, f"{n}_v04_lave.png"))

    # C « Obsidienne » : corps assombri (gamma), légèrement désaturé ; lave plus vive
    h, s, v = couleur.convert("HSV").split()
    v_corps = v.point(lambda x: int(255 * (x / 255) ** 1.25 * 0.92))
    s_corps = s.point(lambda x: int(x * 0.85))
    corps = Image.merge("HSV", (h, s_corps, v_corps)).convert("RGB")
    lave_vive = Image.merge("HSV", (h, s.point(lambda x: min(255, int(x * 1.2))), v.point(lambda x: min(255, int(x * 1.2 + 12))))).convert("RGB")
    c = avec_masque(corps, lave_vive, lave)
    c = c.filter(ImageFilter.UnsharpMask(radius=1.6, percent=80, threshold=2))
    ImageEnhance.Contrast(c).enhance(1.05).save(os.path.join(dst, f"{n}_v04_var_C.png"))

    # D « Vive » : retouche actuelle, saturation globale relevée
    d = ImageEnhance.Color(retouche).enhance(1.4)
    ImageEnhance.Contrast(d).enhance(1.06).save(os.path.join(dst, f"{n}_v04_var_D.png"))
    print("ok", n)
