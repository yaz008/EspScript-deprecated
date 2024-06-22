from sys import argv
from win32clipboard import OpenClipboard
from runtime.parser import Chunk, parse
from runtime.interpreter import execute

OpenClipboard()
chunks: list[Chunk] = parse(argv[1])
try:
    result: str = str(execute(chunks))
    print(result)
except Exception:
    print('<Error>')