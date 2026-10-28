# Retouche de la texture Meshy de Cramosaur : noirs relevés (obsidienne légèrement bleutée), lave plus vive, netteté.
import sys, colorsys
from PIL import Image, ImageFilter, ImageEnhance
src, dst, force = sys.argv[1], sys.argv[2], float(sys.argv[3])
im = Image.open(src).convert("RGB").resize((1024, 1024), Image.LANCZOS)
px = im.load()
W, H = im.size
for y in range(H):
    for x in range(W):
        r, g, b = [c / 255 for c in px[x, y]]
        h, s, v = colorsys.rgb_to_hsv(r, g, b)
        lave = (h < 0.11 or h > 0.95) and s > 0.45 and v > 0.35
        if lave:
            # lave : plus lumineuse, plus saturée, tirée vers l'orange chaud
            v = min(1, v * (1 + 0.35 * force) + 0.05 * force)
            s = min(1, s * (1 + 0.15 * force))
            if h > 0.95: h = h - 1
            h = max(0.0, h + 0.015 * force)
        else:
            # corps : noirs relevés en anthracite, légère teinte froide pour contraster avec la lave
            v = 0.10 * force + v * (1 - 0.10 * force) ** 1
            v = v ** (1 - 0.22 * force)
            if s < 0.25 and v < 0.5:
                h, s = 0.68, max(s, 0.10 * force)
        r, g, b = colorsys.hsv_to_rgb(h % 1, s, v)
        px[x, y] = (int(r * 255), int(g * 255), int(b * 255))
im = im.filter(ImageFilter.UnsharpMask(radius=1.6, percent=int(60 * force + 40), threshold=2))
im = ImageEnhance.Contrast(im).enhance(1 + 0.08 * force)
im.save(dst)
print("ok", dst)
