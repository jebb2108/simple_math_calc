from math import *

def my_div(a, b):
    try:
        res = a / b
        return int(res)
    except ZeroDivisionError:
        return "You can`t divide by zero!"
    except TypeError:
        return "You entered the wrong argument."

def my_sum(a, b):
    try:
        res = a + b
        return res
    except TypeError:
        return "Wrong argument."

def my_sub(a, b):
    try:
        res = a - b
        return res
    except TypeError:
        print('Wrong argument.')