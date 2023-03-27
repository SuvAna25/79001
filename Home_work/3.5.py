num_part = int(input('Кол-во участников: '))
num_people = int(input('Кол-во человек в команде:'))

people_lits = []
num = 1
if num_part % num_people == 0:
    for _ in range(num_part // num_people):
        people_lits.append(list(range(num, num + num_people)))
        num += num_people
    print(people_lits)
else:
    print(num_part, 'невозможно поделить на команды по', num_people, 'человек')