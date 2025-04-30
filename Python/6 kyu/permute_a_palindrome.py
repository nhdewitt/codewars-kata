"""
Write a function that will check whether ANY permutation of the characters of the input string is a palindrome. Bonus points for a solution that is efficient and/or that uses only built-in language functions. Deem yourself brilliant if you can come up with a version that does not use any function whatsoever.

For this kata assume that all characters are lowercase.

Example
madam -> True
adamm -> True
junk -> False

Hint
The brute force approach would be to generate all the permutations of the string and check each one of them whether it is a palindrome. However, an optimized approach will not require this at all.

https://www.codewars.com/kata/58ae6ae22c3aaafc58000079/train/python
"""

def permute_a_palindrome(input):
    char_count = {}
    for c in input:
        char_count[c] = char_count.get(c, 0) + 1
    
    if len(input) % 2 == 0:
        return all(v % 2 == 0 for v in char_count.values())             # if the word is even length and all characters are even length, there is a palindromic permutation
    return sum(v % 2 != 0 for v in char_count.values()) == 1            # if it's odd length and at most one character is odd length, there is a palindromic permutation