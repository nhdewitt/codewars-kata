"""
The input is a string str of digits. Cut the string into chunks (a chunk here is a substring of the initial string) of size sz (ignore the last chunk if its size is less than sz).

If the sum of a chunk's digits is divisible by 2, reverse that chunk; otherwise rotate it to the left by one position. Put together these modified chunks and return the result as a string.

If

sz is <= 0 or if str == "" return ""
sz is greater (>) than the length of str it is impossible to take a chunk of size sz hence return "".
Examples:
("123456987654", 6) --> "234561876549"
("123456987653", 6) --> "234561356789"
("66443875", 4) --> "44668753"
("66443875", 8) --> "64438756"
("664438769", 8) --> "67834466"
("123456779", 8) --> "23456771"
("", 8) --> ""
("123456779", 0) --> "" 
("563000655734469485", 4) --> "0365065073456944"
Example of a string rotated to the left by one position:
s = "123456" gives "234561".

https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991/train/python
"""

def sum_of_digits(substr):
    total = 0
    for s in substr:
        total += int(s)
    
    return total

def rev_rot(strng, sz):
    output = ""
    if sz <= 0 or str == "":
        return ""
    beg_idx = 0
    end_idx = sz
    for i in range(len(strng) // sz):
        substr = strng[beg_idx:end_idx]
        if sum_of_digits(substr) % 2 == 0:
            output += substr[::-1]
        else:
            output += substr[1:] + substr[0]
        beg_idx = end_idx
        end_idx += sz
    
    return output