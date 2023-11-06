from random import Random
from string import ascii_letters, digits, punctuation

class PasswdGenerator:
    
    __PW_ARGS: dict = {'a_letters': ascii_letters, 'digits': digits, 'punctuation': punctuation}
    
    
    def __init__(self, arguments: dict) -> None:
        self.__rand = Random()
        self.__symbols_set = ''
        if self.__check_args(arguments):
            self.__args = arguments
    
    @staticmethod
    def __check_args(arguments: dict):
        if arguments['rows'] < 1 or arguments['cols'] < 1 or arguments['length_of_password'] < 1:
            raise ValueError('Аргументы: "rows", "cols", "length_of_password", должны быть > 0')
        return True
    
    def __set_simbols(self):
        for i in list(self.__PW_ARGS.keys()):
            if i in self.__args:
                self.__symbols_set += self.__PW_ARGS[i]
    
    def create_password(self) -> list:
        self.__check_args(self.__args)
        self.__set_simbols()
        passwords = []
        for _ in range(self.__args['rows']):
            tmp = []
            for _ in range(self.__args['cols']):
                tmp.append(''.join(self.__rand.choices(self.__symbols_set, k=self.__args['length_of_password'])))
            passwords.append(tmp)
        return passwords
    
    def print_password(self, arguments: dict):
        
        pass