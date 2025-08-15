/*
Description:
Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.

Examples
"Hi!" --> "H!!"
"!Hi! Hi!" --> "!H!! H!!"
"aeiou" --> "!!!!!"
"ABCDE" --> "!BCD!"


https://www.codewars.com/kata/57fb09ef2b5314a8a90001ed/train/c
*/

#include <stdlib.h>
#include <string.h>

char *replace(const char *s)
{
  size_t len = strlen(s) + 1;
  char *res = malloc(len * sizeof(char));
  if (!res)   return NULL;
  
  char *q = res;
  
  while (*s) {
    switch (*s) {
        case 'a': case 'e': case 'i': case 'o': case 'u':
        case 'A': case 'E': case 'I': case 'O': case 'U':
          *q++ = '!';
          break;
        default:
          *q++ = *s;
    }
    s++;
  }
  *q = '\0';
  return res;
}