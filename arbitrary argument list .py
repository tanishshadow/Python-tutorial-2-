def fun(*args,sep=",") -> str:
    return sep.join(args) 


driver = fun("tanish","python","tensorflow")
print(driver)
