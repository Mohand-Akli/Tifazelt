# aperçu : le sprite recadré sur le fond vert pâle du combat, à la taille d'affichage
import sys
from PIL import Image
fond = Image.new("RGBA", (1100, 560), (226, 236, 214, 255))
x = 20
for p in sys.argv[2:]:
    im = Image.open(p).convert("RGBA")
    bb = im.getchannel("A").point(lambda a: 255 if a > 8 else 0).getbbox()
    im = im.crop(bb)
    h = 500
    im = im.resize((int(im.width * h / im.height), h), Image.LANCZOS)
    fond.alpha_composite(im, (x, 30))
    x += im.width + 30
fond.convert("RGB").save(sys.argv[1])
