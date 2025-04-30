"""
This kata is about converting numbers to their binary or hexadecimal representation:

If a number is even, convert it to binary.
If a number is odd, convert it to hex.
Numbers will be positive. The hexadecimal string should be lowercased.

https://www.codewars.com/kata/583ade15666df5a64e000058/train/python
"""

def evens_and_odds(n):
    return bin(n)[2:] if n % 2 == 0 else hex(n)[2:]