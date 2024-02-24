from random import choice


class Parents:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.list_children = []

    def add_children(self, children):
        if self.age - children.children_age > 16:
            self.list_children.append(children)
            print(f'{children.name} добавлен в семью.')
        else:
            print(f'{children.name} ты не ребенок {self.name}.')

    def info_parents(self):
        print(f'{self.name} {self.age} лет')
        for children in self.list_children:
            print(f'{children.name} {children.children_age} лет {children.state_calm}'\ 
                  f'и {children.state_hunger}')

    def calm_down(self):
        for children in self.list_children:
            if 'балуется' in children.state_calm:
                print(f'{children.name} {children.state_calm}, успокоим.')
                children.state_calm = 'спокоен'

    def hunger(self):
        for children in self.list_children:
            if 'голоден' in children.state_hunger:
                print(f'{children.name} {children.state_hunger}, накормим.')
                children.state_hunger = 'сыт'


class Children:
    state_calm = ['балуется', 'спокоен']
    state_hunger = ['голоден', 'сыт']

    def __init__(self, name, children_age):
        self.name = name
        self.children_age = children_age
        self.state_calm = choice(Children.state_calm)
        self.state_hunger = choice(Children.state_hunger)


parents = Parents('Роман Владимирович', 45)
children_1 = Children('Даниил', 25)
children_2 = Children('София', 19)

parents.add_children(children_1)
parents.add_children(children_2)

parents.calm_down()
parents.hunger()
parents.info_parents()