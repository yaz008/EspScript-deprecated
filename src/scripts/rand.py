from random import randint, choice, choices

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
        
def randon_string(letters: str, length: str, samples: str | None = None) -> str:
    if samples:
        return [''.join(choices(letters, k=length)) for _ in range(int(samples))]
    return ''.join(choices(letters, k=int(length)))

def random_int(*args: str) -> str:
    match len(args):
        case 0:
            return randint(0, 32767)
        case 1:
            if '-' in args[0]:
                return randint(*map(int, args[0].split(sep='-')))
            return [randint(0, 32767) for _ in range(int(args[0]))]
        case 2:
            return [randint(*map(int, args[0].split(sep='-'))) for _ in range(int(args[1]))]

def rand(*args: str) -> str:
    match args:
        # Integers:
        case ['int', *args]:
            return random_int(*args)
        
        # Strings:
        case ['rna', *args]:
            return randon_string('AUGC', *args)
        case ['dna', *args]:
            return randon_string('ATGC', *args)
        case ['amino', *args]:
            if len(args) == 0:
                return choice(AMINO_ACIDS)
            return choices(AMINO_ACIDS, k=int(args[0]))
        case ['prot', 'protein', *args]:
            return randon_string('ACDEFGHIKLMNPQRSTVWY', *args)