/*
You will be given an array and a limit value. You must check that all values in the array are below or equal to the limit value. If they are, return true. Else, return false.

You can assume all values in the array are numbers.

https://www.codewars.com/kata/57cc981a58da9e302a000214/train/c
*/

#include <stdbool.h>
#include <stddef.h>

bool small_enough(int *arr, size_t length, int limit)
{
  for (size_t i = 0; i < length; i++)
    if (arr[i] > limit)   return false;
  return true;
}