from random import Random

class Pwgen:
    
    def __init__(self, all_args: dict) -> None:
        self.__symbols = ''
        self.__digits = dict()
        for key, value in all_args.items():
            if isinstance(value, str):
                self.__symbols += value
            elif isinstance(value, int):
                self.__digits[key] = value
    
    def __gen_pw(self) -> list:
        """
        ammount - длина каждого пароля;\n
        count - количество паролей.
        """
        result = list()
        rand = Random()
        for _ in range(self.__digits['count']):
            tmp = ''
            for _ in range(self.__digits['ammount']):
                tmp += rand.choice(self.__symbols)
            result.append(tmp)
        return result

    def print_pw(self):
        paswds = self.__gen_pw()
        print('*' * 40)
        print()
        print(*paswds, sep='\n')
        print()
        print('*' * 40)

