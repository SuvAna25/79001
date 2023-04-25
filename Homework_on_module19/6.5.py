incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}
count = sum(incomes.values())
min_count = min(incomes.values())
name_min = min(incomes, key=incomes.get)
incomes.pop(name_min)

print('Общий доход за год составил', count, 'рублей\n')
print('Самый маленький доход у', name_min, '. Он составляет', min_count, 'рублей\n')
print('Итоговый словарь:', incomes)
