/*
This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.


https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/c
*/

#include <stdlib.h>
#include <string.h>
#include <ctype.h>

char *accum(const char *source)
{
  size_t len    = strlen(source);
  size_t buffer = len * (len + 3) / 2 + 1;
  char *out     = malloc(buffer * sizeof *out);
  if (!out)   return NULL;
  size_t j = 0;
  size_t i = 1;
  while (*source) {
    out[j++] = toupper((unsigned char)*source);
    for (size_t p = 1; p < i; p++)
      out[j++] = tolower((unsigned char)*source);
    i++;
    source++;
    if (i <= len)  out[j++] = '-';
  }
  out[j++] = '\0';
  
  return out;
}