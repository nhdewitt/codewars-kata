"""
There are some stones on Bob's table in a row, and each of them can be red, green or blue, indicated by the characters R, G, and B.

Help Bob find the minimum number of stones he needs to remove from the table so that the stones in each pair of adjacent stones have different colors.

Examples:

"RGBRGBRGGB"   => 1
"RGGRGBBRGRR"  => 3
"RRRRGGGGBBBB" => 9

https://www.codewars.com/kata/5f70e4cce10f9e0001c8995a/train/python
"""

import re

def solution(stones):
    groups = [s.group(1) for s in re.finditer(r'((.)\2*)', stones)]
    
    return sum(list(g.count(g[0]) - 1 for g in groups if g.count(g[0]) > 1))