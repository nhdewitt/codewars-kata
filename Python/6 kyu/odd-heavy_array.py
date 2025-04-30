"""
An array of integers is defined to be odd-heavy if it contains at least one odd element and every odd number in it is greater than any even number in it.

Write a function that accepts an integer array and returns whether the array is odd-heavy.

Examples
Array [11,4,9,2,8] is odd-heavy,
because its odd elements [11,9] are greater than all the even elements [4,2,8]

Array [11,4,9,2,3,10] is not odd-heavy,
because one of its even elements (10 from [4,2,10]) is greater than two of
its odd elements (9 and 3 from [11,9,3])

Array [] is not odd-heavy,
because it does not contain any odd numbers

Array [3] is odd-heavy,
because it does not contain any even numbers.

https://www.codewars.com/kata/59c7e477dcc40500f50005c7/train/python
"""

def is_odd_heavy(arr):
    if not any(a % 2 != 0 for a in arr):                                                        # if no odd: False
        return False
    if not any(a % 2 == 0 for a in arr):                                                        # if no even: True
        return True
    return min(list(a for a in arr if a % 2 != 0)) > max(list(a for a in arr if a % 2 == 0))    # otherwise: if min of odds is > max of evens, True