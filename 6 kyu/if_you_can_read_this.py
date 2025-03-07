"""
The idea for this kata came from 9gag today:

The lyrics to "Never gonna give you up" by Rick Astley encoded in the NATO phonetic alphabet

Task
You'll have to translate a string to Pilot's alphabet (NATO phonetic alphabet).

Input:

If, you can read?

Output:

India Foxtrot , Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta ?

Note:

There is a preloaded dictionary that you can use, named NATO. It uses uppercase keys, e.g. NATO['A'] is "Alfa". See comments in the initial code to see how to access it in your language.
The set of used punctuation is ,.!?.
Punctuation should be kept in your return string, but spaces should not.
Xray should not have a dash within.
Every word and punctuation mark should be seperated by a space ' '.
There should be no trailing whitespace

https://www.codewars.com/kata/586538146b56991861000293/train/python
"""

from preloaded import NATO # NATO['A'] == 'Alfa', etc

def to_nato(words : str) -> str:
    nato_output = []
    for c in words:
        if c.upper() in NATO:
            nato_output.append(NATO[c.upper()])
        elif c in ",.!?":
            nato_output.append(c)
    
    return " ".join(nato_output)