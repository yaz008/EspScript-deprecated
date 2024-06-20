# Imports:
from importlib import import_module
from sys import argv, path
from shlex import split
from yaml import load, SafeLoader

# Typing:
from types import ModuleType
from typing import Callable

config = f'{'\\'.join(path[0].split(sep='\\')[:-1])}\\config.json'
with open(file=config, mode='r', encoding='UTF-8') as ConfigFile:
    lookup: dict[str, str] = load(ConfigFile, SafeLoader)
short__name, *args = split(argv[1])

name: str = lookup[short__name]
module: ModuleType = import_module(f'scripts.{name}')
func: Callable[..., str] = getattr(module, name)
result: str = func(*args)
print(result)