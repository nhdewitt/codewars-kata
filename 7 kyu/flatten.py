"""
Write a function that flattens an Array of Array objects into a flat Array. Your function must only do one level of flattening.

flatten [1,2,3] # => [1,2,3]
flatten [[1,2,3],["a","b","c"],[1,2,3]]  # => [1,2,3,"a","b","c",1,2,3]
flatten [[[1,2,3]]] # => [[1,2,3]]

https://www.codewars.com/kata/5250a89b1625e5decd000413/train/python
"""

def flatten(lst):
    flat_list = []
    for l in lst:
        if isinstance(l, list):
            for inner in l:
                flat_list.append(inner)
        else:
            flat_list.append(l)
    
    return flat_list