/*
Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four characters into '#'.

Examples (input --> output):
"4556364607935616" --> "############5616"
     "64607935616" -->      "#######5616"
               "1" -->                "1"
                "" -->                 ""

// "What was the name of your first pet?"
"Skippy" --> "##ippy"
"Nananananananananananananananana Batman!" --> "####################################man!"


https://www.codewars.com/kata/5412509bd436bd33920011bc/train/c
*/

#include <string.h>

char *maskify (char *masked, const char *string)
{
  size_t len = strlen(string);
  size_t mask = (len > 4) ? len - 4 : 0;
  size_t i = 0;
  while (*string) {
    masked[i++] = (i < mask) ? '#' : *string;
    *string++;
  }
	masked[i] = '\0'; // write to masked
	return masked; // return it
}