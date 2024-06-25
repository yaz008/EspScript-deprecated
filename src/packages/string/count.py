from re import findall
from modules.regex import patterns

def count(stdin: str, pattern_name: str) -> int:
    pattern: str = patterns[pattern_name]
    return len(findall(pattern=pattern, string=stdin))