/*
Task
N lamps are placed in a line, some are switched on and some are off. What is the smallest number of lamps that need to be switched so that on and off lamps will alternate with each other?

You are given an array a of zeros and ones - 1 mean switched-on lamp and 0 means switched-off.

Your task is to find the smallest number of lamps that need to be switched.

Example
For a = [1, 0, 0, 1, 1, 1, 0], the result should be 3.

a      --> 1 0 0 1 1 1 0
switch --> 0 1     0
became --> 0 1 0 1 0 1 0
Input/Output
[input] integer array a
array of zeros and ones - initial lamp setup, 1 mean switched-on lamp and 0 means switched-off.

2 < a.length <= 1000

[output] an integer
minimum number of switches.


https://www.codewars.com/kata/58a3c1f12f949e21b300005c/train/c
*/

#include <stdbool.h>
#include <stddef.h>

size_t lamps(size_t n, const bool array[n]) {
  size_t flips_0 = 0;
  size_t flips_1 = 0;
  for (size_t i = 0; i < n; i++)
  {
    if (array[i] != (i & 1))        flips_0++;
    if (array[i] != ((i + 1) & 1))  flips_1++;
  }
  
  return (flips_0 < flips_1) ? flips_0 : flips_1;
}