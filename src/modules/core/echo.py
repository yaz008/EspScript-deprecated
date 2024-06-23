from typing import Any

def echo(stdin: Any, *args: str) -> str:
    return ' '.join(args)