"""
Write a function that removes every lone 9 that is inbetween 7s.

"79712312" --> "7712312"
"79797"    --> "777"

https://www.codewars.com/kata/559f44187fa851efad000087/train/python
"""

def seven_ate9(str_):
    eaten = str_[0]
    for i in range(1, len(str_) - 1):
        if str_[i - 1] == "7" and str_[i] == "9" and str_[i + 1] == "7":
            continue
        else:
            eaten += str_[i]
    
    return eaten + str_[-1]