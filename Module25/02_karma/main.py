from random import randint, choice


class Exception:
    def __str__(self):
        return f'Ошибка {self.__class__.__name__}'


class KillError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


def one_day(list_error):
    num_choice = randint(1, 10)
    if num_choice == 6:
        return choice(list_error)
    return randint(1, 7)


def main():
    errors = [KillError(), DrunkError(), CarCrashError(), GluttonyError(), DepressionError()]
    karma = 500
    total_karma = 0
    day = 0

    while True:
        day += 1
        try:
            result = one_day(errors)
            if isinstance(result, int):
                total_karma += result
                if total_karma < karma:
                    print(f'Прошел {day} день:'
                          f'\nдостигнуто {total_karma} очков кармы.')
                else:
                    total_karma = karma
                    print(f'Просветление наступило на {day} день, получено {total_karma} очков кармы.')
                    break
            else:
                raise TypeError(result)
        except TypeError as exc:
            print(f'Прошел {day} день: '
                  f'\n{exc}')
            with open('karma.log', 'a', encoding='utf-8') as log_file:
                log_file.write(f'{day} день: {exc}\n')


main()
