from colormath.color_objects import sRGBColor, LabColor
from colormath.color_diff import delta_e_cie2000
from colormath.color_conversions import convert_color 


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

