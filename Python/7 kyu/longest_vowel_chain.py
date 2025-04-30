"""
The vowel substrings in the word codewarriors are o,e,a,io. The longest of these has a length of 2. Given a lowercase string that has alphabetic characters only (both vowels and consonants) and no spaces, return the length of the longest vowel substring. Vowels are any of aeiou.

Good luck!

https://www.codewars.com/kata/59c5f4e9d751df43cf000035/train/python
"""

def solve(s):
    return len(sorted("".join([c if c in "aeiou" else "_" for c in s]).split("_"), key=len)[-1])