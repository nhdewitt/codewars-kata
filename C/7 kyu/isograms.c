/*
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true
"aba" --> false
"moOse" --> false (ignore letter case)

https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/c
*/

#include <stdbool.h>
#include <ctype.h>

bool IsIsogram (const char *string) 
{
  bool isogramCheck[26] = {false};
  while (*string) {
    if (isogramCheck[tolower(*string) - 'a'])
      return false;
    isogramCheck[tolower(*string++) - 'a'] = true;
  }
  
  return true;
}