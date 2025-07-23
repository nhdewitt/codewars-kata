"""
Your job is to fix the parentheses so that all opening and closing parentheses (brackets) have matching counterparts. You will do this by appending parenthesis to the beginning or end of the string. The result should be of minimum length. Don't add unnecessary parenthesis.

The input will be a string of varying length, only containing '(' and/or ')'.

For example:

Input: ")("
Output: "()()"

Input: "))))(()("
Output: "(((())))(()())"
Enjoy!


https://www.codewars.com/kata/5d8365b570a6f6001519ecc8/train/python
"""

def fix_parentheses(strng):
    end, front = 0, 0
    for s in strng:
        if s == '(':
            end += 1
        elif s == ')':
            if end > 0:
                end -= 1
            else:
                front += 1
    return '(' * front + strng + ')' * end