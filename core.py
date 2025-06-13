

class Env(dict):
    def __init__(self, parent=None):
        self.parent = parent
    def find(self,var):
        if var in self:
            return self
        elif self.parent:
            return self.parent.find(var)
        else:
            raise NameError(f"unbound variable: {var}")

class Procedure:
    def __init__(self, params, body, env):
        self.params = params
        self.body = body
        self.env = env
    def __call__(self,*args):
        local_env = Env(self.env)
        for param, arg in zip(self.params, args):
            local_env[param] = arg
        return scheme_eval(self.body, local_env)

