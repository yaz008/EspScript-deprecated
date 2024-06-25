from sys import path
from importlib import import_module
from json import load
from types import ModuleType
from typing import Callable, Any

config: str = f'{'\\'.join(path[0].split(sep='\\')[:-1])}\\config.json'
with open(file=config, mode='r', encoding='UTF-8') as ConfigFile:
    lookup: dict[str, str] = load(ConfigFile)

def load_by_name(name: str) -> Callable[..., Any]:
    path, funcname = lookup[name].split(sep='::')
    module: ModuleType = import_module(f'modules.{path}')
    return getattr(module, funcname)