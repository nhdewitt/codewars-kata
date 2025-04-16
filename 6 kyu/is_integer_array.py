"""
Write a function that:

returns true  / True if every element in an array is an integer or a float with no decimals.
returns true  / True if array is empty.
returns false / False for every other input.

https://www.codewars.com/kata/52a112d9488f506ae7000b95/train/python
"""

def is_int_array(arr):
    try:
        return sum([int(a) == a for a in arr]) == len(arr) if isinstance(arr, list) else False          # int(a) == a if float = x.0, if input not list it must be False
    except:
        return False                                                                                    # exception on input of True