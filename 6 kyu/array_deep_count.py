"""
You are given an array. Complete the function that returns the number of ALL elements within an array, including any nested arrays.

Examples
[]                   -->  0
[1, 2, 3]            -->  3
["x", "y", ["z"]]    -->  4
[1, 2, [3, 4, [5]]]  -->  7
The input will always be an array.

https://www.codewars.com/kata/596f72bbe7cd7296d1000029/train/python
"""

def deep_count(a, count=0):
    for el in a:
        if isinstance(el, list):
            count += 1
            count = deep_count(el, count)
        else:
            count += 1
    
    return count