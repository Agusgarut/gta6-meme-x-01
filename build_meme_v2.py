#!/usr/bin/env python3
"""gta6-meme-x-01 v2 — 'VICE MART' flat poster, built to the #1's visual grammar.

Three stacked bands, all drawn in PIL (crisp text, no generator garbling):
  1. a shelf strip of 8 stylised GTA cover tiles, 1997 -> 2026 (NEW! badge),
  2. a Vice City sunset skyline with the REAL make.fun mark huge and centred
     over a magenta counter, a 'make.fun' chip and a gold NOW SERVING #2013 ticket,
  3. a receipt panel itemising the wait, PAID IN FULL stamp, wood footer strip.
Store name and receipt wording are our own; the genre numbers (13 years,
2 delays, 214 GB, 5 sick days, $79.99) are the shared top-8 vocabulary.
"""
import random
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 1500
DIR = "/home/hatch/workspace/makefun/gta6-meme-x-01"

BLACK = "/usr/share/fonts/truetype/noto/NotoSans-Black.ttf"
BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"

NAVY = (23, 32, 63)
MAGENTA = (201, 30, 120)
MAGENTA_DARK = (178, 24, 102)
CREAM = (246, 241, 231)
PAPER = (253, 252, 248)
GOLD = (247, 181, 0)
WOOD = (176, 106, 44)
WOOD_DARK = (140, 80, 30)
GREY = (120, 120, 130)

img = Image.new("RGB", (W, H), CREAM)
d = ImageDraw.Draw(img, "RGBA")


def F(path, size):
    return ImageFont.truetype(path, size)


def text_c(draw, cx, y, s, font, fill):
    w = draw.textlength(s, font=font)
    draw.text((cx - w / 2, y), s, font=font, fill=fill)
    return w


def rrect(draw, box, r, **kw):
    draw.rounded_rectangle(box, radius=r, **kw)


# ---------------------------------------------------------------- frame
d.rectangle([18, 18, W - 18, H - 18], outline=NAVY, width=4)

# ---------------------------------------------------------------- band 1: cover tiles
TILES = [
    ("GTA", "1997"),
    ("GTA II", "1999"),
    ("GTA III", "2001"),
    ("VICE CITY", "2002"),
    ("SAN ANDREAS", "2004"),
    ("GTA IV", "2008"),
    ("GTA V", "2013"),
    ("GTA VI", "2026"),
]
TX0, TY0, TW, TH, TGAP = 36, 44, 130, 168, 12
LABEL_H = 42


def palm(draw, x, y, s, color):
    """Tiny flat palm: curved trunk + drooping fronds. (x, y) = ground point."""
    top = (x + 6 * s, y - 52 * s)
    pts = [(x + (i / 8) * 6 * s, y - (i / 8) * 52 * s - (i / 8) ** 2 * 4 * s) for i in range(9)]
    draw.line(pts, fill=color, width=max(2, int(5 * s)))
    for dx, dy in [(-34, -6), (-22, -18), (-6, -25), (12, -24), (26, -16), (36, -4)]:
        ex, ey = top[0] + dx * s, top[1] + dy * s + 20 * s
        mid = (top[0] + dx * s * 0.55, top[1] + dy * s - 2 * s)
        seg = [top]
        for t in (0.25, 0.5, 0.75, 1.0):
            seg.append(((1 - t) ** 2 * top[0] + 2 * (1 - t) * t * mid[0] + t * t * ex,
                        (1 - t) ** 2 * top[1] + 2 * (1 - t) * t * mid[1] + t * t * ey))
        draw.line(seg, fill=color, width=max(2, int(4 * s)))
    draw.ellipse([top[0] - 4 * s, top[1] - 2 * s, top[0] + 3 * s, top[1] + 5 * s], fill=color)


def tile_art(i, x, y):
    """Draw the motif area of tile i (label strip added by caller)."""
    box = [x, y, x + TW, y + TH - LABEL_H]
    t = Image.new("RGBA", (TW, TH - LABEL_H), (0, 0, 0, 0))
    td = ImageDraw.Draw(t)
    aw, ah = TW, TH - LABEL_H
    if i == 0:  # GTA 1997 — top-down road on red
        td.rectangle([0, 0, aw, ah], fill=(158, 34, 34))
        td.rectangle([aw // 2 - 17, 0, aw // 2 + 17, ah], fill=(52, 52, 58))
        for yy in range(4, ah, 22):
            td.rectangle([aw // 2 - 2, yy, aw // 2 + 2, yy + 11], fill=(250, 204, 60))
    elif i == 1:  # GTA II 1999 — orange city grid
        td.rectangle([0, 0, aw, ah], fill=(224, 123, 36))
        for gx in range(0, aw, 26):
            td.line([(gx, 0), (gx, ah)], fill=(146, 74, 16), width=5)
        for gy in range(0, ah, 26):
            td.line([(0, gy), (aw, gy)], fill=(146, 74, 16), width=5)
        td.rectangle([55, 30, 79, 54], fill=(30, 30, 30))
    elif i == 2:  # GTA III 2001 — blue skyline + cab
        td.rectangle([0, 0, aw, ah], fill=(47, 109, 179))
        for bx, bh in [(4, 52), (30, 74), (58, 44), (82, 66), (106, 50)]:
            td.rectangle([bx, ah - bh, bx + 22, ah], fill=(18, 38, 74))
        td.rectangle([38, ah - 20, 92, ah - 6], fill=(250, 190, 40))
        td.rectangle([52, ah - 28, 78, ah - 20], fill=(250, 190, 40))
    elif i == 3:  # VICE CITY 2002 — pink sky, sun, palm
        td.rectangle([0, 0, aw, ah], fill=(239, 127, 174))
        td.ellipse([70, 14, 112, 56], fill=(255, 230, 160))
        palm(td, 40, ah - 4, 0.9, (90, 30, 70))
    elif i == 4:  # SAN ANDREAS 2004 — green hills, orange peaks
        td.rectangle([0, 0, aw, ah], fill=(46, 139, 110))
        td.ellipse([84, 10, 118, 44], fill=(255, 176, 84))
        td.polygon([(0, ah), (44, 44), (88, ah)], fill=(196, 102, 40))
        td.polygon([(52, ah), (96, 58), (aw, ah)], fill=(150, 74, 32))
    elif i == 5:  # GTA IV 2008 — night skyline, lit windows
        td.rectangle([0, 0, aw, ah], fill=(59, 42, 93))
        rng = random.Random(7)
        for bx, bw, bh in [(4, 26, 84), (36, 22, 62), (64, 28, 96), (98, 26, 70)]:
            td.rectangle([bx, ah - bh, bx + bw, ah], fill=(16, 12, 34))
            for _ in range(9):
                wx = bx + rng.randrange(3, bw - 8)
                wy = ah - bh + rng.randrange(4, bh - 12)
                td.rectangle([wx, wy, wx + 5, wy + 7], fill=(255, 209, 102))
    elif i == 6:  # GTA V 2013 — sunset stripes + palm
        stripes = [(214, 51, 108), (240, 101, 74), (250, 152, 74), (124, 62, 128)]
        for k, c in enumerate(stripes):
            td.rectangle([0, k * ah // 4, aw, (k + 1) * ah // 4], fill=c)
        td.rectangle([0, ah - 16, aw, ah], fill=(30, 16, 54))
        palm(td, 66, ah - 10, 0.85, (30, 16, 54))
    else:  # GTA VI 2026 — pink/purple sunset, big sun, palm
        for k, c in enumerate([(178, 34, 110), (222, 61, 122), (247, 118, 96), (252, 176, 96)]):
            td.rectangle([0, k * ah // 4, aw, (k + 1) * ah // 4], fill=c)
        td.ellipse([36, 26, 94, 84], fill=(255, 222, 140))
        td.rectangle([0, ah - 14, aw, ah], fill=(64, 20, 84))
        palm(td, 96, ah - 6, 0.9, (64, 20, 84))
    img.paste(t, (x, y), t)


for i, (name, year) in enumerate(TILES):
    x = TX0 + i * (TW + TGAP)
    tile_art(i, x, TY0)
    d.rectangle([x, TY0 + TH - LABEL_H, x + TW, TY0 + TH], fill=(20, 16, 40))
    text_c(d, x + TW / 2, TY0 + TH - LABEL_H + 3, name, F(BOLD, 15), (255, 255, 255))
    text_c(d, x + TW / 2, TY0 + TH - LABEL_H + 21, year, F(BOLD, 14), (255, 209, 102))
    d.rectangle([x, TY0, x + TW, TY0 + TH], outline=NAVY, width=3)

# NEW! badge on the GTA VI tile
badge = Image.new("RGBA", (100, 100), (0, 0, 0, 0))
bd = ImageDraw.Draw(badge)
bd.ellipse([8, 8, 92, 92], fill=(230, 30, 110), outline=(255, 255, 255), width=5)
text_c(bd, 50, 38, "NEW!", F(BLACK, 21), (255, 255, 255))
badge = badge.rotate(14, resample=Image.BICUBIC, expand=True)
gx = TX0 + 7 * (TW + TGAP)
img.paste(badge, (gx + TW - 108, TY0 - 2), badge)
d = ImageDraw.Draw(img, "RGBA")

# shelf plank
d.rectangle([30, TY0 + TH + 4, W - 30, TY0 + TH + 28], fill=WOOD)
d.rectangle([30, TY0 + TH + 4, W - 30, TY0 + TH + 10], fill=(205, 138, 70))

# ---------------------------------------------------------------- band 2: sunset skyline
B2Y0, B2Y1 = 268, 716
sky = Image.new("RGB", (1, B2Y1 - B2Y0))
stops = [(0.0, (196, 30, 105)), (0.45, (240, 84, 96)), (0.78, (252, 140, 84)), (1.0, (255, 190, 105))]
px = sky.load()
for yy in range(B2Y1 - B2Y0):
    t = yy / (B2Y1 - B2Y0 - 1)
    for (t0, c0), (t1, c1) in zip(stops, stops[1:]):
        if t0 <= t <= t1:
            f = (t - t0) / (t1 - t0)
            px[0, yy] = tuple(round(c0[k] + (c1[k] - c0[k]) * f) for k in range(3))
            break
sky = sky.resize((W - 72, B2Y1 - B2Y0))
img.paste(sky, (36, B2Y0))
d = ImageDraw.Draw(img, "RGBA")

# sun + glow (right side, like #1)
d.ellipse([872, 330, 1048, 506], fill=(255, 190, 100, 70))
d.ellipse([898, 356, 1022, 480], fill=(255, 224, 148))

# storefront pane lines
for px_x in (412, 788):
    d.line([(px_x, B2Y0), (px_x, B2Y1)], fill=(90, 20, 60, 70), width=3)

# skyline, two layers
rng = random.Random(42)


def skyline(base, top_min, top_max, color, windows):
    x = 30
    while x < W - 30:
        bw = rng.randrange(46, 96)
        top = rng.randrange(top_min, top_max)
        d.rectangle([x, top, x + bw, base], fill=color)
        if windows:
            for wy in range(top + 12, base - 14, 24):
                for wx in range(x + 8, x + bw - 12, 19):
                    if rng.random() < 0.34:
                        d.rectangle([wx, wy, wx + 7, wy + 10], fill=(255, 209, 102))
        x += bw + rng.randrange(2, 10)


skyline(B2Y1, 566, 648, (96, 44, 112), False)
skyline(B2Y1, 606, 690, (33, 20, 64), True)
palm(d, 128, B2Y1 - 2, 1.15, (33, 20, 64))
palm(d, 1078, B2Y1 - 2, 1.15, (33, 20, 64))

# magenta counter trapezoid
d.polygon([(300, B2Y1), (900, B2Y1), (742, 606), (458, 606)], fill=MAGENTA)
d.line([(458, 606), (742, 606)], fill=(232, 90, 160), width=4)

# the REAL make.fun mark, hero-sized and centred
mark = Image.open(f"{DIR}/mark-1024.png").convert("RGBA").resize((408, 408), Image.LANCZOS)
img.paste(mark, (W // 2 - 204, 262), mark)
d = ImageDraw.Draw(img, "RGBA")

# make.fun chip under the ghost
chip_f = F(BLACK, 36)
chip_w = d.textlength("make.fun", font=chip_f) + 40
rrect(d, [W / 2 - chip_w / 2, 664, W / 2 + chip_w / 2, 716], 12, fill=(255, 255, 255), outline=NAVY, width=3)
text_c(d, W / 2, 674, "make.fun", chip_f, NAVY)

# gold ticket
tick_f = F(BLACK, 28)
tick = "NOW SERVING #2013"
tick_w = d.textlength(tick, font=tick_f) + 34
rrect(d, [1152 - tick_w, 640, 1152, 692], 10, fill=GOLD, outline=NAVY, width=3)
text_c(d, 1152 - tick_w / 2, 652, tick, tick_f, NAVY)

d.rectangle([36, B2Y0, W - 36, B2Y1], outline=NAVY, width=3)

# ---------------------------------------------------------------- band 3: receipt
PX0, PY0, PX1, PY1 = 48, 736, 1152, 1396
rrect(d, [PX0, PY0, PX1, PY1], 18, fill=PAPER, outline=NAVY, width=5)
IX0, IX1 = PX0 + 38, PX1 - 38

d.text((IX0, 762), "VICE MART", font=F(BLACK, 66), fill=NAVY)
cd_f = F(BOLD, 25)
cd = "CUSTOMER DISPLAY"
d.text((IX1 - d.textlength(cd, font=cd_f), 792), cd, font=cd_f, fill=MAGENTA)
d.line([(IX0, 852), (IX1, 852)], fill=MAGENTA, width=4)

ROWS = [
    ("13 years in the queue", "$0.00", NAVY),
    ("Two delays — surcharge waived", "$0.00", NAVY),
    ("214 GB download", "$0.00", NAVY),
    ("Patience — completely spent", "$0.00", NAVY),
    ("Sick days for launch week", "5 PTO days", NAVY),
    ("Grand Theft Auto VI — standard", "$79.99", MAGENTA),
]
row_f = F(BOLD, 31)
ry = 880
for label, price, color in ROWS:
    d.text((IX0, ry), label, font=row_f, fill=color)
    pw = d.textlength(price, font=row_f)
    d.text((IX1 - pw, ry), price, font=row_f, fill=color)
    lx = IX0 + d.textlength(label, font=row_f) + 14
    rx = IX1 - pw - 16
    dx = lx
    while dx < rx:
        d.ellipse([dx, ry + 24, dx + 4, ry + 28], fill=GREY)
        dx += 13
    ry += 58

tot_f = F(BLACK, 54)
d.text((IX0, 1246), "TOTAL DUE", font=tot_f, fill=NAVY)
tp = "$79.99"
d.text((IX1 - d.textlength(tp, font=tot_f), 1246), tp, font=tot_f, fill=MAGENTA)

# stamp, rotated, over the total row
stamp = Image.new("RGBA", (560, 140), (0, 0, 0, 0))
sd = ImageDraw.Draw(stamp)
sd.rounded_rectangle([6, 6, 554, 134], radius=14, outline=MAGENTA, width=7)
text_c(sd, 280, 20, "PAID IN FULL", F(BLACK, 42), MAGENTA)
text_c(sd, 280, 78, "BY MY AI AGENT ON MAKE.FUN", F(BOLD, 29), MAGENTA)
stamp = stamp.rotate(7, resample=Image.BICUBIC, expand=True)
img.paste(stamp, (W // 2 - stamp.width // 2 + 24, 1288 - stamp.height // 2), stamp)
d = ImageDraw.Draw(img, "RGBA")

# ---------------------------------------------------------------- footer strip
d.rectangle([36, 1412, W - 36, 1464], fill=WOOD)
d.rectangle([36, 1412, W - 36, 1418], fill=(205, 138, 70))
rrect(d, [58, 1425, 124, 1453], 5, fill=(30, 22, 18))
foot_f = F(BOLD, 25)
d.text((146, 1426), "Checkout powered by make.fun — where AI agents earn real money.",
       font=foot_f, fill=(43, 24, 8))

img.save(f"{DIR}/meme-v2.png")
img.resize((512, 640), Image.LANCZOS).save(f"{DIR}/meme-v2-512.png")
print("saved meme-v2.png", img.size)
