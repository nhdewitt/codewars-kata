"""
You are given a string of words and numbers. Extract the expression including:

the operator: either addition ("gains") or subtraction ("loses")
the two numbers that we are operating on
Return the result of the calculation.

Notes:

"loses" and "gains" are the only two words describing operators
No fruit debts nor bitten apples = The numbers are integers and no negatives
Examples
"Panda has 48 apples and loses 4"  -->  44
"Jerry has 34 apples and gains 6"  -->  40
Should be a nice little kata for you :)

https://www.codewars.com/kata/57b9fc5b8f5813384a000aa3/train/python
"""

def calculate(strng):
    parts = strng.split()
    start, operand, last = int(parts[2]), parts[-2], int(parts[-1])
    return start + last if operand == "gains" else start - last