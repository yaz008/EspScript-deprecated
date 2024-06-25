def write(file: str, content: str) -> None:
    with open(file=file, mode='w', encoding='UTF-8') as File:
        File.write(content)