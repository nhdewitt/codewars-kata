"""
A normal deck of 52 playing cards contains suits 'H', 'C', 'D', 'S' - Hearts, Clubs, Diamonds, Spades respectively - and cards with values from Ace (1) to King (13): 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13

Your Task
Complete the function that returns a shuffled deck of 52 playing cards without repeats.

Each card should have format "{suit} {value}", e.g. the Queen of Hearts is "H 12" and the Ace of Spades is "S 1". The order of the cards must be different each time the function is called.

https://www.codewars.com/kata/5810ad962b321bac8f000178/train/python
"""

from random import shuffle

def shuffled_deck():
    hearts = {f"H {i}" for i in range(1, 14)}
    clubs = {f"C {i}" for i in range(1, 14)}
    diamonds = {f"D {i}" for i in range(1, 14)}
    spades = {f"S {i}" for i in range(1, 14)}
    
    deck = list(hearts | clubs | diamonds | spades)
    shuffle(deck)
    
    return deck