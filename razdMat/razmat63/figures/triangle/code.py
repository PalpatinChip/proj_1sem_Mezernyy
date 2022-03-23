import math

a, b, c = 7, 2, 8


def triangle_perimetr(aa=a, bb=b, cc=c):
    return aa + bb + cc


def triangle_area(aa=a, bb=b, cc=c):
    p = (aa + bb + cc)/2
    return math.sqrt(p*float(p-aa)*float(p-bb)*float(p-cc))
