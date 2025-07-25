/*
Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).

Examples:

Input -> Output
1,2,2 -> true
4,2,3 -> true
2,2,2 -> true
1,2,3 -> false
-5,1,3 -> false
0,2,3 -> false
1,2,9 -> false 

https://www.codewars.com/kata/56606694ec01347ce800001b/train/c
*/

#include <stdbool.h>

bool is_triangle(int a, int b, int c)
{
  if (a > b) {
    int tmp = a;
    a = b;
    b = tmp;
  }
  
  if (a > c) {
    int tmp = a;
    a = c;
    c = tmp;
  }
  
  if (b > c) {
    int tmp = b;
    b = c;
    c = tmp;
  }
  
  return a + b > c;
}