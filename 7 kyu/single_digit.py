"""
The goal of this Kata is to reduce the passed integer to a single digit (if not already) by converting the number to binary, taking the sum of the binary digits, and if that sum is not a single digit then repeat the process.

If the passed integer is already a single digit there is no need to reduce
n will be an integer such that 0 < n < 10^20
For example given 5665 the function should return 5:

5665 --> (binary) 1011000100001
1011000100001 --> (sum of binary digits) 5
Given 123456789 the function should return 1:

123456789 --> (binary) 111010110111100110100010101
111010110111100110100010101 --> (sum of binary digits) 16
16 --> (binary) 10000
10000 --> (sum of binary digits) 1

https://www.codewars.com/kata/5a7778790136a132a00000c1/train/python
"""

def single_digit(n):
    if n < 9: return n
    b = bin(n)[2:]
    ck = b.count("1")
    while ck > 9:
        b = bin(ck)[2:]
        ck = b.count("1")
    return ck