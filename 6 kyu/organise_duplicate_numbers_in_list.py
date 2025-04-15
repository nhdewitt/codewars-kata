"""
Sam is an avid collector of numbers. Every time he finds a new number he throws it on the top of his number-pile. Help Sam organise his collection so he can take it to the International Number Collectors Conference in Cologne.

Given an array of numbers, your function should return an array of arrays, where each subarray contains all the duplicates of a particular number. Subarrays should be in the same order as the first occurence of the number they contain:

group([3, 2, 6, 2, 1, 3])
>>> [[3, 3], [2, 2], [6], [1]]
Assume the input is always going to be an array of numbers. If the input is an empty array, an empty array should be returned.

https://www.codewars.com/kata/5884b6550785f7c58f000047/train/python
"""

def group(arr):
    seen = set()                                                # use seen to track numbers that have already been captured
    organized = []
    for i in range(len(arr)):
        if arr[i] not in seen:
            seen.add(arr[i])
            organized.append([arr[i]] * arr.count(arr[i]))      # if number hasn't been added yet, add the total number of the element to the list, add to seen
    
    return organized