/*
You are going to be given a non-empty string. Your job is to return the middle character(s) of the string.

If the string's length is odd, return the middle character.
If the string's length is even, return the middle 2 characters.
Examples:
"test" --> "es"
"testing" --> "t"
"middle" --> "dd"
"A" --> "A"

https://www.codewars.com/kata/56747fd5cb988479af000028/train/c
*/

#include <string.h>
#include <stdio.h>

/* remember to null-terminate outp! */

char *get_middle(char outp[3], const char *inp)
{
  int len  = strlen(inp);
  int mid  = len / 2;
  if (len % 2 == 0) {
    outp[0] = inp[mid-1];
    outp[1] = inp[mid];
    outp[2] = '\0';
  } else {
    outp[0] = inp[mid];
    outp[1] = '\0';
  }
  
  return outp;
}