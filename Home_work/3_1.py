main = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
first_company = [0, 0, 0]
second_company = [1, 0, 0, 1, 1]
third_company = [1, 1, 1, 0, 1]

for i in first_company, second_company, third_company:
    main.extend(i)

print('Общий список задач:', main)
print('Кол-во невыполненных задач:', main.count(0))

