from core import Procedure,Env
def scheme_eval(expr,env):
    if isinstance(expr,str):
        return env.find(expr)[expr]
    elif not isinstance(expr,list):
        return expr
    if isinstance(expr,int) or isinstance(expr,float):
        return expr

    elif expr[0]=='define':
        _,var,exp=expr
        val=scheme_eval(exp,env)
        env[var]=val
    elif expr[0]=='lambda':
        _,params,body=expr
        return Procedure(params,body,env)
    elif expr[0]=='if':
        _,test,conseq,alt=expr
        if scheme_eval(test,env):
            return scheme_eval(conseq,env)
        else:
            return scheme_eval(alt,env)
    else:
        proc=scheme_eval(expr[0],env)
        args=[scheme_eval(arg,env) for arg in expr[1:]]
        return scheme_apply(proc,args,env)
def scheme_apply(proc,args,env):
    if isinstance(proc,Procedure):
        local_env=Env(proc.env)
        for param,arg in zip(proc.params,args):
            local_env[param]=arg
        return scheme_eval(proc.body,local_env)
    elif callable(proc):
        return proc(*args)
    else:
        raise TypeError('not a procedure')









    

