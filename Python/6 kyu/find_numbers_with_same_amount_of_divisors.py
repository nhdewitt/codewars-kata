"""
The integers 14 and 15 are contiguous (i.e. the difference between them is 1) and have the same number of divisors:

14 ----> 1, 2, 7, 14 # (4 divisors)
15 ----> 1, 3, 5, 15 # (4 divisors)
The next pair of contiguous integers with this property is 21 and 22:

21 -----> 1, 3,  7, 21 # (4 divisors)
22 -----> 1, 2, 11, 22 # (4 divisors)
We have 8 pairs of integers below 50 having this property, they are:

[ [2, 3], [14, 15], [21, 22], [26, 27], [33, 34], [34, 35], [38, 39], [44, 45] ]
Let's see now the integers that have a difference of 3 between them. There are 7 pairs below 100:

[ [2, 5], [35, 38], [55, 58], [62, 65], [74, 77], [82, 85], [91, 94] ]
Let's name:

diff, the difference between two integers, next and prev, (diff = next - prev)
nMax, an upper bound of the range.
We need a function that receives two integer parameters, diff and nMax, and outputs the count of pairs of integers that fulfill this property, all of them being strictly smaller than nMax.

So, for the examples detailed above:

(diff = 1, nMax =  50) -----> 8
(diff = 3, nMax = 100) -----> 7
Happy coding!!!

https://www.codewars.com/kata/55f1614853ddee8bd4000014/train/python
"""

from math import isqrt

def find_divisors(n):
    count = 0
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            count += 1 if i * i == n else 2
    return count

def count_pairs_int(diff, n_max):
    pairs = 0
    for i in range(1, n_max - diff):
        if find_divisors(i) == find_divisors(i + diff):
            pairs += 1

    return pairs