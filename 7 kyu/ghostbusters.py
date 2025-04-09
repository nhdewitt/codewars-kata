"""
Oh no! Ghosts have reportedly swarmed the city. It's your job to get rid of them and save the day!

In this kata, strings represent buildings while whitespaces within those strings represent ghosts.

So what are you waiting for? Return the building(string) without any ghosts(whitespaces)!

Example:

"Sky scra per" -> "Skyscraper"
If the building contains no ghosts, return the string:

"You just wanted my autograph didn't you?"

https://www.codewars.com/kata/5668e3800636a6cd6a000018/train/python
"""

def ghostbusters(building):
    return "You just wanted my autograph didn't you?" if building.count(" ") == 0 else "".join(building.split())