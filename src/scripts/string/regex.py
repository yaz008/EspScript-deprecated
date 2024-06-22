from re import findall

def find(stdin: str, *args: str) -> list[str]:
    match args:
        case ['w']:
            return findall(pattern=r'[a-zA-Z-]+', string=stdin)
        case ['n']:
            return findall(pattern=r'[0-9]+', string=stdin)
        case ['e']:
            return findall(pattern=r'[a-zA-Z\\.]+@[a-z]+.[a-z]+', string=stdin)