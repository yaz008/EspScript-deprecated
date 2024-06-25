from json import load
from sys import path

regex: str = f'{path[0]}\\modules\\regex\\patterns.json'
with open(file=regex, mode='r', encoding='UTF-8') as RegexFile:
    patterns: dict[str, str] = load(RegexFile)