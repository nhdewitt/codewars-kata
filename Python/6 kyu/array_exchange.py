"""
Array Exchange and Reversing

It's time for some array exchange! The objective is simple: exchange the elements of two arrays in-place in a way that their new content is also reversed. The arrays may be of unequal lengths, in which case you will have to expand the shorter one in-place.

# before
my_array = ['a', 'b', 'c']
other_array = [1, 2, 3]

exchange_arrays(my_array, other_array)

# after
my_array == [3, 2, 1]
other_array == ['c', 'b', 'a']

https://www.codewars.com/kata/5353212e5ee40d4694001114/train/python
"""

def exchange_with(a, b):
    temp_a, temp_b = a[:], b[:]
    
    a[:], b[:] = temp_b[::-1], temp_a[::-1]