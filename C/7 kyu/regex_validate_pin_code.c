/*
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.

Examples (Input --> Output)
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false

https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/train/c
*/

#include <stdbool.h>
#include <string.h>

bool validate_pin(const char *pin)
{
  char ch;
  const char *p = pin;
  int length = 0;
  while ((ch = *p++))
  {
    if (ch < '0' || ch > '9')   return false;
    length++;
    if (length > 6)             return false;
  }
  return (length == 4 || length == 6) ? true : false;
}