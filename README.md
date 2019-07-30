# color-mapper
Maps colors for a directory of images to a different color palette. Only intended for pngs. It will keep any transparencies, and just update the color

*Requires:* Python 2.7, matplotlib, colormath

*Note:* This will take a long time to run as it uses CIEDE2000 for calculating distances between colors. This provides a better measure of which colors to choose as it's based on perceived differences as opposed to euclidean distance.

## Usage
    >>> python map_colors.py directory palette [-n/--number no_of_colors]
- directory = directory containing the images (as .pngs)
- palette = type of palette to use (currently available: WAD or AEK)
- number (opt) = number of colors to use in the palette (currently available: 16, 32, or 54)

## Credits
The palettes used here came from these website:
- Wad's Optimum 16 Colors: http://alumni.media.mit.edu/~wad/color/palette.html
- AEK palettes are by Andrew Kensler
  - aek-16 and aek-32: http://eastfarthing.com/blog/2016-05-06-palette/
  - aek-54: http://eastfarthing.com/blog/2016-09-19-palette/
