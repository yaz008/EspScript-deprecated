from win32clipboard import GetClipboardData
from functools import reduce
from runtime.parser.parse import Chunk
from runtime.interpreter.load import load_by_name

from typing import Callable, Any

def execute(chunks: list[Chunk]) -> None:
    result: Any = GetClipboardData()

    for chunk in chunks:
        func: Callable[..., Any] = load_by_name(name=chunk.name)
        match chunk.link:
            case '|':
                result = func(result, *chunk.args)
            case '?':
                result = list(map(func, result))
            case '&':
                result = reduce(func, result)

    return list(result) if isinstance(result, map) else result