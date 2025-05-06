"""
Write a function named first_non_repeating_letter† that takes a string input, and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("");

† Note: the function is called firstNonRepeatingLetter for historical reasons, but your function should handle any Unicode character.

https://www.codewars.com/kata/52bc74d4ac05d0945d00054e/train/python
"""

from collections import Counter

def first_non_repeating_letter(s):
    if len(s) == 1:
        return s
    char_count = Counter(c.lower() for c in s)      # letter frequency normalized to lowercase
    
    for c in s:
        if char_count[c.lower()] == 1:               # find first character with count 1
            return c
    
    return ""                                        # if none, return ""