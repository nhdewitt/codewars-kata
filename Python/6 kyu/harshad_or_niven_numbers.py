"""
Harshad numbers (also called Niven numbers) are positive numbers that can be divided (without remainder) by the sum of their digits.

For example, the following numbers are Harshad numbers:

10, because 1 + 0 = 1 and 10 is divisible by 1
27, because 2 + 7 = 9 and 27 is divisible by 9
588, because 5 + 8 + 8 = 21 and 588 is divisible by 21
While these numbers are not:

19, because 1 + 9 = 10 and 19 is not divisible by 10
589, because 5 + 8 + 9 = 22 and 589 is not divisible by 22
1001, because 1 + 1 = 2 and 1001 is not divisible by 2
Harshad numbers can be found in any number base, but we are going to focus on base 10 exclusively.

Your task
Your task is to complete the skeleton Harshad object ("static class") which has 3 functions:

isValid() that checks if n is a Harshad number or not
getNext() that returns the next Harshad number > n
getSerie() that returns a series of n Harshad numbers, optional start value not included
You do not need to care about the passed parameters in the test cases, they will always be valid integers (except for the start argument in getSerie() which is optional and should default to 0).

Note: only the first 2000 Harshad numbers will be checked in the tests.

Examples
Harshad.is_valid(1)          ==>  True
Harshad.get_next(0)          ==>  1
Harshad.get_series(3)        ==>  [ 1, 2, 3 ]
Harshad.get_series(3, 1000)  ==>  [ 1002, 1008, 1010 ]

https://www.codewars.com/kata/54a0689443ab7271a90000c6/train/python
"""

class Harshad:
    @staticmethod
    def is_valid(number):
        if number <= 10:
            return True
        n = number
        sum = 0
        while n:
            sum += (n % 10)                 # modulo division to create a running sum of the digits, integer division to reduce n until 0
            n //= 10
        return number % sum == 0
    
    @staticmethod
    def get_next(number):
        n = number + 1                      # not checking the current number but starting with the next one
        while not Harshad.is_valid(n):
            n += 1
        return n
    
    @staticmethod
    def get_series(count, start=0):
        s = []
        i = start + 1
        while len(s) < count:               # while the list is shorter than count, append valid Harshad numbers and return
            if Harshad.is_valid(i):
                s.append(i)
            i += 1
        return s