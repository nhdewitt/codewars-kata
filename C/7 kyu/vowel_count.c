/*
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.

https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/c
*/

#include <stddef.h>

size_t get_count(const char *s)
{
  size_t count = 0;
  
  while (*s) {
    switch (*s++) {
    case 'a': case 'e': case 'i': case 'o': case 'u': count++;
    }
  }
  
  return count;
}