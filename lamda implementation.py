# simple usage of lambda expression

avg = lambda x,y:(x+y)/2
print(avg(10,20))

# instead of ----
def average(x,y):
    return (x+y)/2

# print(average(10,20))

# Nested function usage of lambda

def increment(n)->int:
    return lambda x:x+n

f = increment(10) #f is a lambda fucntion now
print(f(1))


# using lambda in sorting

lst = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
lst.sort(key=lambda x:x[1]) #sorting the lst by its second value of every tuple in it.

print(lst)
