from random import randint, uniform, normalvariate
from typing import Callable, Any

def rand_num(randomizer: Callable[..., Any],
             default_range: tuple[Any, Any],
             *args: str) -> Any:
    if len(args) == 0:
        return randomizer(*default_range)
    if len(args) == 1:
        if ':' in args[0]:
            return randomizer(*map(eval, args[0].split(sep=':', maxsplit=1)))
        return [randomizer(*default_range) for _ in range(int(args[0]))]
    return [randomizer(*map(eval,args[0].split(sep=':', maxsplit=1)))
                            for _ in range(int(args[1]))]

def random_number(randomizer: str, *args: str) -> Any:
    match randomizer:
        case 'int':
            return rand_num(randint, (0, 32767), *args)
        case 'u':
            return rand_num(uniform, (0.0, 1.0), *args)
        case 'norm':
            return rand_num(normalvariate, (0.0, 1.0), *args)