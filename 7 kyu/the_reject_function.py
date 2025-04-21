"""
Implement a function which filters out array values which satisfy the given predicate.

reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)  =>  [1, 3, 5]

https://www.codewars.com/kata/52988f3f7edba9839c00037d/train/python
"""

def reject(seq, predicate): 
    return [s for s in seq if not predicate(s)]