# Imports:
from shlex import split
from frontend.types import Chunk

def parse(command: str) -> list[Chunk]:
    chunks: list[Chunk] = []
    prev_link: str = '|'
    current_chunk: str = ''

    for symbol in command:
        if symbol in ('|', '?'):
            chunks.append(Chunk(prev_link, *split(current_chunk)))
            prev_link = symbol
            current_chunk = ''
        else:
            current_chunk += symbol
    if current_chunk != '':
        chunks.append(Chunk(prev_link, *split(current_chunk)))
    
    return chunks