# Imports:
from shlex import split
from dataclasses import dataclass, field
from constants import LINKS

@dataclass(slots=True)
class Chunk:
    link: str
    name: str
    args: tuple[str] = field(default_factory=tuple[str])

    def __init__(self, link: str, name: str, *args: str) -> None:
        self.link = link
        self.name = name
        self.args = args

def divide(command: str) -> list[Chunk]:
    chunks: list[Chunk] = []
    prev_link: str = '|'
    current_chunk: str = ''

    for symbol in command:
        if symbol in LINKS:
            chunks.append(Chunk(prev_link, *split(current_chunk)))
            prev_link = symbol
            current_chunk = ''
        else:
            current_chunk += symbol
    if current_chunk != '':
        chunks.append(Chunk(prev_link, *split(current_chunk)))
    
    return chunks

print(divide(command='f a?len|avg'))