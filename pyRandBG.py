import os
import sys
import subprocess
from random import randint

if len(sys.argv) <= 1:
    print('no argumemts')
    indir = './'
else:
    indir = sys.argv[1]

print('directory:', indir)

files = os.listdir(indir)
numFiles = len(files)

chosenFiles = [indir + files[randint(0, numFiles - 1)],
               indir + files[randint(0, numFiles - 1)],
               indir + files[randint(0, numFiles - 1)],
               indir + files[randint(0, numFiles - 1)]]


singleChosenFull = chosenFiles[0];
print(singleChosenFull)
command = "gconftool-2 --set /desktop/gnome/background/picture_filename --type string '" + singleChosenFull + "'"
status = os.system(command)
print (status)
