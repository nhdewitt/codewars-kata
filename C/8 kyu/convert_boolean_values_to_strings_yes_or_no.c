/*
Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

https://www.codewars.com/kata/53369039d7ab3ac506000467/train/c
*/

#include <stdbool.h>

const char *bool_to_word (bool value)
{
  return (value) ? "Yes" : "No";
}