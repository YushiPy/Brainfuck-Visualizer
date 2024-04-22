
from interpreter import Interpreter

import settings

settings.PRINT_LINE = False
code = """
>>> , > , [- > + >> + <<<]
< [- >> - [<] <]

"""
"""
>> , >>>> +++++ +++++ +++++ + <<<< 
[
    [- > + >>> - [>] <<< [- >>> + <<<] >>> [< + >>] <<<<<] 
    < + >
    > [- << + >>>>> + <<<] >>
    [- << + >>] > [- > + <] <<<
]
< +++++ +++++

"""
"""
>>>> +++++ +++++ <<<< 
[
    [- > + >>> - [>] <<< [- >>> + <<<] >>> [< + >>] <<<<<] 
    < - > +++++ ++ [- < +++++ ++ >]
    > [- << + >>>>> + <<<] >>
    [- << + >>] > [- > + <] <<<
]
<< [. <]
"""

interpreter = Interpreter(code)

print(interpreter.run([255, 0]))
print(interpreter)