/*
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

patrick feeney => P.F


https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/c
*/

#include <ctype.h>

char *get_initials (const char *full_name, char initials[4])
{
  const char *p = full_name;
  initials[0] = toupper(*p);
  initials[1] = '.';
  initials[3] = '\0';
  
  while (*p++ != ' ')
    ;
  initials[2] = toupper(*p);
  
  return initials;
}