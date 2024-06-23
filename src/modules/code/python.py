from sys import path
from typing import Any
from subprocess import run, CompletedProcess

def write(file: str, content: str) -> None:
    with open(file=file, mode='w', encoding='UTF-8') as TmpFile:
        TmpFile.write(content)

def run_code(stdin: str, *args: str) -> str:
    tmp: str = f'{'\\'.join(path[0].split(sep='\\')[:-1])}\\temp\\tmp.py'
    write(file=tmp, content=stdin)
    result: CompletedProcess = run(f'python {tmp} {' '.join([f'\"{arg}\"' for arg in args])}',
                                   capture_output=True,
                                   text=True)
    write(file=tmp, content='')
    return result.stdout if bool(result.stdout) else None

def evaluate(stdin: str) -> Any:
    import math
    return eval(stdin, math.__dict__)