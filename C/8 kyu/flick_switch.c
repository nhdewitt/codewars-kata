/*
Task
Create a function that always returns True/true for every item in a given list.
However, if an element is the word 'flick', switch to always returning the opposite boolean value.

Examples
['codewars', 'flick', 'code', 'wars'] ➞ [True, False, False, False]

['flick', 'chocolate', 'adventure', 'sunshine'] ➞ [False, False, False, False]

['bicycle', 'jarmony', 'flick', 'sheep', 'flick'] ➞ [True, True, False, False, True]
Notes
"flick" will always be given in lowercase.
A list may contain multiple flicks.
Switch the boolean value on the same element as the flick itself.


https://www.codewars.com/kata/64fbfe2618692c2018ebbddb/train/c
*/

//  do not allocate memory for the return
//  assign values to pre-allocated result

#include <stdbool.h>
#include <stddef.h>
#include <string.h>

void flick_switch(size_t length, const char *const array[length], bool result[length]) {
  bool on = true;
  for (size_t i = 0; i < length; i++) {
    if (strcmp(array[i], "flick") == 0) {
      on = !on;
    }
    result[i] = on;
  }
}