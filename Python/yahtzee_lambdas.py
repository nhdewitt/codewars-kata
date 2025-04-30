"""
https://exercism.org/tracks/python/exercises/yacht/iterations
"""

YACHT = lambda x: 50 if len(set(x)) == 1 else 0
ONES = lambda x: 1 * x.count(1)
TWOS = lambda x: 2 * x.count(2)
THREES = lambda x: 3 * x.count(3)
FOURS = lambda x: 4 * x.count(4)
FIVES = lambda x: 5 * x.count(5)
SIXES = lambda x: 6 * x.count(6)
FULL_HOUSE = lambda x: sum(x) if len(set(x)) == 2 and x.count(x[0]) == 2 or x.count(x[0]) == 3 else 0
FOUR_OF_A_KIND = lambda x: 4 * x[0] if len(set(x)) <= 2 and x.count(x[0]) >= 4 else 4 * x[1] if len(set(x)) == 2 and x.count(x[1]) >= 4 else 0
LITTLE_STRAIGHT = lambda x: 30 if len(set(x)) == 5 and sum(x) == 15 else 0
BIG_STRAIGHT = lambda x: 30 if len(set(x)) == 5 and sum(x) == 20 else 0             # could shorten these two to if sorted(x) == [1,2,3,4,5] and if sorted(x) == [2,3,4,5,6], respectively
CHOICE = lambda x: sum(x)


def score(dice, category):
    return category(dice)