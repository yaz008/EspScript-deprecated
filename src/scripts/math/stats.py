from functools import reduce
from typing import Any

def average(stdin: list[Any], *args: str) -> Any:
    if len(stdin) == 0:
        return 0
    return reduce(lambda x, y: x + y, stdin) / len(stdin)