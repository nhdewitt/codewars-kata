"""
Let's play a fun gambling game. A dreidel has four sides; here are the descriptions for each of them:

Nun - nothing happens
Gimel - you take the pot!
Hei - you take half the pot (rounded down)
Shin - you put a piece into the pot
So here's how we play. You, being a raging gambling addict, start with all of your hard earned coins - oy vei! The pot will also have some non-negative amount of coins when the game begins.

Complete the function that given an array of dreidel rolls, the number of coins in your account, and the number of coins in the pot, returns the number of coins left in your account after the last roll.

Notes:

you can have a negative amount at the end of the game, just like real gambling :)
my_coins and pot will always be non-negative
Examples
['Hei', 'Shin'], 10, 20  -->  19            # 10 + 20/2 - 1
['Hei', 'Hei'], 10, 20   -->  25            # 10 + 20/2 + 10/2
['Shin', 'Shin', 'Hei'], 10, 20  -->  19    # 10 - 1 - 1 + 22/2
['Nun', 'Nun', 'Shin', 'Gimel', 'Shin'], 10, 20  -->  29
10 + 0 + 0 - 1 + 21 - 1

https://www.codewars.com/kata/52b013920b1d45c8b4000355/train/python
"""

from math import floor

def gamble(rolls, my_coins, pot):
    for roll in rolls:
        half = floor(pot / 2)
        if roll == "Nun":
            pass
        elif roll == "Gimel":
            my_coins += pot
            pot = 0
        elif roll == "Hei":
            my_coins += half
            pot -= half
        elif roll == "Shin":
            my_coins -= 1
            pot += 1
    return my_coins