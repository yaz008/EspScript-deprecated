from typing import Iterable, Any
from random import choice, choices

def random_choice(stdin: Iterable[Any], *args: str) -> Any:
    return choice(stdin)

def random_choices(stdin: Iterable[Any], *args: str) -> list[Any]:
    return choices(stdin, k=int(args[0]))