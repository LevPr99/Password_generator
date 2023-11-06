from passwordArguments import PasswordArguments

arg = PasswordArguments()

arg.add_arg('length_of_password', type=int, help='''Длина пароля''', default=8)
arg.add_arg('rows', type=int, help='''Количество строк в выводе''', default=8)
arg.add_arg('cols', type=int, help='''Количество столбцов в выводе''', default=4)
print(arg.get_password_arguments())