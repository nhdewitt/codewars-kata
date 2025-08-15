/*
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

Note: input will never be an empty string


https://www.codewars.com/kata/57eae65a4321032ce000002d/train/c
*/

void fakeBin(const char *digits, char *binary) {
  const char *p = digits;
  char *q = binary;
  while (*p) {
    if (*p < '5') *q++ = '0';
    else          *q++ = '1';
    p++;
  }
  *q = '\0';
}