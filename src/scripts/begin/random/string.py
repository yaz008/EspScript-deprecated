from random import choices, randint

def generate_string(collection: str, *args: str) -> str:
    if len(args) == 2:
        if ':' in args[0]:
            return [''.join(choices(collection,
                                    k=randint(*map(eval, args[0].split(sep=':')))))
                                    for _ in range(int(args[1]))]
        return [''.join(choices(collection, k=int(args[0])))
                for _ in range(int(args[1]))]
    return ''.join(choices(collection, k=int(args[0])))

def random_string(randomizer: str, *args: str) -> str:
    match randomizer:
        case 'rna':
            return generate_string('AUGC', *args)
        case 'dna':
            return generate_string('ATGC', *args)