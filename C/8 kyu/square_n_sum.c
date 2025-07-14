/*
Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 because 
1
2
+
2
2
+
2
2
=
9
1 
2
 +2 
2
 +2 
2
 =9.
 
https://www.codewars.com/kata/515e271a311df0350d00000f/train/c
*/

#include <stddef.h>

int square_sum(const int values[/* count */], size_t count)
{
  int sum = 0;
	for (int i = 0; i < count; i++)
    sum += values[i] * values[i];
  
  return sum;
}