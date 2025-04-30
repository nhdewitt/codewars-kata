"""
Story
The Pied Piper has been enlisted to play his magical tune and coax all the rats out of town.

But some of the rats are deaf and are going the wrong way!

Kata Task
How many deaf rats are there?

Legend
P = The Pied Piper
O~ = Rat going left
~O = Rat going right
Example
ex1 ~O~O~O~O P has 0 deaf rats

ex2 P O~ O~ ~O O~ has 1 deaf rat

ex3 ~O~O~O~OP~O~OO~ has 2 deaf rats

https://www.codewars.com/kata/598106cb34e205e074000031/train/python
"""

import re

def count_deaf_rats(town):
    rats = re.split('(P)', town)
    if len(rats) == 2:
        if len(rats[0]) != 0:
            deaf_left = re.findall(r'(?:~O|O~)', rats[0])
        else:
            deaf_right = re.findall(r'(?:~O|O~)', rats[1])
    else:
        deaf_left = re.findall(r'(?:~O|O~)', rats[0])
        deaf_right = re.findall(r'(?:~O|O~)', rats[2])
    
    return deaf_left.count("O~") + deaf_right.count("~O")