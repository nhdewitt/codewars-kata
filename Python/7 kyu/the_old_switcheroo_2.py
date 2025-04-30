"""
This is a follow up to my kata the old switcheroo.

Write a function that takes in a string and replaces all the letters with their respective positions in the English alphabet; e.g. 'a' is 1, 'z' is 26. The function should be case-insensitive.

'abc'      --> '123'
'ABC'      --> '123'
'codewars' --> '315452311819'
'abc-#@5'  --> '123-#@5'

https://www.codewars.com/kata/55d6a0e4ededb894be000005/train/python
"""

def encode(st):
    return "".join([str(ord(s.lower()) - 96) if s.isalpha() else s for s in st])