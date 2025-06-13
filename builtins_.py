
def add_primitives(env):
    env['+'] = lambda x, y: x + y
    env['-'] = lambda x, y: x - y
    env['*'] = lambda x, y: x * y
    env['/'] = lambda x, y: x / y
    env['>'] = lambda x, y: x > y
    env['<'] = lambda x, y: x < y
    env['<='] = lambda x, y: x <= y
    env['='] = lambda x, y: x == y
    env['cons'] = lambda x, y: [x,y]
    env['car'] = lambda x: x[0]
    env['cdr'] = lambda x: x[1:]