/*
The two oldest ages function/method needs to be completed. It should take an array of numbers as its argument and return the two highest numbers within the array. The returned value should be an array in the format [second oldest age,  oldest age].

The order of the numbers passed in could be any order. The array will always include at least 2 items. If there are two or more oldest age, then return both of them in array format.

For example (Input --> Output):

[1, 2, 10, 8] --> [8, 10]
[1, 5, 87, 45, 8, 8] --> [45, 87]
[1, 3, 10, 0]) --> [3, 10]

https://www.codewars.com/kata/511f11d355fe575d2c000001/train/c
*/

#include <stdlib.h>

//result is an output buffer which has to be filled with the solution
void two_oldest_ages(size_t n, const int ages[n], int result[2]) {
  int oldest = ages[0], next_oldest = ages[1];
  if (oldest < next_oldest)
  {
    int temp = oldest;
    oldest = next_oldest;
    next_oldest = temp;
  }
  
  for (size_t i = 2; i < n; i++)
  {
    if (ages[i] > oldest)
    {
      next_oldest = oldest;
      oldest = ages[i];
    }
    else if (ages[i] > next_oldest)
    {
      next_oldest = ages[i];
    }
  }
  
  result[0] = next_oldest;
  result[1] = oldest;
}