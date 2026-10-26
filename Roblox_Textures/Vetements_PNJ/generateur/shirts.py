"""30 hauts (Shirt) au format template Roblox."""
import numpy as np
from lib import *

F, B, U, D = TORSO["F"], TORSO["B"], TORSO["U"], TORSO["D"]
TR, TL = TORSO["R"], TORSO["L"]
PH = {"R": 0, "F": 64, "L": 192, "B": 256}  # continuité autour du torse

SLEEVE = {"long": 116, "34": 86, "short": 46, "none": 0}


def base(t, c, sl="short", sc=None, tuck=False, cuff=None, hem="stitch"):
    sc = sc or c
    for k in ("F", "B", "R", "L", "U", "D"):
        t.rect(TORSO[k], 0, 0, 128, 128, c)
    if tuck:
        for k in SIDES:
            t.clear(TORSO[k], box=(0, 114, 128, 128))
    lv = SLEEVE[sl]
    for L in LIMBS:
        if lv:
            t.rect(L["U"], 0, 0, 64, 64, sc)
            for k in SIDES:
                t.rect(L[k], 0, 0, 64, lv, sc)
    if sl == "none":  # débardeur : emmanchures
        t.clear(U, box=(0, 0, 22, 64))
        t.clear(U, box=(106, 0, 128, 64))
        for fc in (F, B):
            t.clear(fc, pts=[(0, 0), (20, 0), (12, 14), (0, 22)])
            t.clear(fc, pts=[(128, 0), (108, 0), (116, 14), (128, 22)])
    # finitions des manches
    for L in LIMBS:
        if not lv:
            continue
        for k in SIDES:
            if cuff == "rib":
                t.rect(L[k], 0, lv - 9, 64, lv, dark(sc, 0.88))
                for u in range(2, 64, 3):
                    t.line(L[k], [(u, lv - 9), (u, lv)], dark(sc, 0.78), 0.5)
            elif cuff == "band":
                t.rect(L[k], 0, lv - 7, 64, lv, dark(sc, 0.8))
            elif cuff:
                t.rect(L[k], 0, lv - 7, 64, lv, cuff)
            else:
                t.line(L[k], [(0, lv - 4), (64, lv - 4)], dark(sc, 0.8), 0.6)
            # plis du coude / de l'épaule
            if lv > 70 and k in ("F", "B"):
                t.arc(L[k], 14, 54, 50, 66, 200, 340, dark(sc, 0.82), 0.8)
                t.arc(L[k], 20, 60, 44, 70, 210, 330, dark(sc, 0.86), 0.6)
            if k in ("F", "B"):
                t.line(L[k], [(8, 22), (20, 26)], dark(sc, 0.88), 0.6)
    # bas du vêtement
    yb = 114 if tuck else 128
    for k in SIDES:
        fc = TORSO[k]
        w = fc[2]
        if hem == "rib":
            t.rect(fc, 0, yb - 10, w, yb, dark(c, 0.88))
            for u in range(1, w, 3):
                t.line(fc, [(u, yb - 10), (u, yb)], dark(c, 0.78), 0.5)
        elif hem == "stitch":
            t.dashed(fc, (0, yb - 4), (w, yb - 4), dark(c, 0.78), 0.5)
    # plis sous les bras
    t.line(F, [(2, 34), (12, 44)], dark(c, 0.88), 0.7)
    t.line(F, [(126, 34), (116, 44)], dark(c, 0.88), 0.7)
    t.line(B, [(2, 34), (12, 44)], dark(c, 0.9), 0.7)
    t.line(B, [(126, 34), (116, 44)], dark(c, 0.9), 0.7)


# ---------- cols
def crew(t, col, w=3.2):
    t.arc(F, 42, -16, 86, 12, 0, 180, col, w)
    t.arc(B, 46, -10, 82, 6, 0, 180, col, w * 0.9)
    t.ellipse(U, 42, 12, 86, 52, outline=col, w=w)


def vneck(t, col, depth=24):
    t.clear(F, pts=[(48, 0), (80, 0), (64, depth)])
    t.over_skin = True
    t.line(F, [(46, 0), (64, depth + 2), (82, 0)], col, 3)
    t.over_skin = False
    t.arc(B, 46, -10, 82, 6, 0, 180, col, 3)


def shirt_collar(t, col, open_=True, placket=True, btn=None, n=5, top=10):
    if open_:
        t.clear(F, pts=[(56, 0), (72, 0), (64, 10)])
    for pts in ([(42, 0), (63, 1), (56, 15), (44, 9)], [(86, 0), (65, 1), (72, 15), (84, 9)]):
        t.poly(F, pts, col)
        t.line(F, pts + [pts[0]], dark(col, 0.62), 0.8)
    t.rect(B, 40, 0, 88, 6, col)
    t.line(B, [(40, 6), (88, 6)], dark(col, 0.62), 0.8)
    t.ellipse(U, 40, 10, 88, 54, outline=col, w=4)
    if placket:
        pc = dark(col, 0.72) if btn is None else dark(btn, 0.8)
        t.line(F, [(64, 12), (64, 128)], pc, 0.8)
        t.line(F, [(67, 12), (67, 128)], dark(pc, 1.1), 0.5)
        for i in range(n):
            t.button(F, 65.5, top + 12 + i * 20, btn or light(col, 0.4), 1.8)


def polo_collar(t, col, btn):
    shirt_collar(t, col, open_=True, placket=False)
    t.line(F, [(60, 10), (60, 34), (68, 34), (68, 10)], dark(col, 0.6), 0.7)
    t.button(F, 64, 18, btn, 1.6)
    t.button(F, 64, 28, btn, 1.6)


def hood(t, col, strings=(240, 240, 240, 255)):
    t.ellipse(B, 22, -34, 106, 34, col=dark(col, 0.93), outline=dark(col, 0.7), w=1.2)
    t.arc(B, 34, -24, 94, 22, 10, 170, dark(col, 0.75), 0.9)
    t.ellipse(U, 34, 6, 94, 58, outline=dark(col, 0.82), w=7)
    t.arc(F, 38, -18, 90, 14, 0, 180, dark(col, 0.8), 4)
    for u0, u1 in ((54, 52), (74, 76)):
        t.line(F, [(u0, 8), (u1, 40)], strings, 1.4)
        t.rect(F, u1 - 1.2, 39, u1 + 1.2, 44, dark(strings, 0.75))


def turtleneck(t, col):
    t.rect(F, 36, 0, 92, 9, dark(col, 0.9))
    for u in range(37, 92, 3):
        t.line(F, [(u, 0), (u, 9)], dark(col, 0.78), 0.5)
    t.rect(B, 36, 0, 92, 9, dark(col, 0.9))
    t.ellipse(U, 34, 6, 94, 58, outline=dark(col, 0.85), w=8)


# ---------- détails
def zip_(t, col=(170, 170, 178, 255), u=64):
    t.line(F, [(u, 0), (u, 128)], dark(col, 0.6), 2.2)
    t.dashed(F, (u, 0), (u, 128), col, 1.6, 1.2, 1.2)
    t.rect(F, u - 2, 6, u + 2, 16, col)
    t.line(F, [(u - 2, 16), (u + 2, 16)], dark(col, 0.5), 0.6)


def kangaroo(t, col):
    pts = [(30, 76), (98, 76), (108, 114), (20, 114)]
    t.poly(F, pts, dark(col, 0.95))
    t.line(F, pts + [pts[0]], dark(col, 0.75), 0.8)
    t.line(F, [(30, 76), (22, 106)], dark(col, 0.65), 1.2)
    t.line(F, [(98, 76), (106, 106)], dark(col, 0.65), 1.2)


def stripes(t, col, period=12, width=5, sleeves=True, v0=0, v1=128):
    def fn(u, v):
        on = ((v % period) < width).astype(np.float32)
        out = np.zeros(u.shape + (4,), np.float32)
        out[..., 0], out[..., 1], out[..., 2] = col[0], col[1], col[2]
        out[..., 3] = on * 255
        return out
    for k in SIDES:
        t.pattern(TORSO[k], 0, v0, TORSO[k][2], v1, fn)
    if sleeves:
        for L in LIMBS:
            for k in SIDES:
                t.pattern(L[k], 0, 4, 64, 128, fn)


def plaid(t, c1, c2, period=24):
    def fn(u, v):
        a = ((u % period) < period * 0.38).astype(np.float32)
        b = ((v % period) < period * 0.38).astype(np.float32)
        thin = (((u % period) - period * 0.7) ** 2 < 0.6).astype(np.float32) + \
               (((v % period) - period * 0.7) ** 2 < 0.6).astype(np.float32)
        out = np.zeros(u.shape + (4,), np.float32)
        k = np.clip(a * 0.4 + b * 0.4, 0, 1)
        col = np.array(c1[:3], np.float32) * (1 - k[..., None]) + np.array(c2[:3], np.float32) * k[..., None]
        col = col * (1 - 0.25 * (a * b)[..., None])
        col = np.where(np.clip(thin, 0, 1)[..., None] > 0, np.array([235, 225, 200], np.float32), col)
        out[..., :3] = col
        out[..., 3] = 255
        return out
    for k in SIDES:
        t.pattern(TORSO[k], 0, 0, TORSO[k][2], 128, fn, phase=(PH[k], 0))
    t.pattern(U, 0, 0, 128, 64, fn)
    for L in LIMBS:
        for k in SIDES:
            t.pattern(L[k], 0, 0, 64, 128, fn, phase=({"F": 0, "R": 64, "B": 128, "L": 192}[k], 0))
        t.pattern(L["U"], 0, 0, 64, 64, fn)


def dots(t, col, period=14, r=2.4, sleeves=True, flower=None):
    def fn(u, v):
        row = np.floor(v / period)
        uu = u + (row % 2) * period / 2
        du = (uu % period) - period / 2
        dv = (v % period) - period / 2
        d2 = du * du + dv * dv
        out = np.zeros(u.shape + (4,), np.float32)
        out[..., :3] = col[:3]
        if flower:
            ang = np.arctan2(dv, du)
            rr = r * (1 + 0.45 * np.cos(5 * ang))
            petal = (np.sqrt(d2) < rr).astype(np.float32)
            centre = (d2 < (r * 0.38) ** 2)
            out[..., :3] = np.where(centre[..., None], np.array(flower[:3], np.float32), out[..., :3])
            out[..., 3] = petal * 255
        else:
            out[..., 3] = np.clip((r * r - d2) * 2.5, 0, 1) * 255
        return out
    for k in SIDES:
        t.pattern(TORSO[k], 0, 0, TORSO[k][2], 128, fn, phase=(PH[k], 0))
    if sleeves:
        for L in LIMBS:
            for k in SIDES:
                t.pattern(L[k], 0, 0, 64, 128, fn)


def emblem_wave(t, bg, fg, cx=64, cy=54, r=22):
    t.ellipse(F, cx - r, cy - r, cx + r, cy + r, col=bg, outline=fg, w=2)
    for k, dy in enumerate((-8, 0, 8)):
        pts = [(cx - r * 0.72 + i * 0.5, cy + dy + 3.2 * math.sin((i * 0.5 + k * 3) / 3.2)) for i in range(0, int(r * 2.9) + 1)]
        t.line(F, pts, fg, 2.6)


def emblem_sun(t, col, cx=64, cy=54, r=11):
    for i in range(12):
        a = i * math.pi / 6
        t.line(F, [(cx + math.cos(a) * (r + 2), cy + math.sin(a) * (r + 2)),
                   (cx + math.cos(a) * (r + 8), cy + math.sin(a) * (r + 8))], col, 1.8)
    t.ellipse(F, cx - r, cy - r, cx + r, cy + r, col=col)


def emblem_leaf(t, col, cx=88, cy=34):
    t.poly(F, [(cx - 8, cy + 6), (cx - 2, cy - 7), (cx + 8, cy - 9), (cx + 4, cy + 3)], col)
    t.line(F, [(cx - 8, cy + 6), (cx + 6, cy - 7)], dark(col, 0.6), 0.7)


def chest_band(t, col, v0=40, v1=54):
    for k in SIDES:
        t.rect(TORSO[k], 0, v0, TORSO[k][2], v1, col)
    for L in LIMBS:
        for k in SIDES:
            t.rect(L[k], 0, v0 - 30, 64, v1 - 30, col)


def raglan(t, sc):
    for fc in (F, B):
        t.poly(fc, [(0, 0), (36, 0), (0, 44)], sc)
        t.poly(fc, [(128, 0), (92, 0), (128, 44)], sc)
        t.line(fc, [(36, 0), (0, 44)], dark(sc, 0.75), 0.8)
        t.line(fc, [(92, 0), (128, 44)], dark(sc, 0.75), 0.8)
    t.rect(U, 0, 0, 34, 64, sc)
    t.rect(U, 94, 0, 128, 64, sc)
    for fc in (TR, TL):
        t.rect(fc, 0, 0, 64, 44, sc)


def open_jacket(t, inner, col, lapel=True, inner_collar=None):
    t.rect(F, 46, 0, 82, 128, inner)
    if inner_collar:
        t.arc(F, 50, -10, 78, 8, 0, 180, inner_collar, 2.5)
    if lapel:
        for pts in ([(40, 0), (50, 0), (54, 40), (46, 48), (38, 30)],
                    [(88, 0), (78, 0), (74, 40), (82, 48), (90, 30)]):
            t.poly(F, pts, dark(col, 0.92))
            t.line(F, pts + [pts[0]], dark(col, 0.65), 0.8)
    t.line(F, [(46, 0), (46, 128)], dark(col, 0.6), 1.0)
    t.line(F, [(82, 0), (82, 128)], dark(col, 0.6), 1.0)
    t.ellipse(U, 40, 10, 88, 54, outline=dark(col, 0.9), w=5)


def gilet(t, col, inner_v=True, btn=None):
    for k in ("B", "R", "L"):
        t.rect(TORSO[k], 0, 0, TORSO[k][2], 124, col)
    t.poly(F, [(0, 0), (40, 0), (62, 56), (62, 124), (0, 124)], col)
    t.poly(F, [(128, 0), (88, 0), (66, 56), (66, 124), (128, 124)], col)
    t.line(F, [(40, 0), (62, 56), (62, 124)], dark(col, 0.6), 1.0)
    t.line(F, [(88, 0), (66, 56), (66, 124)], dark(col, 0.6), 1.0)
    t.poly(F, [(52, 124), (64, 128), (76, 124)], col)
    for i in range(4):
        t.button(F, 60, 66 + i * 14, btn or dark(col, 0.6), 1.7)
    t.pocket(F, 12, 70, 34, 80, dark(col, 0.94))
    t.pocket(F, 94, 70, 116, 80, dark(col, 0.94))
    t.rect(U, 0, 0, 32, 64, col)
    t.rect(U, 96, 0, 128, 64, col)


def apron(t, col, tie=None, bib=True, v0=30, pocket=True):
    tie = tie or dark(col, 0.85)
    if bib:
        t.rect(F, 26, v0, 102, 128, col)
        t.line(F, [(26, v0), (102, v0)], dark(col, 0.7), 0.8)
        t.line(F, [(30, v0), (40, 0)], tie, 2.4)
        t.line(F, [(98, v0), (88, 0)], tie, 2.4)
        t.line(B, [(40, 0), (88, 0)], tie, 2.4)
    else:
        t.rect(F, 18, 72, 110, 128, col)
    for k in ("R", "L"):
        t.rect(TORSO[k], 0, 70, 64, 75, tie)
    t.rect(B, 0, 70, 128, 75, tie)
    t.ellipse(B, 54, 66, 64, 79, col=tie, outline=dark(tie, 0.7), w=0.7)
    t.ellipse(B, 64, 66, 74, 79, col=tie, outline=dark(tie, 0.7), w=0.7)
    t.line(B, [(62, 78), (58, 98)], tie, 2)
    t.line(B, [(66, 78), (70, 98)], tie, 2)
    for u in (26, 102) if bib else (18, 110):
        t.dashed(F, (u + (2 if u < 64 else -2), v0 + 2 if bib else 74), (u + (2 if u < 64 else -2), 126),
                 dark(col, 0.78), 0.5)
    if pocket:
        t.pocket(F, 42, 88, 86, 108, dark(col, 0.95))
        t.line(F, [(64, 88), (64, 108)], dark(col, 0.75), 0.6)


def epaulettes(t, col, gold):
    for L in LIMBS:
        t.rect(L["U"], 8, 0, 56, 64, col)
        t.line(L["U"], [(10, 50), (54, 50)], gold, 1.6)
    t.rect(U, 4, 14, 28, 50, col)
    t.rect(U, 100, 14, 124, 50, col)
    t.line(U, [(6, 20), (6, 44)], gold, 1.4)
    t.line(U, [(122, 20), (122, 44)], gold, 1.4)


def star_badge(t, col, cx, cy, r=6):
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.45
        pts.append((cx + math.cos(a) * rr, cy + math.sin(a) * rr))
    t.poly(F, pts, col)
    t.line(F, pts + [pts[0]], dark(col, 0.6), 0.6)


def heart_badge(t, col, cx, cy, r=5):
    pts = []
    for i in range(40):
        a = i / 40 * 2 * math.pi
        x = 16 * math.sin(a) ** 3
        y = -(13 * math.cos(a) - 5 * math.cos(2 * a) - 2 * math.cos(3 * a) - math.cos(4 * a))
        pts.append((cx + x * r / 16, cy + y * r / 16))
    t.poly(F, pts, col)


def belt(t, col, buckle=(205, 175, 90, 255), v0=100, h=7):
    for k in SIDES:
        t.rect(TORSO[k], 0, v0, TORSO[k][2], v0 + h, col)
        t.line(TORSO[k], [(0, v0), (TORSO[k][2], v0)], dark(col, 0.6), 0.6)
    t.rect(F, 58, v0 - 1.5, 70, v0 + h + 1.5, buckle)
    t.rect(F, 61, v0 + 1, 67, v0 + h - 1, col)


def embroidery(t, col, v0=112, v1=124):
    def fn(u, v):
        tri = np.abs(((u + 0) % 8) - 4) + (v - v0) * 0.9
        on = (np.abs(tri - 5) < 1.1).astype(np.float32)
        dots_ = (((u % 8) - 4) ** 2 + (v - (v0 + 9)) ** 2 < 1.4).astype(np.float32)
        out = np.zeros(u.shape + (4,), np.float32)
        out[..., :3] = col[:3]
        out[..., 3] = np.clip(on + dots_, 0, 1) * 255
        return out
    for k in SIDES:
        t.pattern(TORSO[k], 0, v0, TORSO[k][2], v1, fn, phase=(PH[k], 0))


def cable_knit(t, col):
    for u0 in (18, 46, 82, 110):
        for v in range(10, 118, 10):
            t.arc(F, u0 - 6, v, u0 + 6, v + 10, 300, 60, dark(col, 0.82), 1.0)
            t.arc(F, u0 - 6, v, u0 + 6, v + 10, 120, 240, dark(col, 0.82), 1.0)
    for u0 in (32, 64, 96):
        t.line(F, [(u0, 10), (u0, 116)], dark(col, 0.85), 0.8)
        t.line(F, [(u0 + 3, 10), (u0 + 3, 116)], dark(col, 0.85), 0.8)


def neck_scarf(t, col):
    t.poly(F, [(48, 0), (80, 0), (64, 26)], col)
    t.line(F, [(48, 0), (64, 26), (80, 0)], dark(col, 0.65), 0.8)
    t.ellipse(F, 60, 4, 68, 12, col=dark(col, 0.85))
    t.line(F, [(62, 10), (56, 34)], col, 3)
    t.line(F, [(66, 10), (72, 32)], col, 3)


def bib_overall(t, col, strap_btn=(205, 175, 90, 255)):
    t.rect(F, 30, 44, 98, 128, col)
    t.line(F, [(30, 44), (98, 44)], dark(col, 0.7), 0.8)
    t.dashed(F, (32, 47), (96, 47), (215, 150, 60, 255), 0.6)
    t.pocket(F, 46, 54, 82, 76, dark(col, 0.95), stitch=(215, 150, 60, 255))
    for u, u2 in ((36, 40), (92, 88)):
        t.line(F, [(u, 46), (u2, 0)], col, 5)
        t.button(F, u, 47, strap_btn, 2.2)
    t.line(B, [(40, 0), (88, 70)], col, 5)
    t.line(B, [(88, 0), (40, 70)], col, 5)
    t.rect(B, 30, 70, 98, 128, col)
    t.rect(U, 30, 0, 44, 64, col)
    t.rect(U, 84, 0, 98, 64, col)
    for k in ("R", "L"):
        t.rect(TORSO[k], 0, 96, 64, 128, col)
        t.button(TORSO[k], 32, 100, strap_btn, 2)


def hawaii(t, c1, c2, c3):
    dots(t, c1, period=22, r=5.2, flower=c2)
    def fn(u, v):
        uu = (u + 11) % 22 - 11
        vv = (v + 11 + np.floor((u + 11) / 22) * 7) % 22 - 11
        leaf = ((uu * 0.6) ** 2 + (vv * 1.6 - uu * 0.6) ** 2 < 9).astype(np.float32)
        out = np.zeros(u.shape + (4,), np.float32)
        out[..., :3] = c3[:3]
        out[..., 3] = leaf * 255
        return out
    for k in SIDES:
        t.pattern(TORSO[k], 0, 0, TORSO[k][2], 128, fn, phase=(PH[k], 0))
    for L in LIMBS:
        for k in SIDES:
            t.pattern(L[k], 0, 0, 64, 50, fn)


def lower_pockets(t, col, v0=82, v1=102, flap=True):
    t.pocket(F, 10, v0, 40, v1, col, flap=flap)
    t.pocket(F, 88, v0, 118, v1, col, flap=flap)


C = dict(blanc=hexc("f2f0ea"), creme=hexc("efe3c8"), noir=hexc("26262b"), gris=hexc("8e9096"),
         gris_f=hexc("54575e"), marine=hexc("27335a"), azur=hexc("2f8fd8"), ciel=hexc("8cc8ef"),
         rouge=hexc("c23b33"), bordeaux=hexc("7a2632"), corail=hexc("ef7d64"), jaune=hexc("f2c230"),
         moutarde=hexc("c99a2e"), vert=hexc("3f9a52"), sapin=hexc("2c5e3f"), kaki=hexc("7d7b4f"),
         sable=hexc("d9c49a"), terre=hexc("a8673f"), brun=hexc("6b4a32"), rose=hexc("e99ab0"),
         lavande=hexc("a79bd6"), turquoise=hexc("2ab3a6"), jean=hexc("3f6696"), jean_c=hexc("7397c0"),
         or_=hexc("d5ad4c"), orange=hexc("e88a2e"), prune=hexc("6a3d6e"), olive=hexc("5f6b3a"))


def S01(t):
    base(t, C["blanc"]); crew(t, dark(C["blanc"], 0.9))
def S02(t):
    base(t, C["azur"]); crew(t, dark(C["azur"], 0.85)); emblem_wave(t, C["blanc"], dark(C["azur"], 0.8))
def S03(t):
    base(t, C["gris"], "34", C["marine"], cuff="band"); raglan(t, C["marine"]); crew(t, C["marine"])
def S04(t):
    base(t, C["jaune"], "short", cuff=C["rouge"]); crew(t, C["rouge"], 3.6); emblem_sun(t, C["orange"])
def S05(t):
    base(t, C["vert"], "none", hem="stitch")
    t.over_skin = True
    t.arc(F, 40, -22, 88, 20, 0, 180, dark(C["vert"], 0.8), 3)
    t.over_skin = False
    t.clear(F, pts=[(46, 0), (82, 0), (64, 14)])
def S06(t):
    base(t, C["blanc"], "34"); stripes(t, C["marine"], 12, 5); crew(t, C["marine"], 2.6)
def S07(t):
    base(t, C["corail"], "short", tuck=True, cuff="band"); polo_collar(t, C["corail"], C["blanc"])
def S08(t):
    base(t, C["blanc"], "long", tuck=True, cuff=dark(C["blanc"], 0.93)); shirt_collar(t, C["blanc"])
    t.pocket(F, 80, 26, 100, 46, dark(C["blanc"], 0.97))
def S09(t):
    base(t, C["rouge"], "long", tuck=False, cuff=dark(C["rouge"], 0.8)); plaid(t, C["rouge"], dark(C["rouge"], 0.6), 28)
    shirt_collar(t, dark(C["rouge"], 0.85)); t.pocket(F, 20, 28, 40, 46, dark(C["rouge"], 0.85), flap=True)
    t.pocket(F, 88, 28, 108, 46, dark(C["rouge"], 0.85), flap=True)
def S10(t):
    base(t, C["jean_c"], "long", tuck=True, cuff=C["jean"]); shirt_collar(t, C["jean"], btn=C["blanc"])
    for u in (20, 88):
        t.pocket(F, u, 26, u + 20, 46, C["jean"], stitch=(225, 160, 70, 255), flap=True)
def S11(t):
    base(t, C["turquoise"], "short", cuff="band"); hawaii(t, C["blanc"], C["jaune"], C["sapin"])
    shirt_collar(t, C["turquoise"], btn=C["blanc"], n=5)
def S12(t):
    base(t, C["bordeaux"], "long", cuff="rib", hem="rib"); crew(t, dark(C["bordeaux"], 0.8), 4)
def S13(t):
    base(t, C["creme"], "long", cuff="rib", hem="rib"); cable_knit(t, C["creme"]); turtleneck(t, C["creme"])
def S14(t):
    base(t, C["moutarde"], "long", cuff="rib", hem="rib")
    t.poly(F, [(44, 0), (84, 0), (66, 60), (62, 60)], C["blanc"])
    t.rect(F, 62, 60, 66, 128, C["blanc"])
    t.line(F, [(44, 0), (62, 60), (62, 128)], dark(C["moutarde"], 0.7), 1)
    t.line(F, [(84, 0), (66, 60), (66, 128)], dark(C["moutarde"], 0.7), 1)
    for i in range(4):
        t.button(F, 69, 68 + i * 14, C["brun"], 1.8)
    t.pocket(F, 12, 80, 34, 98, dark(C["moutarde"], 0.95)); t.pocket(F, 94, 80, 116, 98, dark(C["moutarde"], 0.95))
def S15(t):
    base(t, C["gris"], "long", cuff="rib", hem="rib"); hood(t, C["gris"]); kangaroo(t, C["gris"])
def S16(t):
    base(t, C["azur"], "long", cuff="rib", hem="rib"); hood(t, C["azur"]); zip_(t)
    for L in LIMBS:
        t.rect(L[OUTER[id(L)]], 26, 0, 38, 116, C["blanc"])
    t.rect(TR, 26, 0, 38, 118, C["blanc"]); t.rect(TL, 26, 0, 38, 118, C["blanc"])
def S17(t):
    base(t, C["jean"], "long", cuff=dark(C["jean"], 0.85), hem="band")
    open_jacket(t, C["blanc"], C["jean"], inner_collar=dark(C["blanc"], 0.88))
    for u in (14, 92):
        t.pocket(F, u, 24, u + 22, 44, dark(C["jean"], 0.95), stitch=(225, 160, 70, 255), flap=True)
    for k in SIDES:
        t.rect(TORSO[k], 0, 118, TORSO[k][2], 128, dark(C["jean"], 0.85))
def S18(t):
    base(t, C["noir"], "long", cuff="rib", hem="rib"); zip_(t, C["gris"])
    t.ellipse(U, 34, 6, 94, 58, outline=dark(C["noir"], 0.8), w=7)
    t.arc(F, 38, -16, 90, 12, 0, 180, hexc("3a3a40"), 5)
    t.line(F, [(18, 70), (30, 96)], hexc("444449"), 1.6); t.line(F, [(110, 70), (98, 96)], hexc("444449"), 1.6)
    t.rect(F, 86, 20, 106, 26, C["orange"])
def S19(t):
    base(t, C["blanc"], "long", cuff=dark(C["blanc"], 0.92)); shirt_collar(t, C["blanc"], placket=False)
    gilet(t, C["brun"], btn=C["or_"])
def S20(t):
    base(t, C["jaune"], "long", cuff=dark(C["jaune"], 0.85), hem="band"); hood(t, C["jaune"], strings=C["blanc"])
    for i in range(4):
        y = 30 + i * 22
        t.rect(F, 60, y, 68, y + 3, C["brun"]); t.line(F, [(56, y + 1.5), (72, y + 1.5)], C["brun"], 1)
    t.line(F, [(64, 12), (64, 128)], dark(C["jaune"], 0.7), 1)
    lower_pockets(t, dark(C["jaune"], 0.93), flap=True)
def S21(t):
    base(t, C["sable"], "34", tuck=False, cuff="band")
    crew(t, dark(C["sable"], 0.85))
    t.rect(F, 0, 0, 128, 128, C["kaki"]) if False else None
    for k in ("B", "R", "L"):
        t.rect(TORSO[k], 0, 0, TORSO[k][2], 122, C["kaki"])
    t.poly(F, [(0, 0), (44, 0), (58, 30), (58, 122), (0, 122)], C["kaki"])
    t.poly(F, [(128, 0), (84, 0), (70, 30), (70, 122), (128, 122)], C["kaki"])
    zip_(t, C["gris"], 59); t.line(F, [(70, 30), (70, 122)], dark(C["kaki"], 0.6), 1)
    for (u, v) in ((6, 36), (30, 36), (78, 36), (102, 36), (8, 76), (100, 76)):
        t.pocket(F, u, v, u + 20, v + 22, dark(C["kaki"], 0.92), flap=True)
    t.rect(U, 0, 0, 34, 64, C["kaki"]); t.rect(U, 94, 0, 128, 64, C["kaki"])
def S22(t):
    base(t, C["blanc"], "short", cuff="band"); crew(t, dark(C["blanc"], 0.88))
    apron(t, C["creme"], tie=C["terre"])
    t.ellipse(F, 54, 50, 74, 64, outline=C["terre"], w=1.2)
def S23(t):
    base(t, C["ciel"], "long", tuck=False, cuff=dark(C["ciel"], 0.85)); shirt_collar(t, C["ciel"], placket=False)
    apron(t, C["sapin"], tie=dark(C["sapin"], 0.8)); emblem_leaf(t, C["vert"], 64, 54)
def S24(t):
    base(t, C["marine"], "long", tuck=True, cuff=dark(C["marine"], 0.8)); shirt_collar(t, C["marine"], btn=C["or_"])
    epaulettes(t, dark(C["marine"], 0.85), C["or_"])
    for u in (16, 88):
        t.pocket(F, u, 24, u + 24, 44, dark(C["marine"], 0.93), flap=True)
    star_badge(t, C["or_"], 28, 18, 5.5)
    t.rect(F, 92, 50, 108, 54, C["azur"])
def S25(t):
    base(t, C["blanc"], "short", cuff=C["turquoise"]); vneck(t, C["turquoise"], 26)
    t.pocket(F, 80, 34, 102, 54, dark(C["blanc"], 0.96)); t.line(F, [(80, 34), (102, 34)], C["turquoise"], 1.6)
    heart_badge(t, C["turquoise"], 30, 32, 5)
    lower_pockets(t, dark(C["blanc"], 0.96), v0=86, v1=106, flap=False)
def S26(t):
    base(t, C["blanc"], "long", cuff=dark(C["blanc"], 0.92), hem="stitch")
    open_jacket(t, C["lavande"], C["blanc"], inner_collar=dark(C["lavande"], 0.8))
    lower_pockets(t, dark(C["blanc"], 0.95), v0=80, v1=104, flap=False)
    t.pocket(F, 90, 28, 110, 44, dark(C["blanc"], 0.95))
    t.line(F, [(96, 22), (96, 34)], C["azur"], 1.6); t.line(F, [(101, 22), (101, 34)], C["rouge"], 1.6)
def S27(t):
    base(t, C["bordeaux"], "long", tuck=True, cuff=dark(C["bordeaux"], 0.8))
    open_jacket(t, C["blanc"], C["bordeaux"]); neck_scarf(t, C["or_"])
    for i in range(2):
        t.button(F, 86, 74 + i * 14, C["or_"], 1.9)
    t.pocket(F, 92, 24, 112, 30, dark(C["bordeaux"], 0.9))
def S28(t):
    base(t, C["sable"], "long", cuff=C["terre"], hem="none")
    t.clear(F, pts=[(54, 0), (74, 0), (64, 20)])
    t.over_skin = True
    t.line(F, [(52, 0), (64, 22), (76, 0)], C["terre"], 2.2)
    t.over_skin = False
    embroidery(t, C["terre"], 114, 126); embroidery(t, C["turquoise"], 4, 14) if False else None
    belt(t, C["terre"], C["or_"], 96, 6)
    for v in range(28, 90, 12):
        t.ellipse(F, 62, v, 66, v + 4, col=C["turquoise"])
def S29(t):
    base(t, C["blanc"], "short", cuff="band"); stripes(t, C["rouge"], 10, 4); crew(t, C["rouge"], 2.6)
    bib_overall(t, C["jean"])
def S30(t):
    base(t, C["rose"], "short", tuck=False, cuff="band"); dots(t, C["blanc"], 13, 2.0)
    t.arc(F, 40, -16, 88, 14, 0, 180, C["blanc"], 4)
    t.ellipse(F, 58, 10, 70, 20, col=C["blanc"])
    t.rect(F, 60, 18, 68, 30, C["blanc"])


SHIRTS = [
    (S01, "T-shirt blanc"), (S02, "T-shirt azur à vague"), (S03, "Raglan gris et marine"),
    (S04, "T-shirt jaune soleil"), (S05, "Débardeur vert"), (S06, "Marinière"),
    (S07, "Polo corail"), (S08, "Chemise blanche"), (S09, "Chemise à carreaux rouge"),
    (S10, "Chemise en jean"), (S11, "Chemise hawaïenne"), (S12, "Pull bordeaux"),
    (S13, "Pull torsadé crème"), (S14, "Cardigan moutarde"), (S15, "Sweat à capuche gris"),
    (S16, "Veste zippée azur"), (S17, "Veste en jean"), (S18, "Blouson noir"),
    (S19, "Gilet de marchand"), (S20, "Ciré jaune"), (S21, "Veste de pêche kaki"),
    (S22, "Tablier de boulangère"), (S23, "Tablier de jardinier"), (S24, "Uniforme de garde"),
    (S25, "Tunique d'infirmière"), (S26, "Blouse de laboratoire"), (S27, "Veston de la Guilde"),
    (S28, "Tunique brodée sable"), (S29, "Haut de salopette rayé"), (S30, "Blouse rose à pois"),
]
