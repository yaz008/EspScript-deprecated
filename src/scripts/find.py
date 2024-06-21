from win32clipboard import OpenClipboard, GetClipboardData
from re import findall
OpenClipboard()

def find(*args: str) -> list[str]:
    clip: str = GetClipboardData()
    
    match args:
        case ['w']:
            return findall(pattern=r'[a-zA-Z-]+', string=clip)
        case ['n']:
            return findall(pattern=r'[0-9]+', string=clip)
        case ['m']:
            return findall(pattern=r'[a-zA-Z\\.]+@[a-z]+.[a-z]+', string=clip)
    return findall(pattern=args[0], string=clip)