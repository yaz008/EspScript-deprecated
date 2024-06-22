# Imports:
from shlex import split
from dataclasses import dataclass, field
from constants import LINKS

@dataclass(slots=True)
class Chunk:
    name: str
    args: tuple[str] = field(default_factory=tuple[str])

    def __init__(self, name: str, *args: str) -> None:
        self.name = name
        self.args = args

def divide(command: str) -> list[Chunk]:
    chunks: list[Chunk] = []
    current_chunk: str = ''

    for symbol in command:
        if symbol in LINKS:
            chunks.append(Chunk(*split(current_chunk)))
            chunks.append(Chunk(name=symbol))
            current_chunk = ''
        else:
            current_chunk += symbol
    if current_chunk != '':
        chunks.append(Chunk(*split(current_chunk)))
    
    return chunks