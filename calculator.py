# https://github.com/miawaleri/lab10-CF-MW.git
# Partner 1: Charley Fike
# Partner 2: Mia Waleri

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def add(a, b):
    return a + b

def subtract(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if a == 0:
        raise ZeroDivisionError

    return b/a


# First example
def square_root(a):
    try:
        result = math.sqrt(a)
        return result
    except ValueError:
        raise ValueError


def hypotenuse(a, b):
    return math.hypot(a, b)


def logarithm(a, b):
    if b <= 0 or a<=0:
        raise ValueError

    return math.log(b, a)
def exp(a, b):
    return a ** b





