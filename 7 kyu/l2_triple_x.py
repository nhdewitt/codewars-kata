"""
Given a string, return true if the first instance of "x" in the string is immediately followed by the string "xx".

"abraxxxas" → true
"xoxotrololololololoxxx" → false
"softX kitty, warm kitty, xxxxx" → true
"softx kitty, warm kitty, xxxxx" → false
Note :

capital X's do not count as an occurrence of "x".
if there are no "x"'s then return false

https://www.codewars.com/kata/568dc69683322417eb00002c/train/python
"""

def triple_x(s):
    try:
        idx = s.index("x")
    except:
        return False
    return s[idx] == s[idx + 1] == s[idx + 2] if idx + 2 < len(s) else False