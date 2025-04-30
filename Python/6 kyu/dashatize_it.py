"""
Given an integer, return a string with dash '-' marks before and after each odd digit, but do not begin or end the string with a dash mark.

Ex:

274 -> '2-7-4'
6815 -> '68-1-5'

https://www.codewars.com/kata/58223370aef9fc03fd000071/train/python
"""

def dashatize(n):
    s = str(abs(n))
    result = []
    current_evens = ""
    
    for d in s:
        if int(d) % 2 == 0:
            current_evens += d
        else:
            if current_evens:
                result.append(current_evens)
                current_evens = ""
            result.append(d)
    
    if current_evens:
        result.append(current_evens)
    
    return "-".join(result)