from typing import Any

def echo(stdin: str, *args: str) -> str:
    return ' '.join(args)

def rand(stdin: str, *args: str) -> Any:
    match args:
        case [randomizer, *rest] if randomizer in ('int', 'u', 'norm'):
            from scripts.begin.random.number import random_number
            return random_number(randomizer, *rest)
        case [randomizer, *rest] if randomizer in ('rna', 'dna'):
            from scripts.begin.random.string import random_string
            return random_string(randomizer, *rest)