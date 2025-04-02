"""
Given an array of strings, write a function that returns an array containing only the elements of the given array whose length is an even number.

Example
["One", "Two", "Three", "Four"] --> ["Four"]

https://www.codewars.com/kata/59564f3bcc15b5591a00004a/train/python
"""

def filter_even_length_words(words):
    return [word for word in words if len(word) % 2 == 0]