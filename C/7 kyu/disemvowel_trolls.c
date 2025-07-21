/*
Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel.


https://www.codewars.com/kata/52fba66badcd10859f00097e/train/c
*/

#include <stdlib.h>
#include <string.h>

//solution must allocate all required memory
//and return a free-able buffer to the caller.

char *disemvowel(const char *str)
{
  char *out = malloc(strlen(str) + 1);
  char *p = out;
  char ch;
  
  if (!out)   return NULL;
  
  while ((ch = *str++))
  {
    switch (ch)
    {
        case 'a': case 'A': case 'e': case 'E': case 'i': case 'I': case 'o': case 'O': case 'u': case 'U':   break;
        default:  *p++ = ch;
    }
  }
  *p = '\0';
  return out;
}