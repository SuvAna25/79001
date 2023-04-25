# Напишите программу, которая получает сам текст и считает,
# сколько раз в строке встречается каждый символ. На экран нужно
# вывести содержимое в виде таблицы, отсортированное по алфавиту,
# а также максимальное значение частоты.

def histogram(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    return sym_dict


text = input('Введите текст: ')
hist = histogram(text)

for i in sorted(hist.keys()):
    print(i, ':', hist[i])

print('Максимальная частота:', max(hist.values()))