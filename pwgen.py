from argparser_wizardx import ArgParser
from generator_passwd_wizardx import Pwgen

a = ArgParser()
arg_int = dict(type=int, default=8)
a.new_argument('ammount', **arg_int)
a.new_argument('count', **arg_int)
a.new_argument('letters', action='store_const')
a.new_argument('punctuation', action='store_const')
a.new_argument('digits', action='store_const')
a.set_default_argument('letters')

p = Pwgen(a.get_arguments())
p.print_pw()