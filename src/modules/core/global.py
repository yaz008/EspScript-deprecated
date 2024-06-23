from typing import Iterable, Sized

def length(stdin: Sized) -> int:
    return len(stdin)

def minimum[T](stdin: Iterable[T]) -> T:
    return min(stdin)

def maximum[T](stdin: Iterable[T]) -> T:
    return max(stdin)