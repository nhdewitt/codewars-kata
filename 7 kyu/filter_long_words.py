"""
Write a function that takes a string and an an integer n as parameters and returns a list of all words that are longer than n.

Example:

* With input "The quick brown fox jumps over the lazy dog", 4
* Return ['quick', 'brown', 'jumps']

https://www.codewars.com/kata/5697fb83f41965761f000052/train/python
"""

def filter_long_words(sentence, n):
    match = []
    for s in sentence.split():
        if len(s) > n:
            match.append(s)
    
    return match