"""
Create a parser to interpret and execute the Deadfish language.

Deadfish operates on a single value in memory, which is initially set to 0.

It uses four single-character commands:

i: Increment the value
d: Decrement the value
s: Square the value
o: Output the value to a result array
All other instructions are no-ops and have no effect.

Examples
Program "iiisdoso" should return numbers [8, 64].
Program "iiisdosodddddiso" should return numbers [8, 64, 3600].

https://www.codewars.com/kata/51e0007c1f9378fa810002a9/train/python
"""

def parse(data):
    memory = 0
    output = []
    for d in data:
        if d == "i":
            memory += 1
        elif d == "d":
            memory -= 1
        elif d == "s":
            memory *= memory
        elif d == "o":
            output.append(memory)
    return output