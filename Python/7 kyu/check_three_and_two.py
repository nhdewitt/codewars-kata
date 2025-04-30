"""
Given an array with exactly 5 strings "a", "b" or "c" (chars in Java, characters in Fortran, Chars in Haskell), check if the array contains three and two of the same values.

Examples
["a", "a", "a", "b", "b"] ==> true  // 3x "a" and 2x "b"
["a", "b", "c", "b", "c"] ==> false // 1x "a", 2x "b" and 2x "c"
["a", "a", "a", "a", "a"] ==> false // 5x "a"

https://www.codewars.com/kata/5a9e86705ee396d6be000091/train/python
"""

def check_three_and_two(array):
    return (array.count("a") == 3 or array.count("b") == 3 or array.count("c") == 3) and (array.count("a") == 2 or array.count("b") == 2 or array.count("c") == 2)