/*
Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string (alphabetical ascending), the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

https://www.codewars.com/kata/5656b6906de340bd1b0000ac/train/c
*/

#include <stdlib.h>
#include <stdbool.h>

char *longest (const char *s1, const char *s2)
{
  char *out = malloc(27);
  if (!out) return NULL;
  bool letter_set[26] = {false};
  while (*s1)
    letter_set[*s1++ - 'a'] = true;
  while (*s2)
    letter_set[*s2++ - 'a'] = true;
  int i = 0;
  for (int idx = 0; idx < 26; idx++) {
    if (letter_set[idx])
      out[i++] = 'a' + idx;
  }
  out[i] = '\0';
  
  return out;
}