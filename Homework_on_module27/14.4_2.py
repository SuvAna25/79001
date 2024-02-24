from typing import Callable, Dict


PLUGINS: Dict[str, Callable] = dict()


def register(func: Callable) -> Callable:
    """"Декоратор . Регистрирует ф-ии как плагин"""
    PLUGINS[func.__name__] = func
    return func


@register
def say_hello(name: str) -> str:
    return "Hello!"


print(PLUGINS)
