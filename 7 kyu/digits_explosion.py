"""
Given a string made of digits [0-9], return a string where each digit is repeated a number of times equals to its value.

Examples
"312" should return "333122"
"102269" should return "12222666666999999999"

https://www.codewars.com/kata/585b1fafe08bae9988000314/train/python
"""

def explode(s):
    explode = ""
    for c in s:
        explode += f"{c * int(c)}"
    
    return explode