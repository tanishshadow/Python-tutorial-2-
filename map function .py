def prod(n):
    return n*n

it=[1,2,3,4]
print(list(map(prod,it)))

# this is equivalent to-----

print([i**2 for i in it ])
