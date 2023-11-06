from passwordArguments import PasswordArguments
from randomPasswdGen import PasswdGenerator


arg = PasswordArguments()

arg.add_arg('length_of_password', help='Длина пароля', default=8)
arg.add_arg('rows', help='Количество строк в выводе', default=8)
arg.add_arg('cols', help='Количество столбцов в выводе', default=4)
arg.add_arg('a_letters', type=bool, help='', default=True)
arg.add_arg('digits', type=bool, help='', default=False)
arg.add_arg('punctuation', type=bool, help='', default=False)

generator = PasswdGenerator(arg.get_password_arguments())
print(generator.create_password())


print(arg.get_password_arguments())