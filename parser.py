def tokenize(source_code):
    s=source_code.replace('(', ' ( ').replace(')', ' ) ')
    return s.split()
def parse(tokens):
    if len(tokens) == 0:
        raise SyntaxError("Unexpected EOF while reading")
    token = tokens.pop(0)
    if token == '(':
        L = []
        while tokens[0] != ')':
            L.append(parse(tokens))
        tokens.pop(0)
        return L
    elif token == ')':
        raise SyntaxError("Unexpected )")
    else:
        return atom(token)

def atom(token):
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return token