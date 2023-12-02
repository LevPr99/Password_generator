from argparse import ArgumentParser
from string import digits, ascii_letters


class ArgParser:
    
    punctuation = '''#$%&'()*+,-./:;<=>?@[]^_`{|}~'''
    
    def __init__(self) -> None:
        self.__parser = ArgumentParser()
        self.__args_dict = {'punctuation':self.punctuation, 
                               'digits':digits, 
                               'letters':ascii_letters}
        self.set_default_argument()
        
    def new_argument(self, f_name, **kwargs) -> None:
        name = '-' + f_name[0]
        if f_name in self.__args_dict:
            kwargs['const'] = self.__args_dict.pop(f_name)
        f_name = '--' + f_name
        self.__parser.add_argument(name, f_name, **kwargs)
    
    def set_default_argument(self, argument: str='help'):
        """
        Args:
            argument (str) -- default argument e.g. "argument"
        """
        self.__default_argument = ['-' + argument[0]]
            
    def get_arguments(self, *args) -> dict:
        if len(args) < 1:
            args = list(args)
            args.append(self.__default_argument)
        tmp = vars(self.__parser.parse_args(*args))
        return tmp
    