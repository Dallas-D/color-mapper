from utils import float_rgb, dec_rgb

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

