nums_list = []

N = int(input('Кол-во чисел в списке: '))

for _ in range(N):
    num = int(input('Очередное число: '))
    nums_list.append(num)

min_number = min(nums_list)
max_number = max(nums_list)
print('Максимальное число в списке:', max_number)
print('Минимальное число в списке:', min_number)