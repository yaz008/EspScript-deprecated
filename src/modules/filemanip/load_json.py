from json import load
from sys import path
from typing import Any

def load_json(relative_path: str) -> Any:
    file_path: str = f'{path[0]}\\{relative_path}'
    with open(file=file_path, mode='r', encoding='UTF-8') as RegexFile:
        return load(RegexFile)