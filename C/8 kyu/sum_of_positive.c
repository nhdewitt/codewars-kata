/*
Task
You get an array of numbers, return the sum of all of the positives ones.

Example
[1, -4, 7, 12] => 
1
+
7
+
12
=
20
1+7+12=20
Note
If there is nothing to sum, the sum is default to 0.

https://www.codewars.com/kata/5715eaedb436cf5606000381/train/c
*/

#include <stddef.h>

int positive_sum(const int values[/* count */], size_t count)
{
  int sum = 0;
  for (int i = 0; i < count; i++) {
    if (values[i] > 0)  sum += values[i];
  }
  
  return sum;
}