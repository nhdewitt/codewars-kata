/*
An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).

Note: anagrams are case insensitive

Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.

Examples
"foefet" is an anagram of "toffee"

"Buckethead" is an anagram of "DeathCubeK"

https://www.codewars.com/kata/529eef7a9194e0cbc1000255/train/c
*/

#include <stdbool.h>
#include <ctype.h>

bool is_anagram(const char *s1, const char *s2)
{
  int alphabet[26] = {0};
  while (*s1)
  {
    alphabet[tolower(*s1++) - 'a']++;
  }
  while (*s2)
  {
    alphabet[tolower(*s2++) - 'a']--;
  }
  
  for (int i = 0; i < 26; i++)
  {
    if (alphabet[i] != 0)   return false;
  }
  
  return true;
}