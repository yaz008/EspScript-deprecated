from re import findall, sub
from yaml import load, SafeLoader
from sys import path

regex: str = f'{path[0]}\\modules\\string\\patterns.json'
with open(file=regex, mode='r', encoding='UTF-8') as RegexFile:
    lookup: dict[str, str] = load(RegexFile, SafeLoader)

def find(stdin: str, pattern_name: str) -> list[str]:
    pattern: str = lookup[pattern_name]
    return findall(pattern=pattern, string=stdin)

def count(stdin: str, pattern_name: str) -> int:
    pattern: str = lookup[pattern_name]
    return len(findall(pattern=pattern, string=stdin))

def substitute(stdin: str, pattern_name: str, replacement: str) -> str:
    pattern: str = lookup[pattern_name]
    return sub(pattern=pattern, repl=replacement, string=stdin)