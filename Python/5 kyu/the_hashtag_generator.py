"""
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
Examples
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false

https://www.codewars.com/kata/52449b062fb80683ec000024/train/python
"""

def generate_hashtag(s):
    if not s:
        return False
    words = f"#{''.join([w.title() for w in s.split()])}"       # split on whitespace, capitalize first letter of each word, join into a string with # at the front
    return words if len(words) <= 140 else False                # check if final string is greater than 140 before returning