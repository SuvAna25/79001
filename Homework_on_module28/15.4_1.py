from abc import ABC, abstractmethod


class Music:
    def play_music(self):
        print("song")


class Transport(ABC):
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


amph_transport = Amphibian()
amph_transport.ride_on_earth()
amph_transport.ride_on_water()
amph_transport.play_music()
