"""
Triangular number is any amount of points that can fill an equilateral triangle.

Example: the number 6 is a triangular number because all sides of a triangle has the same amount of points.

alt text

Hint!
T(n) = n * (n + 1) / 2,
n - is the size of one side.
T(n) - is the triangular number.
Given a number T from interval [1..2147483646], find if it is triangular number or not.

Appreciate the feedback!

https://www.codewars.com/kata/56d0a591c6c8b466ca00118b/train/python
"""

from math import sqrt

def is_triangular(t):
    k = (-1 + sqrt(1 + 8 * t)) / 2
    return k.is_integer()