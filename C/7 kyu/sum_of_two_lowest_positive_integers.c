/*
Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

[10, 343445353, 3453445, 3453545353453] should return 3453455.


https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/c
*/

#include <stddef.h>

long sum_two_smallest_numbers(size_t n, const int numbers[n]) {
  long lowest, nextLowest;
  if (numbers[0] < numbers[1]) {
    lowest = numbers[0];
    nextLowest = numbers[1];
  } else {
    lowest = numbers[1];
    nextLowest = numbers[0];
  }
  for (size_t i = 2; i < n; i++) {
    if (numbers[i] < lowest) {
      nextLowest = lowest;
      lowest = numbers[i];
    } else if (numbers[i] < nextLowest)
      nextLowest = numbers[i];
  }
  return lowest + nextLowest;
}