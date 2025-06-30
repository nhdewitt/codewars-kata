"""
For a given string s find the character c (or C) with longest consecutive repetition and return:

(c, l)
where l (or L) is the length of the repetition. If there are two or more characters with the same l return the first in order of appearance.

For empty string return:

('', 0)
Happy coding! :)

https://www.codewars.com/kata/586d6cefbcc21eed7a001155/train/python
"""

def longest_repetition(chars):
    if len(chars) == 0:
        return ("", 0)
    
    res = (chars[0], 1)
    current_count = 1
    
    i = 1
    while i < len(chars):
        if chars[i] == chars[i - 1]:
            current_count += 1
        else:
            current_count = 1
        
        if current_count > res[1]:
            res = (chars[i], current_count)
        
        i += 1
    
    return res