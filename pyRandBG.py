import os
import sys
import subprocess
import time
from random import randint
from PIL import Image, ImageFilter


def get_random_files():
    indir = '/home/adrian/Bilder/Wallpaper/'
    files = os.listdir(indir)
    num_files = len(files)

    ret = [indir + files[randint(0, num_files - 1)],
           indir + files[randint(0, num_files - 1)],
           indir + files[randint(0, num_files - 1)],
           indir + files[randint(0, num_files - 1)]]

    return ret


def create_spanning(files):

    im1 = Image.open(files[0]).resize(2560,1440)
    im2 = Image.open(files[1]).resize(2560,1440)
    im3 = Image.open(files[2]).resize(2560,1440)
    im4 = Image.open(files[3]).resize(1920,1200)

    ret=Image.new(9600,1440)
    return files[0]


def set_background(file):
    command = " gsettings set org.gnome.desktop.background picture-uri file://" + file + ""
    print(command)
    status = os.system(command)
    print(status)

while True:
    files = get_random_files()
    spanned = create_spanning(files)
    set_background(spanned)
    time.sleep(30)