"""
In your class, you have started lessons about geometric progression. Since you are also a programmer, you have decided to write a function that will print first n elements of the sequence with the given constant r and first element a.

Result should be separated by comma and space.

Example
geometric_sequence_elements(2, 3, 5) == '2, 6, 18, 54, 162'
More info: https://en.wikipedia.org/wiki/Geometric_progression

https://www.codewars.com/kata/55caef80d691f65cb6000040/train/python
"""

def geometric_sequence_elements(a, r, n):
    return ", ".join(list(map(str, (a * (r ** (i - 1)) for i in range(1, n + 1)))))