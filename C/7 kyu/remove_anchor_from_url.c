/*
Complete the function/method so that it returns the url with anything after the anchor (#) removed.

Examples
"www.codewars.com#about" --> "www.codewars.com"
"www.codewars.com?page=1" -->"www.codewars.com?page=1"


https://www.codewars.com/kata/51f2b4448cadf20ed0000386/train/c
*/

#include <stdlib.h>
#include <string.h>

//  return a heap-allocated C-string
//  (memory will be freed by tester)

char *remove_url_anchor(const char *url_in) {
  int i = 0;
  char c;
  
  char *url_out = malloc(strlen(url_in) + 1);
  while ((c = *url_in++))
  {
    if (c == '#')   break;
    url_out[i++] = c;
  }
  url_out[i] = '\0';
  
  return url_out;
}