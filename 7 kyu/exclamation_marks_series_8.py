"""
Description:
Move all exclamation marks to the end of the sentence

Examples
"Hi!"          ---> "Hi!"
"Hi! Hi!"      ---> "Hi Hi!!"
"Hi! Hi! Hi!"  ---> "Hi Hi Hi!!!"
"Hi! !Hi Hi!"  ---> "Hi Hi Hi!!!"
"Hi! Hi!! Hi!" ---> "Hi Hi Hi!!!!"

https://www.codewars.com/kata/57fafd0ed80daac48800019f/train/python
"""

def remove(string : str) -> str:
    excl = string.count("!")
    return f"{string.replace('!','')}{'!' * excl}"