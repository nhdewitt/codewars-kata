"""
Let's pretend your company just hired your friend from college and paid you a referral bonus. Awesome! To celebrate, you're taking your team out to the terrible dive bar next door and using the referral bonus to buy, and build, the largest three-dimensional beer can pyramid you can. And then probably drink those beers, because let's pretend it's Friday too.

A beer can pyramid will square the number of cans in each level - 1 can in the top level, 4 in the second, 9 in the next, 16, 25...

Complete the beeramid function to return the number of complete levels of a beer can pyramid you can make, given the parameters of:

your referral bonus, and

the price of a beer can

For example:

beeramid(1500, 2); // should === 12
beeramid(5000, 3); // should === 16

https://www.codewars.com/kata/51e04f6b544cf3f6550000c1/train/python
"""

from math import floor

def beeramid(bonus, price):
    if bonus <= 0:                                          # bonus = 0 means no beers could be purchased
        return 0
    total_beers = floor(bonus / price)                      # floor bonus / price to ensure a whole number value of beers
    low, high = 0, total_beers
    while low <= high:                                      # binary search
        mid = (low + high) // 2
        total = mid * (mid + 1) * (2 * mid + 1) // 6        # sum of squares: i(i+1)(2i+1)/6 <= N
        if total <= total_beers:
            low = mid + 1
        else:
            high = mid - 1
    
    return low - 1