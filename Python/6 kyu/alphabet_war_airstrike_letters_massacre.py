"""
Introduction
There is a war...between alphabets!
There are two groups of hostile letters. The tension between left side letters and right side letters was too high and the war began. The letters called airstrike to help them in war - dashes and dots are spread throughout the battlefield. Who will win?

Task
Write a function that accepts a fight string which consists of only small letters and * which represents a bomb drop place. Return who wins the fight after bombs are exploded. When the left side wins return Left side wins!, and when the right side wins return Right side wins!. In other cases, return Let's fight again!.

The left side letters and their power:

 w - 4
 p - 3 
 b - 2
 s - 1
The right side letters and their power:

 m - 4
 q - 3 
 d - 2
 z - 1
The other letters don't have power and are only victims.
The * bombs kill the adjacent letters ( i.e. aa*aa => a___a, **aa** => ______ );

Example (Input --> Output)
"s*zz"           --> "Right side wins!"
"*zd*qm*wp*bs*"  --> "Let's fight again!"
"zzzz*s*"        --> "Right side wins!"
"www*www****z"   --> "Left side wins!"

https://www.codewars.com/kata/5938f5b606c3033f4700015a/train/python
"""

left_chars = {
    'w': 4,
    'p': 3,
    'b': 2,
    's': 1
}

right_chars = {
    'm': 4,
    'q': 3,
    'd': 2,
    'z': 1
}

def alphabet_war(fight):
    fight = list(c for c in fight)
    for i, c in reversed(list(enumerate(fight))):
        if c == "*":
            if i > 0:
                fight[i - 1] = '_'
            if i < len(fight) - 1:
                fight[i + 1] = '_'
    left, right = 0, 0
    for c in fight:
        if c in left_chars.keys():
            left += left_chars[c]
        elif c in right_chars.keys():
            right += right_chars[c]
    
    return "Right side wins!" if right > left else "Left side wins!" if left > right else "Let's fight again!"