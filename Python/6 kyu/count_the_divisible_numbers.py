"""
Complete the function that takes 3 numbers x, y and k (where x ≤ y), and returns the number of integers within the range [x..y] (both ends included) that are divisible by k.

More scientifically: { i : x ≤ i ≤ y, i mod k = 0 }

Example
Given x = 6, y = 11, k = 2 the function should return 3, because there are three numbers divisible by 2 between 6 and 11: 6, 8, 10

Note: The test cases are very large. You will need a O(log n) solution or better to pass. (A constant time solution is possible.)


https://www.codewars.com/kata/55a5c82cd8e9baa49000004c/train/python
"""

def divisible_count(x, y, k):
    if x > y or k == 0:
        return 0
    
    first = (x + k - 1) // k
    last = y // k
    
    if last < first:
        return 0
    
    return last - first + 1