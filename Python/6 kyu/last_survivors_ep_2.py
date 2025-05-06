"""
Substitute two equal letters by the next letter of the alphabet (two letters convert to one):

"aa" => "b", "bb" => "c", .. "zz" => "a".
The equal letters do not have to be adjacent.
Repeat this operation until there are no possible substitutions left.
Return a string.

Example:

let str = "zzzab"
    str = "azab"
    str = "bzb"
    str = "cz"
return "cz"
Notes
The order of letters in the result is not important.
The letters "zz" transform into "a".
There will only be lowercase letters.
If you like this kata, check out another one: Last Survivor Ep.3

https://www.codewars.com/kata/60a1aac7d5a5fc0046c89651/train/python
"""

from string import ascii_lowercase
from collections import Counter

def rot1(c):
    return chr((ord(c) - 97 + 1) % 26 + 97)
    

def last_survivors(string):
    if not string: return ""
    freq_dict = Counter(string)
    for alpha in ascii_lowercase:
        freq_dict.setdefault(alpha, 0)                                              # set default keys for the rest of the letters since we'll be shifting into new letters
    changed = True
    while changed:
        changed = False
        for k, v in freq_dict.items():
            if freq_dict[k] > 1:                                                    # will always be reducing to 1 or 0 characters per letter
                changed = True                                                      # if there are any changes, we'll need to reiterate to check the new values
                shift = v // 2
                freq_dict[rot1(k)] += shift
                freq_dict[k] %= 2
    return "".join(sorted(list(c for c in freq_dict.keys() if freq_dict[c] > 0)))