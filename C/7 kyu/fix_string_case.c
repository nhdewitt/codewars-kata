/*
In this Kata, you will be given a string that may have mixed uppercase and lowercase letters and your task is to convert that string to either lowercase only or uppercase only based on:

make as few changes as possible.
if the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.
For example:

solve("coDe") = "code". Lowercase characters > uppercase. Change only the "D" to lowercase.
solve("CODe") = "CODE". Uppercase characters > lowecase. Change only the "e" to uppercase.
solve("coDE") = "code". Upper == lowercase. Change all to lowercase.
More examples in test cases. Good luck!

Please also try:

Simple time difference

Simple remove duplicates

https://www.codewars.com/kata/5b180e9fedaa564a7000009a/train/c
*/

#include <string.h>
#include <stdlib.h>
#include <ctype.h>

// return a dynamically allocated string
// (to be freed by the testing function)

char *solve(const char *str) {
  size_t len = strlen(str);
  char *out = malloc(len + 1);
  int upper = 0, lower = 0;
  for (const char *p = str; *p; p++)
  {
    (isupper(*p)) ? upper++ : lower++;
  }
  
  size_t i = 0;
  while (*str)
  {
    out[i++] = (lower >= upper) ? tolower(*str++) : toupper(*str++);
  }
  out[i] = '\0';
  
  return out;
}