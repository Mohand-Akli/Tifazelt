import os, sys, time, unicodedata, re
from PIL import Image, ImageDraw, ImageFont
from lib import *
import shirts, pants

OUT = sys.argv[1]
os.makedirs(OUT + "/Hauts", exist_ok=True)
os.makedirs(OUT + "/Bas", exist_ok=True)


def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^A-Za-z0-9]+", "_", s).strip("_")


only = sys.argv[2] if len(sys.argv) > 2 else None
files = {"H": [], "B": []}
for kind, lst, sub in (("H", shirts.SHIRTS, "Hauts"), ("B", pants.PANTS, "Bas")):
    for i, (fn, name) in enumerate(lst, 1):
        p = f"{OUT}/{sub}/{kind}{i:02d}_{slug(name)}.png"
        files[kind].append((p, name))
        if only and only != f"{kind}{i:02d}" and only != kind:
            continue
        t0 = time.time()
        t = Tpl(); fn(t); t.finish(p, all_faces(), seed=i)
        print(kind, i, name, round(time.time() - t0, 2), flush=True)

# ---------- aperçus (mannequin R6 avant / arrière)
SKIN = (234, 192, 160, 255)


def crop(img, r):
    x, y, w, h = r
    return img.crop((x, y, x + w, y + h))


def mannequin(sh, pa, back=False):
    W2, H2 = 256, 320
    im = Image.new("RGBA", (W2, H2), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    # tête
    d.rounded_rectangle([96, 0, 160, 62], 14, fill=SKIN)
    if not back:
        d.ellipse([112, 22, 120, 32], fill=(30, 30, 30, 255)); d.ellipse([136, 22, 144, 32], fill=(30, 30, 30, 255))
        d.arc([112, 30, 144, 50], 20, 160, fill=(30, 30, 30, 255), width=3)
    tf = "B" if back else "F"
    arms = [(shirts.LIMB_L, 0), (shirts.LIMB_R, 192)] if back else [(shirts.LIMB_R, 0), (shirts.LIMB_L, 192)]
    legs = [(shirts.LIMB_L, 64), (shirts.LIMB_R, 128)] if back else [(shirts.LIMB_R, 64), (shirts.LIMB_L, 128)]
    def put(src_list, r, x, y):
        blk = Image.new("RGBA", (r[2], r[3]), SKIN)
        for s in src_list:
            if s is not None:
                blk.alpha_composite(crop(s, r))
        im.alpha_composite(blk, (x, y))
    put([pa, sh], TORSO[tf], 64, 64)
    for L, x in arms:
        put([sh], L[tf], x, 64)
    for L, x in legs:
        put([pa], L[tf], x, 192)
    return im


def sheet(pairs, path, title):
    cols = 6
    cw, ch = 300, 230
    rows = (len(pairs) + cols - 1) // cols
    out = Image.new("RGBA", (cols * cw, rows * ch + 50), (238, 240, 244, 255))
    d = ImageDraw.Draw(out)
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 17)
        big = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 26)
    except Exception:
        font = big = ImageFont.load_default()
    d.text((16, 12), title, fill=(30, 30, 40), font=big)
    for n, (label, sh, pa) in enumerate(pairs):
        cx, cy = (n % cols) * cw, (n // cols) * ch + 50
        f = mannequin(sh, pa).resize((128, 160), Image.LANCZOS)
        b = mannequin(sh, pa, back=True).resize((128, 160), Image.LANCZOS)
        fs = mannequin(sh, pa).resize((256, 320), Image.LANCZOS)
        out.alpha_composite(f.resize((136, 170), Image.LANCZOS), (cx + 10, cy + 10))
        out.alpha_composite(b.resize((136, 170), Image.LANCZOS), (cx + 154, cy + 10))
        d.text((cx + 10, cy + 190), label, fill=(30, 30, 40), font=font)
    out.convert("RGB").save(path, quality=90)


if not only:
    load = lambda p: Image.open(p).convert("RGBA")
    neutral_p = load(files["B"][0][0])
    neutral_s = load(files["H"][0][0])
    sheet([(f"H{i:02d} {n}", load(p), neutral_p) for i, (p, n) in enumerate(files["H"], 1)],
          OUT + "/apercu_hauts.jpg", "30 hauts (avec Jean bleu)")
    sheet([(f"B{i:02d} {n}", neutral_s, load(p)) for i, (p, n) in enumerate(files["B"], 1)],
          OUT + "/apercu_bas.jpg", "30 bas (avec T-shirt blanc)")
