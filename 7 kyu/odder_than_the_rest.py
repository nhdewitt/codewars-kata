"""
Create a method that takes an array/list as an input, and outputs the index at which the sole odd number is located.

This method should work with arrays with negative numbers. If there are no odd numbers in the array, then the method should output -1.

Examples:

odd_one([2,4,6,7,10]) # => 3
odd_one([2,16,98,10,13,78]) # => 4
odd_one([4,-8,98,-12,-7,90,100]) # => 4
odd_one([2,4,6,8]) # => -1

https://www.codewars.com/kata/5983cba828b2f1fd55000114/train/python
"""

def odd_one(arr):
    return [i % 2 for i in arr].index(1) if [i % 2 for i in arr].count(1) > 0 else -1