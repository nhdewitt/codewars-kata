/*
Implement a function which convert the given boolean value into its string representation.

Note: Only valid inputs will be given.

In C, do not allocate memory, return a string literal.

https://www.codewars.com/kata/551b4501ac0447318f0009cd/train/c
*/

#include <stdbool.h>

//The returned string should be statically allocated and it won't be freed
const char *boolean_to_string(bool b)
{
  const char* t = "true";
  const char* f = "false";
  if (!b)
    return f;
  return t;
}