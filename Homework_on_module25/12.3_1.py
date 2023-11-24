class Ship:
    def __init__(self, model='корабль'):
        self.model = model

    def __str__(self):
        return self.model

    def to_go(self):
        print(f'{self.model} идет по воде!')


class Warship(Ship):
    def __init__(self, weapons, model='военный корабль!'):
        super().__init__(model)
        self.weapons = weapons

    def attack(self):
        print(f'{self} корабль атакует!')


class Carship(Ship):
    def __init__(self, model='грузовой корабль!'):
        super().__init__(model)
        self.fullness = 0

    def loading(self):
        self.fullness += 1

    def unloading(self):
        self.fullness -= 1


cargoship = Carship('ship2')
warship = Warship('ship1', 'пушки')

warship.attack()
cargoship.loading()