left = int(input('Левая граница:'))
right = int(input('Правая граница:'))

cube = [i ** 3 for i in range(left, right + 1)]
square = [j ** 2 for j in range(left, right + 1)]

print('Список кубов чисел в диапазоне от', left, 'до', right, ':', cube)
print('Список квадратов чисел в диапазоне от', left, 'до', right, ':', square)