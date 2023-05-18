def element(data):
    result = []
    if isinstance(data, dict):
        data = data.values()
    for index, value in enumerate(data):
        if index % 2 == 0:
            result.append(value)
    return result


print(element('О Дивный Новый мир!'))
print(element([100, 200, 300, 'буква', 0, 2, 'а']))