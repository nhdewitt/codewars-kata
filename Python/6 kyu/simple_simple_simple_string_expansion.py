"""
Given a string that includes alphanumeric characters ("3a4B2d") return the expansion of that string: The numeric values represent the occurrence of each letter preceding that numeric value. There should be no numeric characters in the final string.

Notes
The first occurrence of a numeric value should be the number of times each character behind it is repeated, until the next numeric value appears
If there are multiple consecutive numeric characters, only the last one should be used (ignore the previous ones)
Empty strings should return an empty string.
Your code should be able to work for both lower and capital case letters.

"3D2a5d2f"  -->  "DDDaadddddff"    # basic example: 3 * "D" + 2 * "a" + 5 * "d" + 2 * "f"
"3abc"      -->  "aaabbbccc"       # not "aaabc", nor "abcabcabc"; 3 * "a" + 3 * "b" + 3 * "c"
"3d332f2a"  -->  "dddffaa"         # multiple consecutive digits: 3 * "d" + 2 * "f" + 2 * "a"
"abcde"     -->  "abcde"           # no digits
"1111"      -->  ""                # no characters to repeat
""          -->  ""                # empty string

https://www.codewars.com/kata/5ae326342f8cbc72220000d2/train/python
"""

import re

def string_expansion(s):
    exp = ""
    sp = re.split(r"(\d+)", s)
    sp = [int(item[-1]) if item.isdigit() else item for item in sp if item]
    i = 0
    while i < len(sp):
        if type(sp[i]) == int:
            if i == len(sp) - 1:
                break
            if len(sp[i + 1]) > 1:
                for j in range(len(sp[i + 1])):
                    exp += f"{sp[i + 1][j] * sp[i]}"
            else:
                exp += f"{sp[i + 1] * sp[i]}"
            i += 2
        else:
            exp += f"{sp[i]}"
            i += 1
    return exp