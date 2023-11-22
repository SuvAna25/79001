class Man:
    count = 0

    def __init__(self, name, age):
        self.__name = ''
        self.__age = 0
        self.set_name(name)
        self.set_age(age)
        Man.count += 1

    def set_age(self, value):
        if isinstance(value, (int, float)) and 0 <= value <= 100:
            self.__age = value
        else:
            raise ValueError('Ошибка в возрасте')

    def set_name(self, value):
        if isinstance(value, str) and value.isalpha():
            self.__name = value
        else:
            raise ValueError('Ошибка в имени')

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


man = Man('Tom', 100)
print(man.count)
print(man.get_age())

man.Man__age = 99
print(man.count)
print(man.Man__age)
