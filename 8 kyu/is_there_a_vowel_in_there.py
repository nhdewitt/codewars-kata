"""
Given an array of numbers, check if any of the numbers are the character codes for lower case vowels (a, e, i, o, u).

If they are, change the array value to a string of that vowel.

Return the resulting array.

https://www.codewars.com/kata/57cff961eca260b71900008f/train/python
"""

vowel_dict = {
    97: "a",
    101: "e",
    105: "i",
    111: "o",
    117: "u"
}

def is_vow(inp):
    out = []
    for i in inp:
        if i in vowel_dict.keys():
            out.append(vowel_dict[i])
        else:
            out.append(i)
    
    return out