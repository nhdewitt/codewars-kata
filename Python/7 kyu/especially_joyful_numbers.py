"""
Positive integers that are divisible exactly by the sum of their digits are called Harshad numbers. The first few Harshad numbers are: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 18, ...

We are interested in Harshad numbers where the product of its digit sum s and s with the digits reversed, gives the original number n. For example consider number 1729:

its digit sum, s = 1 + 7 + 2 + 9 = 19
reversing s = 91
and 19 * 91 = 1729 --> the number that we started with.
Complete the function which tests if a positive integer n is Harshad number, and returns True if the product of its digit sum and its digit sum reversed equals n; otherwise return False.

https://www.codewars.com/kata/570523c146edc287a50014b1/train/python
"""

def number_joy(n):
    s = sum(int(j) for j in str(n))
    rev_s = int("".join(k for k in str(s)[::-1]))
    return s * rev_s == n