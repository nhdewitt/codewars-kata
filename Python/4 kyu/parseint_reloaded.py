"""
In this kata we want to convert a string into an integer. The strings simply represent the numbers in words.

Examples:

"one" => 1
"twenty" => 20
"two hundred forty-six" => 246
"seven hundred eighty-three thousand nine hundred and nineteen" => 783919
Additional Notes:

The minimum number is "zero" (inclusively)
The maximum number, which must be supported is 1 million (inclusively)
The "and" in e.g. "one hundred and twenty-four" is optional, in some cases it's present and in others it's not
All tested numbers are valid, you don't need to validate them

https://www.codewars.com/kata/525c7c5ab6aecef16e0001a5/train/python
"""

def parse_int(string):
    numbers = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
        "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
        "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70,
        "eighty": 80, "ninety": 90,
    }
    
    string = string.replace("-", " ")
    string = [s for s in string.split() if s != "and"]
    
    if len(string) == 1:
        return numbers[string[0]]
    
    total = 0
    current = 0
    
    for s in string:
        if s == "million":
            current *= 1_000_000
            total += current
            current = 0
        elif s == "thousand":
            current *= 1_000
            total += current
            current = 0
        elif s == "hundred":
            current *= 100
        else:
            current += numbers[s]
            
    return total + current