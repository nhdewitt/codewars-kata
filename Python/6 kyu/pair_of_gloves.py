"""
Pair of gloves
Winter is coming, you must prepare your ski holidays. The objective of this kata is to determine the number of pair of gloves you can constitute from the gloves you have in your drawer.

Given an array describing the color of each glove, return the number of pairs you can constitute, assuming that only gloves of the same color can form pairs.

Examples:
input = ["red", "green", "red", "blue", "blue"]
result = 2 (1 red pair + 1 blue pair)

input = ["red", "red", "red", "red", "red", "red"]
result = 3 (3 red pairs)


https://www.codewars.com/kata/58235a167a8cb37e1a0000db/train/python
"""

from collections import Counter

def number_of_pairs(gloves):
    glove_count = Counter(gloves)
    pairs = 0
    for k, v in glove_count.items():
        pairs += v // 2
    return pairs