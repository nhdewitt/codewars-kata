"""
Definition
A Tidy Number is a number whose digits are in non-decreasing order.

Task
Given a number, determine if it is tidy or not.

Notes
The number passed will always be positive.
Return the result as a boolean.
Examples
12 ==> return true
Explanation: Digits {1, 2} are in non-decreasing order (1 <= 2).

32 ==> return false
Explanation: Digits {3, 2} are not in non-decreasing order (3 > 2).

1024 ==> return false
Explanation: Digits {1, 0, 2, 4} are not in non-decreasing order (1 > 0).

13579 ==> return true
Explanation: Digits {1, 3, 5, 7, 9} are in non-decreasing order.

2335 ==> return true
Explanation: Digits {2, 3, 3, 5} are in non-decreasing order (3 = 3).

https://www.codewars.com/kata/5a87449ab1710171300000fd/train/python
"""

def tidyNumber(n):
    str_n = str(n)
    for i, c in enumerate(str_n):
        if i == 0:
            continue
        if int(str_n[i]) < int(str_n[i - 1]):
            return False
    
    return True