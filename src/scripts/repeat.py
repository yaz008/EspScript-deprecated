from win32clipboard import OpenClipboard, GetClipboardData
OpenClipboard()

def repeat(string: str, times: str, sep: str = '') -> str:
    if string == '%':
        string = GetClipboardData()
    return f'{string}{sep}' * (int(times) - 1) + string