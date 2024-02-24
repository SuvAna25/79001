import random


class Man:
    def __init__(self, name, satiety=50, house=True, food=50, money=0):
        self.name = name
        self.satiety = satiety
        self.house = house
        self.food = food
        self.money = money

    def day(self, action):
        if self.satiety < 20 and self.food >= 10:
            self.satiety += 10
            self.food -= 10
            print(f'{self.name} поел')
        elif self.food < 10 and self.money > 0:
            self.food += 20
            self.money -= 10
            print(f'{self.name} сходил в магазин')
        elif action == 1:
            self.satiety -= 10
            self.money += 50
            print(f'{self.name} сходил на работу')
        elif action == 2:
            self.satiety += 10
            self.food -= 10
            print(f'{self.name} поел')
        else:
            self.satiety -= 10
            print(f'{self.name} играет')


class Result:
    def __init__(self, man_1, man_2):
        self.man_1 = man_1
        self.man_2 = man_2

    def life(self):
        if self.man_1.satiety == 0 or self.man_2.satiety == 0:
            return True, print('Один из людей умер')


humen_1 = Man('Артем')
humen_2 = Man('Олег')
result = Result(humen_1, humen_2)
count_day = 0

while True:
    count_day += 1
    if count_day == 365:
        print('Эксперемент удался, все выжили')
        break
    elif result.life():
        break
    else:
        r = random.randint(1, 6)
        humen_1.day(r)
        humen_2.day(r)

print(count_day)






