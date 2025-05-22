"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !

https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python
"""

def pig_it(text):
    return " ".join(list(t[1:] + t[0] + "ay" if t.isalpha() else t for t in text.split()))