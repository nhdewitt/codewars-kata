"""
This is the simple version of Shortest Code series. If you need some challenges, please try the challenge version.

Task:
Find out "B"(Bug) in a lot of "A"(Apple).

There will always be one bug in apple, not need to consider the situation that without bug or more than one bugs.

input: string Array apple

output: Location of "B", [x,y


https://www.codewars.com/kata/56fe97b3cc08ca00e4000dc9/train/python
"""

def sc(apple):
    for row, i in enumerate(apple):
        for col, v in enumerate(apple[row]):
            if v == 'B':
                return (row, col)