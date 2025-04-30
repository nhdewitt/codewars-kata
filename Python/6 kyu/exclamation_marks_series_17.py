"""
Each exclamation mark's weight is 2; each question mark's weight is 3. Putting two strings left and right on the balance - are they balanced?

If the left side is more heavy, return "Left"; if the right side is more heavy, return "Right"; if they are balanced, return "Balance".

Examples
"!!", "??"     -->  "Right"
"!??", "?!!"   -->  "Left"
"!?!!", "?!?"  -->  "Left"
"!!???!????", "??!!?!!!!!!!"  -->  "Balance"

https://www.codewars.com/kata/57fb44a12b53146fe1000136/train/python
"""

def balance(left, right):
    left = sum(3 if l is "?" else 2 for l in left)
    right = sum(3 if r is "?" else 2 for r in right)
    
    return "Balance" if left - right == 0 else "Left" if left - right > 0 else "Right"