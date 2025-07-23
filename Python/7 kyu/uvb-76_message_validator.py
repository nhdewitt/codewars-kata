"""
Transmitted messages have always the same format like this:

MDZHB 01 213 SKIF 38 87 23 95
or

MDZHB 80 516 GANOMATIT 21 23 86 25
Message format consists of following parts:

Initial keyword "MDZHB";
Two groups of digits, 2 digits in first and 3 in second ones;
Some keyword of arbitrary length consisting only of uppercase letters;
Final 4 groups of digits with 2 digits in each group.
Your task is to write a function that can validate the correct UVB-76 message. Function should return true if message is in correct format and false otherwise.


https://www.codewars.com/kata/56445cc2e5747d513c000033/train/python
"""

def validate(message):
    parts = message.split()
    if len(parts) != 8:
        return False
    if parts[0] != "MDZHB":
        return False
    if not parts[1].isnumeric() or not parts[2].isnumeric():
        return False
    if len(parts[1]) != 2 or len(parts[2]) != 3:
        return False
    if not parts[3].isalpha() and not parts[3].isnumeric():
        return False
    if not parts[4].isnumeric() or not parts[5].isnumeric() or not parts[6].isnumeric() or not parts[7].isnumeric():
        return False
    if len(parts[4]) != 2 or len(parts[5]) != 2 or len(parts[6]) != 2 or len(parts[7]) != 2:
        return False
    return True