"""
Remember the spongebob meme that is meant to make fun of people by repeating what they say in a mocking way?

"Dont use that weird spongebob mocking meme" Me: DonT uSe thAt WeIrd SpoNgEboB MoCkinG MEme

You need to create a function that converts the input into this format, with the output being the same string expect there is a pattern of uppercase and lowercase letters.

Example:

input:  "stop Making spongebob Memes!"
output: "StOp mAkInG SpOnGeBoB MeMeS!"

https://www.codewars.com/kata/5982619d2671576e90000017/train/python
"""

def sponge_meme( s ):
    return "".join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s))