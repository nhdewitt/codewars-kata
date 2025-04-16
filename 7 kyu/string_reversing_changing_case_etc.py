"""
Given 2 string parameters, show a concatenation of:

the reverse of the 2nd string with inverted case; e.g Fish -> HSIf
a separator in between both strings: @@@
the 1st string reversed with inverted case and then mirrored; e.g Water -> RETAwwATER 
** Keep in mind that this kata was initially designed for Shell, I'm aware it may be easier in other languages.**

https://www.codewars.com/kata/58305403aeb69a460b00019a/train/python
"""

def reverse_and_mirror(s1, s2):
    new_s2 = "".join(s.upper() if s.islower() else s.lower() for s in s2[::-1])
    new_s1 = "".join(s.upper() if s.islower() else s.lower() for s in s1[::-1])
    
    return f"{new_s2}@@@{new_s1}{new_s1[::-1]}"