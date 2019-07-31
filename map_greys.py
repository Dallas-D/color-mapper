import cv2
import numpy as np
import fnmatch
import os
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Maps colors in a image to a \
            color from a specific color palette; iterates recursively throuhg a\
            directory of images.')
    parser.add_argument('directory', type=str, help='Directory with images to\
            convert')
    args = parser.parse_args()

    all_images = []
    for root, dirnames, filenames in os.walk(args.directory):
        for filename in fnmatch.filter(filenames, '*.png'):
            all_images.append(os.path.join(root, filename))

    curr_index = 0
    for name in all_images:
        if curr_index % 100 == 0:
            print ('%d images left' % (len(all_images) - curr_index))
        curr_index += 1
        try:
            img = cv2.imread(name, cv2.IMREAD_UNCHANGED)
        except:
            print 'Could not read:' + name
            continue
        bgr = img[:,:,:3]
        grey = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
        bgr = cv2.cvtColor(grey, cv2.COLOR_GRAY2BGR)
        if img.shape[2] == 4:
            alpha = img[:,:,3]
            result = np.dstack([bgr, alpha])
        else:
            result = bgr
        try:
            cv2.imwrite(name, result)
        except:
            print 'Could not write:' + name

