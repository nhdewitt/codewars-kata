"""
Compare two strings by comparing the sum of their values (ASCII character code).

For comparing treat all letters as UpperCase
null/NULL/Nil/None should be treated as empty strings
If the string contains other characters than letters, treat the whole string as it would be empty
Your method should return true, if the strings are equal and false if they are not equal.

Examples:
"AD", "BC"  -> equal
"AD", "DD"  -> not equal
"gf", "FG"  -> equal
"zz1", ""   -> equal (both are considered empty)
"ZzZz", "ffPFF" -> equal
"kl", "lz"  -> not equal
null, ""    -> equal

https://www.codewars.com/kata/576bb3c4b1abc497ec000065/train/python
"""

from string import ascii_uppercase

def compare(s1, s2):
    try:
        s1 = s1.upper()
    except:
        s1 = ""
    try:
        s2 = s2.upper()
    except:
        s2 = ""
    s1_sum = []
    s2_sum = []
    for c in s1:
        if c not in ascii_uppercase:
            s1_sum = []
            break
        else:
            s1_sum.append(ord(c))
    for c in s2:
        if c not in ascii_uppercase:
            s2_sum = []
            break
        else:
            s2_sum.append(ord(c))
        
    return sum(s1_sum) == sum(s2_sum)