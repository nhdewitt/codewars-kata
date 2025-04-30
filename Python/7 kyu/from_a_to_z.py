"""
Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter.
Note that if the range is given in capital letters, return the string in capitals also!

Examples
"a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
"h-o" ➞ "hijklmno"
"Q-Z" ➞ "QRSTUVWXYZ"
"J-J" ➞ "J"
Notes
A hyphen will separate the two letters in the string.
You don't need to worry about error handling in this kata (i.e. both letters will be the same case and the second letter will not be before the first alphabetically).

https://www.codewars.com/kata/6512b3775bf8500baea77663/train/python
"""

def gimme_the_letters(sp):
    first, last = sp.split("-")
    
    return "".join(chr(i) for i in range(ord(first), ord(last) + 1))