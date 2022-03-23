import math

default_radius = 5


def circle_perimetr(rad=default_radius):
    return 2 * rad * math.pi


def circle_area(rad=default_radius):
    return math.pi * rad**2
