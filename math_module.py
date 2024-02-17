from math import *

def check_division(a, b):
    try:
        c = a / b
        return float(c)
    except DivisionByZerroError:
        return "You can`t divide by zero!"
    except TypeError:
        return "You entered the wrong argument."
    finaly:
        return "Your calculation is completed. Redo it in case of an error."


def my_sum(a, b):
    try:
        c = a + b
        return 'c'
    except TypeError:
        return "Wrong argument."
    
