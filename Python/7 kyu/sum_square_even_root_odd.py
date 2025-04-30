"""
Complete the function that takes a list of numbers (nums), as the only argument to the function. Take each number in the list and square it if it is even, or square root the number if it is odd. Take this new list and return the sum of it, rounded to two decimal places.

The list will never be empty and will only contain values that are greater than or equal to zero.

Good luck!

https://www.codewars.com/kata/5a4b16435f08299c7000274f/train/python
"""

def sum_square_even_root_odd(nums):
    return round(sum([n ** 2 if n % 2 == 0 else n ** 0.5 for n in nums]), 2)