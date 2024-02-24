from typing import Callable, Any


def ingredients(func : Callable) -> Callable:
    """"Декоратор. Выводящий ингредиенты"""
    def wrapped_func(*args, **kwargs) -> Any:
        print("#помидоры#")
        func(*args, **kwargs)
        print("~салат~")
    return wrapped_func


def buns(func : Callable) -> Callable:
    """"Декоратор, выводящий хлеб"""
    def wrapped_func(*args, **kwargs) -> Any:
        print("</------\>")
        func(*args, **kwargs)
        print("<\____/>")
    return wrapped_func


@buns
@ingredients
def sandwich(filler):
    print(filler)


sandwich("-ветчина-")

