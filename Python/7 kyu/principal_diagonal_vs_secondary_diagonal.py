"""
Principal Diagonal -- The principal diagonal in a matrix identifies those elements of the matrix running from North-West to South-East.

Secondary Diagonal -- the secondary diagonal of a matrix identifies those elements of the matrix running from North-East to South-West.

For example:

matrix:             [1, 2, 3]
                    [4, 5, 6]
                    [7, 8, 9]

principal diagonal: [1, 5, 9]
secondary diagonal: [3, 5, 7]
Task
Your task is to find which diagonal is "larger": which diagonal has a bigger sum of their elements.

If the principal diagonal is larger, return "Principal Diagonal win!"
If the secondary diagonal is larger, return "Secondary Diagonal win!"
If they are equal, return "Draw!"
Note: You will always receive matrices of the same dimension.

https://www.codewars.com/kata/5a8c1b06fd5777d4c00000dd/train/python
"""

def diagonal(matrix):
    principal, secondary = [], []
    
    x, y = 0, 0
    while x < len(matrix[0]):
        principal.append(matrix[x][y])
        x = y = y + 1
    x = len(matrix) - 1
    y = 0
    while y < len(matrix[0]):
        secondary.append(matrix[x][y])
        x -= 1
        y += 1
    
    return "Principal Diagonal win!" if sum(principal) > sum(secondary) else "Secondary Diagonal win!" if sum(secondary) > sum(principal) else "Draw!"