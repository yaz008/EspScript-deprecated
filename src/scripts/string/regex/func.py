from re import findall
from yaml import load, SafeLoader
from sys import path

regex: str = f'{path[0]}\\scripts\\string\\regex\\patterns.json'
with open(file=regex, mode='r', encoding='UTF-8') as RegexFile:
    lookup: dict[str, str] = load(RegexFile, SafeLoader)

def find(stdin: str, *args: str) -> list[str]:
    pattern: str = lookup[args[0]]
    return findall(pattern=pattern, string=stdin)