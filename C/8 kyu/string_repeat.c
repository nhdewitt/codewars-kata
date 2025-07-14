/*
Write a function that accepts a non-negative integer n and a string s as parameters, and returns a string of s repeated exactly n times.

Examples (input -> output)
6, "I"     -> "IIIIII"
5, "Hello" -> "HelloHelloHelloHelloHello"

https://www.codewars.com/kata/57a0e5c372292dd76d000d7e/train/c
*/

#include <stdlib.h>
#include <string.h>

char *repeat_str(size_t count, const char *src)
{
  size_t n = strlen(src);
  char *dst = malloc(n*count + 1);
  if (!dst) return NULL;
  char *p = dst;
  
  for (size_t i = 0; i < count; i++) {
    memcpy(p, src, n);
    p += n;
  }
  *p = '\0';
  
  return dst;
}