from win32clipboard import OpenClipboard, GetClipboardData
from re import findall
from string import punctuation
OpenClipboard()

abc: str = "abcdefghijklmnopqrstuvwxyz"
ABC: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def count_group(clip: str, group: str) -> int:
    cnt: int = 0
    for symbol in clip:
        cnt += int(symbol in group)
    return cnt

def count(*args: str):
    clip: str = GetClipboardData()

    match args:
        # Symbols:
        case ['s']:
            return len(clip)
        case ['l']:
            return count_group(clip, abc + ABC)
        case ['-l']:
            return len(clip) - count_group(clip, abc + ABC)
        case ['d']:
            return count_group(clip, '0123456789')
        case ['-d']:
            return len(clip) - count_group(clip, '0123456789')
        case ['p']:
            return count_group(clip, punctuation)
        case ['-p']:
            return len(clip) - count_group(clip, punctuation)
        case ['ws']:
            return count_group(clip, ' \t\n\r\v\f')
        case ['-ws']:
            return len(clip) - count_group(clip, ' \t\n\r\v\f')
        case ['g', group]:
            return clip.count(group)
        case ['-g', group]:
            return len(clip) - clip.count(group)
        case ['sub', substring]:
            return clip.count(substring)
        
        # Patterns:
        case ['w']:
            return len(findall(pattern=r'[a-zA-Z\\-]+', string=clip))
        case ['n']:
            return len(findall(pattern=r'[0-9]+', string=clip))
        case ['m']:
            return len(findall(pattern=r'[a-zA-Z\\.]+@[a-z]+.[a-z]+', string=clip))
        
    return len(findall(pattern=args[0], string=clip))