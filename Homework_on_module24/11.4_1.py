class Toyota:
    def __init__(self, color = 'red', price = 1e6, max_speed = 200, current_speed = 0):
        self.color = color
        self.price = price
        self.max_speed = max_speed
        self.current_speed = current_speed

    def info(self):
        print('Color car: {}\nSpeed: {}\nMax_speed: {}\nCurrent_speed: {}\n'.format(
            self.color, self.price, self.max_speed, self.current_speed))

    def change_speed(self, new_speed):
        self.current_speed = new_speed


car = Toyota()
car.info()
car.change_speed(100)
car.info()

