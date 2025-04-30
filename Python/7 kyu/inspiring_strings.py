"""
Given a string of space separated words, return the longest word.
If there are multiple longest words, return the rightmost longest word.

Examples
"red white blue"  =>  "white"
"red blue gold"   =>  "gold"

https://www.codewars.com/kata/5939ab6eed348a945f0007b2/train/python
"""

def longest_word(string_of_words):
    return sorted([(i, v) for i, v in enumerate(string_of_words.split())], key=lambda x: (-len(x[1]), -x[0]))[0][1]