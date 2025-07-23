"""
Given a mathematical equation that has *,+,-,/, reverse it as follows:

solve("100*b/y") = "y/b*100"
solve("a+b-c/d*30") = "30*d/c-b+a"
More examples in test cases.

Good luck!

Please also try:

Simple time difference

Simple remove duplicates


https://www.codewars.com/kata/5aa3af22ba1bb5209f000037/train/python
"""

import re

def solve(eq):
    eq = re.split(r"(\+|\-|\*|/|\(|\))", eq)
    return "".join(eq[::-1])