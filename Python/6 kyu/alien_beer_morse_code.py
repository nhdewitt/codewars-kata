"""
The Earth has been invaded by aliens. They demand our beer and threaten to destroy the Earth if we do not supply the exact number of beers demanded.

Unfortunately, the aliens only speak Morse code. Write a program to convert morse code into numbers using the following convention:

1 .---- 2 ..--- 3 ...-- 4 ....- 5 ..... 6 -.... 7 --... 8 ---.. 9 ----. 0 -----

https://www.codewars.com/kata/56dc4f570a10feaf0a000850/train/python
"""

MORSE = {
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    "-----": "0"
}

def morse_converter(strng):
    return int("".join(list(MORSE[strng[i:i + 5]] for i in range(0, len(strng), 5))))   # slice strng into len(5) slices, join the string and convert to integer