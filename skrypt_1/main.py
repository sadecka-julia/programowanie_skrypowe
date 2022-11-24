from fractions import Fraction
import cmath


def sum(arg1, arg2):
    try:
        if type(arg1) == str:
            arg1 = float(arg1)
    except ValueError:
        arg1 = 0
    try:
        if type(arg2) == str:
            arg2 = float(arg2)
    except ValueError:
        arg2 = 0
    return arg1+arg2


print('__name__ = {}'.format(__name__))
