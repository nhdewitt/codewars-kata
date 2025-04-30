"""
In this kata, you need to write a function that takes a string and a letter as input and then returns the index of the second occurrence of that letter in the string. If there is no such letter in the string, or if the letter occurs only once in the string, -1 should be returned.

Examples:

for inputs  "Hello world!!!", 'l'  ->  return 3
for inputs  "Hello world!!!", 'A'  ->  return -1
Good luck ;) And don't forget to rate this kata if you liked it.

https://www.codewars.com/kata/63f96036b15a210058300ca9/train/python
"""

def second_symbol(s, symbol):
    if s.count(symbol) < 2:
        return -1
    i = 0
    sym_count = 0
    for c in s:
        if c == symbol:
            sym_count += 1
            if sym_count == 2:
                return i
        i += 1