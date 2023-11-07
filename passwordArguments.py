from sys import argv
from typing import Any


class ArgumentDeskriptor:
    
    def __set_name__(self, owner, name):
        self.name = '__' + name
    
    def __getattribute__(self, obj, __name: str) -> Any:
        value = getattr(obj, self.name)
        return value
    
    def __setattr__(self, obj, __name: str, __value: Any) -> None:
        setattr(obj, self.name, __value)


class Arguments:
    
    args = ArgumentDeskriptor()
    kwarg = ArgumentDeskriptor()
    
    def __init__(self, arg_name: str,) -> None:
        self.args = argv[1:]
        self.kwarg