import copy


def find_key(struct, key, name):
    if key in struct:
        struct[key] == name
    for substruct in struct.values():
        if isinstance(substruct, dict):
            result = find_key(substruct, key, name)
            if result:
                return struct


clients = []
count_site = int(input('Сколько сайтов: '))
for _ in range(count_site):
    product = input('\nВведите название для нового сайта: ')

    site = {
        'html': {
            'head': {
            'title': f'Куплю/продам {product} недорого'
            },
            'body': {
            'h2': f'У нас самая низкая цена на {product}',
            'div': 'Купить',
            'p': 'Продать'
            }
        }
    }

    for info in site:
        find_key(site, info, site[info])
    clients.append((f'\nСайт для {product}:',
                    f'{copy.deepcopy(site)}'))
    for client in clients:
        print('\n'.join(client))
