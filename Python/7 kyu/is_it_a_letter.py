"""
Write a function, isItLetter or is_it_letter or IsItLetter, which tells us if a given character is a letter or not.

https://www.codewars.com/kata/57a06b07cf1fa58b2b000252/train/python
"""

def is_it_letter(s):
    return s.isalpha() and len(s) == 1