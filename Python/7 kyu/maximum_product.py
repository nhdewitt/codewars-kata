"""
Task
Given an array of integers , Find the maximum product obtained from multiplying 2 adjacent numbers in the array. Note that the array size is at least 2 and consists a mixture of positive, negative integers and also zeroes.

Examples
[1, 2, 3] returns 6 because the maximum product is obtained from multiplying 2∗3=6
[9, 5, 10, 2, 24, -1, -48] returns 50 because the maximum product is obtained from multiplying 5*10=50
[-23, 4, -5, 99, -27, 329, -2, 7, -921] returns -14 because the maximum product is obtained from multiplying -2*7=-14

https://www.codewars.com/kata/5a4138acf28b82aa43000117
 """

def adjacent_element_product(array):
    print(array)
    prod = float("-inf")
    for i, v in enumerate(array):
        if i == len(array) - 1:
            return prod
        if v * array[i + 1] > prod:
            prod = v * array[i + 1]