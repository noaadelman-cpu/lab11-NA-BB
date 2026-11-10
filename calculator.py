"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        raise ValueError

def hypotenuse(a,b):
    try:
        return math.hypot(a, b)
    except ValueError:
        raise ValueError

# First example
def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b


def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError
    return math.log(b, a)



def mul(a,b):
    return a*b

def div(a,b):
    if b == 0:
        raise ZeroDivisionError
    else:
        return b/a


def exp(a,b):
    return a**b

