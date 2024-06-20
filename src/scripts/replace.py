from win32clipboard import OpenClipboard, GetClipboardData
OpenClipboard()

def replace(old: str, new: str) -> str:
    clip: str = GetClipboardData()
    return clip.replace(old, new)