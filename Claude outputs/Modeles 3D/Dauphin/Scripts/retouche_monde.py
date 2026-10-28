# Texture du monde (SA_Retouche) des dauphins : couleur recuite, 1024 px, saturation 0,8 et éclaircissement par espèce (PROVISOIRE).
# Usage : python3 retouche_monde.py <Textures> <sortie> [saturation]
import sys, os
from PIL import Image, ImageEnhance
src, dst = sys.argv[1], sys.argv[2]
sat = float(sys.argv[3]) if len(sys.argv) > 3 else 1.3
ECLAIRCIR = {"Dauphimyst": 1.1, "Dauphiclos": 1.25, "Dauphiracle": 1.45}
for n in ("Dauphimyst", "Dauphiclos", "Dauphiracle"):
    im = Image.open(os.path.join(src, n + "_cuit_couleur.png")).convert("RGB").resize((1024, 1024), Image.LANCZOS)
    im = ImageEnhance.Color(im).enhance(sat)
    # la lumière de Roblox assombrit les violets : on éclaircit (gamma), plus pour les stades sombres (PROVISOIRE)
    g = ECLAIRCIR.get(n, 1.0)
    im = im.point(lambda x: round(255 * (x / 255) ** (1 / g)))
    im.save(os.path.join(dst, n + "_cuit_retouche.png")); print("ok", n)
