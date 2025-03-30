"""
In this kata, your job is to create a class Dictionary which you can add words to and their entries. Example:

>>> d = Dictionary()

>>> d.newentry('Apple', 'A fruit that grows on trees')

>>> print(d.look('Apple'))
A fruit that grows on trees

>>> print(d.look('Banana'))
Can't find entry for Banana
Good luck and happy coding!

https://www.codewars.com/kata/57a93f93bb9944516d0000c1/train/python
"""

class Dictionary():
    def __init__(self):
        self.words = []
        
    def newentry(self, word, definition):
        if word not in self.words:
            self.words.append((word, definition))
        
    def look(self, key):
        for word in self.words:
            if word[0] == key:
                return word[1]
        return f"Can't find entry for {key}"