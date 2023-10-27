class Point:
    count = 0

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        Point.count += 1

    def info(self):
        print('X: {}\nY: {}\n'.format(
            self.x, self.y)
        )


point = Point()
point.info()
point = Point(5, 6)
point.info()
