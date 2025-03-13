"""
Consider the word "abode". We can see that the letter a is in position 1 and b is in position 2. In the alphabet, a and b are also in positions 1 and 2. Notice also that d and e in abode occupy the positions they would occupy in the alphabet, which are positions 4 and 5.

Given an array of words, return an array of the number of letters that occupy their positions in the alphabet for each word. For example,

solve(["abode","ABc","xyzD"]) = [4, 3, 1]
See test cases for more examples.

Input will consist of alphabet characters, both uppercase and lowercase. No spaces.

Good luck!

If you like this Kata, please try:

Last digit symmetry

Alternate capitalization

https://www.codewars.com/kata/59d9ff9f7905dfeed50000b0/train/python
"""

def pos_check(char):
    return (ord(char) - ord('A') + 1) if char.isupper() else (ord(char) - ord('a') + 1)

def solve(strings : list[str]) -> list[int]:
    char_count = []
    for string in strings:
        count = 0
        for i, c in enumerate(string, 1):
            if pos_check(c) == i:
                count += 1
        char_count.append(count)
    
    return char_count