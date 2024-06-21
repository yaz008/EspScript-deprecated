from num2words import num2words

def name_amino(name: str) -> str:
    return {
        'g': 'Glycine', 'gly': 'Glycine',
        'a': 'Alanine', 'ala': 'Alanine',
        'v': 'Valine', 'val': 'Valine',
        'l': 'Leucine', 'leu': 'Leucine',
        'i': 'Isoleucine', 'ile': 'Isoleucine',
        't': 'Threonine', 'thr': 'Threonine',
        's': 'Serine', 'ser': 'Serine',
        'm': 'Methionine', 'met': 'Methionine',
        'c': 'Cystein', 'cys': 'Cystein',
        'p': 'Proline', 'pro': 'Proline',
        'f': 'Phenylalanine', 'phe': 'Phenylalanine',
        'y': 'Tyrosine', 'tyr': 'Tyrosine',
        'w': 'Tryptophane', 'trp': 'Tryptophane',
        'h': 'Histidine', 'his': 'Histidine',
        'k': 'Lysine', 'lys': 'Lysine',
        'r': 'Argenine', 'arg': 'Argenine',
        'd': 'Aspartate', 'asp': 'Aspartate',
        'e': 'Glutamate', 'glu': 'Glutamate',
        'n': 'Asparagine', 'asn': 'Asparagine',
        'q': 'Glutamine', 'gln': 'Glutamine'
    }.get(name.lower(), '<Unknown>')

def name_number(number: str, *args: str) -> str:
    if len(args) == 0:
        return num2words(number=number)
    if len(args) == 1:
        if args[0] == '-o':
            return num2words(number=number, ordinal=True)
        return num2words(number=number, lang=args[0])
    return num2words(number=number, ordinal='-o' in args, lang=args[0])

def name(*args: str) -> str:
    match args:
        case ['amino', *args]:
            return name_amino(*args)
        case ['prot' | 'protein', *args]:
            return [name_amino(amino) for amino in args[0]]
    return name_number(*args)