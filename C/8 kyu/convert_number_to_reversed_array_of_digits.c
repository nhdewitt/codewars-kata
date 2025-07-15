/*
Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

Example (Input => Output):
35231 => [1,3,2,5,3]
0     => [0]

https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/c
*/

#include <stddef.h>
#include <inttypes.h>

void digitize (uint64_t n, uint8_t digits[], size_t *length_out)
{
  uint8_t i = 0;
  if (n == 0) {
    digits[0] = 0;
    *length_out = 1;
    return;
  }
  
  while (n > 0) {
    digits[i++] = n % 10;
    n /= 10;
  }
  
  *length_out = i;
}