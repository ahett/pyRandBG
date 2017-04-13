import os
import time
import random
from PIL import Image, ImageFilter


def get_random_files():
    indir = '/home/adrian/Bilder/Wallpaper/'    # hardcoded for my personal use
    files = os.listdir(indir)                   # get files in directory
    num_files = len(files)                      #get number of files in directory

    # rmove final composed picture, we do not want this to be drawn
    files.remove("__00final.png")

    not_yet_drawn = list(range(0, num_files-1))
    # make sure a file is not drawn twice
    # for that we remove the just drawn index from the possible choices
    idx0 = random.choice(not_yet_drawn)
    not_yet_drawn.remove(idx0)
    idx1 = random.choice(not_yet_drawn)
    not_yet_drawn.remove(idx1)
    idx2 = random.choice(not_yet_drawn)
    not_yet_drawn.remove(idx2)
    idx3 = random.choice(not_yet_drawn)

    # create filelist
    ret = [indir + files[idx0],
           indir + files[idx1],
           indir + files[idx2],
           indir + files[idx3]]

    return ret


def create_spanning(files):

    im1 = Image.open(files[0]).resize((2560,1440))  # open and resize images in case the picture has the wrong size
    im2 = Image.open(files[1]).resize((2560,1440))
    im3 = Image.open(files[2]).resize((2560,1440))
    im4 = Image.open(files[3]).resize((1920,1200))  # last monitor has a different resolution

    ret = Image.new("RGB",(9600,1440))              # create new image with correct size hat spans above all monitors
    ret.paste(im1, (0,0))                           # paste images into new image
    ret.paste(im2, (2560,0))
    ret.paste(im3, (5120,0))
    ret.paste(im4, (7680,0))

    finalname='/home/adrian/Bilder/Wallpaper/__00final.png'     # hardcoded, __00final because it should be first appearing image, so it can be easyly excluded
    ret.save(finalname)                             # save file
    return finalname                                # return name


def set_background(file):
    os.system("gsettings set org.gnome.desktop.background picture-options spanned")         # set setting to 'spanned'
    os.system("gsettings set org.gnome.desktop.background picture-uri file://" + file + "") # set image


while True:
    files = get_random_files()          # get random files
    spanned = create_spanning(files)    # create spanned images
    set_background(spanned)             # set background
    time.sleep(300)                      # sleep 30 seconds