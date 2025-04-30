"""
Round any given number to the closest 0.5 step

I.E.

solution(4.2) = 4
solution(4.3) = 4.5
solution(4.6) = 4.5
solution(4.8) = 5
Round up if number is as close to previous and next 0.5 steps.

solution(4.75) == 5

https://www.codewars.com/kata/51f1342c76b586046800002a/train/python
"""

def solution(n):
    whole, frac = str(n).split(".")
    whole = int(whole)
    frac = float(f"0.{frac}")
    return whole if frac < 0.25 else round(float(f"{whole}.5"), 1) if frac < 0.75 else whole + 1