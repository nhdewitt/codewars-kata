"""
Your job at E-Corp is both boring and difficult. It isn't made any easier by the fact that everyone constantly wants to have a meeting with you, and that the meeting rooms are always taken!

In this kata, you will be given an array. Each value represents a meeting room. Your job? Find the first empty one and return its index (N.B. There may be more than one empty room in some test cases).

'X' --> busy
'O' --> empty
If all rooms are busy, return "None available!"

https://www.codewars.com/kata/57f604a21bd4fe771b00009c/train/python
"""

def meeting(rooms):
    return rooms.index("O") if "O" in rooms else "None available!"