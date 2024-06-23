from typing import Callable

def add[T](x: T, y: T) -> T:
    return x + y

def mul[T](x: T, y: T) -> T:
    return x * y

def load_predicate[T](name: str) -> Callable[[T, T], T]:
    lookup: dict[str, Callable[[T, T], T]] = {
        '+': add,
        '*': mul,
    }
    return lookup[name]