"""
7 kyu
Hearts (Card Game) Kata 1 of 3
4389% of 49169p4songer
 Python
3.11
VIM
EMACS
Instructions
Output
This Kata is the first of three katas that I'm making on the game of hearts. We're getting started by simply scoring a hand, and working our way up to scoring a whole game!
In this Kata, your goal is to evaluate a single hand of hearts, and determine the winning card. Follow this link (https://gamerules.com/rules/hearts-card-game/) for more in depth rules, but the basic rules are as follows.

There are no "trump" cards in hearts. This means that the first card played will always win the hand if it is the only card of that suit.

EG: If Alex plays the two of clubs "2C" Bob plays the three of spades "3S" Chris plays the king of diamonds "KD" and Dave plays the two of hearts "2H" Alex wins that hand.

Card values are 2 as the lowest card and Ace as the highest card, following typical deck of cards order. There will be no duplicate cards given.

The return value of this function should be the winning card as a string, Case Sensitive

For the sake of this Kata, there are no other major rules that need to be followed. In other words, it does not matter if this is the first hand, or the last hand. All that matters is the value of the highest card in regard to the other rules. This is only for a 4-player game of hearts. No need for testing more or less players.

Here are a few examples of what a sucessful code would do. See other test cases for more in depth tests. A set of 50 random tests will be used before you can submit.

 The hand played (input) : ['10C', 'JC','AC', 'QC'] Everyone played in suit, so the highest card in this set wins. Output should be: 'AC'

The hand played (input) : ['4C', 'KH', 'QS', '10D'] Alex led with clubs. No one else played clubs, so Alex wins this hand even though everyone else's card is higher. Output should be: '4C'

The hand played (input) : ['9D', '9C', 'QD', '9S'] Only Alex and Chris played in suit. Of the two cards that are in suit, Chris' card is a higher value. Output should be: 'QD'.


https://www.codewars.com/kata/64d16a4d8a9c272bb4f3316c/train/python
"""

class Card:
    face_cards = {
        'J':  11,
        'Q':  12,
        'K':  13,
        'A':  14,
         11: 'J',
         12: 'Q',
         13: 'K',
         14: 'A',
    }
    
    def __init__(self, card: str):
        self.suit = card[-1]
        rank = card[:-1:]
        if rank.isnumeric():
            self.rank = int(rank)
        else:
            self.rank = self.face_cards[rank]
            
    def __str__(self):
        if self.rank <= 10:
            return f"{self.rank}{self.suit}"
        return f"{self.face_cards[self.rank]}{self.suit}"
            

def score_a_hand(cards):
    hands = [Card(card) for card in cards]
    trump_suit = hands[0].suit
    trump_rank = hands[0].rank
    
    for hand in hands[1:]:
        if hand.suit != trump_suit:
            continue
        if hand.rank > trump_rank:
            trump_rank = hand.rank
    
    return str(Card(f"{trump_rank}{trump_suit}"))