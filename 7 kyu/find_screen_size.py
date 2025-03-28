"""
Cheesy Cheeseman just got a new monitor! He is happy with it, but he just discovered that his old desktop wallpaper no longer fits. He wants to find a new wallpaper, but does not know which size wallpaper he should be looking for, and alas, he just threw out the new monitor's box. Luckily he remembers the width and the aspect ratio of the monitor from when Bob Mortimer sold it to him. Can you help Cheesy out?

The Challenge
Given an integer width and a string ratio written as WIDTH:HEIGHT, output the screen dimensions as a string written as WIDTHxHEIGHT.

Note: The calculated height should be represented as an integer. If the height is fractional, truncate it.

https://www.codewars.com/kata/5bbd279c8f8bbd5ee500000f/solutions/python
"""

def find_screen_height(width, ratio): 
    return f"{width}x{int(int(width) * (int(ratio.split(':')[1]) / int(ratio.split(':')[0])))}"