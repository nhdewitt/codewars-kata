"""
Write Number in Expanded Form - Part 2
This is version 2 of my 'Write Number in Exanded Form' Kata.

You will be given a number and you will need to return it as a string in expanded form :

expanded form illustration

For example:

807.304 --> "800 + 7 + 3/10 + 4/1000"
  1.24  --> "1 + 2/10 + 4/100"
  7.304 --> "7 + 3/10 + 4/1000"
  0.04  --> "4/100"
  
https://www.codewars.com/kata/58cda88814e65627c5000045/train/python
"""

def expanded_form(num):
    integer, decimal = str(num).split(".")                                              # split integer and decimal, handle differently
    int_as_string = list(str(integer))
    dec_as_string = list(str(decimal))
    
    integer, decimal = [], []

    for i in range(len(int_as_string)):
        if int_as_string[i] == "0":
            continue
        place_value = int(int_as_string[i]) * (10 ** (len(int_as_string) - i - 1))      # expanded form: i * 10 ^ (tens place)
        
        integer.append(str(place_value))
    
    for i in range(len(dec_as_string)):
        if dec_as_string[i] == "0":
            continue
        place_value = (10 ** (i + 1))                                                   # expanded form: i / 10 ^ (decimal place)
        
        decimal.append(f"{dec_as_string[i]}/{str(place_value)}")
    
    return " + ".join(integer + decimal)   