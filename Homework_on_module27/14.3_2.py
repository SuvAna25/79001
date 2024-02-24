import time
from typing import Callable, Any


def timer(func : Callable) -> Callable:
    """"Декоратор выводящий время, которое заняло выполнение декорируемой ф-и"""
    def wrapped_func(*args, **kwargs) -> Any:
        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        run_time = round(ended_at - started_at, 4)
        print(f'Функция работала {run_time} секунд(ы)')
        return result
    return wrapped_func


@timer
def hard_func() -> int:
    return [x ** 2 ** x for x in range(22)]


hard_func()