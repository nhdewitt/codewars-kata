/*
Your task is to sum the differences between consecutive pairs in the array in descending order.

Example
[2, 1, 10]  -->  9
In descending order: [10, 2, 1]

Sum: (10 - 2) + (2 - 1) = 8 + 1 = 9

If the array is empty or the array has only one element the result should be 0 (Nothing in Haskell, None in Rust).


https://www.codewars.com/kata/5b73fe9fb3d9776fbf00009e/train/c
*/

#include <stddef.h>
#include <stdlib.h>
#include <string.h>

int compare(const void *a, const void *b) {
  return (*(int*)b - *(int*)a);
}

int diffsum(const int *arr, size_t n)
{
  if (n < 2)  return 0;
  
  int *temp;
  temp = malloc(n * sizeof(int));
  if (!temp)    return 0;
  
  memcpy(temp, arr, n * sizeof *temp);
  
  qsort(temp, n, sizeof *temp, compare);
  
  int diff = 0;
  for (size_t i = 0; i < n - 1; i++)
    diff += (temp[i] - temp[i + 1]);
  
  free(temp);
  temp = NULL;
  
  return diff;
}