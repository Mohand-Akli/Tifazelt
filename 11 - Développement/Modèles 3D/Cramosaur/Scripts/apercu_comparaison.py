import sys
from PIL import Image, ImageOps
fond = Image.new("RGBA", (1500, 470), (226, 236, 214, 255))
x = 20
for p in sys.argv[2:]:
    im = ImageOps.mirror(Image.open(p).convert("RGBA"))
    bb = im.getchannel("A").point(lambda a: 255 if a > 8 else 0).getbbox()
    im = im.crop(bb); h = 430
    im = im.resize((int(im.width * h / im.height), h), Image.LANCZOS)
    fond.alpha_composite(im, (x, 20)); x += im.width + 60
fond.convert("RGB").save(sys.argv[1])
