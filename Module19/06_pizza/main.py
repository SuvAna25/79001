def fun(dct, key, arg):
    dct[key] = dct.setdefault(key, 0) + int(arg)
    return dct


order = dict()
for i in range(int(input('Введите кол-во заказов через пробел(фамилия, пицца, кол-во):'))):
    name, pizza, count = input(f'{i + 1} заказ: ').rsplit(maxsplit=3)
    order[name] = fun(order.get(name, {}), pizza, count)

for name in sorted(order):
    print(f'{name}:')
    for pizza, count in sorted(order.get(name).items()):
        print(f'{pizza}: {count}')
    print()
