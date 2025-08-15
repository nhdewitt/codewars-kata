/*
Description:
Remove n exclamation marks in the sentence from left to right. n is positive integer.

Examples
remove("Hi!",1) === "Hi"
remove("Hi!",100) === "Hi"
remove("Hi!!!",1) === "Hi!!"
remove("Hi!!!",100) === "Hi"
remove("!Hi",1) === "Hi"
remove("!Hi!",1) === "Hi!"
remove("!Hi!",100) === "Hi"
remove("!!!Hi !!hi!!! !hi",1) === "!!Hi !!hi!!! !hi"
remove("!!!Hi !!hi!!! !hi",3) === "Hi !!hi!!! !hi"
remove("!!!Hi !!hi!!! !hi",5) === "Hi hi!!! !hi"
remove("!!!Hi !!hi!!! !hi",100) === "Hi hi hi"


https://www.codewars.com/kata/57faf7275c991027af000679/train/c
*/

#include <stdlib.h>
#include <string.h>

char *remove(const char *str_in, int n) {
  size_t len = strlen(str_in) + 1;
  char *res = malloc(len * sizeof(char));
  if (!res)   return NULL;
  
  char *q = res;
  
  while (*str_in) {
    if (n && *str_in == '!') {
      n--;
    } else {
      *q++ = *str_in;
    }
    str_in++;
  }
  *q = '\0';
  return res;
}