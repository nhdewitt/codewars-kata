"""
In this Kata, you will be given a string and your task will be to return a list of ints detailing the count of uppercase letters, lowercase, numbers and special characters (everything else), as follows.

The order is: uppercase letters, lowercase letters, numbers and special characters.

"*'&ABCDabcde12345" --> [ 4, 5, 5, 3 ]
More examples in the test cases.

Good luck!

https://www.codewars.com/kata/5a29a0898f27f2d9c9000058/train/python
"""

def solve(s):
    dict = {
        "upper": 0,
        "lower": 0,
        "number": 0,
        "special": 0
    }
    
    for c in s:
        if c.isupper():
            dict["upper"] += 1
        elif c.islower():
            dict["lower"] += 1
        elif c.isnumeric():
            dict["number"] += 1
        else:
            dict["special"] += 1
    
    return [dict["upper"], dict["lower"], dict["number"], dict["special"]]