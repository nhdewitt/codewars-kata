/*
Write a small function that returns the values of an array that are not odd.

All values in the array will be integers. Return the good values in the order they are given.

https://www.codewars.com/kata/51fd6bc82bc150b28e0000ce/train/c
*/

#include <stddef.h>

//  assign even numbers to preallocated *filtered
//  set pointer *f to length of this return array

void no_odds(size_t a, const int array[a], int *filtered, size_t *f) {
  size_t j = 0;
  for (size_t i = 0; i < a; i++)
    if (array[i] % 2 == 0)
      filtered[j++] = array[i];
  
  *f = j;
}