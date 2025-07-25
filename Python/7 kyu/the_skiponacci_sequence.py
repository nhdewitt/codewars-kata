"""
Your task is to generate the Fibonacci sequence to n places, with each alternating value as "skip". For example:

"1 skip 2 skip 5 skip 13 skip 34"

Return the result as a string

You can presume that n is always a positive integer between (and including) 1 and 64.


https://www.codewars.com/kata/580777ee2e14accd9f000165/train/python
"""

def skiponacci(n):
    if n == 1:
        return "1"
    fib = [1, 1]
    while len(fib) < n:
        fib.append(fib[-2] + fib[-1])
    return " ".join(str(v) if i % 2 == 0 else "skip" for i, v in enumerate(fib))