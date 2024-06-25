from re import findall
from modules.regex import patterns

def find(stdin: str, pattern_name: str) -> list[str]:
    pattern: str = patterns[pattern_name]
    return findall(pattern=pattern, string=stdin)