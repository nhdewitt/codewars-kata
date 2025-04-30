"""
Task
Given an array of integers , Find the minimum sum which is obtained from summing each Two integers product .

Notes
Array/list will contain positives only .
Array/list will always have even size
Input >> Output Examples
minSum({5,4,2,3}) ==> return (22) 
Explanation:
The minimum sum obtained from summing each two integers product ,  5*2 + 3*4 = 22
minSum({12,6,10,26,3,24}) ==> return (342)
Explanation:
The minimum sum obtained from summing each two integers product ,  26*3 + 24*6 + 12*10 = 342
minSum({9,2,8,7,5,4,0,6}) ==> return (74)
Explanation:
The minimum sum obtained from summing each two integers product ,  9*0 + 8*2 +7*4 +6*5 = 74

https://www.codewars.com/kata/5a523566b3bfa84c2e00010b
"""

from math import prod

def min_sum(arr):
    sorted_arr = sorted(arr)
    first_elements = sorted_arr[:len(sorted_arr) // 2]
    last_elements = sorted_arr[len(sorted_arr) // 2:][::-1]
    zipped = zip(first_elements, last_elements)
    total = 0
    for z in zipped:
        total += prod(z)
    
    return total