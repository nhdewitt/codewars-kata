"""
Create a function that takes a string as a parameter and does the following, in this order:

Replaces every letter with the letter following it in the alphabet (see note below)
Makes any vowels capital
Makes any consonants lower case
Note:

the alphabet should wrap around, so Z becomes A
in this kata, y isn't considered as a vowel.
So, for example the string "Cat30" would return "dbU30" (Cat30 --> Dbu30 --> dbU30)

https://www.codewars.com/kata/58039f8efca342e4f0000023/train/python
"""

from string import ascii_letters

def rot_1(st):
    return "".join(
    chr((ord(c) - 97 + 1) % 26 + 97) if c in ascii_letters and c.islower() else
    chr((ord(c) - 65 + 1) % 26 + 65) if c in ascii_letters and c.isupper() else c
    for c in st
    )

def changer(s):
    return "".join(c.upper() if c.lower() in "aeiou" else c.lower() for c in rot_1(s))