/*
Write a function which takes a number as input and returns the sum of the absolute value of each of the number's decimal digits.

For example: (Input --> Output)

10 --> 1
99 --> 18
-32 --> 5
Let's assume that all numbers in the input will be integer values.


https://www.codewars.com/kata/52f3149496de55aded000410/train/c
*/

#import <stdlib.h>

int sum_digits(int n) {
  int sum = 0;
  while (n)
  {
    sum += n % 10;
    n /= 10;
  }
  return abs(sum);
}