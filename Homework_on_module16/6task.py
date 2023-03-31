#Напишите программу, которая генерирует случайные значения
# в первых двух списках в заданных диапазонах, а также генерирует список,
# состоящий из фраз «Погиб» или «Выжил». Выведите все списки на экран.

import random

monsters_1 = [random.randint(50, 80) for _ in range(10)]
monsters_2 = [random.randint(30, 60) for _ in range(10)]
monsters_3 = [('Погиб' if monsters_1[i] + monsters_2[i] > 100
               else 'Выжил') for i in range(10)]
print('Урон первого отряда:', monsters_1)
print('Урон второго отряда: ', monsters_2)
print('Состояние третьего отряда:', monsters_3)
