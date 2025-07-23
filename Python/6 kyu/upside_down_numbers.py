"""
Consider the numbers 6969 and 9116. When you rotate them 180 degrees (upside down), these numbers remain the same. To clarify, if we write them down on a paper and turn the paper upside down, the numbers will be the same. Try it and see! Some numbers such as 2 or 5 don't yield numbers when rotated.

Given a range, return the count of upside down numbers within that range. For example, solve(0,10) = 3, because there are only 3 upside down numbers >= 0 and < 10. They are 0, 1, 8.

More examples in the test cases.

Good luck!

If you like this Kata, please try

Simple Prime Streaming

Life without primes

Please also try the performance version of this kata at Upside down numbers - Challenge Edition


https://www.codewars.com/kata/59f7597716049833200001eb/train/python
"""

def upside_down(n):
    if n < 10:
        return n in (0, 1, 8)
    parsed = str(n)
    if parsed[-1] == "0":
        return False
    
    upside_down_map = {
    "0": "0",
    "1": "1",
    "8": "8",
    "6": "9",
    "9": "6",
    }
    
    p, q = 0, len(parsed) - 1
    while p <= q:
        if upside_down_map.get(parsed[p]) != parsed[q]:
            return False
        p += 1
        q -= 1
    return True
        
def solve(a, b):
    return sum(upside_down(i) for i in range(a, b))