import time
from typing import Callable, Any


def timer(func : Callable) -> Any:
    start = time.time()
    func()
    ended = time.time()
    run_timer = round(ended - start, 4)
    return run_timer


def hard_func() -> int:
    return [x ** 2 ** x for x in range(22)]


print('Функция работает {} секунд(ы)'.format(timer(hard_func)))