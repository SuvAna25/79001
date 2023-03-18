import math
def found_money(x, y):
    distance = math.sqrt(x ** 2 + y ** 2)
    return distance

coord_x = float(input('Введите координату икс :'))
coord_y = float(input('Введите коорпдинату игрек :'))
radius = float(input('Введите радиус :'))
money = found_money(coord_x, coord_y)
if money <= radius:
    print('Монетка где-то рядом')
else:
    print('Монетки в области нет')

