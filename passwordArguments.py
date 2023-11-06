from sys import argv


class PasswordArguments:
    
    def __init__(self) -> None:
        self.__args = argv[1:]
        self.parser.add_help

    def __parse_args(self):
        lenght = len(self.__args)
        if len(self.__args) % 2 == 0:
            kwargs = dict()
            for i in self.__args[1:]:
                kwargs.setdefault(self.__args()[i])
    
    def add_arg(self, arg_name: str, help: str, default: int=None, type=int, required: bool = False) -> None:
        self.parser.add_argument(
                                '-' + arg_name[0], 
                                '--' + arg_name, 
                                type=type, 
                                metavar='', 
                                help=help, 
                                default=default, 
                                required=required,
                                )
        
    def get_password_arguments(self) -> dict:
        return self.parser.parse_args().__dict__