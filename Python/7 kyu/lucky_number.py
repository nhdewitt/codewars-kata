"""
###Lucky number

Write a function to find if a number is lucky or not. If the sum of all digits is 0 or multiple of 9 then the number is lucky.

1892376 => 1+8+9+2+3+7+6 = 36. 36 is divisible by 9, hence number is lucky.

Function will return true for lucky numbers and false for others.

https://www.codewars.com/kata/55afed09237df73343000042/train/python
"""

def num_sum(x):
    return sum(list(int(i) for i in str(x)))

def is_lucky(n):
    return num_sum(n) % 9 == 0 or num_sum(n) == 0