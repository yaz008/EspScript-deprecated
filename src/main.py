from sys import argv, path
from win32clipboard import OpenClipboard
from runtime.parser import Chunk, parse
from runtime.interpreter import execute

OpenClipboard()
try:
    chunks: list[Chunk] = parse(argv[1])
    result: str = str(execute(chunks))
    print(result)
except Exception as exeption:
    from datetime import datetime
    error_log: str = f'{'\\'.join(path[0].split(sep='\\')[:-1])}\\logs\\errors.log'
    with open(file=error_log, mode='a', encoding='UTF-8') as ErrorLog:
        ErrorLog.write(f'Error at {datetime.now()}:\n{exeption}\n\n')
    print('<Error>')