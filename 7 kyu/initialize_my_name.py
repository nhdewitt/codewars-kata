"""
Some people just have a first name; some people have first and last names and some people have first, middle and last names.

You task is to initialize the middle names (if there is any).

Examples
'Jack Ryan'                   => 'Jack Ryan'
'Lois Mary Lane'              => 'Lois M. Lane'
'Dimitri'                     => 'Dimitri'
'Alice Betty Catherine Davis' => 'Alice B. C. Davis'

https://www.codewars.com/kata/5768a693a3205e1cc100071f/train/python
"""

def initialize_names(name):
    name = name.split()
    middle = len(name) - 1
    if middle > 0:
        for i in range(1, middle):
            name[i] = f"{name[i][0]}."
    return " ".join(name)
