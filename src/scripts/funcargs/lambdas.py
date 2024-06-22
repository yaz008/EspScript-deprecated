from typing import Callable

def add[T](*args: str) -> Callable[[T, T], T]:
    return lambda x, y: x + y

def mul[T](*args: str) -> Callable[[T, T], T]:
    return lambda x, y: x * y

def concat(sep: str = '') -> Callable[[str, str], str]:
    def wrapper(x: str, y: str) -> str:
        return f'{x}{sep}{y}'
    return wrapper