from argparse import ArgumentParser


class PasswordArguments:
    
    def __init__(self) -> None:
        self.parser = ArgumentParser()
        self.parser.add_help

    def add_arg(self, arg_name: str, type, help: str, default: int, required: bool = False) -> None:
        self.parser.add_argument(
                                '-' + arg_name[0], 
                                '--' + arg_name, 
                                type=type, 
                                metavar='', 
                                help=help, 
                                default=default, 
                                required=required
                                )
        
    def get_password_arguments(self) -> dict:
        return self.parser.parse_args().__dict__