"""
Quadratic (and Linear) Equation Solver
Write a function that solves a quadratic equation from a string input.

The input is a string in the format "a b c", where a, b, and c are real numbers (integers or floats).
Your task is to return real roots of the equation:

If a ≠ 0, solve the quadratic equation: a * x² + b * x + c = 0
If a = 0, solve the linear equation: b * x + c = 0
Input:
A string of three space-separated numbers: "a b c"
Output:
A list of real roots, sorted in ascending order.
If the equation has one real root, return a list with one element.
If the equation has no real roots, return an empty list.
Rules:
Roots should be returned as floats.
If the input represents a linear equation (i.e. a = 0), return the root if it exists.
If both a = 0, b = 0 and c ≠ 0, there are no solutions → return []
GARANTIERED THAT CASE a = b = c = 0 IS NOT PROVE
Examples:
solve("1 -3 2")       # → [1.0, 2.0]   (quadratic with two roots)
solve("1 2 1")        # → [-1.0]       (quadratic with one root)
solve("1 0 1")        # → []           (no real roots)

solve("0 2 -4")       # → [2.0]        (linear equation)
solve("0 0 5")        # → []           (no solution)
Notes:
Do not use external libraries like numpy or sympy.
You may assume that input is always a valid string of three real numbers.

https://www.codewars.com/kata/68526d1eba6bf8562fed1216/train/python
"""

from math import sqrt

def solve(equation: str) -> list:
    a, b, c = map(int, equation.split())
    if a == 0 and b == 0:
        return []
    if a != 0:
        d = ((b ** 2) - (4 * a * c))
        if d < 0:
            return []
        x1 = (-b - sqrt(d))/(2 * a)
        x2 = (-b + sqrt(d))/(2 * a)
        if d == 0:
            return [x1]
        return sorted([x1, x2])
    else:
        return [-(c / b)]