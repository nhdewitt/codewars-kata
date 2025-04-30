"""
Make your strings more nerdy: Replace all 'a'/'A' with 4, 'e'/'E' with 3 and 'l' with 1 e.g. "Fundamentals" --> "Fund4m3nt41s"

https://www.codewars.com/kata/59e9f404fc3c49ab24000112/train/python
"""

def nerdify(txt):
    return txt.replace('a','4').replace('A','4').replace('e','3').replace('E','3').replace('l','1')