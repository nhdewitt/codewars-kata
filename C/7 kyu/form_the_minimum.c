/*
Task
Given a list of digits, return the smallest number that could be formed from these digits, using the digits only once (ignore duplicates). Only positive integers in the range of 1 to 9 will be passed to the function.

Examples
[1, 3, 1] ==> 13
[5, 7, 5, 9, 7] ==> 579
[1, 9, 3, 1, 7, 4, 6, 6, 7]  ==> 134679
Playing with Numbers Series

Playing With Lists/Arrays Series

Bizarre Sorting-katas

For More Enjoyable Katas

https://www.codewars.com/kata/5ac6932b2f317b96980000ca/train/c
*/

#include <stdlib.h>
#include <stdbool.h>

int minValue(const int* values, const size_t len)
{
  bool seen[10] = {false};
  for (const int *p = values; p < values + len; p++)
    seen[*p] = true;
  int res = 0;
  for (int i = 1; i < 10; i++)
    if (seen[i])
      res = res * 10 + i;
  if (seen[0])  res *= 10;

  return res;
}