"""
Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"

Your task is to process a string with "#" symbols.

Examples
"abc#d##c"      ==>  "ac"
"abc##d######"  ==>  ""
"#######"       ==>  ""
""              ==>  ""

https://www.codewars.com/kata/5727bb0fe81185ae62000ae3/train/python
"""

def clean_string(s):
    output = []                 # initialize stack
    for c in s:
        if c != "#":
            output.append(c)    # if pointer is not #, append to stack
        else:
            if output:          # if # and stack not empty, pop
                output.pop()
    return "".join(output)