def repeat(string: str, times: str, sep: str = '') -> str:
    return f'{string}{sep}' * (int(times) - 1) + string