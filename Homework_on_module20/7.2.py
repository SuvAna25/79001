import math

radius = int(input('Введите радиус:'))
height = int(input('Введите высоту:'))
def cylinder(rad, hei):
    side = 2 * math.pi * rad * hei
    full = side + 2 * math.pi * rad ** 2
    return side, full

side_area, full_area = cylinder(radius, height)

print(side_area, full_area)