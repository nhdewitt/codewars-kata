"""
In this Kata, you will be given two numbers, a and b, and your task is to determine if the first number a is divisible by all the prime factors of the second number b. For example: solve(15,12) = False because 15 is not divisible by all the prime factors of 12 (which include2).

See test cases for more examples.

Good luck!

https://www.codewars.com/kata/59ec2d112332430ce9000005/train/python
"""

def solve(a,b):
    d = 2
    while d * d <= b:               # prime factorization, checking in place and short-circuiting if a is not divisible
        while (b % d) == 0:
            if a % d != 0:
                return False
            b //= d
        d += 1
    if b > 1:
        if a % b != 0:
            return False
    return True