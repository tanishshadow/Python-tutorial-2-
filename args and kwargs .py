def func(arg , *arg1, **args):
    print(arg)
    print(arg1) # *args is a tuple
    print({k:v for k,v in args.items()}) # since **args is a dictinary

func(1,"something","tanish",clas="10",roll = "60")
