from abc import ABC, abstractmethod


class Figure(ABC):

    def __init__(self, pos_x: int, pos_y: int, length: int, width: int) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.length = length
        self.width = width

    def move(self, pos_x: int, pos_y: int) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y

    def resize(self, length: int, width: int) -> None:
        pass


class Rectangle(Figure):
    def resize(self, length: int, width: int) -> None:
        self.length = length
        self.width = width


class Square(Figure):

    def __init__(self, pos_x: int, pos_y: int, size: int) -> None:
        super().__init__(pos_x, pos_y, size, size)

    def resize(self, length: int, width: int) -> None:
        if width == length:
            self.length = length
            self.width = width
        else:
            print("У квадрата стороны равны!")


rect1 = Rectangle(pos_x=10, pos_y=20, length=5, width=6)
rect2 = Rectangle(pos_x=30, pos_y=40, length=10, width=11)
square1 = Square(pos_x=50, pos_y=70, size=7)




