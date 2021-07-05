# Demonstrating the use of map function in python
'''
Syntax :

map(fun, iter)
Parameters :

fun : It is a function to which map passes each element of given iterable.
iter : It is a iterable which is to be mapped.

NOTE : You can pass one or more iterable to the map() function.



Returns :

Returns a list of the results after applying the given function  
to each item of a given iterable (list, tuple etc.) 
'''


def prod(n):
    return n*n

it=[1,2,3,4]
print(list(map(prod,it)))

# this is equivalent to-----

print([i**2 for i in it ])
