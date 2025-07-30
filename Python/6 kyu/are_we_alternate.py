"""
Task
Create a function that accepts a string as an argument and validates whether the vowels (a, e, i, o, u) and consonants are in alternate order.

Examples
"amazon" --> true
"apple" --> false
"banana" --> true
Note
Arguments consist of only lowercase letters.


https://www.codewars.com/kata/59325dc15dbb44b2440000af/train/python
"""

def is_alt(s):
    vowels = {"a","e","i","o","u"}
    first_char_vowel = True if s[0] in vowels else False
    
    for i, c in enumerate(s):
        actual = c in vowels
        expected = (i % 2 == 0) == first_char_vowel
        if actual != expected:
            return False
        
    return True