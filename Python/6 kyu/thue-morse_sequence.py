"""
Given a positive integer n, return first n dgits of Thue-Morse sequence, as a string (see examples).

Thue-Morse sequence is a binary sequence with 0 as the first element. The rest of the sequence is obtained by adding the boolean (binary) complement of a group obtained so far.

For example:

0
01
0110
01101001
and so on...
alt

Ex.:

 1 --> "0"
 2 --> "01"
 5 --> "01101"
10 --> "0110100110"
You don't need to test if n is valid - it will always be a positive integer.
n will be between 1 and 10000
Thue-Morse on Wikipedia

Another kata on Thue-Morse by @myjinxin2015


https://www.codewars.com/kata/591aa1752afcb02fa300002a/train/python
"""

def thue_morse(n, seed="0"):
    if len(seed) >= n:
        return seed[:n]
    return thue_morse(n, seed + "".join("1" if b == "0" else "0" for b in seed))