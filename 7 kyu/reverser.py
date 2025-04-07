"""
Impliment the reverse function, which takes in input n and reverses it. For instance, reverse(123) should return 321. You should do this without converting the inputted number into a string.

# Please do not use anything from the following list:
['encode','decode','join','zfill','codecs','chr','bytes','ascii', 'substitute','template','bin', 'os','sys','re', '"', "'", 'str','repr', '%s', 'format', 'type', '__', '.keys','eval','exec','subprocess']
            

https://www.codewars.com/kata/58069e4cf3c13ef3a6000168/train/python
"""

def reverse(n):
    rev = 0
    while n > 0:
        last_d = n % 10
        rev = (rev * 10) + last_d
        n //= 10
    
    return rev