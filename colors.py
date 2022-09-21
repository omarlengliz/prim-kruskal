from random import randint
def color(n):
    colors = []

    for i in range(n):
        colors.append('#%06X' % randint(0, 0xFFFFFF))
    return colors
