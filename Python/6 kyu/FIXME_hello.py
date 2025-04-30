"""
The code provided has a method hello which is supposed to show only those attributes which have been explicitly set. Furthermore, it is supposed to say them in the same order they were set.

But it's not working properly.

Notes
There are 3 attributes

name
age
sex ('M' or 'F')
When the same attribute is assigned multiple times the hello method shows it only once. If this happens the order depends on the first assignment of that attribute, but the value is from the last assignment.

Examples
Hello.
Hello. My name is Bob. I am 27. I am male.
Hello. I am 27. I am male. My name is Bob.
Hello. My name is Alice. I am female.
Hello. My name is Batman.
Task
Fix the code so we can all go home early.

https://www.codewars.com/kata/5b0a80ce84a30f4762000069/train/python
"""

class Dinglemouse(object):
    
    def __init__(self):
        self.name = None
        self.sex  = None
        self.age  = None
        self.attrib_order = []                          # Hold the order in which attributes are set
    
    def setAge(self, age):
        self.age = age
        if 'A' not in self.attrib_order:                # For each attrib, if it's not been set, add it to the order for output. In either case, replace the value.
            self.attrib_order.append('A')
        return self
        
    def setSex(self, sex):
        self.sex = sex
        if 'S' not in self.attrib_order:
            self.attrib_order.append('S')
        return self
        
    def setName(self, name):
        self.name = name
        if 'N' not in self.attrib_order:
            self.attrib_order.append('N')
        return self
        
    def hello(self):
        output = ["Hello."]                                                             # Default case
        for attrib in self.attrib_order:                                                # Adds in order attribute was first set
            if attrib == 'A':
                output.append(f"I am {self.age}.")
            elif attrib == 'S':
                output.append(f"I am {'male' if self.sex == 'M' else 'female'}.")
            elif attrib == 'N':
                output.append(f"My name is {self.name}.")
        
        return " ".join(output)