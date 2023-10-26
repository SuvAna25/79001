class Toyota:
    color = 'red'
    price = '1e6'
    max_speed = '200'
    current_speed = 0

    def info(self):
        print(
            'Color a car: {}\nPrice: {}\nMax speed: {}\nCurrent speed: {}\n'.format(
                self.color, self.price, self.max_speed, self.current_speed)
            )

    def speed(self, new_speed):
        self.current_speed = new_speed


car = Toyota()
car.info()
car.speed(100)
car.info()
print(Toyota.current_speed)