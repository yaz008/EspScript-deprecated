from win32clipboard import OpenClipboard, GetClipboardData
import csv
from io import StringIO
from functools import reduce
OpenClipboard()

def get2d(csv_data: str, delimiter: str) -> list[list[str]]:
    csv_file = StringIO(csv_data)
    reader = csv.reader(csv_file, delimiter=delimiter)
    table = [row for row in reader]
    return table

def dim(table: list[list[str]]) -> list[int]:
    return [max(map(lambda x: len(x), row)) for row in map(list, zip(*table))]

def table(delimiter: str = ',') -> str:
    if delimiter == '\\sc':
        delimiter = ';'

    csv: str = GetClipboardData()
    table: list[list[str]] = get2d(csv, delimiter)
    col_widths: list[int] = dim(table)
    
    result: str = f'```table\n'
    for row in table:
        result += reduce(lambda x, y: x + y,
                         map(lambda x: f'+{'-' * x}',
                             col_widths)) + '+\n'
        result += reduce(lambda x, y: x + y,
                         map(lambda x: f'|{x[0].rjust(x[1])}',
                             zip(row, col_widths))) + '|\n'
    result += reduce(lambda x, y: x + y,
                         map(lambda x: f'+{'-' * x}',
                             col_widths)) + '+\n```'

    return result