from re import sub
from modules.regex import patterns

def substitute(stdin: str, pattern_name: str, replacement: str) -> str:
    pattern: str = patterns[pattern_name]
    return sub(pattern=pattern, repl=replacement, string=stdin)