# combining two elements of two lists like cartesian product of sets if they are not equal-----

list_comp = [(x,y) for  x in [1,2,3] for y in [3,1,4] if x != y]
print(list_comp)
# this is equivalent to -- 

lst = []
for i in [1,2,3]:
    for b in [3,1,4]:
        if i!=b : 
            lst.append((i,b))

print(lst)
            

ints = [1,-1,2,0,3]
# only the values greater than zero
print([x for x in ints if x>=0])
# all the values but made +ve
print([abs(x) for x in ints])

# flattening a list --
vec = [[1,2,3],[2,4,5]]
# [num for elem in vec for 
print([y for x in vec for y in x])
lst0 = []
for x  in vec:
    for y in x :
        lst0.append(y)

print(lst0)
