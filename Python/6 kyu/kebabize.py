"""Modify the kebabize function so that it converts a camel case string into a kebab case.

"camelsHaveThreeHumps"  -->  "camels-have-three-humps"
"camelsHave3Humps"  -->  "camels-have-humps"
"CAMEL"  -->  "c-a-m-e-l"
Notes:

the returned string should only contain lowercase letters

https://www.codewars.com/kata/57f8ff867a28db569e000c4a/train/python
"""

from string import ascii_uppercase, digits

def kebabize(st):
    kebab = ""
    for c in st:
        if c in ascii_uppercase:
            kebab += f"-{c.lower()}"
        elif c in digits:
            continue
        else:
            kebab += c
    
    return kebab.strip("-")