"""
You get an array of arrays.
If you sort the arrays by their length, you will see, that their length-values are consecutive.
But one array is missing!


You have to write a method, that return the length of the missing array.

Example:
[[1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]] --> 3

If the array of arrays is null/nil or empty, the method should return 0.

When an array in the array is null or empty, the method should return 0 too!
There will always be a missing element and its length will be always between the given arrays.

Have fun coding it and please don't forget to vote and rank this kata! :-)

I have created other katas. Have a look if you like coding and challenges.

https://www.codewars.com/kata/57b6f5aadb5b3d0ae3000611/train/python
"""

def get_length_of_missing_array(array_of_arrays):
    if not array_of_arrays:                         # check initial array for None
        return 0
    res = []
    for array in array_of_arrays:
        if not array:                               # check each nested array for None, if not None, append the length
            return 0
        res.append(len(array))
    res.sort()                                      # sort by length
    i = 1
    while i < len(res):
        if res[i] - res[i - 1] != 1:                # find the missing length and return
            return res[i] - 1
        i += 1