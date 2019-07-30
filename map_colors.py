from colormath.color_objects import sRGBColor, LabColor
from colormath.color_diff import delta_e_cie2000
from colormath.color_conversions import convert_color 
from matplotlib import pyplot as plt
import fnmatch
import os
import argparse


def rgb_distance(rgb1, rgb2):
    return 2*(rgb1[0]-rgb2[0])**2 + 4*(rgb1[1]-rgb2[1])**2 + 3*(rgb1[2]-rgb2[2])**2


def float_rgb(rgb):
    return [(i + 0.5) / 256.0 for i in rgb]


def dec_rgb(rgb):
    return [int(i * 256) for i in rgb]


def closest_color(rgb, color_dict, use_cie=True):
    dist_dict = {}
    for name, clr in color_dict.items():
        if use_cie:
            dist_dict[name] = ciede_distance(rgb, clr)
        else:
            dist_dict[name] = rgb_distance(rgb, clr)
    return color_dict[min(dist_dict, key=dist_dict.get)]


def ciede_distance(rgb1, rgb2):
    lab1 = convert_color(sRGBColor(rgb1[0], rgb1[1], rgb1[2]), LabColor)
    lab2 = convert_color(sRGBColor(rgb2[0], rgb2[1], rgb2[2]), LabColor)
    return delta_e_cie2000(lab1, lab2)

WAD_OPTIMUM_DEC = {
    'black': [0, 0, 0],
    'blue': [42, 75, 215],
    'brown': [129, 74, 25],
    'cyan': [41, 208, 208],
    'dark_gray': [87, 87, 87],
    'green': [29, 105, 20],
    'light_blue': [157, 175, 255],
    'light_gray': [160, 160, 160],
    'light_green': [129, 197, 122],
    'orange': [255, 146, 51],
    'pink': [255, 205, 243],
    'purple': [129, 38, 192],
    'red': [173, 35, 35],
    'tan': [233, 222, 187],
    'white': [255, 255, 255],
    'yellow': [255, 238, 51],
}

WAD_OPTIMUM = {name:float_rgb(clr) for name, clr in WAD_OPTIMUM_DEC.items()}

AEK_16 = {
        'sapphire': [0.250, 0.195, 0.681],
        'hot_magenta': [0.889, 0.58, 0.759],
        'pale_violet': [0.728, 0.664, 0.998],
        'white': [1.000, 1.000, 1.000],
        'rose_pink': [0.999, 0.582, 0.617],
        'red': [0.907, 0.08, 0.00],
        'wine': [0.478, 0.142, 0.241],
        'black': [0.00, 0.00, 0.00],
        'dark_blue_green': [0.100, 0.336, 0.283],
        'mossy_green': [0.416, 0.539, 0.154],
        'minty_green': [0.89, 0.929, 0.459],
        'topaz': [0.197, 0.756, 0.763],
        'cerulean': [0.22, 0.499, 0.758],
        'mud_brown': [0.433, 0.307, 0.140],
        'dull_orange': [0.787, 0.562, 0.300],
        'piss_yellow': [0.935, 0.890, 0.23],
        }

AEK_16_DEC = {name:dec_rgb(clr) for name, clr in AEK_16.items()}

AEK_32 = {
        'pinkish_tan': [0.840, 0.626, 0.564],
        'orangey_red': [0.996, 0.231, 0.118],
        'rouge': [0.633, 0.175, 0.196],
        'strong_pink': [0.980, 0.185, 0.477],
        'bubblegum_pink': [0.982, 0.624, 0.855],
        'pink/purple': [0.901, 0.111, 0.968],
        'warm_purple': [0.599, 0.186, 0.487],
        'burgundy': [0.279, 0.05, 0.125],
        'navy_blue': [0.23, 0.67, 0.333],
        'blue/purple': [0.312, 0.09, 0.923],
        'medium_blue': [0.177, 0.413, 0.795],
        'azure': [0.03, 0.649, 0.933],
        'robins_egg': [0.435, 0.919, 0.999],
        'blue/green': [0.32, 0.636, 0.605],
        'dark_aqua': [0.167, 0.401, 0.415],
        'dark_forest_green': [0.24, 0.212, 0.100],
        'black': [0.00, 0.00, 0.00],
        'charcoal_grey': [0.290, 0.286, 0.343],
        'greyish_purple': [0.555, 0.483, 0.644],
        'light_periwinkle': [0.717, 0.753, 0.998],
        'white': [1.000, 1.000, 1.000],
        'greenish_grey': [0.674, 0.744, 0.612],
        'medium_grey': [0.509, 0.488, 0.440],
        'brown': [0.352, 0.233, 0.110],
        'umber': [0.682, 0.396, 0.28],
        'yellowish_orange': [0.968, 0.664, 0.190],
        'yellowish': [0.955, 0.915, 0.360],
        'pea_soup': [0.606, 0.584, 0.04],
        'mud_green': [0.339, 0.384, 0.17],
        'kelley_green': [0.70, 0.588, 0.231],
        'toxic_green': [0.317, 0.880, 0.76],
        'bright_teal': [0.35, 0.991, 0.798],
        }

AEK_32_DEC = {name:dec_rgb(clr) for name, clr in AEK_32.items()}

AEK_54 = {
        'bright_teal': [0.21, 0.992, 0.757],
        'green_blue': [0.198, 0.684, 0.531],
        'blue_green': [0.219, 0.447, 0.382],
        'black': [0.00, 0.00, 0.00],
        'charcoal': [0.110, 0.203, 0.167],
        'navy_green': [0.167, 0.323, 0.100],
        'tree_green': [0.177, 0.519, 0.189],
        'green': [0.04, 0.718, 0.86],
        'poison_green': [0.314, 0.992, 0.204],
        'light_grey_green': [0.634, 0.819, 0.558],
        'green_grey': [0.519, 0.574, 0.425],
        'silver': [0.668, 0.730, 0.702],
        'eggshell_blue': [0.804, 1.000, 0.942],
        'aqua_blue': [0.21, 0.861, 0.865],
        'turquoise_blue': [0.287, 0.623, 0.666],
        'sea_blue': [0.187, 0.429, 0.510],
        'azure': [0.223, 0.580, 0.842],
        'lightblue': [0.471, 0.805, 0.971],
        'light_periwinkle': [0.734, 0.774, 0.924],
        'lavender_blue': [0.555, 0.551, 0.989],
        'bright_blue': [0.121, 0.393, 0.955],
        'cobalt': [0.147, 0.279, 0.494],
        'dark_lavender': [0.449, 0.385, 0.623],
        'heather': [0.641, 0.554, 0.708],
        'light_lavendar': [0.961, 0.719, 0.953],
        'light_magenta': [0.874, 0.435, 0.945],
        'electric purple': [0.657, 0.194, 0.933],
        'strong_blue': [0.212, 0.66, 0.887],
        'dark_indigo': [0.142, 0.72, 0.404],
        'darkish_purple': [0.498, 0.139, 0.528],
        'aubergine': [0.278, 0.105, 0.228],
        'berry': [0.575, 0.153, 0.305],
        'mauve': [0.593, 0.407, 0.466],
        'dull_pink': [0.897, 0.494, 0.640],
        'purpley_pink': [0.835, 0.188, 0.615],
        'pink_red': [0.866, 0.219, 0.355],
        'salmon': [0.945, 0.503, 0.443],
        'tomato_red': [0.931, 0.164, 0.69],
        'brownish_red': [0.617, 0.158, 0.123],
        'chocolate_brown': [0.306, 0.130, 0.102],
        'purplish_brown': [0.356, 0.316, 0.348],
        'mud_brown': [0.371, 0.303, 0.159],
        'ugly_brown': [0.494, 0.458, 0.104],
        'puke_green': [0.636, 0.684, 0.135],
        'sickly_yellow': [0.878, 0.960, 0.247],
        'egg_shell': [1.000, 0.982, 0.776],
        'white': [1.000, 1.000, 1.000],
        'pinkish_grey': [0.872, 0.724, 0.728],
        'pale_brown': [0.671, 0.548, 0.462],
        'light_peach': [0.931, 0.754, 0.569],
        'ochre': [0.757, 0.566, 0.162],
        'golden_yellow': [0.972, 0.794, 0.102],
        'orange': [0.917, 0.475, 0.143],
        'earth': [0.630, 0.370, 0.189],
        }

AEK_54_DEC = {name:dec_rgb(clr) for name, clr in AEK_54.items()}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Maps colors in a image to a \
            color from a specific color palette; iterates recursively throuhg a\
            directory of images.')
    parser.add_argument('directory', type=str, help='Directory with images to\
            convert')
    parser.add_argument('palette', type=str, help='Name of the color palette to\
            use (WAD or AEK)')
    parser.add_argument('-n', '--number', type=int, default=16, help='Number of\
            colors to use in the color palette')
    args = parser.parse_args()

    if args.palette == 'WAD':
        color_pal = WAD_OPTIMUM
        if args.number > 16:
            print 'The WAD palette only has 16 colors, defaulting to 16'
    else:
        color_pal = {16:AEK_16, 32:AEK_32, 54:AEK_54}[args.number]

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
        
