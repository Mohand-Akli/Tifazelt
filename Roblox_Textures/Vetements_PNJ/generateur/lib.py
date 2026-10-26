"""Bibliothèque de dessin pour les templates Shirt/Pants Roblox (585x559)."""
import math, random
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

W, H = 585, 559
S = 3  # suréchantillonnage (anticrénelage)

TORSO = dict(F=(231, 74, 128, 128), B=(427, 74, 128, 128), R=(165, 74, 64, 128),
             L=(361, 74, 64, 128), U=(231, 8, 128, 64), D=(231, 204, 128, 64))
# bras droit / jambe droite : face L = côté intérieur, R = extérieur
LIMB_R = dict(L=(19, 355, 64, 128), B=(85, 355, 64, 128), R=(151, 355, 64, 128),
              F=(217, 355, 64, 128), U=(217, 289, 64, 64), D=(217, 485, 64, 64))
# bras gauche / jambe gauche : face R = intérieur, L = extérieur
LIMB_L = dict(F=(308, 355, 64, 128), L=(374, 355, 64, 128), B=(440, 355, 64, 128),
              R=(506, 355, 64, 128), U=(308, 289, 64, 64), D=(308, 485, 64, 64))
LIMBS = (LIMB_R, LIMB_L)
SIDES = ("F", "B", "R", "L")
OUTER = {id(LIMB_R): "R", id(LIMB_L): "L"}
INNER = {id(LIMB_R): "L", id(LIMB_L): "R"}

SHADE = dict(F=1.0, B=0.93, R=0.87, L=0.87, U=1.05, D=0.78)


def hexc(h, a=255):
    h = h.lstrip("#")
    return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), a)


def mix(c1, c2, t):
    return tuple(int(round(c1[i] * (1 - t) + c2[i] * t)) for i in range(3)) + (c1[3] if len(c1) > 3 else 255,)


def dark(c, f=0.75):
    return (int(c[0] * f), int(c[1] * f), int(c[2] * f), c[3] if len(c) > 3 else 255)


def light(c, f=0.35):
    return mix(c, (255, 255, 255, 255), f)


class Tpl:
    def __init__(self):
        self.im = Image.new("RGBA", (W * S, H * S), (0, 0, 0, 0))
        self.d = ImageDraw.Draw(self.im)
        self.mask = np.zeros((H * S, W * S), dtype=np.float32)  # facteur d'ombrage
        self.regions = []  # (rect, kind) pour ombrage
        self.over_skin = False

    # ---- coordonnées
    @staticmethod
    def P(face, u, v):
        x, y, w, h = face
        return ((x + u) * S, (y + v) * S)

    def box(self, face, u0, v0, u1, v1):
        x, y, w, h = face
        u0, u1 = max(0, min(w, u0)), max(0, min(w, u1))
        v0, v1 = max(0, min(h, v0)), max(0, min(h, v1))
        return [(x + u0) * S, (y + v0) * S, (x + u1) * S - 1, (y + v1) * S - 1]

    # ---- primitives (coordonnées locales à la face, en pixels du template)
    def rect(self, face, u0, v0, u1, v1, col):
        b = self.box(face, u0, v0, u1, v1)
        if b[2] > b[0] and b[3] > b[1]:
            if len(col) > 3 and col[3] < 255:
                self.clip(face, lambda d: d.rectangle(b, fill=col))
            else:
                self.d.rectangle(b, fill=col)

    def blend_rect(self, b, col):
        layer = Image.new("RGBA", self.im.size, (0, 0, 0, 0))
        ImageDraw.Draw(layer).rectangle(b, fill=col)
        self.im.alpha_composite(layer)

    def clip(self, face, fn):
        """Dessine fn(draw) sur un calque, rogné à la face, puis compose."""
        x, y, w, h = face
        bx, by, bw, bh = x * S, y * S, w * S, h * S
        layer = Image.new("RGBA", (bw, bh), (0, 0, 0, 0))
        dl = ImageDraw.Draw(layer)

        class Off:  # décale les coordonnées absolues vers le calque local
            def __getattr__(_, name):
                f = getattr(dl, name)

                def g(xy, *a, **k):
                    if isinstance(xy, (list, tuple)) and xy and isinstance(xy[0], (list, tuple)):
                        xy = [(p[0] - bx, p[1] - by) for p in xy]
                    elif isinstance(xy, (list, tuple)) and len(xy) == 4:
                        xy = [xy[0] - bx, xy[1] - by, xy[2] - bx, xy[3] - by]
                    return f(xy, *a, **k)
                return g
        fn(Off())
        # ne peindre que là où le vêtement existe déjà (alpha > 0)
        base = self.im.crop((bx, by, bx + bw, by + bh))
        la = np.array(layer)
        ba = np.array(base)
        if not self.over_skin:
            la[..., 3] = np.where(ba[..., 3] > 0, la[..., 3], 0)
        base.alpha_composite(Image.fromarray(la))
        self.im.paste(base, (bx, by))
        self.d = ImageDraw.Draw(self.im)

    def poly(self, face, pts, col):
        self.clip(face, lambda d: d.polygon([self.P(face, u, v) for u, v in pts], fill=col))

    def line(self, face, pts, col, w=1.0):
        self.clip(face, lambda d: d.line([self.P(face, u, v) for u, v in pts], fill=col,
                                          width=max(1, int(w * S)), joint="curve"))

    def ellipse(self, face, u0, v0, u1, v1, col=None, outline=None, w=1.0):
        b = [self.P(face, u0, v0), self.P(face, u1, v1)]
        self.clip(face, lambda d: d.ellipse(b, fill=col, outline=outline, width=max(1, int(w * S))))

    def arc(self, face, u0, v0, u1, v1, a0, a1, col, w=1.0):
        b = [self.P(face, u0, v0), self.P(face, u1, v1)]
        self.clip(face, lambda d: d.arc(b, a0, a1, fill=col, width=max(1, int(w * S))))

    def dashed(self, face, p0, p1, col, w=0.8, dash=3, gap=2):
        (u0, v0), (u1, v1) = p0, p1
        L = math.hypot(u1 - u0, v1 - v0)
        if L == 0:
            return
        t = 0
        segs = []
        while t < L:
            t2 = min(L, t + dash)
            segs.append(((u0 + (u1 - u0) * t / L, v0 + (v1 - v0) * t / L),
                         (u0 + (u1 - u0) * t2 / L, v0 + (v1 - v0) * t2 / L)))
            t = t2 + gap

        def fn(d):
            for a, b in segs:
                d.line([self.P(face, *a), self.P(face, *b)], fill=col, width=max(1, int(w * S)))
        self.clip(face, fn)

    def clear(self, face, pts=None, box=None):
        """Rend transparent (la peau du personnage apparaît)."""
        m = Image.new("L", self.im.size, 0)
        dm = ImageDraw.Draw(m)
        if box:
            dm.rectangle(self.box(face, *box), fill=255)
        if pts:
            dm.polygon([self.P(face, u, v) for u, v in pts], fill=255)
        a = np.array(self.im)
        mm = np.array(m) > 0
        a[mm] = 0
        self.im = Image.fromarray(a)
        self.d = ImageDraw.Draw(self.im)

    def pattern(self, face, u0, v0, u1, v1, fn, phase=(0, 0)):
        """fn(u, v) -> (r, g, b, a) ou None ; appliqué en vectoriel (numpy)."""
        b = self.box(face, u0, v0, u1, v1)
        x0, y0, x1, y1 = b[0], b[1], b[2] + 1, b[3] + 1
        if x1 <= x0 or y1 <= y0:
            return
        fx, fy = face[0], face[1]
        ys, xs = np.mgrid[y0:y1, x0:x1].astype(np.float32)
        u = xs / S - fx + phase[0]
        v = ys / S - fy + phase[1]
        rgba = fn(u, v)  # tableau (h, w, 4) float 0..255, alpha = couverture
        a = np.array(self.im).astype(np.float32)
        sub = a[y0:y1, x0:x1]
        al = rgba[..., 3:4] / 255.0
        has = sub[..., 3:4] > 0
        sub[..., :3] = np.where(has, sub[..., :3] * (1 - al) + rgba[..., :3] * al, sub[..., :3])
        a[y0:y1, x0:x1] = sub
        self.im = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
        self.d = ImageDraw.Draw(self.im)

    def button(self, face, u, v, col, r=2.2):
        self.ellipse(face, u - r, v - r, u + r, v + r, col=col, outline=dark(col, 0.6), w=0.7)
        self.ellipse(face, u - r * 0.35 - 0.5, v - r * 0.35 - 0.5, u - r * 0.35 + 0.5, v - r * 0.35 + 0.5,
                     col=light(col, 0.6))

    def pocket(self, face, u0, v0, u1, v1, col, stitch=None, flap=False):
        self.rect(face, u0, v0, u1, v1, col)
        self.line(face, [(u0, v0), (u1, v0)], dark(col, 0.7), 0.8)
        self.line(face, [(u0, v1), (u1, v1), (u1, v0)], dark(col, 0.82), 0.6)
        st = stitch or light(col, 0.3)
        self.dashed(face, (u0 + 1.5, v0 + 2), (u0 + 1.5, v1 - 1.5), st, 0.5)
        self.dashed(face, (u1 - 1.5, v0 + 2), (u1 - 1.5, v1 - 1.5), st, 0.5)
        self.dashed(face, (u0 + 1.5, v1 - 1.5), (u1 - 1.5, v1 - 1.5), st, 0.5)
        if flap:
            fh = (v1 - v0) * 0.32
            self.rect(face, u0 - 0.5, v0, u1 + 0.5, v0 + fh, dark(col, 0.92))
            self.line(face, [(u0 - 0.5, v0 + fh), (u1 + 0.5, v0 + fh)], dark(col, 0.65), 0.8)
            self.button(face, (u0 + u1) / 2, v0 + fh - 1.6, dark(col, 0.7), 1.3)

    # ---- ombrage et grain
    def shade(self, faces_rects, grain=3.0, seed=0):
        a = np.array(self.im).astype(np.float32)
        Hh, Ww = a.shape[:2]
        fac = np.ones((Hh, Ww), dtype=np.float32)
        for face, kind in faces_rects:
            x, y, w, h = face
            x0, y0, x1, y1 = x * S, y * S, (x + w) * S, (y + h) * S
            ys, xs = np.mgrid[y0:y1, x0:x1].astype(np.float32)
            v = (ys - y0) / (y1 - y0)
            u = (xs - x0) / (x1 - x0)
            f = SHADE.get(kind, 1.0) * np.ones_like(v)
            if kind in SIDES:
                f *= 1.045 - 0.11 * v           # plus clair en haut
                edge = np.minimum(u, 1 - u)
                f *= 1 - 0.07 * np.clip(1 - edge / 0.12, 0, 1)  # arrondi des bords
            fac[y0:y1, x0:x1] = f
        rng = np.random.default_rng(seed)
        noise = rng.normal(0, grain, (Hh // S + 1, Ww // S + 1)).astype(np.float32)
        noise = np.kron(noise, np.ones((S, S), dtype=np.float32))[:Hh, :Ww]
        a[..., :3] = a[..., :3] * fac[..., None] + noise[..., None]
        out = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
        return out

    def finish(self, path, faces_rects, seed=0, grain=3.0):
        img = self.shade(faces_rects, grain=grain, seed=seed)
        img = img.resize((W, H), Image.LANCZOS)
        # alpha net (pas de demi-transparence parasite au bord des faces)
        a = np.array(img)
        al = a[..., 3]
        a[..., 3] = np.where(al > 110, 255, 0).astype(np.uint8)
        Image.fromarray(a).save(path, optimize=True)


def all_faces():
    out = [(TORSO[k], k) for k in TORSO]
    for L in LIMBS:
        out += [(L[k], k) for k in L]
    return out
