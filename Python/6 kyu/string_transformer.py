"""
Given a string, return a new string that has transformed based on the input:

Change case of every character, ie. lower case to upper case, upper case to lower case.
Reverse the order of words from the input.
Note: You will have to handle multiple spaces, and leading/trailing spaces.

For example:

"Example Input" ==> "iNPUT eXAMPLE"
You may assume the input only contain English alphabet and spaces.

https://www.codewars.com/kata/5878520d52628a092f0002d0/train/python
"""

import re

def change_case(string):
    if string.isspace():
        return string
    output = ""
    for s in string:
        if s == " ":
            output += s
        if s.isupper():
            output += s.lower()
        else:
            output += s.upper()
    
    return output

def string_transformer(s):
    split = re.split(r"(\s+)", s)
    
    return "".join([change_case(string) for string in split[::-1]])