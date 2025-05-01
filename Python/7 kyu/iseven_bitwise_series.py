"""
Is the number even?
If the numbers is even return true. If it's odd, return false.





Oh yeah... the following symbols/commands have been disabled!

use of %
use of .even? in Ruby
use of mod in Python

https://www.codewars.com/kata/592a33e549fe9840a8000ba1/train/python
"""

def is_even(n):
    return bin(n)[-1] == "0"        # check binary 1