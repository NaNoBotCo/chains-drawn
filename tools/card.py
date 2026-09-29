"""Share card, 1200x630: a creek, five towns each with a stove, and the title."""
import pathlib
from PIL import Image, ImageDraw, ImageFont

out = pathlib.Path(__file__).resolve().parent.parent / "docs" / "card.jpg"
W, H = 1200, 630
G, INK, GOLD, RUST, WOOD, CREEK, PANEL = (15, 23, 20), (232, 239, 233), (240, 194, 60), (229, 138, 69), (176, 122, 76), (47, 95, 134), (23, 33, 28)
img = Image.new("RGB", (W, H), G)
d = ImageDraw.Draw(img)
import math
for t in range(-20, H + 20, 2):
    x = 940 + 55 * math.sin(t / 45)
    d.ellipse([x - 24, t - 24, x + 24, t + 24], fill=CREEK)
d.line([(850, 330), (1040, 330)], fill=WOOD, width=14)

def town(x, y):
    d.polygon([(x - 34, y), (x, y - 34), (x + 34, y)], fill=PANEL, outline=INK, width=4)
    d.rectangle([x - 34, y, x + 34, y + 38], fill=PANEL, outline=INK, width=4)
    d.rectangle([x - 9, y + 12, x + 9, y + 38], fill=WOOD)
    sx, sy = x - 88, y + 2
    d.rectangle([sx, sy, sx + 42, sy + 34], fill=(44, 58, 50), outline=INK, width=3)
    d.rectangle([sx + 30, sy - 22, sx + 40, sy], fill=(44, 58, 50), outline=INK, width=2)
    d.ellipse([sx + 10, sy + 8, sx + 30, sy + 28], fill=RUST)
    d.rectangle([sx + 6, sy - 44, sx + 36, sy - 24], fill=GOLD, outline=INK, width=2)

for x, y in [(840, 70), (840, 500), (1110, 120), (1110, 300), (1110, 490)]:
    town(x, y)
fade = Image.new("L", (W, H), 0)
fd = ImageDraw.Draw(fade)
for i in range(620):
    fd.line([(i, 0), (i, H)], fill=int(255 * max(0.0, 1 - i / 620) ** 0.5))
img.paste(Image.new("RGB", (W, H), G), (0, 0), fade)
F = "/System/Library/Fonts/Supplemental/"
big = ImageFont.truetype(F + "Georgia Bold.ttf", 96)
th = ImageFont.truetype(F + "Tahoma Bold.ttf", 56)
small = ImageFont.truetype(F + "Courier New Bold.ttf", 28)
thsmall = ImageFont.truetype(F + "Tahoma.ttf", 30)
d.text((64, 110), "CHAINSATLAS & KIN, AS TOYS", font=small, fill=GOLD)
d.text((60, 160), "Chains, Drawn", font=big, fill=INK)
d.text((64, 285), "โซ่ วาดให้ดู", font=th, fill=(154, 169, 160))
d.text((64, 410), "Carry the mule, or carry the stove?", font=small, fill=INK)
d.text((64, 452), "จูงล่อข้ามไป หรือแบกเตาไปเอง", font=thsmall, fill=(154, 169, 160))
d.text((64, 560), "nanobotco.github.io/chains-drawn", font=small, fill=GOLD)
img.save(out, quality=88)
print(out)
