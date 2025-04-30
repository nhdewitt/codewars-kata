"""
Find the longest substring in alphabetical order.

Example: the longest alphabetical substring in "asdfaaaabbbbcttavvfffffdf" is "aaaabbbbctt".

There are tests with strings up to 10 000 characters long so your code will need to be efficient.

The input will only consist of lowercase characters and will be at least one letter long.

If there are multiple solutions, return the one that appears first.

Good luck :)

https://www.codewars.com/kata/5a7f58c00025e917f30000f1/train/python
"""

def longest(st):
    if not st:
        return ""
    o = [ord(s) for s in st]                                # convert to ord to check alphabetically
    longest_str = st[0]
    temp_str = ""
    for i in range(1, len(o)):
        if o[i] >= o[i - 1]:                                # keep appending to temp string if the string remains alphabetical
            if not temp_str:
                temp_str = st[i - 1]
            temp_str += st[i]
        else:
            if len(temp_str) > len(longest_str):            # if it's longer than the current longest, make it the new longest
                longest_str = temp_str
            temp_str = ""
    
    if len(temp_str) > len(longest_str):                    # check once more at the end for the last character and return
        longest_str = temp_str
    
    return longest_str