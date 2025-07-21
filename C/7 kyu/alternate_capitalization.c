/*
Given a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below. Index 0 will be considered even.

For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.

The input will be a lowercase string with no spaces.

Good luck!

If you like this Kata, please try:

Indexed capitalization

Even-odd disparity

https://www.codewars.com/kata/59cfc000aeb2844d16000075/train/c
*/

#include <stdlib.h>
#include <string.h>
#include <ctype.h>

char **capitalize(const char *test_str) {
// return a dynamically-allocated array of 2 dynamically-allocated strings
// the array and the 2 strings will be freed by the tests

  char **pair = malloc(2 * sizeof *pair);
  size_t len = strlen(test_str) + 1;
  pair[0] = calloc(len, sizeof *pair[0]);
  pair[1] = calloc(len, sizeof *pair[1]);
  if (!pair[0] || !pair[1])
  {
    free(pair[0]);
    free(pair[1]);
    free(pair);
    return NULL;
  }
  
  char *p = pair[0];
  char *q = pair[1];
  int i = 0;
  char ch;
  
  while ((ch = *test_str++))
  {
    if (i % 2 == 0)
    {
      *p++ = toupper((unsigned char)ch);
      *q++ = tolower((unsigned char)ch);
    } else
    {
      *p++ = tolower((unsigned char)ch);
      *q++ = toupper((unsigned char)ch);
    }
    i++;
  }
  *p = *q = '\0';
  
  return pair;
}