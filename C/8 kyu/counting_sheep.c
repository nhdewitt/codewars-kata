/*
Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

For example,

{ true,  true,  true,  false,
  true,  true,  true,  true,
  true,  false, true,  false,
  true,  false, false, true,
  true,  true,  true,  true,
  false, false, true,  true }
The correct answer would be 17.

Hint: Don't forget to check for bad values like null/undefined

https://www.codewars.com/kata/54edbc7200b811e956000556/train/c
*/

#include <stdbool.h>
#include <stddef.h>

size_t count_sheep(const bool sheep[/* count */], size_t count)
{
  size_t sum = 0;
  for (size_t i = 0; i < count; i++)
    if (sheep[i])
      sum++;
  
  return sum;
}