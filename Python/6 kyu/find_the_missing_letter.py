"""
Find the missing letter
Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'
(Use the English alphabet with 26 letters!)

Have fun coding it and please don't forget to vote and rank this kata! :-)

I have also created other katas. Take a look if you enjoyed this kata!

https://www.codewars.com/kata/5839edaa6754d6fec10000a2/train/python
"""

def find_missing_letter(chars):
    for i in range(len(chars)):
        if chr(ord(chars[i]) + 1) != chr(ord(chars[i + 1])):
            return chr(ord(chars[i]) + 1)