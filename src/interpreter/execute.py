from win32clipboard import GetClipboardData
from frontend.parse import Chunk
from interpreter.load import load_by_name

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

    return list(result) if isinstance(result, map) else result