def repeat(stdin: str, times: str, sep: str | None = None) -> str:
    if sep is None:
        return stdin * int(times)
    return f'{stdin}{sep}' * (int(times) - 1) + stdin