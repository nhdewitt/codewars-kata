"""
Format any integer provided into a string with "," (commas) in the correct places.

Example:

For n = 100000 the function should return '100,000';
For n = 5678545 the function should return '5,678,545';
for n = -420902 the function should return '-420,902'.

https://www.codewars.com/kata/565c4e1303a0a006d7000127/train/python
"""

def number_format(n):
    negative = False
    if n < 0:
        negative = True                                                                 # if the number is negative, set bool; need to str the number so can avoid dealing with the "-"
    i = abs(n)
    str_n = "".join([x for x in str(i)])
    formatted = []
    for i in range(3, len(str_n) + 1, 3):                                               # divide the numbers up by groups of threes
        if -i + 3 == 0:
            formatted.append(str_n[-i:])
        else:
            formatted.append(str_n[-i:-i + 3])
    
    if len(str_n) % 3 != 0:
        formatted.append(str_n[:len(str_n) % 3])                                        # any remainders will be added to the list if they exist
    
    return f"-{','.join(formatted[::-1])}" if negative else ",".join(formatted[::-1])   # output the reverse of the groups to get the original number formatted