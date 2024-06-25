from importlib import import_module
from modules.filemanip import load_json
from types import ModuleType
from typing import Callable, Any

lookup: dict[str, str] = load_json(relative_path='..\\config.json')

def load_by_name(name: str) -> Callable[..., Any]:
    path, funcname = lookup[name].split(sep='::')
    module: ModuleType = import_module(f'packages.{path}')
    return getattr(module, funcname)