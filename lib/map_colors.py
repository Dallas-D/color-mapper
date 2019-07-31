from matplotlib import pyplot as plt
import fnmatch
import os
from utils import closest_color, ciede_distance
from aek import *
from wad import *
from grey import *

# Possible color-palettes:
# 16 color: WAD_OPTIMUM, AEK_16
# 32 color: AEK_32
# 54 color: AEK_54

dir = 'testing'
extend_grey_palette(16)
color_pal = GREY
rgb = False
use_archive = False

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
            if (img.shape[2] == 4 and pixel[3] != 0) or img.shape[2] == 3:
                pixel[:3] = closest_color(pixel[:3], color_pal, rgb, use_archive)
    plt.imshow(img)
    plt.show()
    try:
        plt.imsave('testing_' + name, img)
    except:
        print 'Could not write:' + name

