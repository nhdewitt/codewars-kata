/*
For every good kata idea there seem to be quite a few bad ones!

In this kata you need to check the provided array (x) for good ideas 'good' and bad ideas 'bad'. If there are one or two good ideas, return 'Publish!', if there are more than 2 return 'I smell a series!'. If there are no good ideas, as is often the case, return 'Fail!'.

For C: do not dynamically allocate memory, instead return a string literal


https://www.codewars.com/kata/57f222ce69e09c3630000212/train/c
*/

#include <stddef.h>
#include <string.h>

const char *well(size_t n, const char *ideas[n]) {
  int good = 0;
  for (size_t i = 0; i < n; i++)
    if (strcmp(ideas[i], "good") == 0)  good++;
  switch (good) {
      case 0:           return "Fail!";
      case 1: case 2:   return "Publish!";
      default:          return "I smell a series!";        
  }
}