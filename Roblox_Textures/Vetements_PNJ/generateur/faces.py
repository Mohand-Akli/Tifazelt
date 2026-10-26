"""24 visages classiques (décalcomanie de tête Roblox), 512x512 transparents."""
import os, sys, math
from PIL import Image, ImageDraw, ImageFont

N = 512
SS = 3
K = (28, 24, 26, 255)      # trait
WHITE = (255, 255, 255, 255)


class Face:
    def __init__(self):
        self.im = Image.new("RGBA", (N * SS, N * SS), (0, 0, 0, 0))
        self.d = ImageDraw.Draw(self.im)

    def p(self, x, y):
        return (x * SS, y * SS)

    def ell(self, x0, y0, x1, y1, fill=None, outline=None, w=0):
        self.d.ellipse([self.p(x0, y0), self.p(x1, y1)], fill=fill, outline=outline, width=int(w * SS))

    def arc(self, x0, y0, x1, y1, a0, a1, col=K, w=10):
        self.d.arc([self.p(x0, y0), self.p(x1, y1)], a0, a1, fill=col, width=int(w * SS))
        # bouts arrondis
        cx, cy, rx, ry = (x0 + x1) / 2, (y0 + y1) / 2, (x1 - x0) / 2 - w / 2, (y1 - y0) / 2 - w / 2
        for a in (a0, a1):
            r = math.radians(a)
            px, py = cx + rx * math.cos(r), cy + ry * math.sin(r)
            self.ell(px - w / 2, py - w / 2, px + w / 2, py + w / 2, fill=col)

    def line(self, pts, col=K, w=10):
        self.d.line([self.p(*q) for q in pts], fill=col, width=int(w * SS), joint="curve")
        for q in (pts[0], pts[-1]):
            self.ell(q[0] - w / 2, q[1] - w / 2, q[0] + w / 2, q[1] + w / 2, fill=col)

    def poly(self, pts, col):
        self.d.polygon([self.p(*q) for q in pts], fill=col)

    def save(self, path):
        self.im.resize((N, N), Image.LANCZOS).save(path, optimize=True)


EX = (196, 316)  # centres des yeux (gauche, droite à l'écran)
EY = 228


def eyes(f, kind, iris=None, size=1.0):
    for cx in EX:
        if kind == "points":
            r = 17 * size
            f.ell(cx - r, EY - r * 1.25, cx + r, EY + r * 1.25, fill=K)
            f.ell(cx - r * 0.2, EY - r * 0.9, cx + r * 0.45, EY - r * 0.25, fill=WHITE)
        elif kind == "ovales":
            rx, ry = 20 * size, 30 * size
            f.ell(cx - rx, EY - ry, cx + rx, EY + ry, fill=WHITE, outline=K, w=6)
            ic = iris or K
            f.ell(cx - rx * 0.62, EY - ry * 0.35, cx + rx * 0.62, EY + ry * 0.75, fill=ic)
            f.ell(cx - rx * 0.32, EY - ry * 0.05, cx + rx * 0.32, EY + ry * 0.48, fill=K)
            f.ell(cx - rx * 0.05, EY - ry * 0.12, cx + rx * 0.38, EY + ry * 0.18, fill=WHITE)
        elif kind == "grands":
            rx, ry = 26, 34
            f.ell(cx - rx, EY - ry, cx + rx, EY + ry, fill=K)
            if iris:
                f.ell(cx - rx * 0.7, EY - ry * 0.4, cx + rx * 0.7, EY + ry * 0.8, fill=iris)
                f.ell(cx - rx * 0.4, EY - ry * 0.1, cx + rx * 0.4, EY + ry * 0.55, fill=K)
            f.ell(cx - 3, EY - ry * 0.7, cx + 14, EY - ry * 0.2, fill=WHITE)
            f.ell(cx - 14, EY + ry * 0.2, cx - 5, EY + ry * 0.45, fill=WHITE)
        elif kind == "fermes":   # yeux rieurs ^ ^
            f.arc(cx - 24, EY - 14, cx + 24, EY + 26, 200, 340, K, 10)
        elif kind == "fatigues":
            r = 16
            f.ell(cx - r, EY - r * 0.9, cx + r, EY + r * 1.2, fill=K)
            f.poly([(cx - 30, EY - 30), (cx + 30, EY - 30), (cx + 30, EY - 2), (cx - 30, EY - 2)], (0, 0, 0, 0))
            f.d.rectangle([f.p(cx - 30, EY - 30), f.p(cx + 30, EY - 1)], fill=(0, 0, 0, 0))
            f.line([(cx - 22, EY - 1), (cx + 22, EY - 1)], K, 8)
        elif kind == "amande":
            f.d.chord([f.p(cx - 26, EY - 22), f.p(cx + 26, EY + 26)], 180, 360, fill=K)
            f.d.chord([f.p(cx - 26, EY - 4), f.p(cx + 26, EY + 10)], 0, 180, fill=K)
            f.ell(cx - 2, EY - 12, cx + 10, EY - 2, fill=WHITE)
            f.line([(cx + 22, EY - 2), (cx + 32, EY - 10)], K, 6)
    if kind == "clin":
        cx = EX[0]
        r = 17
        f.ell(cx - r, EY - r * 1.25, cx + r, EY + r * 1.25, fill=K)
        f.ell(cx - 3, EY - 15, cx + 8, EY - 4, fill=WHITE)
        f.arc(EX[1] - 24, EY - 14, EX[1] + 24, EY + 26, 200, 340, K, 10)


def brows(f, kind):
    if kind is None:
        return
    for i, cx in enumerate(EX):
        s = -1 if i == 0 else 1
        if kind == "fins":
            f.arc(cx - 26, EY - 66, cx + 26, EY - 26, 220, 320, K, 7)
        elif kind == "epais":
            f.line([(cx - 26 * s * -1 if False else cx - 24, EY - 50 + (4 if s < 0 else 0)),
                    (cx + 24, EY - 50 + (0 if s < 0 else 4))], K, 13)
        elif kind == "leves":
            f.arc(cx - 26, EY - 84, cx + 26, EY - 40, 210, 330, K, 8)
        elif kind == "fronces":
            inner = cx + 22 if s < 0 else cx - 22
            outer = cx - 24 if s < 0 else cx + 24
            f.line([(outer, EY - 58), (inner, EY - 44)], K, 10)
        elif kind == "inquiets":
            inner = cx + 22 if s < 0 else cx - 22
            outer = cx - 24 if s < 0 else cx + 24
            f.line([(outer, EY - 44), (inner, EY - 60)], K, 8)


MY = 330


def mouth(f, kind, lips=None):
    cx = 256
    if kind == "sourire":
        f.arc(cx - 62, MY - 60, cx + 62, MY + 34, 25, 155, K, 10)
    elif kind == "petit":
        f.arc(cx - 34, MY - 36, cx + 34, MY + 16, 30, 150, K, 9)
    elif kind == "grand":
        f.d.chord([f.p(cx - 66, MY - 64), f.p(cx + 66, MY + 40)], 10, 170, fill=K)
        f.d.chord([f.p(cx - 52, MY - 30), f.p(cx + 52, MY + 4)], 0, 180, fill=WHITE)
        f.d.rectangle([f.p(cx - 60, MY - 30), f.p(cx + 60, MY - 14)], fill=(0, 0, 0, 0))
        f.d.chord([f.p(cx - 66, MY - 64), f.p(cx + 66, MY + 40)], 10, 170, outline=K, width=6 * SS)
        f.ell(cx - 22, MY + 12, cx + 22, MY + 34, fill=(214, 96, 104, 255))
    elif kind == "rire":
        f.d.chord([f.p(cx - 58, MY - 50), f.p(cx + 58, MY + 50)], 0, 180, fill=K)
        f.ell(cx - 26, MY + 18, cx + 26, MY + 46, fill=(214, 96, 104, 255))
        f.d.rectangle([f.p(cx - 48, MY - 2), f.p(cx + 48, MY + 8)], fill=WHITE)
    elif kind == "neutre":
        f.line([(cx - 30, MY), (cx + 30, MY)], K, 9)
    elif kind == "moue":
        f.arc(cx - 34, MY - 4, cx + 34, MY + 40, 205, 335, K, 9)
    elif kind == "o":
        f.ell(cx - 16, MY - 20, cx + 16, MY + 18, fill=K)
    elif kind == "en_coin":
        f.arc(cx - 50, MY - 50, cx + 50, MY + 20, 20, 110, K, 9)
        f.line([(cx - 34, MY + 4), (cx - 4, MY + 10)], K, 8)
    elif kind == "dents":
        f.d.rounded_rectangle([f.p(cx - 44, MY - 8), f.p(cx + 44, MY + 22)], 14 * SS, fill=WHITE, outline=K, width=6 * SS)
        f.line([(cx - 40, MY + 7), (cx + 40, MY + 7)], K, 4)
    if lips and kind in ("sourire", "petit", "neutre", "moue"):
        # rouge à lèvres léger par-dessus le trait
        pass


def extras(f, ex):
    for e in ex:
        if e == "joues":
            for cx in (156, 356):
                f.ell(cx - 30, 280, cx + 30, 306, fill=(240, 120, 130, 110))
        elif e == "rousseur":
            for cx, s in ((168, -1), (344, 1)):
                for dx, dy in ((-16, 0), (0, 10), (14, -4), (-6, 18), (10, 22)):
                    f.ell(cx + dx * s - 4, 282 + dy - 4, cx + dx * s + 4, 282 + dy + 4, fill=(165, 95, 60, 200))
        elif e == "cils":
            for i, cx in enumerate(EX):
                s = -1 if i == 0 else 1
                f.line([(cx + 20 * s, EY - 20), (cx + 32 * s, EY - 32)], K, 6)
                f.line([(cx + 10 * s, EY - 28), (cx + 16 * s, EY - 42)], K, 6)
        elif e == "lunettes_rondes":
            for cx in EX:
                f.ell(cx - 40, EY - 40, cx + 40, EY + 40, outline=(70, 50, 40, 255), w=9)
            f.arc(226, EY - 18, 286, EY + 14, 200, 340, (70, 50, 40, 255), 8)
        elif e == "lunettes_carrees":
            for cx in EX:
                f.d.rounded_rectangle([f.p(cx - 42, EY - 30), f.p(cx + 42, EY + 32)], 10 * SS,
                                      outline=(30, 30, 34, 255), width=10 * SS, fill=(160, 200, 230, 50))
            f.line([(238, EY - 6), (274, EY - 6)], (30, 30, 34, 255), 9)
        elif e == "moustache":
            col = (90, 60, 40, 255)
            f.d.chord([f.p(196, MY - 52), f.p(258, MY - 6)], 180, 360, fill=col)
            f.d.chord([f.p(254, MY - 52), f.p(316, MY - 6)], 180, 360, fill=col)
        elif e == "moustache_grise":
            col = (200, 200, 205, 255)
            f.d.chord([f.p(196, MY - 52), f.p(258, MY - 6)], 180, 360, fill=col)
            f.d.chord([f.p(254, MY - 52), f.p(316, MY - 6)], 180, 360, fill=col)
        elif e == "barbe":
            col = (90, 62, 42, 255)
            f.d.chord([f.p(140, 210), f.p(372, 450)], 0, 180, fill=col)
            f.d.chord([f.p(200, MY - 36), f.p(312, MY + 40)], 0, 180, fill=(0, 0, 0, 0))
        elif e == "barbe_grise":
            col = (210, 210, 214, 255)
            f.d.chord([f.p(150, 230), f.p(362, 450)], 0, 180, fill=col)
            f.d.chord([f.p(206, MY - 30), f.p(306, MY + 34)], 0, 180, fill=(0, 0, 0, 0))
        elif e == "grain":
            for x in range(170, 344, 12):
                for y in range(350, 410, 12):
                    if (x - 256) ** 2 / 90 ** 2 + (y - 330) ** 2 / 80 ** 2 < 1 and abs(x - 256) > 10 or y > 372:
                        f.ell(x - 2, y - 2, x + 2, y + 2, fill=(70, 60, 55, 120))
        elif e == "rides":
            f.arc(130, EY - 20, 170, EY + 30, 120, 220, (120, 90, 80, 200), 4)
            f.arc(342, EY - 20, 382, EY + 30, 320, 420, (120, 90, 80, 200), 4)
            f.arc(190, MY - 70, 230, MY - 10, 120, 200, (120, 90, 80, 160), 4)
            f.arc(282, MY - 70, 322, MY - 10, 340, 420, (120, 90, 80, 160), 4)
        elif e == "cernes":
            for cx in EX:
                f.arc(cx - 22, EY + 8, cx + 22, EY + 40, 20, 160, (130, 100, 110, 150), 4)
        elif e == "rouge":
            f.arc(256 - 62, MY - 60, 256 + 62, MY + 34, 40, 140, (190, 60, 80, 255), 6)
        elif e == "grain_beaute":
            f.ell(318, 300, 328, 310, fill=(80, 50, 40, 255))
        elif e == "pansement":
            f.d.rounded_rectangle([f.p(330, 280), f.p(388, 300)], 6 * SS, fill=(230, 190, 150, 255), outline=(180, 140, 110, 255), width=3 * SS)
            f.line([(346, 285), (346, 295)], (180, 140, 110, 255), 2); f.line([(372, 285), (372, 295)], (180, 140, 110, 255), 2)


BLEU, VERT, NOISETTE, GRIS = (70, 130, 200, 255), (80, 150, 90, 255), (140, 95, 50, 255), (120, 130, 140, 255)
FACES = [
    ("Sourire classique", dict(y="points", b=None, m="sourire")),
    ("Content", dict(y="points", b="fins", m="grand")),
    ("Rieur", dict(y="fermes", b="leves", m="rire", e=["joues"])),
    ("Timide", dict(y="points", b="inquiets", m="petit", e=["joues"])),
    ("Malicieux", dict(y="clin", b="fins", m="en_coin")),
    ("Rousseur", dict(y="ovales", i=VERT, b="fins", m="sourire", e=["rousseur"])),
    ("Yeux bleus", dict(y="ovales", i=BLEU, b="fins", m="petit", e=["cils"])),
    ("Regard doux", dict(y="amande", b="fins", m="petit", e=["cils", "rouge"])),
    ("Pétillante", dict(y="grands", i=NOISETTE, b="leves", m="grand", e=["cils", "joues"])),
    ("Sérieux", dict(y="points", b="epais", m="neutre")),
    ("Bourru", dict(y="points", b="fronces", m="moue")),
    ("Étonné", dict(y="ovales", i=NOISETTE, b="leves", m="o")),
    ("Endormi", dict(y="fatigues", b="fins", m="neutre", e=["cernes"])),
    ("Lunettes rondes", dict(y="points", b="fins", m="sourire", e=["lunettes_rondes"])),
    ("Lunettes carrées", dict(y="points", b="epais", m="petit", e=["lunettes_carrees"])),
    ("Moustachu", dict(y="points", b="epais", m="sourire", e=["moustache"])),
    ("Barbu", dict(y="points", b="epais", m="sourire", e=["barbe"])),
    ("Barbe de trois jours", dict(y="amande", b="fins", m="en_coin", e=["grain"])),
    ("Grand-père", dict(y="fermes", b="fins", m="sourire", e=["moustache_grise", "rides"])),
    ("Grand-mère", dict(y="points", b="fins", m="sourire", e=["lunettes_rondes", "rides", "joues"])),
    ("Vieux marin", dict(y="fatigues", b="epais", m="neutre", e=["barbe_grise", "rides"])),
    ("Enfant espiègle", dict(y="grands", b="leves", m="dents", e=["pansement", "rousseur"])),
    ("Enfant joyeux", dict(y="grands", b=None, m="rire", e=["joues"])),
    ("Sage", dict(y="ovales", i=GRIS, b="fins", m="petit", e=["grain_beaute"])),
]


def build(spec):
    f = Face()
    if spec.get("y") != "clin":
        eyes(f, spec["y"], spec.get("i"))
    else:
        eyes(f, "clin")
    brows(f, spec.get("b"))
    ex = spec.get("e", [])
    pre = [e for e in ex if e in ("barbe", "barbe_grise", "grain")]
    extras(f, pre)
    mouth(f, spec["m"])
    extras(f, [e for e in ex if e not in pre])
    return f


if __name__ == "__main__":
    import unicodedata, re
    out = sys.argv[1]
    os.makedirs(out + "/Visages", exist_ok=True)
    tiles = []
    for i, (name, spec) in enumerate(FACES, 1):
        s = re.sub(r"[^A-Za-z0-9]+", "_", unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()).strip("_")
        p = f"{out}/Visages/V{i:02d}_{s}.png"
        build(spec).save(p)
        tiles.append((f"V{i:02d} {name}", p))
    cols = 6
    sheet = Image.new("RGB", (cols * 220, 4 * 250 + 50), (238, 240, 244))
    d = ImageDraw.Draw(sheet)
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 15)
    d.text((14, 12), "24 visages (sur une tête couleur peau)", fill=(30, 30, 40),
           font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24))
    for n, (lab, p) in enumerate(tiles):
        x, y = (n % cols) * 220 + 10, (n // cols) * 250 + 50
        head = Image.new("RGBA", (200, 200), (0, 0, 0, 0))
        ImageDraw.Draw(head).rounded_rectangle([0, 0, 199, 199], 46, fill=(234, 192, 160, 255))
        head.alpha_composite(Image.open(p).resize((200, 200), Image.LANCZOS))
        sheet.paste(head, (x, y), head)
        d.text((x, y + 206), lab, fill=(30, 30, 40), font=font)
    sheet.save(out + "/apercu_visages.jpg", quality=90)
