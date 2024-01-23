import random

numbers = int(input('Введите кол-во чисел: '))
num = [random.randint(-10, 10) for _ in range(numbers)]

buffer_iter = iter(num)

while True:
    try:
        print(next(buffer_iter))
    except StopIteration:
        print('End')
        break