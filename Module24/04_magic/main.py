class Water:
    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Gale()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        elif isinstance(other, Cold):
            return Hail()
        else:
            None


class Air:
    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        else:
            None


class Fire:
    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()
        else:
            None


class Earth:
    def __str__(self):
        return 'Земля'


class Cold:
    def __str__(self):
        return 'Холод'


class Gale:
    def __str__(self):
        return 'Шторм'


class Steam:
    def __str__(self):
        return 'Пар'


class Dirt:
    def __str__(self):
        return 'Грязь'


class Lightning:
    def __str__(self):
        return 'Молния'


class Dust:
    def __str__(self):
        return 'Пыль'


class Lava:
    def __str__(self):
        return 'Лава'


class Hail:
    def __str__(self):
        return 'Град'


water = Water()
air = Air()
earth = Earth()
fire = Fire()
cold = Cold()
print(f'Вода + Воздух = {water + air}')
print(f'Вода + Огонь = {water + fire}')
print(f'Вода + Земля = {water + earth}')
print(f'Вода + Холод = {water + cold}')
print(f'Воздух + Огонь = {air + fire}')
print(f'Воздух + Земля = {air + earth}')
print(f'Огонь + Земля = {fire + earth}')


