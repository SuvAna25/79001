def histogram(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    return sym_dict


text = input('Введите текст:').lower()
original = histogram(text)
print('Оригинальный словарь частот:')

for i in sorted(original.keys()):
    print(i, ':', original[i])
inverted = {}
print('Инвертированный словарь частот:,')

for k, v, in original.items():
    inverted.setdefault(v, []).append(k)
for i in inverted.keys():
    print(i, ':', inverted[i])
