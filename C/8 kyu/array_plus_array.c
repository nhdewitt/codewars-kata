/*
I'm new to coding and now I want to get the sum of two arrays... Actually the sum of all their elements. I'll appreciate for your help.

P.S. Each array includes only integer numbers. Output is a number too.

https://www.codewars.com/kata/5a2be17aee1aaefe2a000151/train/c
*/

#include <stddef.h>

long long arr_plus_arr(const int a[/* na */],  const int b[/* nb */], size_t na, size_t nb)
{
  long long sum = 0;
  for (int i = 0; i < na; i++)
    sum += a[i];
  for (int i = 0; i < nb; i++)
    sum += b[i];
  return sum;
}