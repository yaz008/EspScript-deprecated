from random import randint, choice, choices, uniform, normalvariate
from typing import Callable

AMINO_ACIDS: list[str] = [
    'Glycine',
    'Alanine',
    'Valine',
    'Leucine',
    'Isoleucine',
    'Threonine',
    'Serine',
    'Methionine',
    'Cystein',
    'Proline',
    'Phenylalanine',
    'Tyrosine',
    'Tryptophane',
    'Histidine',
    'Lysine',
    'Argenine',
    'Aspartate',
    'Glutamate',
    'Asparagine',
    'Glutamine'
]
        
def random_string(letters: str, length: str, samples: str | None = None) -> str:
    if samples:
        return [''.join(choices(letters, k=int(length))) for _ in range(int(samples))]
    return ''.join(choices(letters, k=int(length)))

def random_number(randomizer: Callable, default_range: tuple, *args: str) -> str:
    match len(args):
        case 0:
            return randomizer(*default_range)
        case 1:
            if '-' in args[0]:
                return randomizer(*map(eval, args[0].split(sep='-', maxsplit=1)))
            return [randomizer(*default_range) for _ in range(int(args[0]))]
        case 2:
            return [randomizer(*map(eval,
                                    args[0].split(sep='-', maxsplit=1))) 
                    for _ in range(int(args[1]))]

def rand(*args: str) -> str:
    match args:
        # Numbers:
        case ['int', *args]:
            return random_number(randint, (0, 32767), *args)
        case ['uniform', *args]:
            return random_number(uniform, (0.0, 1.0), *args)
        case ['norm', *args]:
            return random_number(normalvariate, (0.0, 1.0), *args)
        
        # Strings:
        case ['rna', *args]:
            return random_string('AUGC', *args)
        case ['dna', *args]:
            return random_string('ATGC', *args)
        case ['amino', *args]:
            if len(args) == 0:
                return choice(AMINO_ACIDS)
            return choices(AMINO_ACIDS, k=int(args[0]))
        case ['prot' | 'protein', *args]:
            return random_string('ACDEFGHIKLMNPQRSTVWY', *args)