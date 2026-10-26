"""30 bas (Pants) au format template Roblox."""
import numpy as np
from lib import *
from shirts import C

F, B = TORSO["F"], TORSO["B"]
LEG = {"long": 128, "34": 92, "short": 58, "court": 46, "skirt": 66, "skirtlong": 112}
ORANGE_ST = (220, 150, 60, 255)


def shoes(t, kind, col, sole=None, h=None):
    sole = sole or C["blanc"]
    hh = h or {"basket": 16, "chaussure": 13, "botte": 40, "bottine": 24, "ballerine": 9,
               "sandale": 12, "botte_pluie": 46, "mocassin": 12}[kind]
    for L in LIMBS:
        for k in SIDES:
            fc = L[k]
            if kind == "sandale":
                for v in (116, 122):
                    t.rect(fc, 0, v, 64, v + 3, col)
                t.rect(fc, 0, 125, 64, 128, sole)
                continue
            t.rect(fc, 0, 128 - hh, 64, 128, col)
            sh = 4 if kind in ("basket", "botte_pluie") else 2.5
            t.rect(fc, 0, 128 - sh, 64, 128, sole)
            t.line(fc, [(0, 128 - hh), (64, 128 - hh)], dark(col, 0.65), 0.8)
            if kind == "basket":
                if k == "F":
                    for i in range(3):
                        y = 128 - hh + 3 + i * 3
                        t.line(fc, [(24, y), (40, y + 2)], C["blanc"], 0.9)
                        t.line(fc, [(40, y), (24, y + 2)], C["blanc"], 0.9)
                if k in ("R", "L"):
                    t.arc(fc, 10, 128 - hh + 2, 54, 128 + 6, 200, 340, light(col, 0.5), 2)
            elif kind in ("botte", "botte_pluie", "bottine"):
                t.rect(fc, 0, 128 - hh, 64, 128 - hh + 4, dark(col, 0.85))
                if kind == "bottine" and k == "F":
                    for i in range(4):
                        t.button(fc, 32, 128 - hh + 7 + i * 4, dark(col, 0.6), 0.8)
            elif kind == "mocassin" and k == "F":
                t.arc(fc, 16, 128 - hh + 2, 48, 128 + 6, 180, 360, dark(col, 0.6), 0.8)
            elif kind == "chaussure" and k == "F":
                t.line(fc, [(28, 128 - hh + 3), (36, 128 - hh + 3)], dark(col, 0.5), 0.8)
            elif kind == "ballerine" and k == "F":
                t.ellipse(fc, 28, 128 - hh + 1, 36, 128 - hh + 5, col=dark(col, 0.8))
        t.rect(L["D"], 0, 0, 64, 64, dark(sole, 0.85) if kind != "sandale" else dark(col, 0.8))


def socks(t, col, h=12, shoe_h=16):
    for L in LIMBS:
        for k in SIDES:
            t.rect(L[k], 0, 128 - shoe_h - h, 64, 128 - shoe_h, col)
            for u in range(2, 64, 3):
                t.line(L[k], [(u, 128 - shoe_h - h), (u, 128 - shoe_h - h + 4)], dark(col, 0.85), 0.5)


def base(t, c, leg="long", belt=None, waist=16, fly=True, loops=True):
    for k in SIDES:
        t.rect(TORSO[k], 0, 128 - waist, TORSO[k][2], 128, c)
    t.rect(TORSO["D"], 0, 0, 128, 64, c)
    lv = LEG[leg]
    for L in LIMBS:
        t.rect(L["U"], 0, 0, 64, 64, c)
        for k in SIDES:
            t.rect(L[k], 0, 0, 64, lv, c)
    # ceinture
    if belt:
        for k in SIDES:
            w = TORSO[k][2]
            t.rect(TORSO[k], 0, 114, w, 121, belt)
            t.line(TORSO[k], [(0, 114), (w, 114)], dark(belt, 0.6), 0.6)
            t.line(TORSO[k], [(0, 121), (w, 121)], dark(belt, 0.6), 0.6)
            if loops:
                for u in range(10, w, 30):
                    t.rect(TORSO[k], u, 113, u + 3, 122, c)
        t.rect(F, 57, 112.5, 71, 122.5, (205, 180, 110, 255))
        t.rect(F, 60, 115, 68, 120, belt)
    else:
        for k in SIDES:
            t.rect(TORSO[k], 0, 112, TORSO[k][2], 118, dark(c, 0.9))
            t.line(TORSO[k], [(0, 118), (TORSO[k][2], 118)], dark(c, 0.7), 0.6)
    if fly and leg not in ("skirt", "skirtlong"):
        t.line(F, [(64, 121), (64, 128)], dark(c, 0.62), 0.9)
        t.arc(F, 58, 116, 70, 134, 270, 360, dark(c, 0.62), 0.8)
    # plis : entrejambe, genoux, chevilles
    for L in LIMBS:
        if leg in ("skirt", "skirtlong"):
            break
        for k in ("F", "B"):
            t.line(L[k], [(INNER[id(L)] == "L" and 6 or 58, 4), (32, 14)], dark(c, 0.86), 0.7)
            if lv > 80:
                t.arc(L[k], 14, 58, 50, 70, 200, 340, dark(c, 0.84), 0.8)
                t.arc(L[k], 18, 66, 46, 74, 210, 330, dark(c, 0.87), 0.6)
        if lv > 100:
            for k in SIDES:
                t.line(L[k], [(6, lv - 22), (24, lv - 18), (40, lv - 22), (58, lv - 18)], dark(c, 0.86), 0.6)
    return lv


def hem(t, c, lv, kind="stitch"):
    for L in LIMBS:
        for k in SIDES:
            if kind == "roll":
                t.rect(L[k], 0, lv - 7, 64, lv, light(c, 0.12))
                t.line(L[k], [(0, lv - 7), (64, lv - 7)], dark(c, 0.7), 0.7)
            elif kind == "elastic":
                t.rect(L[k], 0, lv - 8, 64, lv, dark(c, 0.88))
                for u in range(2, 64, 3):
                    t.line(L[k], [(u, lv - 8), (u, lv)], dark(c, 0.78), 0.5)
            else:
                t.dashed(L[k], (0, lv - 3), (64, lv - 3), dark(c, 0.75), 0.5)


def jean_details(t, c, lv, stitch=ORANGE_ST, fade=True):
    for L in LIMBS:
        o, i = OUTER[id(L)], INNER[id(L)]
        t.dashed(L[o], (32, 0), (32, lv), stitch, 0.6)
        t.line(L[o], [(30.5, 0), (30.5, lv)], dark(c, 0.8), 0.6)
        t.dashed(L[i], (32, 6), (32, lv), stitch, 0.5)
        f = L["F"]
        if o == "R":  # jambe droite : bord extérieur à gauche de la face avant
            t.arc(f, -14, -12, 22, 22, 0, 90, dark(c, 0.62), 1.0)
            t.arc(f, -12, -10, 20, 20, 0, 90, stitch, 0.5)
        else:
            t.arc(f, 42, -12, 78, 22, 90, 180, dark(c, 0.62), 1.0)
            t.arc(f, 44, -10, 76, 20, 90, 180, stitch, 0.5)
        t.pocket(L["B"], 14, 4, 50, 28, c, stitch=stitch)
        t.line(L["B"], [(14, 4), (50, 4)], dark(c, 0.7), 0.8)
        if fade:
            lc = light(c, 0.4)
            def ffn(u, v, lc=lc):
                out = np.zeros(u.shape + (4,), np.float32)
                out[..., :3] = lc[:3]
                out[..., 3] = 110 * np.exp(-((u - 32) / 13) ** 2) * np.exp(-((v - 50) / 34) ** 2)
                return out
            for k in ("F", "B"):
                t.pattern(L[k], 0, 0, 64, lv, ffn)
    t.dashed(F, (60, 120), (60, 128), stitch, 0.5)


def cargo(t, c):
    for L in LIMBS:
        t.pocket(L[OUTER[id(L)]], 14, 48, 50, 76, dark(c, 0.93), flap=True)


def side_stripe(t, col, lv, n=1):
    for L in LIMBS:
        o = L[OUTER[id(L)]]
        if n == 1:
            t.rect(o, 27, 0, 37, lv, col)
        else:
            for u in (22, 30, 38):
                t.rect(o, u, 0, u + 4, lv, col)
    for k in ("R", "L"):
        if n == 1:
            t.rect(TORSO[k], 27, 112, 37, 128, col)
        else:
            for u in (22, 30, 38):
                t.rect(TORSO[k], u, 112, u + 4, 128, col)


def crease(t, c, lv):
    for L in LIMBS:
        for k in ("F", "B"):
            t.line(L[k], [(32, 2), (32, lv)], dark(c, 0.8), 0.7)
            t.line(L[k], [(33.2, 2), (33.2, lv)], light(c, 0.15), 0.5)


def pleats(t, c, lv, step=8):
    for L in LIMBS:
        for k in SIDES:
            for u in range(step // 2, 64, step):
                t.line(L[k], [(u, 0), (u - 1.5, lv)], dark(c, 0.78), 0.9)
                t.line(L[k], [(u + 1.2, 0), (u - 0.3, lv)], light(c, 0.15), 0.5)
    for k in SIDES:
        for u in range(step // 2, TORSO[k][2], step):
            t.line(TORSO[k], [(u, 118), (u, 128)], dark(c, 0.8), 0.7)


def skirt_hem(t, c, lv):
    for L in LIMBS:
        for k in SIDES:
            t.rect(L[k], 0, lv - 5, 64, lv, dark(c, 0.86))
            t.line(L[k], [(0, lv), (64, lv)], dark(c, 0.6), 0.8)


def pattern_legs(t, fn, lv, torso=True):
    PH = {"F": 0, "R": 64, "B": 128, "L": 192}
    for L in LIMBS:
        for k in SIDES:
            t.pattern(L[k], 0, 0, 64, lv, fn, phase=(PH[k], 0))
    if torso:
        for k in SIDES:
            t.pattern(TORSO[k], 0, 112, TORSO[k][2], 128, fn, phase=(PH[k], 0))


def plaid_fn(c2, period=20):
    def fn(u, v):
        a = ((u % period) < period * 0.3).astype(np.float32)
        b = ((v % period) < period * 0.3).astype(np.float32)
        out = np.zeros(u.shape + (4,), np.float32)
        out[..., :3] = c2[:3]
        out[..., 3] = np.clip(a * 0.5 + b * 0.5, 0, 1) * 255
        return out
    return fn


def flowers_fn(c1, c2, period=18):
    def fn(u, v):
        row = np.floor(v / period)
        uu = u + (row % 2) * period / 2
        du = (uu % period) - period / 2
        dv = (v % period) - period / 2
        ang = np.arctan2(dv, du)
        rr = 3.6 * (1 + 0.45 * np.cos(5 * ang))
        d = np.sqrt(du * du + dv * dv)
        out = np.zeros(u.shape + (4,), np.float32)
        out[..., :3] = np.where((d < 1.4)[..., None], np.array(c2[:3], np.float32), np.array(c1[:3], np.float32))
        out[..., 3] = (d < rr) * 255
        return out
    return fn


def stripes_v_fn(col, period=10, w=4):
    def fn(u, v):
        out = np.zeros(u.shape + (4,), np.float32)
        out[..., :3] = col[:3]
        out[..., 3] = ((u % period) < w) * 255
        return out
    return fn


BRUN_CUIR = hexc("5a3a24")


def P01(t):
    lv = base(t, C["jean"], belt=BRUN_CUIR); jean_details(t, C["jean"], lv); hem(t, C["jean"], lv); shoes(t, "basket", C["blanc"], hexc("d8d8d8"))
def P02(t):
    c = C["jean_c"]; lv = base(t, c, belt=hexc("3a2a20")); jean_details(t, c, lv); hem(t, c, lv, "roll"); shoes(t, "basket", C["azur"])
def P03(t):
    c = hexc("2d2f36"); lv = base(t, c, belt=C["noir"]); jean_details(t, c, lv, stitch=hexc("6c6e76"), fade=False); hem(t, c, lv); shoes(t, "bottine", C["noir"], hexc("3a3a3a"))
def P04(t):
    c = hexc("cdb38a"); lv = base(t, c, belt=BRUN_CUIR); crease(t, c, lv); hem(t, c, lv)
    for L in LIMBS:
        t.line(L["B"], [(16, 10), (48, 10)], dark(c, 0.7), 0.9)
    shoes(t, "mocassin", hexc("7a4a2a"), hexc("3a2616"))
def P05(t):
    c = C["kaki"]; lv = base(t, c, belt=hexc("3d3a26")); cargo(t, c); hem(t, c, lv); shoes(t, "botte", hexc("6a4a30"), hexc("2a2018"))
def P06(t):
    c = C["gris"]; lv = base(t, c, belt=None, fly=False); hem(t, c, lv, "elastic")
    for k in SIDES:
        t.rect(TORSO[k], 0, 112, TORSO[k][2], 120, dark(c, 0.9))
    t.line(F, [(56, 120), (54, 128)], C["blanc"], 0.9); t.line(F, [(72, 120), (74, 128)], C["blanc"], 0.9)
    side_stripe(t, C["blanc"], lv - 8); shoes(t, "basket", C["noir"], C["blanc"])
def P07(t):
    c = C["marine"]; lv = base(t, c, belt=None, fly=False); hem(t, c, lv, "elastic"); side_stripe(t, C["blanc"], lv - 8, n=3)
    shoes(t, "basket", C["blanc"], C["marine"])
def P08(t):
    c = hexc("44474f"); lv = base(t, c, belt=C["noir"]); crease(t, c, lv); hem(t, c, lv); shoes(t, "chaussure", hexc("1e1e22"), hexc("111114"))
def P09(t):
    c = C["marine"]; lv = base(t, c, belt=C["noir"]); crease(t, c, lv); side_stripe(t, C["or_"], lv); shoes(t, "chaussure", C["noir"], hexc("111111"))
    t.rect(F, 57, 112.5, 71, 122.5, C["or_"])
def P10(t):
    c = C["blanc"]; lv = base(t, c, belt=None); crease(t, c, lv); hem(t, c, lv); shoes(t, "basket", C["blanc"], C["turquoise"])
def P11(t):
    c = hexc("7b5236"); lv = base(t, c, belt=hexc("2e1f14"))
    def fn(u, v):
        out = np.zeros(u.shape + (4,), np.float32)
        out[..., :3] = dark(c, 0.8)[:3]
        out[..., 3] = ((u % 4) < 1.3) * 200
        return out
    pattern_legs(t, fn, lv, torso=False); hem(t, c, lv); shoes(t, "bottine", hexc("3a2a1e"), hexc("1e140e"))
def P12(t):
    c = hexc("355d8c"); lv = base(t, c, belt=BRUN_CUIR); hem(t, c, lv)
    for L in LIMBS:
        t.rect(L["F"], 8, 52, 56, 76, dark(c, 0.82)); t.dashed(L["F"], (10, 54), (54, 54), ORANGE_ST, 0.5)
        t.dashed(L["F"], (10, 74), (54, 74), ORANGE_ST, 0.5)
        t.pocket(L[OUTER[id(L)]], 16, 20, 48, 46, dark(c, 0.9))
        t.rect(L[OUTER[id(L)]], 44, 20, 48, 40, C["gris"])
    shoes(t, "botte", hexc("5a3e26"), hexc("201810"), 30)
def P13(t):
    c = C["jean"]; lv = base(t, c, "short", belt=BRUN_CUIR); jean_details(t, c, lv, fade=False); hem(t, c, lv, "roll")
    socks(t, C["blanc"], 8, 16); shoes(t, "basket", C["blanc"], hexc("cccccc"))
def P14(t):
    c = C["sable"]; lv = base(t, c, "short", belt=hexc("6a4a2a")); cargo(t, c) if False else None
    for L in LIMBS:
        t.pocket(L[OUTER[id(L)]], 14, 18, 50, 44, dark(c, 0.92), flap=True)
    hem(t, c, lv); shoes(t, "sandale", hexc("6a4a2a"), hexc("3a2a1a"))
def P15(t):
    c = C["turquoise"]; lv = base(t, c, "court", belt=None, fly=False)
    pattern_legs(t, stripes_v_fn(C["blanc"], 12, 4), lv); hem(t, c, lv)
    for k in SIDES:
        t.rect(TORSO[k], 0, 112, TORSO[k][2], 118, C["blanc"])
    t.line(F, [(60, 118), (58, 126)], C["blanc"], 1); t.line(F, [(68, 118), (70, 126)], C["blanc"], 1)
    shoes(t, "sandale", C["azur"], C["marine"])
def P16(t):
    c = C["sapin"]; lv = base(t, c, "short", belt=hexc("2a2a2a")); lv2 = lv
    for L in LIMBS:
        t.rect(L["F"], 0, lv - 6, 64, lv, dark(c, 0.9))
    hem(t, c, lv, "roll"); shoes(t, "basket", hexc("d9c49a"), C["blanc"])
def P17(t):
    c = C["marine"]; lv = base(t, c, "34", belt=None); hem(t, c, lv, "roll")
    for L in LIMBS:
        t.line(L[OUTER[id(L)]], [(32, lv - 14), (32, lv)], C["blanc"], 1)
    shoes(t, "espadrille" if False else "ballerine", C["rouge"], dark(C["rouge"], 0.6))
def P18(t):
    c = C["marine"]; lv = base(t, c, "skirt", belt=None, fly=False); pleats(t, c, lv); skirt_hem(t, c, lv)
    socks(t, C["blanc"], 30, 10); shoes(t, "ballerine", C["noir"], hexc("222222"), 10)
def P19(t):
    c = C["terre"]; lv = base(t, c, "skirt", belt=hexc("4a2e1e"), fly=False, loops=False); skirt_hem(t, c, lv)
    for L in LIMBS:
        for k in SIDES:
            t.line(L[k], [(20, 6), (16, lv - 6)], dark(c, 0.85), 0.8); t.line(L[k], [(44, 6), (48, lv - 6)], dark(c, 0.85), 0.8)
    shoes(t, "ballerine", hexc("6a3a2a"), hexc("3a2015"), 10)
def P20(t):
    c = C["creme"]; lv = base(t, c, "skirtlong", belt=None, fly=False); pattern_legs(t, flowers_fn(C["rose"], C["jaune"]), lv)
    skirt_hem(t, c, lv); shoes(t, "sandale", hexc("8a5a3a"), hexc("4a3020"))
def P21(t):
    c = C["jean"]; lv = base(t, c, "skirt", belt=BRUN_CUIR, fly=False); skirt_hem(t, c, lv)
    for L in LIMBS:
        t.dashed(L["F"], (0, lv - 7), (64, lv - 7), ORANGE_ST, 0.5)
        t.pocket(L["B"], 14, 4, 50, 26, c, stitch=ORANGE_ST)
    t.line(F, [(64, 118), (64, 128)], dark(c, 0.6), 0.9)
    for L in LIMBS:
        t.line(L["F"], [(INNER[id(L)] == "L" and 64 or 0, 0), (INNER[id(L)] == "L" and 64 or 0, lv)], dark(c, 0.6), 1)
    shoes(t, "basket", C["rose"], C["blanc"])
def P22(t):
    c = C["jean"]; lv = base(t, c, belt=None); jean_details(t, c, lv); hem(t, c, lv, "roll")
    for k in ("R", "L"):
        t.rect(TORSO[k], 0, 112, 64, 128, c)
    shoes(t, "botte", hexc("6a4a30"), hexc("2a2018"), 26)
def P23(t):
    c = C["jaune"]; lv = base(t, c, belt=None, fly=False)
    for k in SIDES:
        t.rect(TORSO[k], 0, 112, TORSO[k][2], 120, dark(c, 0.85))
    for L in LIMBS:
        for k in ("F", "B"):
            t.line(L[k], [(10, 30), (54, 34)], dark(c, 0.85), 0.8)
    shoes(t, "botte_pluie", C["sapin"], dark(C["sapin"], 0.6))
def P24(t):
    c = hexc("4f5a6e"); lv = base(t, c, belt=C["noir"]); pattern_legs(t, plaid_fn(hexc("7d8aa3")), lv); crease(t, c, lv)
    shoes(t, "chaussure", hexc("5a3a24"), hexc("2a1a10"))
def P25(t):
    c = hexc("232327"); lv = base(t, c, belt=None, fly=False, waist=14)
    shoes(t, "bottine", hexc("7a4a2a"), hexc("3a2616"), 28)
def P26(t):
    c = C["sable"]; lv = base(t, c, belt=None, fly=False)
    for k in SIDES:
        t.rect(TORSO[k], 0, 112, TORSO[k][2], 122, C["terre"])
    embroidery_b(t, C["turquoise"])
    for L in LIMBS:
        for k in SIDES:
            t.arc(L[k], 4, 40, 60, 70, 200, 340, dark(c, 0.82), 0.9)
            t.arc(L[k], 4, 70, 60, 98, 200, 340, dark(c, 0.84), 0.8)
            t.rect(L[k], 0, 100, 64, 112, dark(c, 0.92))
            for u in range(2, 64, 3):
                t.line(L[k], [(u, 100), (u, 112)], dark(c, 0.8), 0.5)
    shoes(t, "sandale", C["terre"], hexc("4a2e1e"))
def P27(t):
    c = hexc("a4462f"); lv = base(t, c, belt=hexc("3a2418")); crease(t, c, lv); hem(t, c, lv, "roll"); shoes(t, "basket", C["blanc"], C["rouge"])
def P28(t):
    c = C["olive"]; lv = base(t, c, belt=hexc("3d3a26")); cargo(t, c)
    for L in LIMBS:
        t.rect(L["F"], 10, 50, 54, 74, dark(c, 0.85))
    shoes(t, "botte_pluie", C["vert"], dark(C["vert"], 0.55))
def P29(t):
    c = hexc("6f7076"); lv = base(t, c, "skirtlong", belt=None, fly=False); pleats(t, c, lv, 12); skirt_hem(t, c, lv)
    shoes(t, "chaussure", hexc("3a2a20"), hexc("1e140e"))
def P30(t):
    c = C["rouge"]; lv = base(t, c, "short", belt=None); hem(t, c, lv, "roll")
    for L in LIMBS:
        t.pocket(L["B"], 16, 6, 48, 24, dark(c, 0.92))
    socks(t, C["blanc"], 28, 16)
    for L in LIMBS:
        for k in SIDES:
            t.rect(L[k], 0, 86, 64, 89, C["azur"]); t.rect(L[k], 0, 91, 64, 93, C["azur"])
    shoes(t, "basket", C["azur"], C["blanc"])


def embroidery_b(t, col):
    def fn(u, v):
        tri = np.abs((u % 8) - 4) + (v - 112) * 0.9
        on = (np.abs(tri - 5) < 1.1).astype(np.float32)
        out = np.zeros(u.shape + (4,), np.float32)
        out[..., :3] = col[:3]
        out[..., 3] = on * 255
        return out
    for k in SIDES:
        t.pattern(TORSO[k], 0, 112, TORSO[k][2], 122, fn)


PANTS = [
    (P01, "Jean bleu"), (P02, "Jean délavé"), (P03, "Jean noir"), (P04, "Chino beige"),
    (P05, "Pantalon cargo kaki"), (P06, "Jogging gris"), (P07, "Survêtement marine"),
    (P08, "Pantalon de costume"), (P09, "Pantalon d'uniforme"), (P10, "Pantalon blanc"),
    (P11, "Velours côtelé"), (P12, "Pantalon de travail"), (P13, "Short en jean"),
    (P14, "Short cargo beige"), (P15, "Short de plage rayé"), (P16, "Bermuda vert"),
    (P17, "Pantacourt marine"), (P18, "Jupe plissée marine"), (P19, "Jupe terracotta"),
    (P20, "Jupe longue fleurie"), (P21, "Jupe en jean"), (P22, "Bas de salopette"),
    (P23, "Ciré de pêche et bottes"), (P24, "Pantalon à carreaux"), (P25, "Legging noir"),
    (P26, "Sarouel sable"), (P27, "Pantalon brique"), (P28, "Pantalon de jardinier"),
    (P29, "Jupe longue grise"), (P30, "Short rouge et chaussettes"),
]
