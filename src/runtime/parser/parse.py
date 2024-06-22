# Imports:
from shlex import split
from parser.types import Chunk

def parse(command: str) -> list[Chunk]:
    chunks: list[Chunk] = []
    prev_link: str = '|'
    current_chunk: str = ''
    in_quotes: bool = False

    for symbol in command:
        if symbol in ('|', '?') and not in_quotes:
            chunks.append(Chunk(prev_link, *split(current_chunk)))
            prev_link = symbol
            current_chunk = ''
        else:
            current_chunk += symbol
            if symbol == '\'':
                in_quotes = not in_quotes
    if current_chunk != '':
        chunks.append(Chunk(prev_link, *split(current_chunk)))
    
    return chunks