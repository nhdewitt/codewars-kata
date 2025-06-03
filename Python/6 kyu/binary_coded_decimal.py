"""
Convert a number to a binary coded decimal (BCD).

You can assume input will always be an integer. If it is a negative number then simply place a minus sign in front of the output string. Output will be a string with each digit of the input represented as 4 bits (0 padded) with a space between each set of 4 bits.

Ex.

n =  10 -> "0001 0000"
n = -10 -> "-0001 0000"

https://www.codewars.com/kata/5521d84b95c172461d0000a4/train/python
"""

def to_bcd(n):
    output = []
    str_n = (int(i) for i in str(n) if i.isdigit())                 # convvert to string (ignoring negative sign)
    for c in str_n:
        output.append(bin(c)[2:].zfill(4))                          # for each digit, convert to binary and pad to 4 with zeros
    return ' '.join(output) if n >= 0 else f"-{' '.join(output)}"   # join the output, adding the negative sign if applicable