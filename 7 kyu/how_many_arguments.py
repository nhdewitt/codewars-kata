"""
Write a function that returns the number of arguments it received.

args_count() --> 0
args_count('a') --> 1
args_count('a', 'b') --> 2
The function must work for keyword arguments too:

args_count(x=10, y=20, 'z') --> 3

https://www.codewars.com/kata/5c44b0b200ce187106452139/train/python
"""

def args_count(*args, **kwargs):
    return len(args) + len(kwargs)