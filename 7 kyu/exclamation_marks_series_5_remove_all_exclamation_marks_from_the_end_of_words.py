"""
Task
Remove all exclamation marks from the end of words. Words are separated by a single space. There are no exclamation marks within a word.

Examples
remove("Hi!") === "Hi"
remove("Hi!!!") === "Hi"
remove("!Hi") === "!Hi"
remove("!Hi!") === "!Hi"
remove("Hi! Hi!") === "Hi Hi"
remove("!!!Hi !!hi!!! !hi") === "!!!Hi !!hi !hi"

https://www.codewars.com/kata/57faf32df815ebd49e000117/train/python
"""

def remove(st):
    return " ".join([c.rstrip("!") for c in st.split()])