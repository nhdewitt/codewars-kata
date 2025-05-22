"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python
"""

def move_zeros(lst):
    i, j, l = 0, 0, len(lst)        # two pointers
    while i < l:
        if lst[i] == 0:             # if i == 0, only increment i
            i += 1
        elif i == j:                # if not 0 and i and j reference the same point, increment both
            i += 1
            j += 1
        else:
            lst[j] = lst[i]         # otherwise, move [i] element to j
            lst[i] = 0              # clear out [i]
            i += 1                  # increment both
            j += 1
    return lst