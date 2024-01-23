class CanFly:

    height = 0
    speed = 0

    def take_off(self):
        pass

    def fly(self):
        pass

    def get_land_on(self):
        self.height = 0
        self.speed = 0

    def __str__(self):
        return '{}, высота:{} скорость:{}'.format(
            self.__class__.__name__, self.height, self.speed,
        )


class ButterFly(CanFly):

    def take_off(self):
        self.height = 1

    def fly(self):
        self.speed = 0.5


class Rocket(CanFly):

    def take_off(self):
        self.height = 500
        self.speed = 1000

    def get_land_on(self):
        self.height = 0
        print('Взрыв!!!!')


but = ButterFly()
but.get_land_on()



