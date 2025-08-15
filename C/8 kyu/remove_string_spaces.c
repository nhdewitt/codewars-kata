/*
Write a function that removes the spaces from the string, then return the resultant string.

Examples (Input -> Output):

"8 j 8   mBliB8g  imjB8B8  jl  B" -> "8j8mBliB8gimjB8B8jlB"
"8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd" -> "88Bifk8hB8BB8BBBB888chl8BhBfd"
"8aaaaa dddd r     " -> "8aaaaaddddr"
For C and Nasm, you must return a new dynamically allocated string.


https://www.codewars.com/kata/57eae20f5500ad98e50002c5/train/c
*/

#include <stdlib.h>
#include <string.h>

char *no_space(const char *str_in) {
  size_t len = strlen(str_in) + 1;
  char *res = malloc(len * sizeof(char));
  if (!res)   return NULL;
  
  char *p = res;
  
  while (*str_in) {
    switch (*str_in) {
        case ' ': break;
        default:  *p++ = *str_in;
    }
    str_in++;
  }
  *p = '\0';
  return res;
}