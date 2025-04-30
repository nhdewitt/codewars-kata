"""
Strong number is a number with the sum of the factorial of its digits is equal to the number itself.

For example, 145 is strong, because 1! + 4! + 5! = 1 + 24 + 120 = 145.

Task
Given a positive number, find if it is strong or not, and return either "STRONG!!!!" or "Not Strong !!".

Examples
1 is a strong number, because 1! = 1, so return "STRONG!!!!".
123 is not a strong number, because 1! + 2! + 3! = 9 is not equal to 123, so return "Not Strong !!".
145 is a strong number, because 1! + 4! + 5! = 1 + 24 + 120 = 145, so return "STRONG!!!!".
150 is not a strong number, because 1! + 5! + 0! = 122 is not equal to 150, so return "Not Strong !!".

https://www.codewars.com/kata/5a4d303f880385399b000001/train/python
"""

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

def strong_num(number):
    string = str(number)
    fact_check = []
    for c in string:
        fact_check.append(fact(int(c)))
    total = sum(fact_check)
    
    return "STRONG!!!!" if total == number else "Not Strong !!"