/*
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.

https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/c
*/

#include <sys/types.h>
#include <string.h>
#include <limits.h>

ssize_t find_short(const char *s)
{
  ssize_t shortest_length = SSIZE_MAX;
  
  while (*s)
  {
    ssize_t length = 0;
    while (*s && *s++ != ' ')
    {
      length++;
    }
    if (length == 1)  return 1;
    if (length < shortest_length)   shortest_length = length;
    length = 0;
  }
  return shortest_length;
}