"""
How can you tell an extrovert from an introvert at NSA?
Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it?
According to Wikipedia, ROT13 is frequently used to obfuscate jokes on USENET.

For this task you're only supposed to substitute characters. Not spaces, punctuation, numbers, etc.

Test examples:

"EBG13 rknzcyr." -> "ROT13 example."

"This is my first ROT13 excercise!" -> "Guvf vf zl svefg EBG13 rkprepvfr!"

https://www.codewars.com/kata/52223df9e8f98c7aa7000062/train/python
"""

from string import ascii_lowercase, ascii_uppercase

def rot13(message):
    rot = ascii_lowercase[13:] + ascii_lowercase[:13] + ascii_uppercase[13:] + ascii_uppercase[:13]
    alpha = ascii_lowercase + ascii_uppercase
    trans = str.maketrans(rot, alpha)
    
    return message.translate(trans)