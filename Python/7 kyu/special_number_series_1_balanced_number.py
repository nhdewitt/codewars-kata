"""
A balanced number is a number where the sum of digits to the left of the middle digit(s) and the sum of digits to the right of the middle digit(s) are equal.

If the number has an odd number of digits, then there is only one middle digit. (For example, 92645 has one middle digit, 6.) Otherwise, there are two middle digits. (For example, the middle digits of 1301 are 3 and 0.)

The middle digit(s) should not be considered when determining whether a number is balanced or not, e.g. 413023 is a balanced number because the left sum and right sum are both 5.

The task
Given a number, find if it is balanced, and return the string "Balanced" or "Not Balanced" accordingly. The passed number will always be positive.

Examples
7 ==> return "Balanced"
Explanation:
middle digit(s): 7
sum of all digits to the left of the middle digit(s) -> 0
sum of all digits to the right of the middle digit(s) -> 0
0 and 0 are equal, so it's balanced.
295591 ==> return "Not Balanced"
Explanation:
middle digit(s): 55
sum of all digits to the left of the middle digit(s) -> 11
sum of all digits to the right of the middle digit(s) -> 10
11 and 10 are not equal, so it's not balanced.
959 ==> return "Balanced"
Explanation:
middle digit(s): 5
sum of all digits to the left of the middle digit(s) -> 9
sum of all digits to the right of the middle digit(s) -> 9
9 and 9 are equal, so it's balanced.
27102983 ==> return "Not Balanced"
Explanation:
middle digit(s): 02
sum of all digits to the left of the middle digit(s) -> 10
sum of all digits to the right of the middle digit(s) -> 20
10 and 20 are not equal, so it's not balanced.

https://www.codewars.com/kata/5a4e3782880385ba68000018/train/python
"""

def sum_of_digits(num):
    sum = 0
    for c in num:
        sum += int(c)
    
    return sum

def balanced_num(number):
    num_as_string = str(number)
    if len(num_as_string) <= 2:
        return "Balanced"
    if len(num_as_string) == 3:
        if int(num_as_string[0]) == int(num_as_string[-1]):
            return "Balanced"
        else:
            return "Not Balanced"
    half = len(num_as_string) // 2
    if len(num_as_string) % 2 == 0:
        left_half, right_half = num_as_string[0:half - 1], num_as_string[half + 1:]
    else:
        left_half, right_half = num_as_string[0:half], num_as_string[half + 1:]
    
    return "Balanced" if sum_of_digits(left_half) == sum_of_digits(right_half) else "Not Balanced"