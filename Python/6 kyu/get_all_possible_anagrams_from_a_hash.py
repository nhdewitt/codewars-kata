"""
Given a hash of letters and the number of times they occur, recreate all of the possible anagram combinations that could be created using all of the letters, sorted alphabetically.

The inputs will never include numbers, spaces or any special characters, only lowercase letters a-z.

E.g. get_words({2=>["a"], 1=>["b", "c"]}) => ["aabc", "aacb", "abac", "abca", "acab", "acba", "baac", "baca", "bcaa", "caab", "caba", "cbaa"]

https://www.codewars.com/kata/543e926d38603441590021dd/train/python
"""

import itertools

def get_words(hash_of_letters):
    letters = [char for (count, chars) in hash_of_letters.items() for char in chars for _ in range(count)]  # cycle through dictionary keys, adding x number of characters based on the dictionary key value
    combos = {"".join(p) for p in itertools.permutations(letters)}                                          # join the permutations as a set of strings to remove duplicates
    return sorted(combos)                                                                                   # return sorted to match the expected output