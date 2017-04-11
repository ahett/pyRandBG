import os
import time
from random import randint
from PIL import Image, ImageFilter


def get_random_files():
    indir = '/home/adrian/Bilder/Wallpaper/'    # hardcoded for my personal use
    files = os.listdir(indir)
    num_files = len(files)

    # exclude first picture, this is our composed picture and we do not want this to be drawn
    ret = [indir + files[randint(1, num_files - 1)],
           indir + files[randint(1, num_files - 1)],
           indir + files[randint(1, num_files - 1)],
           indir + files[randint(1, num_files - 1)]]

    return ret


def create_spanning(files):

    im1 = Image.open(files[0]).resize((2560,1440))
    im2 = Image.open(files[1]).resize((2560,1440))
    im3 = Image.open(files[2]).resize((2560,1440))
    im4 = Image.open(files[3]).resize((1920,1200))

    ret = Image.new("RGB",(9600,1440))
    ret.paste(im1, (0,0))
    ret.paste(im2, (2560,0))
    ret.paste(im3, (5120,0))
    ret.paste(im4, (7680,0))

    finalname='/home/adrian/Bilder/Wallpaper/__00final.png'
    ret.save(finalname)
    return finalname


def set_background(file):
    os.system("gsettings set org.gnome.desktop.background picture-uri file://" + file + "")
    os.system("gsettings set org.gnome.desktop.background picture-options spanned")


while True:
    files = get_random_files()
    spanned = create_spanning(files)
    set_background(spanned)
    time.sleep(30)