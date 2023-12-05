from argparser_wizardx import ArgParser
from generator_passwd_wizardx import Pwgen

arg_int = dict(type=int, default=8)
arguments = ArgParser()
arguments.new_argument('ammount', **arg_int)
arguments.new_argument('count', **arg_int)
arguments.new_argument('letters', action='store_const')
arguments.new_argument('punctuation', action='store_const')
arguments.new_argument('digits', action='store_const')
arguments.set_default_argument('letters')

passwords = Pwgen(arguments.get_arguments())
passwords.print_pw()