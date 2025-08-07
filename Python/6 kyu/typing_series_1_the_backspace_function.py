"""
This kata is a harder version of this kata: https://www.codewars.com/kata/5727bb0fe81185ae62000ae3

If you haven't done it yet, you should do that one first before doing this one.

You are given a string of letters that you need to type out. In the string there is a special function: [backspace]. Once you encounter a [backspace] , you delete the character right before it. If there is nothing to backspace , just carry on. Return the final string .

e.g. oopp[backspace]s return oops (delete the p)

Walkthrough:

o
oo
oop
oopp
oop [backspace]
oops

e.g. ooppp[backspace][backspace]s return oops (delete both p's)

Walkthrough:

o
oo
oop
oopp
ooppp
oopp [backspace]
oop [backspace]
oops

e.g. a[backspace][backspace]ooppp[backspace][backspace]s return oops

Walkthrough:

a
[nothing]
[nothing]
o
oo
oop
oopp
ooppp
oopp [backspace]
oop [backspace]
oops

But there's a twist! [backspace][backspace][backspace] can appear as [backspace]*3 or even [backspace]*2[backspace]

Basically, [backspace][backspace] ... [backspace] n times can appear as [backspace]*n (n can even be 1, but not less than 1 ([backspace]*0 will not occur))

e.g. a[backspace]*2oopppp[backspace]*2[backspace]s return oops

Walkthrough:

a
[nothing] [backspace]*2
o
oo
oop
oopp
ooppp
oopppp
oopp [backspace]*2
oop [backspace]
oops

To make it easier, only letters, spaces. and the [backspace] function will be in the initial string.

Good luck!

https://www.codewars.com/kata/62b3e38df90eac002c7a983f/train/python
"""

import re

def solve(s):
    s = s.replace("[backspace]", "#")
    res = re.sub(r'#\*(\d+)',
                lambda m: '#' * int(m.group(1)),
                s)
    out = []
    for c in res:
        if c == "#":
            if out:
                out.pop()
        else:
            out.append(c)
    
    return "".join(out)