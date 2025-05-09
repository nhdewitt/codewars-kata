"""
Mothers arranged a dance party for the children in school. At that party, there are only mothers and their children. All are having great fun on the dance floor when suddenly all the lights went out. It's a dark night and no one can see each other. But you were flying nearby and you can see in the dark and have ability to teleport people anywhere you want.

Legend:
-Uppercase letters stands for mothers, lowercase stand for their children, i.e. "A" mother's children are "aaaa".
-Function input: String contains only letters, uppercase letters are unique.
Task:
Place all people in alphabetical order where Mothers are followed by their children, i.e. "aAbaBb" => "AaaBbb".

https://www.codewars.com/kata/58539230879867a8cd00011c/train/python
"""

def find_children(dancing_brigade):
    parents = sorted(list(filter(lambda x: x.isupper(), dancing_brigade)))
    children = sorted(list(filter(lambda x: x.islower(), dancing_brigade)))
    
    return "".join([c + c.lower() * children.count(c.lower()) for c in parents])