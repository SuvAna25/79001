array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

new_array_1 = {1, 5, 10, 20, 40, 80, 100}
new_array_2 = {6, 7, 20, 80, 100}
new_array_3 = {3, 4, 15, 20, 30, 70, 80, 120}

print('Задача 1:')
array_4 = []
for i in array_1:
    if i in (array_2 and array_3):
        array_4.append(i)
print('Решение без множеств:', ', '.join(map(str, array_4)))

new_array_4 = set(new_array_1 & new_array_2 & new_array_3)
print('Решение с множествами:', ', '.join(map(str, new_array_4)))
print('Задача 2:')

new = []
for i in array_1:
    if i not in (array_2 or array_3):
        new.append(i)
print('Решение без множеств:', ', '.join(map(str, new)))

new_1 = set(new_array_1 - (new_array_2 or new_array_3))
print('Решение с множествами:', ', '.join(map(str, new_1)))

