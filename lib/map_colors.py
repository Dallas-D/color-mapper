from matplotlib import pyplot as plt
import fnmatch
import os
from .utils import closest_color, ciede_distance
from color_palettes import *

# Possible color-palettes:
# 16 color: WAD_OPTIMUM, AEK_16
# 32 color: AEK_32
# 54 color: AEK_54

dir = 'directory to search/'
color_pal = COLOR_PALETTE_TO_USE

all_images = []
for root, dirnames, filenames in os.walk(dir):
    for filename in fnmatch.filter(filenames, '*.png'):
        all_images.append(os.path.join(root, filename))

curr_index = 0
for name in all_images:
    if curr_index % 100 == 0:
        print ('%d images left' % (len(all_images) - curr_index))
    curr_index += 1
    try:
        img = plt.imread(name)
    except:
        print 'Could not read:' + name
        continue
    for row in img:
        for pixel in row:
            pixel[:3] = closest_color(pixel[:3], color_pal)
    try:
        plt.imsave(name, img)
    except:
        print 'Could not write:' + name

