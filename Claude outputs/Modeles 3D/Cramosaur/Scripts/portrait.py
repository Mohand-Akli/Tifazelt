# Portrait de Tifazelt pour Kit.portrait : buste rendu dans Blender, retourné (regarde vers la gauche),
# 512 px, contour encre tracé en 2D autour du Tifazelt, puis découpé en disque aux bords lissés.
# Usage : python3 portrait.py <rendu brut> <sortie>
import sys
from PIL import Image, ImageFilter, ImageDraw
src, dst = sys.argv[1], sys.argv[2]
T, CONTOUR, COUL = 512, 4, (59, 42, 34)
im = Image.open(src).convert("RGBA").transpose(Image.FLIP_LEFT_RIGHT)
im = im.convert("RGBa").resize((T, T), Image.LANCZOS).convert("RGBA")
a = im.getchannel("A")
dil = a.point(lambda v: 255 if v > 40 else 0).filter(ImageFilter.MaxFilter(2 * CONTOUR + 1)).filter(ImageFilter.GaussianBlur(0.8))
fond = Image.new("RGBA", (T, T), COUL + (0,)); fond.putalpha(dil); fond.alpha_composite(im)
# disque lissé (dessiné à 4x puis réduit)
m = Image.new("L", (T * 4, T * 4), 0)
ImageDraw.Draw(m).ellipse((8, 8, T * 4 - 8, T * 4 - 8), fill=255)
m = m.resize((T, T), Image.LANCZOS)
alpha = Image.composite(fond.getchannel("A"), Image.new("L", (T, T), 0), m)
fond.putalpha(alpha)
fond.save(dst)
