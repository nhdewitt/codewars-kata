"""
Pine's grandma is hearing impaired: whatever you say to her, she responds with "HUH?! SPEAK UP, SONNY!", unless you shout it (type in all capitals).

If you shout, she can hear you (or at least she thinks so) and yells back, "NO, NOT SINCE 1938!" You can't stop talking to grandma until you shout "BYE".

When you shout "BYE", grandma shouts back "OK, BYE!" and end the conversation.

Your input is an array with a list of strings with all the words/sentences you say in order
You can expect there is aways a "BYE", although it is not necessarily the last word in the list
Your output is an array with a list of strings and every sentence Pine's grandma replies
Words/sentences are always a string
Example
["hi grandma", "WHAT", "bye", "BYE"]  -->
["HUH?! SPEAK UP, SONNY!", "NO, NOT SINCE 1938!", "HUH?! SPEAK UP, SONNY!", "OK, BYE!"]
Based, inspired and stolen with love from Learn to Program, by Chris Pine

https://www.codewars.com/kata/572b82bf4903c13b1b001079/train/python
"""

def deaf_grandma(you):
    output = []
    for y in you:
        if y == "BYE":
            output.append("OK, BYE!")                       # break condition, exit the loop and return
            return output
        if all(c.isupper() for c in y if c.isalpha()):      # ignore punctuation (could just do y.isupper() here)
            output.append("NO, NOT SINCE 1938!")
        else:
            output.append("HUH?! SPEAK UP, SONNY!")