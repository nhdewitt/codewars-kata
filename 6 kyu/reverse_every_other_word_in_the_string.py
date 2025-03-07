"""
Reverse every other word in a given string, then return the string. Throw away any leading or trailing whitespace, while ensuring there is exactly one space between each word. Punctuation marks should be treated as if they are a part of the word in this kata.

https://www.codewars.com/kata/58d76854024c72c3e20000de/train/python
"""

def reverse_alternate(st):
    split_string = st.split()
    for i in range(1, len(split_string), 2):
        split_string[i] = split_string[i][::-1]
    
    return " ".join(split_string)