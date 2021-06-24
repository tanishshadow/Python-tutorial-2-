# factorial.py
'''Returns the factorial of any number'''
# functions


def factorial(n):
    if n == 0:
        return fac_0
    elif n == 1:
        return fac_1
    else:
        return n*factorial(n-1)


print(factorial(int(input("Enter a number:\n"))))

# constants
fac_1=1
fac_0=1
