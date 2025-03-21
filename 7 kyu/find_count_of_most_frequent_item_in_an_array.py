"""
Complete the function to find the count of the most frequent item of an array. You can assume that input is an array of integers. For an empty array return 0

Example
input array: [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]
ouptut: 5 
The most frequent number in the array is -1 and it occurs 5 times.

https://www.codewars.com/kata/56582133c932d8239900002e/train/python
"""

from collections import Counter

def most_frequent_item_count(collection):
    if collection == []:
        return 0
    counts = Counter(collection)
    return collection.count(sorted(collection, key=lambda x: (-counts[x], x))[0])