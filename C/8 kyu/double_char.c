/*
Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

Examples (Input -> Output):
* "String"      -> "SSttrriinngg"
* "Hello World" -> "HHeelllloo  WWoorrlldd"
* "1234!_ "     -> "11223344!!__  "
Good Luck!

https://www.codewars.com/kata/56b1f01c247c01db92000076/train/c
*/


#include <stdlib.h>
#include <string.h>

char *double_char (const char *string, char *doubled)
{
  if (!string || !doubled) return NULL;
  
  const char *src = string;
  char *dst = doubled;
  
  while (*src) {
    *dst++ = *src;
    *dst++ = *src;
    src++;
  }
  
  *dst = '\0';
  return doubled;
}