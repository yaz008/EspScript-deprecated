def repeat(string: str, *args: str) -> str:
    match args:
        case [times]:
            return string * int(times)
        case [times, sep]:
            return f'{string}{sep}' * (int(times) - 1) + string