# standard arg


def standard(arg):
    print(arg)
standard(1)
standard(arg=1)

# position only
def position_only(arg,/):
    print(arg)

position_only(10)
# position_only(arg=10) # this cant be done

def keyword_only(*,arg):
    print(arg)

# keyword_only(10) # keyword_only() takes 0 positional arguments but 1 was given
keyword_only(arg=100)


# combined form 
def combined(standard,pos_only,/,*,kwd_only):
    print(standard,pos_only,kwd_only)

combined(10,100,kwd_only=1000)


# kwds **

def foo(name,**kw):
    return 'name' in kw


# print(foo("tanish",clas=10,roll=60,name="tanish"))
# print(foo(1, **{'name': 1})) # foo() takes 1 positional argument but 2 were given
# correct----

def fooo(name,/,**kw):
    return 'name' in kw

print(fooo('tanish',**{'name':'tanish'}))
