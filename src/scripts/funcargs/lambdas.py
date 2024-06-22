from typing import Callable

def add[T](x: T, y: T) -> T:
    return x + y

def mul[T](x: T, y: T) -> T:
    return x * y

def concat(sep: str) -> Callable[[str, str], str]:
    def wrapper(x: str, y: str) -> str:
        return f'{x}{sep}{y}'
    return wrapper