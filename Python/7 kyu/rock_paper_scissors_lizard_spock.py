"""
In this kata, your task is to implement an extended version of the famous rock-paper-scissors game. The rules are as follows:

Scissors cuts Paper
Paper covers Rock
Rock crushes Lizard
Lizard poisons Spock
Spock smashes Scissors
Scissors decapitates Lizard
Lizard eats Paper
Paper disproves Spock
Spock vaporizes Rock
Rock crushes Scissors
Task:
Given two values from the above game, return the Player result as "Player 1 Won!", "Player 2 Won!", or "Draw!".

Inputs
Values will be given as one of "rock", "paper", "scissors", "lizard", "spock".

https://www.codewars.com/kata/57d29ccda56edb4187000052/train/python
"""

def rpsls(pl1, pl2):
    if pl1 == pl2:
        return "Draw!"
    if pl1 == "scissors" and (pl2 == "paper" or pl2 == "lizard"):
        return "Player 1 Won!"
    if pl1 == "paper" and (pl2 == "rock" or pl2 == "spock"):
        return "Player 1 Won!"
    if pl1 == "rock" and (pl2 == "lizard" or pl2 == "scissors"):
        return "Player 1 Won!"
    if pl1 == "lizard" and (pl2 == "spock" or pl2 == "paper"):
        return "Player 1 Won!"
    if pl1 == "spock" and (pl2 == "scissors" or pl2 == "rock"):
        return "Player 1 Won!"
    
    return "Player 2 Won!"