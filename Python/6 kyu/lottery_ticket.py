"""
Time to win the lottery!

Given a lottery ticket (ticket), represented by an array of 2-value arrays, you must find out if you've won the jackpot.

Example ticket:

[ [ 'ABC', 65 ], [ 'HGR', 74 ], [ 'BYHT', 74 ] ]
To do this, you must first count the 'mini-wins' on your ticket. Each subarray has both a string and a number within it. If the character code of any of the characters in the string matches the number, you get a mini win. Note you can only have one mini win per sub array.

Once you have counted all of your mini wins, compare that number to the other input provided (win). If your total is more than or equal to (win), return 'Winner!'. Else return 'Loser!'.

All inputs will be in the correct format. Strings on tickets are not always the same length.

https://www.codewars.com/kata/57f625992f4d53c24200070e/train/python
"""

def bingo(ticket,win):
    winner = []
    for mini_win in ticket:
        if chr(mini_win[1]) in mini_win[0]:
            winner.append(1)
            
    return "Winner!" if winner.count(1) >= win else "Loser!"