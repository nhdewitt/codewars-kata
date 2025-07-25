"""
Create range generator function that will take up to 3 parameters - start value, step and stop value. This function should return an iterable object with numbers. For simplicity, assume all parameters to be positive numbers.

Examples:

range(5) --> 1,2,3,4,5
range(3, 7) --> 3,4,5,6,7
range(2, 3, 15) --> 2,5,8,11,14


https://www.codewars.com/kata/584ebd7a044a1520f20000d5/train/python
"""

def range_function(*args):
    start, step = 1, 1
    if len(args) == 3:
        start, step, stop = args
    elif len(args) == 2:
        start, stop = args
    else:
        stop = args[0]
    i = start
    while i <= stop:
        yield i
        i += step