class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return 'точка: x = {}, y = {}'.format(self.__x, self.__y)

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, x):
        if self.__x:
            self.__x = x
        elif isinstance(self.__x, int):
            raise Exception('Вы ввели x не число')

    def set_y(self, y):
        if self.__y:
            self.__y = y
        elif isinstance(self.__y, int):
            raise Exception('Вы ввели y не число')


point = Point(1, 1)
print(point)
print(point.get_x())
print(point.get_y())

new_x = 7
new_y = 6

point.set_x(new_x)
point.set_y(new_y)
print(point.get_x())
print(point.get_y())


