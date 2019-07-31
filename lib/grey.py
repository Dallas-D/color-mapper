
GREY = {'black': [0.0, 0.0, 0.0], 'white': [1.0, 1.0, 1.0]}


def extend_grey_palette(n):
    inc = 1.0 / (n - 1)
    for i in range(1, n-1):
        val = i * inc
        GREY[str(i)] = [val, val, val]

