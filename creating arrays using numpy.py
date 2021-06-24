import numpy as np
L=[1,2,3,4]

print(ar:=np.array(L)) # returns the array
print(type(ar)) #returns the type of array (numpy.ndarray)
print(ar.shape) #returns the shape array i.e 1D,2D
print(ar.itemsize) #returns the number of elments in the array
print(ar.dtype) #returns the datatype of the elements

# creating arrays using functions of numpy
a=np.arange(1,10,2,np.int32) 
print(r:=np.linspace(1,10,5))
print(r.itemsize)
# print(a)
print(np.sin(L))
