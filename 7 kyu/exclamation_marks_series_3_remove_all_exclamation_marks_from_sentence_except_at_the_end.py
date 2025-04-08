"""
Description:
Remove all exclamation marks from sentence except at the end.

Examples
"Hi!"     ---> "Hi!"
"Hi!!!"   ---> "Hi!!!"
"!Hi"     ---> "Hi"
"!Hi!"    ---> "Hi!"
"Hi! Hi!" ---> "Hi Hi!"
"Hi"      ---> "Hi"

https://www.codewars.com/kata/57faefc42b531482d5000123/train/python
"""

def remove(s):
    replaced = s.count("!") - s.rstrip("!").count("!")          # total count - count after removing from right = amount that need to be re-added on the return
    return f"{s.replace('!','')}{'!' * replaced}"