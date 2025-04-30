"""
Friday 13th or Black Friday is considered as unlucky day. Calculate how many unlucky days are in the given year.

Find the number of Friday 13th in the given year.

Input: Year in Gregorian calendar as integer.

Output: Number of Black Fridays in the year as an integer.

Examples:

unluckyDays(2015) == 3
unluckyDays(1986) == 1

https://www.codewars.com/kata/56eb0be52caf798c630013c0/train/python
"""

from datetime import datetime

def unlucky_days(year):
    black_fridays = []
    for i in range(1, 13):
        if datetime(year, i, 13).isoweekday() == 5:
            black_fridays.append(True)
        else:
            black_fridays.append(False)
    
    return black_fridays.count(1)