"""
In this Kata, you will write a function doubles that will remove double string characters that are adjacent to each other.

For example:

doubles('abbcccdddda') = 'aca', because, from left to right:

a) There is only one 'a' on the left hand side, so it stays.
b) The 2 b's disappear because we are removing double characters that are adjacent. 
c) Of the 3 c's, we remove two. We are only removing doubles. 
d) The 4 d's all disappear, because we first remove the first double, and again we remove the second double.
e) There is only one 'a' at the end, so it stays.
Two more examples: doubles('abbbzz') = 'ab' and doubles('abba') = "". In the second example, when we remove the b's in 'abba', the double a that results is then removed.

The strings will contain lowercase letters only. More examples in the test cases.

Good luck!


https://www.codewars.com/kata/5a145ab08ba9148dd6000094/train/python
"""

from copy import copy

def doubles(s):
    inp = copy(s)
    out = []
    i = 0
    while i <= len(s) - 1:
        char = s[i]
        count = 1
        if i != len(s) - 1 and s[i + 1] == char:
            while i != len(s) - 1 and s[i + 1] == char:
                i += 1
                count += 1
        i += 1
        if count % 2 == 0:
            continue
        out.append(char)
    out = "".join(out)
    if out == inp:
        return out
    return doubles(out)