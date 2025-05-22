"""
Complete the function that

accepts two integer arrays of equal length
compares the value each member in one array to the corresponding member in the other
squares the absolute value difference between those two values
and returns the average of those squared absolute value difference between each member pair.
Examples
[1, 2, 3], [4, 5, 6]              -->   9   because (9 + 9 + 9) / 3
[10, 20, 10, 2], [10, 25, 5, -2]  -->  16.5 because (0 + 25 + 25 + 16) / 4
[-1, 0], [0, -1]                  -->   1   because (1 + 1) / 2


https://www.codewars.com/kata/51edd51599a189fe7f000015/train/python
"""

def solution(array_a, array_b):
    array_squared = []
    for i, _ in enumerate(array_a):
        array_squared.append((abs(array_a[i] - array_b[i]) ** 2))       # arrays are of even length, so we can just enumerate a and find abs of the corresponding b at i
    return sum(array_squared) / len(array_a)                            # square them, sum them and divide by the len to get the average