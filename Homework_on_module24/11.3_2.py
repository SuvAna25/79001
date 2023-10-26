class Family:
    surname = 'Common family'
    money = 100000
    have_a_house = False

    def family_info(self):
        print(
            'Family name: {}\nFamily funds: {}\nHaving a house: {}\n'.format(
                self.surname, self.money, self.have_a_house
            )
        )

    def earn_money(self, amount):
        self.money += amount
        print('Earned {} money! Current value: {}'.format(amount, self.money))


    def by_house(self, house_price, discount=0):
        house_price * discount / 100
        if self.money >= house_price:
            self.money -= house_price
            self.have_a_house = True
            print('House purchased! Current money: {}\n'.format(self.money))
        else:
            print('Not enough money!\n')


my_family = Family()
my_family.family_info()

print('Try to buy a house')
my_family.by_house(10 ** 6)

if not my_family.have_a_house:
    my_family.earn_money(900000)
    print('Try to buy a house again')
    my_family.by_house(10 ** 6, 10)

my_family.family_info()