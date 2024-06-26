from sys import path
from typing import Any
from subprocess import run, CompletedProcess
from modules.filemanip import write

def evaluate(stdin: str) -> Any:
    import math
    return eval(stdin, math.__dict__)

def run_code(stdin: str, *args: str) -> str:
    tmp: str = f'{path[0]}\\temp\\tmp.py'
    write(file=tmp, content=stdin)
    result: CompletedProcess = run(f'python {tmp} {' '.join([f'\"{arg}\"' for arg in args])}',
                                   capture_output=True,
                                   text=True)
    return result.stdout if bool(result.stdout) else None