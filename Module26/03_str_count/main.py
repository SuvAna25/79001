import os
from collections.abc import Iterator


def count_line(file: str) -> (int, int):
    cnt = 0
    with open(file, 'r', encoding='utf8') as r_file:
        for total, line in enumerate(r_file):
            if not line.lstrip().startswith('#') and len(line.split()) != 0:
                cnt += 1
        return total + 1, cnt


def num_files(path: str) -> Iterator:
    print(f'\nПоиск питоновских файлов в директории: \n{path}')
    for root, dirs, files in os.walk(path):
        for i_file in files:
            if i_file.endswith('.py'):
                print(f'Файл: {i_file}')
                yield count_line(os.path.join(root, i_file))


def main():
    user_path = os.path.abspath(os.path.join('..', ))

    try:
        if os.path.exists(user_path):
            for i_path in num_files(user_path):
                total_l, cnt_l = i_path
                print(f'Общее количество строк в файле {total_l}, '
                      f'из них на {cnt_l} написан код')

        else:
            raise FileNotFoundError('Нет такой директории')
    except FileNotFoundError as exc:
        print(exc)


main()