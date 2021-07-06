def fun(a, L=None) -> list:
    if L is None:
        L=[]
        L.append(a)
    
    return L

print(fun(1)) #[1]
print(fun(2)) #[2]

def func(a,l=[]) -> list:
    l.append(a)
    return l

print(func(1)) #[1]
print(func(2)) # [1,2]
print(func(3)) # [1,2,3]
