"""
In this Kata, you will be given an array of arrays and your task will be to return the number of unique arrays that can be formed by picking exactly one element from each subarray.

For example: solve([[1,2],[4],[5,6]]) = 4, because it results in only 4 possibilites. They are [1,4,5],[1,4,6],[2,4,5],[2,4,6].

Make sure that you don't count duplicates; for example solve([[1,2],[4,4],[5,6,6]]) = 4, since the extra outcomes are just duplicates.

See test cases for more examples.

Good luck!

If you like this Kata, please try:

Sum of integer combinations

Sum of array singles

https://www.codewars.com/kata/59e66e48fc3c499ec5000103/train/python
"""

from itertools import product                   # itertools.product() generates all permutations of N lists

def solve(arr):
    return len(set(list(product(*arr))))        # pack the lists into the permutations, convert the list to a set to remove duplicates, calculate length to find number of permutations