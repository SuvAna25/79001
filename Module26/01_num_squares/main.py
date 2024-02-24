#класс-итератор
class MyGen:
    def __init__(self, number):
        self.count = 0
        self.number = number

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count == self.number:
            raise StopIteration
        else:
            return self.count ** 2


user = int(input('Введите число: '))
my_gen = MyGen(user)

for i_elem in my_gen:
    print(i_elem)


# функция-генератор
def gen_num(num):
    for n in range(1, num):
       yield n ** 2


input_num = int(input('Введите число: '))
gen = gen_num(input_num)
for elem in gen:
    print(elem, end=', ')

#генераторное выражение
user = int(input('\nВведите число: '))
gen = (j_elem ** 2 for j_elem in range(1, user))
for i in gen:
    print(i, end=', ')