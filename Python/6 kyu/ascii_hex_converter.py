"""
Write a pair of functions that convert from ASCII to hexadecimal and the other way around.

To make the conversion well defined, each ASCII character is represented by exactly two hex digits, left-padding with a 0 if needed.

The conversion from ascii to hex should produce lowercase strings (i.e. f6 instead of F6).

Example
ascii to hex: "Look mom, no hands" => "4c6f6f6b206d6f6d2c206e6f2068616e6473"

hex to ascii: "4c6f6f6b206d6f6d2c206e6f2068616e6473" => "Look mom, no hands"

https://www.codewars.com/kata/52fea6fd158f0576b8000089/train/python
"""

class Converter():
    @staticmethod
    def to_ascii(h):
        output = []
        i = 0
        while i < len(h):
            output.append(chr(int(h[i:i+ 2], 16)))      # hex in groups of two, convert to int, grab char, append and increment pointer by 2
            i += 2
        return "".join(output)
    
    @staticmethod
    def to_hex(s):
        output = []
        for c in s:
            output.append(hex(ord(c))[2:])              # strip 0x before appending and join
        return "".join(output)