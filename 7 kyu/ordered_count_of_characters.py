"""
Count the number of occurrences of each character and return it as a (list of tuples) in order of appearance. For empty output return (an empty list).

Consult the solution set-up for the exact data structure implementation depending on your language.

https://www.codewars.com/kata/57a6633153ba33189e000074
"""

def ordered_count(inp):
    char_count = {}
    for i in inp:
        char_count[i] = char_count.get(i, 0) + 1
    
    return [(key, value) for key, value in char_count.items()]