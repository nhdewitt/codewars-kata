"""
Task
You are given a string representing a number in binary. Your task is to delete all the unset bits in this string and return the corresponding number (after keeping only the '1's).

In practice, you should implement this function:

def eliminate_unset_bits(number):
Examples
eliminate_unset_bits("11010101010101") ->  255 (= 11111111)
eliminate_unset_bits("111") ->  7
eliminate_unset_bits("1000000") -> 1
eliminate_unset_bits("000") -> 0

https://www.codewars.com/kata/5a0d38c9697598b67a000041/train/python
"""

def eliminate_unset_bits(number):
    return int("".join([n for n in number if n == "1"]), 2) if number.count("1") > 0 else 0