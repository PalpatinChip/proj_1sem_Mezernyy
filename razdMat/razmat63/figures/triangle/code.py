import math

_a, _b, _c = 7, 2, 8


def triangle_perimetr(aa=_a, bb=_b, cc=_c):
    return aa + bb + cc


def triangle_area(aa=a, bb=_b, cc=_c):
    p = (aa + bb + cc)/2
    return math.sqrt(p*float(p-aa)*float(p-bb)*float(p-cc))
