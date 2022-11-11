from analyse import *
import timeit

def timing(func):
    print(timeit.timeit(func, number=1))



