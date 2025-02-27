"""

Examples
Let's see some cases (input -> output):

1, 10  --> [1, 2, 3, 4, 5, 6, 7, 8, 9]
1, 100 --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
If there are no numbers of this kind in the range 
[
a
,
b
]
[a,b] the function should output an empty list.

90, 100 --> []
Enjoy it!!

https://www.codewars.com/kata/5626b561280a42ecc50000d1
"""

def is_eureka(num):
    num_str = str(num)
    total = 0
    for i, digit in enumerate(num_str):
        total += int(digit) ** (i + 1)
    return total == num

def sum_dig_pow(a, b):
    eureka_list = []
    for i in range(a, b + 1):
        if is_eureka(i):
            eureka_list.append(i)
    
    return eureka_list