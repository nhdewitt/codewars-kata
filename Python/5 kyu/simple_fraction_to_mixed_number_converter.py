"""
Task
Given a string representing a simple fraction x/y, your function must return a string representing the corresponding mixed fraction in the following format:

[sign]a b/c

where a is integer part and b/c is irreducible proper fraction. There must be exactly one space between a and b/c. Provide [sign] only if negative (and non zero) and only at the beginning of the number (both integer part and fractional part must be provided absolute).

If the x/y equals the integer part, return integer part only. If integer part is zero, return the irreducible proper fraction only. In both of these cases, the resulting string must not contain any spaces.

Division by zero should raise an error (preferably, the standard zero division error of your language).

Value ranges
-10 000 000 < x < 10 000 000
-10 000 000 < y < 10 000 000
Examples
Input: 42/9, expected result: 4 2/3.
Input: 6/3, expedted result: 2.
Input: 4/6, expected result: 2/3.
Input: 0/18891, expected result: 0.
Input: -10/7, expected result: -1 3/7.
Inputs 0/0 or 3/0 must raise a zero division error.
Note
Make sure not to modify the input of your function in-place, it is a bad practice.

https://www.codewars.com/kata/556b85b433fb5e899200003f/train/python
"""

import math

def mixed_fraction(s: str):
    num, denom = parse_fraction(s)                          # split the string fraction into integers
    if denom == 0:                                          # can stop here if either is 0
        raise ZeroDivisionError
    if num == 0:
        return "0"
    sign, num, denom = normalize_sign(num, denom)           # determine if negative, abs() both num and den
    whole, num, denom = mixed_components(num, denom)        # calculate whole number, reduce fraction
    return format_output(sign, whole, num, denom)           # return formatted output

def parse_fraction(s: str):
    num, denom = map(int, s.split("/"))
    return (num, denom)

def normalize_sign(num: int, den: int):
    sign = ""
    if (num < 0 and den > 0) or (num > 0 and den < 0):
        sign = "-"
    return (sign, abs(num), abs(den))

def mixed_components(num: int, den: int):
    whole, rem = divmod(num, den)
    g = math.gcd(rem, den)
    return (whole, rem // g, den // g)

def format_output(sign: str, whole: int, num: int, den: int):
    if num == 0:
        return f"{sign}{whole}"
    if whole == 0:
        return f"{sign}{num}/{den}"
    return f"{sign}{whole} {num}/{den}"