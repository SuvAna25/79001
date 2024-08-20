from contextlib import contextmanager
from collections.abc import Iterator
import time


@contextmanager
def timer() -> Iterator:
    start = time.time()
    try:
        yield
    finally:
        print(time.time() - start)


with timer():
    val = 100 * 100 ** 100000

