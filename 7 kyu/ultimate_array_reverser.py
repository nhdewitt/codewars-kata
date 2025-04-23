"""
Task
Given an array of strings, reverse them and their order in such way that their length stays the same as the length of the original inputs.

Example:
Input:  {"I", "like", "big", "butts", "and", "I", "cannot", "lie!"}
Output: {"!", "eilt", "onn", "acIdn", "ast", "t", "ubgibe", "kilI"}
Good luck!

https://www.codewars.com/kata/5c3433a4d828182e420f4197/train/python
"""

def reverse(a):
    lengths = list(len(s) for s in a)               # put the lengths into a list
    merged = "".join(a)[::-1]                       # merge the list and reverse
    
    output = []
    
    i = 0
    for length in lengths:
        output.append(merged[i:i + length])         # list slicing to rearrange the reversed list
        i += length
    
    return output