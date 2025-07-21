/*
Given a string made of digits [0-9], return a string where each digit is repeated a number of times equals to its value.

Examples
"312" should return "333122"
"102269" should return "12222666666999999999"

https://www.codewars.com/kata/585b1fafe08bae9988000314/train/c
*/

#include <stdlib.h>
#include <string.h>

char *digits_explode (const char *digits)
{
  size_t in_len = strlen(digits);
  size_t out_len = 0;
  
  for (size_t i = 0; i < in_len; ++i)
  {
    int count = digits[i] - '0';
    out_len += count;
  }
  
  char *out = malloc(out_len + 1);
  if (!out)   return NULL;
  
  char *p = out;
  for (size_t i = 0; i < in_len; ++i)
  {
    int count = digits[i] - '0';
    for (int j = 0; j < count; ++j)
      *p++ = digits[i];
  }
  
  *p = '\0';
  
  return out;
}