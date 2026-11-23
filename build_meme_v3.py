#!/usr/bin/env python3
"""gta6-meme-x-01 v3 — 'CERTIFICATE OF LIVE BIRTH' for GTA VI.

Built to the live top-20 grammar for this bounty: an official-paperwork
document on cream paper, navy type, itemised bill whose jokes all carry a
number, a red rubber stamp, one deadpan punchline, and a single magenta
band at the bottom where the make.fun ghost pays the bill.

The fiction: after 13 years of labour (17 Sep 2013 -> 19 Nov 2026, two
inductions that sent everyone home — Fall 2025 and May 2026), Leonida
General Hospital issues the birth certificate for Grand Theft Auto VI.
Weight 214 GB. First witnesses: Jason & Lucia. Bill total: $79.99.
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1440
ASSETS = "/home/hatch/workspace/makefun/gta6-meme-x-01"
OUT = "/home/hatch/workspace/makefun/gta6-meme-x-01-repo/meme-v3.png"

SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF_I = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
SANS_BLACK = "/usr/share/fonts/truetype/noto/NotoSans-Black.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
MONO = "/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf"
MONO_B = "/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf"

NAVY = (23, 32, 63)
INK = (38, 38, 44)
MAGENTA = (201, 30, 120)
CREAM = (246, 241, 231)
PAPER = (253, 252, 248)
GOLD = (176, 134, 32)
GREY = (110, 108, 118)
STAMP_RED = (196, 30, 44)
WHITE = (255, 255, 255)


def F(path, size):
    return ImageFont.truetype(path, size)


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img, "RGBA")


def text_c(cx, y, s, font, fill, tracking=0):
    """Draw centred text, optionally letterspaced."""
    if tracking:
        widths = [d.textlength(ch, font=font) for ch in s]
        total = sum(widths) + tracking * (len(s) - 1)
        x = cx - total / 2
        for ch, wch in zip(s, widths):
            d.text((x, y), ch, font=font, fill=fill)
            x += wch + tracking
        return total
    w = d.textlength(s, font=font)
    d.text((cx - w / 2, y), s, font=font, fill=fill)
    return w


def rule(y, x0=92, x1=W - 92, fill=NAVY, width=3):
    d.line([(x0, y), (x1, y)], fill=fill, width=width)


# ---------------------------------------------------------------- paper frame
d.rectangle([34, 34, W - 34, H - 34], outline=NAVY, width=4)
d.rectangle([48, 48, W - 48, H - 48], outline=NAVY, width=1)

# ---------------------------------------------------------------- form header
d.text((92, 60), "FORM LGB-13 · REGISTRY OF LIVE BIRTHS", font=F(MONO, 22), fill=GREY)
cert = "CERT. NO. VI-13-2026"
d.text((W - 92 - d.textlength(cert, font=F(MONO_B, 22)), 60), cert, font=F(MONO_B, 22), fill=NAVY)

# ---------------------------------------------------------------- letterhead
text_c(W / 2, 92, "LEONIDA GENERAL HOSPITAL", F(SERIF_B, 50), NAVY, tracking=2)
text_c(W / 2, 150, "VICE CITY · STATE OF LEONIDA · EST. 1986", F(SANS_B, 20), GREY, tracking=5)
rule(192)
rule(199, width=1)

# ---------------------------------------------------------------- title
text_c(W / 2, 214, "CERTIFICATE OF LIVE BIRTH", F(SERIF_B, 54), NAVY, tracking=3)

# ---------------------------------------------------------------- headline
text_c(W / 2, 284, "IT'S A VI.", F(SANS_BLACK, 104), NAVY)

# ---------------------------------------------------------------- fields
LX, RX = 110, 762          # two field columns
COLW = 568
FY = 420


def field(x, y, label, value, value_size=31):
    d.text((x, y), label, font=F(SANS_B, 19), fill=GREY)
    d.text((x, y + 26), value, font=F(SERIF_B, value_size), fill=NAVY)
    d.line([(x, y + 26 + value_size + 12), (x + COLW, y + 26 + value_size + 12)],
           fill=(178, 174, 186), width=1)


field(LX, FY, "NAME OF CHILD", "GRAND THEFT AUTO VI")
field(RX, FY, "DATE OF BIRTH", "19 NOVEMBER 2026")
field(LX, FY + 80, "PLACE OF BIRTH", "VICE CITY, LEONIDA")
field(RX, FY + 80, "WEIGHT AT BIRTH", "214 GB")
field(LX, FY + 160, "MOTHER", "ROCKSTAR GAMES")
field(RX, FY + 160, "FATHER", "THE PLAYER")
field(LX, FY + 240, "FATHER IN WAITING ROOM SINCE", "17 SEP 2013", value_size=28)
field(RX, FY + 240, "FIRST WITNESSES", "JASON & LUCIA")

LY = FY + 320
d.text((LX, LY), "LABOUR", font=F(SANS_B, 19), fill=GREY)
d.text((LX, LY + 26),
       "13 YEARS — INDUCED TWICE (FALL 2025 · MAY 2026), SENT HOME BOTH TIMES",
       font=F(SERIF_B, 25), fill=NAVY)
d.line([(LX, LY + 64), (W - 110, LY + 64)], fill=(178, 174, 186), width=1)

# ---------------------------------------------------------------- the bill
BY = LY + 88
rule(BY, x0=110, x1=W - 110, width=2)
text_c(W / 2, BY + 10, "ITEMISED HOSPITAL ACCOUNT · ACCOUNT NO. 2013–2026",
       F(SANS_B, 22), NAVY, tracking=3)
rule(BY + 48, x0=110, x1=W - 110, width=2)

BILL = [
    ("Delivery suite — 4,811 days of labour", 47.99),
    ("Waiting-room coffee for the father — 13 years", 12.00),
    ("Trailers screened in the waiting room — 87", 6.50),
    ("Newborn's first download — 214 GB", 13.50),
    ("Two false alarms — Fall 2025 · May 2026 (sent home)", 0.00),
    ("Father's patience — used in full", 0.00),
]
assert abs(sum(p for _, p in BILL) - 79.99) < 1e-9, "bill must total $79.99"

row_f = F(SERIF, 26)
price_f = F(MONO_B, 26)
ry = BY + 62
for label, price in BILL:
    d.text((110, ry), label, font=row_f, fill=INK)
    ps = f"${price:,.2f}"
    pw = d.textlength(ps, font=price_f)
    d.text((W - 110 - pw, ry), ps, font=price_f, fill=INK)
    lx = 110 + d.textlength(label, font=row_f) + 16
    x = lx
    while x < W - 126 - pw:
        d.ellipse([x, ry + 21, x + 3, ry + 24], fill=(170, 166, 178))
        x += 11
    ry += 34

rule(ry + 2, x0=110, x1=W - 110, width=1)
rule(ry + 7, x0=110, x1=W - 110, width=3)
d.text((110, ry + 14), "TOTAL DUE", font=F(SERIF_B, 32), fill=NAVY)
tp = "$79.99"
d.text((W - 110 - d.textlength(tp, font=F(MONO_B, 32)), ry + 14), tp,
       font=F(MONO_B, 32), fill=MAGENTA)
TOTAL_Y = ry + 14

# ---------------------------------------------------------------- stamp
stamp = Image.new("RGBA", (520, 160), (0, 0, 0, 0))
sd = ImageDraw.Draw(stamp)
sd.rounded_rectangle([6, 6, 514, 154], radius=14, outline=STAMP_RED + (235,), width=7)
sd.rounded_rectangle([20, 20, 500, 140], radius=9, outline=STAMP_RED + (200,), width=2)
sf = F(SANS_BLACK, 78)
sw = sd.textlength("DELIVERED", font=sf)
sd.text(((520 - sw) / 2, 36), "DELIVERED", font=sf, fill=STAMP_RED + (225,))
stamp = stamp.rotate(13, expand=True, resample=Image.BICUBIC)
img.paste(stamp, (648, BY + 54), stamp)
d = ImageDraw.Draw(img, "RGBA")

# ---------------------------------------------------------------- punchline
text_c(W / 2, TOTAL_Y + 62,
       "Thirteen years in labour. The father never left the waiting room.",
       F(SERIF_I, 34), NAVY)

# ---------------------------------------------------------------- bottom band
BAND_Y = 1210
d.rectangle([0, BAND_Y, W, H], fill=MAGENTA)

ghost = Image.open(f"{ASSETS}/ghost-cutout.png").convert("RGBA")
gh = 198
ghost = ghost.resize((int(ghost.width * gh / ghost.height), gh), Image.LANCZOS)
img.paste(ghost, (64, BAND_Y + (H - BAND_Y - gh) // 2), ghost)
d = ImageDraw.Draw(img, "RGBA")

TX = 400
d.text((TX, BAND_Y + 36), "PAID BY MY AI AGENT", font=F(SANS_BLACK, 50), fill=WHITE)
d.text((TX, BAND_Y + 102), "with real money it won in make.fun bounties.",
       font=F(SERIF_I, 30), fill=WHITE)

# make.fun pill: white rounded chip, real mark + wordmark
mark = Image.open(f"{ASSETS}/mark-1024.png").convert("RGBA").resize((48, 48), Image.LANCZOS)
pill_f = F(SANS_BLACK, 30)
pill_label = "make.fun"
pill_w = 48 + 14 + d.textlength(pill_label, font=pill_f) + 40
pill_x, pill_y = TX, BAND_Y + 152
d.rounded_rectangle([pill_x, pill_y, pill_x + pill_w, pill_y + 64], radius=32, fill=WHITE)
img.paste(mark, (int(pill_x + 9), int(pill_y + 8)), mark)
d = ImageDraw.Draw(img, "RGBA")
d.text((pill_x + 70, pill_y + 15), pill_label, font=pill_f, fill=NAVY)

img.save(OUT)
print("saved", OUT, img.size)
