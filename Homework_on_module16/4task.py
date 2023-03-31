num_1 = int(input('Введите число:'))
num_2 = int(input('Введите число:'))
number = [i for i in range(num_1, num_2) if i % 2 == 0]
print(number)