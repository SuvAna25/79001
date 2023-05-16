import random
num = tuple([random.randint(0, 5) for _ in range(10)])
num_2 = tuple([random.randint(-5, 0) for _ in range(10)])
num_3 = num + num_2
print(num_3, f'Кол-во нулей: {num_3.count(0)}', sep='\n')