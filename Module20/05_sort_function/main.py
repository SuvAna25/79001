def tpl_sort(num):
    num = tuple(list(sorted(num)))
    return num


tpl = (6, 3, -1, 8, 4, 10, -5)
print(tpl_sort(tpl))