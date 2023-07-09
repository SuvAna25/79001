
site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
                },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
                }
            }
        }


def search_elem():
    answer = input('Введиет искомый ключ: ')
    while True:
        question = input('Хотите ввести максимальную глубину? Y/N: ').lower()
        if question == 'y':
            depth = int(input('Введите макстмальную глубину: '))
            break
        if question == 'n':
            depth = None
            break
    value = search_struct(site, answer, depth)
    if value:
        print('Значение ключа: {}'.format(value))
    else:
        print('Значение ключа: None')


def search_struct(struct, i_key, depth, count_depth=0):
    if depth is not None and count_depth >= depth:
        return None
    for key, value in struct.items():
        if key == i_key:
            return value
        if isinstance(value, dict):
            result = search_struct(value, i_key, depth, count_depth + 1)
            if result is not None:
                return result
    return None


search_elem()
