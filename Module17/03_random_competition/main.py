import random

first_team = [round(random.uniform(5, 10), 2) for i in range(20)]
second_team = [round(random.uniform(5, 10), 2) for j in range(20)]
winners = [(first_team[i] if first_team[i] > second_team[i] else second_team[i]) for i in range(len(first_team))]

print('Первая команда:', first_team, '\n', 'Вторая команда:', second_team)
print('Победители тура:', winners)
