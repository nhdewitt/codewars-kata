/*
Complete the solution so that it reverses the string passed into it.

'world'  =>  'dlrow'
'word'   =>  'drow'

https://www.codewars.com/kata/5168bb5dfe9a00b126000018/train/c
*/

#include <string.h>

char *strrev (char *string)
{
  char tmp;
  size_t len = strlen(string) - 1;
  int i = 0, j = len;
  
  while (i < j) {
    tmp = string[j];
    string[j--] = string[i];
    string[i++] = tmp;
  }
  
  return string;
}