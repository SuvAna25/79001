import os
from contextlib import contextmanager

@contextmanager
def in_dir(path):
    cur_path = os.getcwd()
    os.chdir(path)
    try:
        yield
    except FileNotFoundError:
        print("Такого пути не существует")
    finally:
        os.chdir(cur_path)


with in_dir('C:\\'):
    print(os.listdir())
