class Robots:
    def __init__(self, model):
        self.model = model

    def __str__(self):
        return '{} model {}'.format(self.__class__.__name__, self.model)

    def operate(self):
        print('Робот ездит по кругу')


class WarRobot(Robots):

    def __init__(self, gun, model):
        super().__init__(model)
        self.gun = gun

    def operate(self):
        print(f'{self.model} охраняет военный объкт при помощи {self.gun}')


class VacuumRobot(Robots):

    def __init__(self, model):
        super().__init__(model)
        self.bag = 0

    def operate(self):
        print(f'{self.model} пылесосит пол')


class SubmarineRobot(WarRobot):
    def __init__(self, gun, model, depth):
        super().__init__(gun, model)
        self.depth = depth

    def operate(self):
        super().operate()
        print(f'Охрана ведется под водой на глубине {self.depth}')


warrobot = WarRobot('пушки', 'Военный робот')
warrobot.operate()

vacuum = VacuumRobot('Робот-пылесос')
vacuum.operate()

submarine = SubmarineRobot('торпед', 'Подводная лодка', '100 метров')
submarine.operate()
