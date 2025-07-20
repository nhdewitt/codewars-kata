"""
Kata Task
Given 3 points a, b, c

            c
            
                     b         
  a

Find the shortest distance from point c to a straight line that passes through points a and b

Notes

all points are of the form [x,y] where x >= 0 and y >= 0
if a and b are the same then just return distance between a and c
use Euclidean distance

https://www.codewars.com/kata/59c053f070a3b7d19100007e/train/python
"""

from math import sqrt

def distance_from_line(a, b, c):
    ax, ay = a
    bx, by = b
    cx, cy = c
    
    dx = bx - ax
    dy = by - ay
    
    denom = sqrt(dx * dx + dy * dy)
    if denom == 0:
        return sqrt((cx - ax) ** 2 + (cy - ay) ** 2)
    
    numer = abs(dx * (cy - ay) - (cx - ax) * dy)
    
    return numer / denom