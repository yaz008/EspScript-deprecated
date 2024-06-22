from typing import Iterable, Any

def cast_to_list(stdin: Iterable[Any], *args: str) -> list[Any]:
    return list(stdin)

def cast_to_set(stdin: Iterable[Any], *args: str) -> list[Any]:
    return set(stdin)