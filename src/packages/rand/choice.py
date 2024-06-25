from typing import Sequence, Any
from random import choice, choices

def random_choice(stdin: Sequence[Any], number: str | None = None) -> Any:
    if number is None:
        return choice(stdin)
    return choices(stdin, k=int(number))