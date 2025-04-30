"""
When provided with a String, capitalize all vowels

For example:

Input : "Hello World!"

Output : "HEllO WOrld!"

Note: Y is not a vowel in this kata.

https://www.codewars.com/kata/5831c204a31721e2ae000294/train/python
"""

def swap(st):
    vowels = ""
    for c in st:
        if c in {"a", "e", "i", "o", "u"}:
            vowels += c.upper()
        else:
            vowels += c
    
    return vowels