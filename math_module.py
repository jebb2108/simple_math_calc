import math
from math import *

def my_div(a, b):
    try:
        res = int(a) / int(b)
        return round(res, 2)
    except ZeroDivisionError:
        return "You can`t divide by zero!"

def my_sum(a, b):
    res = int(a) + int(b)
    return res

def my_sub(a, b):
    res = int(a) - int(b)
    return math.ceil(res)