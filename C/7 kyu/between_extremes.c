/*
Given an array of numbers, return the difference between the largest and smallest values.

For example:

[23, 3, 19, 21, 16] should return 20 (i.e., 23 - 3).

[1, 434, 555, 34, 112] should return 554 (i.e., 555 - 1).

The array will contain a minimum of two elements. Input data range guarantees that max-min will cause no integer overflow.


https://www.codewars.com/kata/56d19b2ac05aed1a20000430/train/c
*/

#include <stddef.h>

int between_extremes(size_t length, const int numbers[length]) {
  const int *p;
  int min = numbers[0];
  int max = numbers[0];
  
  for (p = numbers; p < numbers + length; p++) {
    if (*p < min)
      min = *p;
    if (*p > max)
      max = *p;
  }
  return max - min;
}