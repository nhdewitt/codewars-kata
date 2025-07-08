/*
Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

[1, 2, 3, 4, 5] --> [-1, -2, -3, -4, -5]
[1, -2, 3, -4, 5] --> [-1, 2, -3, 4, -5]
[] --> []
Notes:
All values are greater than INT_MIN
The input should be modified, not returned.

https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad/train/c
*/

#include <stddef.h>

void invert(int array[/* length */], size_t length)
{
  for (size_t i = 0; i < length; i++)
    array[i] = -array[i];
}