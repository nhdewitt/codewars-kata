"""
Background
You're modelling the interaction between a large number of quarks and have decided to create a Quark class so you can generate your own quark objects.

Quarks are fundamental particles and the only fundamental particle to experience all four fundamental forces.

Your task
Your Quark class should allow you to create quarks of any valid color ("red", "blue", and "green") and any valid flavor ('up', 'down', 'strange', 'charm', 'top', and 'bottom').

Every quark has the same baryon_number (BaryonNumber in C#): 1/3.

Every quark should have an .interact() (.Interact() in C#) method that allows any quark to interact with another quark via the strong force. When two quarks interact they exchange colors.

Example
>>> q1 = Quark("red", "up")
>>> q1.color
"red"
>>> q1.flavor
"up"
>>> q2 = Quark("blue", "strange")
>>> q2.color
"blue"
>>> q2.baryon_number
0.3333333333333333
>>> q1.interact(q2)
>>> q1.color
"blue"
>>> q2.color
"red"

https://www.codewars.com/kata/5882b052bdeafec15e0000e6/train/python
"""

class Quark(object):
    def __init__(self, color, flavor):
        if color in ["red", "blue", "green"]:
            self.color = color
        else:
            self.color = None
        if flavor in ["up", "down", "strange", "charm", "top", "bottom"]:
            self.flavor = flavor
        else:
            self.flavor = None
        self.baryon_number = 1/3
    
    def interact(self, other_quark):
        self.color, other_quark.color = other_quark.color, self.color