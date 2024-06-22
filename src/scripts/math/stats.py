from functools import reduce
from typing import Any

def average(stdin: list[Any], *args: str) -> Any:
    return reduce(lambda x, y: x + y, stdin) / len(stdin)