"""
Write a method (or function, depending on the language) that converts a string to camelCase, that is, all words must have their first letter capitalized and spaces must be removed.

Examples (input --> output):
"hello case" --> "HelloCase"
"camel case word" --> "CamelCaseWord"
Don't forget to rate this kata! Thanks :)

https://www.codewars.com/kata/587731fda577b3d1b0001196/train/python
"""

def camel_case(s):
    return "".join(t.title() for t in s.split())        # not camelCase :|