"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"

https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python
"""

def to_camel_case(text):
    if not text:
        return ""
    text = text.replace("_"," ").replace("-", " ").split()
    return "".join([text[0]] + list(t.title() for t in text[1:]))