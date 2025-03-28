"""
Finding your seat on a plane is never fun, particularly for a long haul flight... You arrive, realise again just how little leg room you get, and sort of climb into the seat covered in a pile of your own stuff.

To help confuse matters (although they claim in an effort to do the opposite) many airlines omit the letters 'I' and 'J' from their seat naming system.

the naming system consists of a number (in this case between 1-60) that denotes the section of the plane where the seat is (1-20 = front, 21-40 = middle, 41-60 = back). This number is followed by a letter, A-K with the exclusions mentioned above.

Letters A-C denote seats on the left cluster, D-F the middle and G-K the right.

Given a seat number, your task is to return the seat location in the following format:

'2B' would return 'Front-Left'.

If the number is over 60, or the letter is not valid, return 'No Seat!!'.

https://www.codewars.com/kata/57e8f757085f7c7d6300009a/train/python
"""

def plane_seat(a):
    section, seat = int(a[:-1]), ord(a[-1])
    if section > 60 or (73 <= seat <= 74):
        return "No Seat!!"
    if section <= 20:
        section = "Front"
    elif section <= 40:
        section = "Middle"
    else:
        section = "Back"
    if 65 <= seat <= 67:
        seat = "Left"
    elif 68 <= seat <= 70:
        seat = "Middle"
    else:
        seat = "Right"
    return f"{section}-{seat}"