# function annotations --- 

def foo(*some_string) -> str: #this just gives the return type of function (this is return annotation)
    return some_string


print(foo("Tanish op","python op"))

def fun(name:str) : # to declare the type of the argument (this is a annotation)
    print(name,"This is a string as expected")

fun("Tanish")


print(foo.__annotations__) # gives the annotation (in a dictionary)  ({'return': <class 'str'>})
print(fun.__annotations__) # gives the annotation  ({'name': <class 'str'>})
