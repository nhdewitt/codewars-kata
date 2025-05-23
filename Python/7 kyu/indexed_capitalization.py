"""
Given a string and an array of integers representing indices, capitalize all letters at the given indices.

For example:

capitalize("abcdef",[1,2,5]) = "aBCdeF"
capitalize("abcdef",[1,2,5,100]) = "aBCdeF". There is no index 100.
The input will be a lowercase string with no spaces and an array of digits.

Good luck!

https://www.codewars.com/kata/59cfc09a86a6fdf6df0000f1/train/python
"""

def capitalize(s, ind):
    for i in ind:
        if i < len(s):
            s = s[:i] + s[i].upper() + s[i + 1:]
    
    return s