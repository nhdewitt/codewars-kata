"""
Create a function that takes in the sum and age difference of two people, calculates their individual ages, and returns a pair of values (oldest age first) if those exist or null/None or {-1, -1} in C if:

sum < 0
difference < 0
Either of the calculated ages come out to be negative

https://www.codewars.com/kata/58e0bd6a79716b7fcf0013b1/train/python
"""

def get_ages(sum_, difference):
    if sum_ < 0 or difference < 0:
        return None
    high, low = (round((sum_ / 2) + (difference / 2), 1), round((sum_ / 2) - (difference / 2), 1))
    if high < 0 or low < 0:
        return None
    return (high, low)