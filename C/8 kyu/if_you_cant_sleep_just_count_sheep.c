/*
If you can't sleep, just count sheeps!!

Task:
Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.


https://www.codewars.com/kata/5b077ebdaf15be5c7f000077/train/c
*/

#include <stdlib.h>
#include <stdio.h>

static size_t digit_count(unsigned n) {
  size_t d = 1;
  while (n >= 10) {
    n /= 10;
    d++;
  }
  return d;
}

char *count_sheep(unsigned n)
{
  if (n == 0) {
    char *empty = malloc(1);
    if (empty)  empty[0] = '\0';
    return empty;
  }
  
  size_t per = digit_count(n) + 9;
  size_t cap = (size_t)n * per + 1;
  
  char *res = malloc(cap);
  if (!res)   return NULL;
  
  char *p = res;
  size_t remain = cap;
  
  for (unsigned i = 1; i <= n; i++) {
    int written = snprintf(p, remain, "%u sheep...", i);
    if (written < 0 || (size_t)written >= remain) {
      free(res);
      return NULL;
    }
    p += (size_t)written;
    remain -= (size_t)written;
  }
  
  return res;
}