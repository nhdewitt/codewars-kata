/*
Task
Given an array of integers , Find the maximum product obtained from multiplying 2 adjacent numbers in the array. Note that the array size is at least 2 and consists a mixture of positive, negative integers and also zeroes.

Examples
[1, 2, 3] returns 6 because the maximum product is obtained from multiplying 
 
2
∗
3
=
6
 2∗3=6
[9, 5, 10, 2, 24, -1, -48] returns 50 because the maximum product is obtained from multiplying 
 
5
∗
10
=
50
 5∗10=50
[-23, 4, -5, 99, -27, 329, -2, 7, -921] returns -14 because the maximum product is obtained from multiplying 
 
−
2
∗
7
=
−
14
 −2∗7=−14
Playing with Numbers Series

Playing With Lists/Arrays Series

For More Enjoyable Katas

https://www.codewars.com/kata/5a4138acf28b82aa43000117/train/c
*/

#include <stddef.h>
#include <limits.h>

int adjacentElementsProduct(int inputArray[], size_t input_size) 
{
  int *q = inputArray + 1;
  int prod = INT_MIN;
  
  for (int *p = inputArray; q < inputArray + input_size; p++, q++)
    if ((*p * *q) > prod)
      prod = (*p * *q);
  
  return prod;
}