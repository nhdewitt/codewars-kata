"""
Your task is to write function factorial.

https://en.wikipedia.org/wiki/Factorial

https://www.codewars.com/kata/57a049e253ba33ac5e000212/train/python
"""

def factorial(n):
    prod = 1
    while (n > 0):
        prod *= n
        n -= 1
    return prod