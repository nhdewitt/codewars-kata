/*
Background:
You're working in a number zoo, and it seems that one of the numbers has gone missing!

Zoo workers have no idea what number is missing, and are too incompetent to figure it out, so they're hiring you to do it for them.

In case the zoo loses another number, they want your program to work regardless of how many numbers there are in total.

Task:
Write a function that takes a shuffled list of unique numbers from 1 to n with one element missing (which can be any number including n). Return this missing number.

Note: huge lists will be tested.

Examples:
[1, 3, 4]  =>  2
[1, 2, 3]  =>  4
[4, 2, 3]  =>  1


https://www.codewars.com/kata/5276c18121e20900c0000235/train/c
*/

#include <stdlib.h>

unsigned find_number(const unsigned *arr, size_t len)
{
  unsigned sum = 0;
  
  for (size_t i = 0; i < len; i++)
    sum += arr[i];

  size_t n = len + 1;
  
  return ((n * (n + 1)) / 2) - sum;
}