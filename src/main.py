from sys import argv
from win32clipboard import OpenClipboard
from frontend import Chunk, parse
from interpreter import execute

OpenClipboard()
chunks: list[Chunk] = parse(argv[1])
print(execute(chunks))