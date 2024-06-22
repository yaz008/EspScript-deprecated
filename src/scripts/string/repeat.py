def repeat(stdin: str, *args: str) -> str:
    match args:
        case [times]:
            return stdin * int(times)
        case [times, sep]:
            return f'{stdin}{sep}' * (int(times) - 1) + stdin