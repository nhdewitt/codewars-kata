"""
Given a mixed array of number and string representations of integers, add up the non-string integers and subtract the total of the string integers.

Return as a number.

https://www.codewars.com/kata/57eaec5608fed543d6000021/train/python
"""

def div_con(x):
    total = 0
    for element in x:
        if type(element) is int:
            total += element
        else:
            total -= int(element)
    
    return total