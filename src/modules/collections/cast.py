from typing import Iterable, Any

def cast_to_list(stdin: Iterable[Any]) -> list[Any]:
    return list(stdin)

def cast_to_set(stdin: Iterable[Any]) -> set[Any]:
    return set(stdin)