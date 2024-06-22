from re import findall, sub
from yaml import load, SafeLoader
from sys import path

regex: str = f'{path[0]}\\scripts\\string\\regex\\patterns.json'
with open(file=regex, mode='r', encoding='UTF-8') as RegexFile:
    lookup: dict[str, str] = load(RegexFile, SafeLoader)

def find(stdin: str, *args: str) -> list[str]:
    pattern: str = lookup[args[0]]
    return findall(pattern=pattern, string=stdin)

def count(stdin: str, *args: str) -> int:
    pattern: str = lookup[args[0]]
    return len(findall(pattern=pattern, string=stdin))

def substitute(stdin: str, *args: str) -> str:
    pattern: str = lookup[args[0]]
    return sub(pattern=pattern, repl=args[1], string=stdin)