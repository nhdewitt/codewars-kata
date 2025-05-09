"""
Write a function, factory, that takes a number as its parameter and returns another function.

The returned function should take an array of numbers as its parameter, and return an array of those numbers multiplied by the number that was passed into the first function.

In the example below, 5 is the number passed into the first function. So it returns a function that takes an array and multiplies all elements in it by five.

Translations and comments (and upvotes) welcome!

Example
fives = factory(5)          # returns a function - fives
my_array = [1, 2, 3]
fives(my_array)             # returns [5, 10, 15]

https://www.codewars.com/kata/563f879ecbb8fcab31000041/train/python
"""

def factory(x):
    def inner(l):
        return [e * x for e in l]
    return inner