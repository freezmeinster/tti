import glob
import os
import textwrap
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

width = 1920
height = 1080
BASE = Path(".") / "result"
COLOR = (10, 149,255 )

def calfont(message):
    ln = len(message)
    return abs(ln - 170)

def genimg(message, fname):
    img = Image.new('RGBA', (width, height))
    font = ImageFont.truetype("LiberationSans-Regular.ttf",
            size=calfont(message))

    imgDraw = ImageDraw.Draw(img)

    message = "\n".join(textwrap.wrap(message, width=30))

    imgDraw.text((width/2, height/2),
            message,font=font,anchor="mm",align='center', fill=COLOR)

    target = str(BASE / str(fname)) + ".png"
    img.save(target) 

for fn in glob.glob(str(BASE) + "/*"):
    os.unlink(fn)

with open("source.txt") as src:
    ct = src.read()
    splt = ct.splitlines()
    for inx, txt in enumerate(splt):
        genimg(txt, inx)
