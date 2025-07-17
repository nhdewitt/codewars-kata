/*
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).

https://www.codewars.com/kata/54da5a58ea159efa38000836/train/c
*/

#include <stddef.h>
#include <stdlib.h>

int find_odd (size_t length, const int array[length])
{
  if (length == 1)
    return array[0];
  int min = array[0], max = array[0];
  for (size_t i = 1; i < length; i++) {
    if (array[i] > max)
      max = array[i];
    if (array[i] < min)
      min = array[i];
  }
  
  size_t span = (size_t)(max - min + 1);
  int *freq = calloc(span, sizeof *freq);
  
  for (size_t i = 0; i < length; i++)
    freq[array[i] - min]++;
  int v;
  for (v = min; v <= max; v++)
    if (freq[v - min] % 2 != 0)
      break;
  
  return v;
}