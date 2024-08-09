from abc import ABC, abstractmethod


class Music:
    def play_music(self):
        print("song")


class Transport(ABC):
    def __init__(self, color, speed):
        self._color = color
        self._speed = speed

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value

    @abstractmethod
    def ride_on_earth(self):
        pass

    @abstractmethod
    def ride_on_water(self):
        pass


class Car(Transport):
    def ride_on_earth(self):
        print("Едем по земле!")


class Boat(Transport):
    def ride_on_water(self):
        print("Плывем по воде!")


class Amphibian(Car, Boat, Music):
    pass


amph_transport = Amphibian("blue", 123)
amph_transport.ride_on_earth()
amph_transport.ride_on_water()
amph_transport.play_music()
print(amph_transport.color)
amph_transport.color = "white"
print(amph_transport.color)
