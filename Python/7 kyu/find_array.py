"""
You are given two arrays, arr1 and arr2, where arr2 always contains integers.

Write a function returning the elements of arr1 pointed at ( zero-based ) by arr2, in order, such that:

for arr1 = ['a', 'a', 'a', 'a', 'a'], arr2 = [2, 4] the function returns ['a', 'a']

for arr1 = [0, 1, 5, 2, 1, 8, 9, 1, 5], arr2 = [1, 4, 7] the function returns [1, 1, 1]

for arr1 = [0, 3, 4], arr2 = [2, 6] the function returns [4]

for arr1 = ['a','b','c','d'] , arr2 = [2,2,2], the function returns ['c','c','c']

for arr1 = ['a','b','c','d'], arr2 = [3,0,2] the function returns ['d','a','c']

Note: when an element of arr2 is greater than the index of the last element of arr1 no element of arr1 should be added to the resulting array. If either arr1 or arr2 is empty, you should return an empty array (empty list in python, empty vector in c++).

Note: for c++ use std::vector<T> arr1, arr2.

https://www.codewars.com/kata/59a2a3ba5eb5d4e609000055/train/python
"""

def find_array(arr1, arr2):
    if arr1 is None or arr2 is None:
        return []
    l = len(arr1)
    return [arr1[i] for i in arr2 if i <= l - 1]