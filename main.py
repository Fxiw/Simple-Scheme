from parser import tokenize,parse
from eval_apply import scheme_eval,scheme_apply

from core import Env,Procedure
from builtins_ import add_primitives
env=Env()
add_primitives(env)
while True:
    source_code=input('scheme>')
    if source_code=='quit':
        break
    tokens=tokenize(source_code)
    ast=parse(tokens)
    result=scheme_eval(ast,env)
    print(result)