"""
In this Kata, you will be given a lower case string and your task will be to remove k characters from that string using the following rule:

- first remove all letter 'a', followed by letter 'b', then 'c', etc...
- remove the leftmost character first.
For example: 
solve('abracadabra', 1) = 'bracadabra' # remove the leftmost 'a'.
solve('abracadabra', 2) = 'brcadabra'  # remove 2 'a' from the left.
solve('abracadabra', 6) = 'rcdbr'      # remove 5 'a', remove 1 'b' 
solve('abracadabra', 8) = 'rdr'
solve('abracadabra',50) = ''
More examples in the test cases. Good luck!

Please also try:

Simple time difference

Simple remove duplicates

https://www.codewars.com/kata/5b728f801db5cec7320000c7/train/python
"""

def solve(st,k): 
    if k >= len(st):                                                    # if we're removing anything more than the size of st-1, we're removing it all, so skip the rest
        return ""
    removed = sorted(list(enumerate(st)), key=lambda x: x[1])[k:]       # enumerate to preserve indices, sort alphabetically, then eliminate the first k characters
    sort_removed = sorted(removed, key=lambda x: x[0])                  # re-sort by index
    
    return "".join([c[1] for c in sort_removed])                        # get chars from tuple, output to string