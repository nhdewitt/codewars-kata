"""
1, 246, 2, 123, 3, 82, 6, 41 are the divisors of number 246.

Squaring these divisors we get: 1, 60516, 4, 15129, 9, 6724, 36, 1681.

The sum of these squares is 84100 which is 290 * 290.

Task
Find all integers between m and n (m and n are integers with 1 <= m <= n) such that the sum of their squared divisors is itself a square.

We will return an array of subarrays or of tuples (in C an array of Pair) or a string.

The subarrays (or tuples or Pairs) will have two elements: first the number the squared divisors of which is a square and then the sum of the squared divisors.

Example:
m =  1, n = 250 --> [[1, 1], [42, 2500], [246, 84100]]
m = 42, n = 250 --> [[42, 2500], [246, 84100]]
The form of the examples may change according to the language, see "Sample Tests".

Note
In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing whitespace: you can use dynamically allocated character strings.

https://www.codewars.com/kata/55aa075506463dac6600010d/train/python
"""

from math import sqrt

def get_divisors(x):
    divisors = []
    for i in range(1, int(sqrt(x)) + 1):
        if x % i == 0:
            divisors.append(i)
            if i != x // i:
                divisors.append(x // i)
    divisors.sort()
    
    return [d ** 2 for d in divisors]

def is_perfect_square(n):
    return (int(sqrt(n)) * int(sqrt(n))) == n

def list_squared(m, n):
    divisors = []
    for i in range(m, n + 1):
        j = sum(get_divisors(i))
        if is_perfect_square(j):
            divisors.append([i, j])
    j = sum
    
    return divisors