/*
Task
Given a string str, reverse it and omit all non-alphabetic characters.

Example
For str = "krishan", the output should be "nahsirk".

For str = "ultr53o?n", the output should be "nortlu".

Input/Output
[input] string str
A string consists of lowercase latin letters, digits and symbols.

[output] a string


https://www.codewars.com/kata/58b8c94b7df3f116eb00005b/train/c
*/

#include <stdlib.h>
#include <string.h>
#include <ctype.h>

char *reverse_letter(const char *str)
{
  size_t len = strlen(str);
  char *out = malloc(len + 1);
  if (!out)   return NULL;
  
  size_t j = 0;
  for (size_t i = 0; i < len; i++)
  {
    char c = str[len - 1 - i];
    if (isalpha((unsigned char)c))
    {
      out[j++] = c;
    }
  }
  out[j] = '\0';
  
  return out;
}