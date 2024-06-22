from json import loads

def cast_to_object(stdin: str, *args) -> object:
    return loads(stdin)