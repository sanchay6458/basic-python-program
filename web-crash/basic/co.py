# create a simple module

# A simple module, calc.py
def add(x, y):
    return (x+y)
def subtract(x, y):
    return (x-y)
def mul(x, y):
    return (x+y)

# Factorial
def factorial(num):
    fact = 1
    i= 1
    if (num<=0):
        return 0
    else:
        while (i <= num):
            fact = fact *i
            i = i + 1
        return fact
