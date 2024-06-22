from typing import Sequence, Any
from random import choice, choices

def random_choice(stdin: Sequence[Any], *args: str) -> Any:
    return choice(stdin)

def random_choices(stdin: Sequence[Any], *args: str) -> list[Any]:
    return choices(stdin, k=int(args[0]))