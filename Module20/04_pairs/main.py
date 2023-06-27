import random

new_manuscript = []
manuscript = [random.randint(0, 10) for _ in range(10)]
zip_list = zip(manuscript[::2], manuscript[1::2])
for index in zip_list:
    new_manuscript.append(index)
print('Оригинальный список: ', manuscript)
print('Новый список: ', new_manuscript)

# второе решение задачи

original_list = [random.randint(0, 10) for _ in range(10)]
new_list = list(zip(original_list[::2], original_list[1::2]))
print('Оригинальный список: ', original_list)
print('Новый список: ', new_list)

# третье решение задачи

list_original = [random.randint(0, 10) for _ in range(10)]
print('Оригинальный список: ', list_original)
print('Новый список: ', [*map(tuple, zip(list_original[::2], list_original[1::2]))])