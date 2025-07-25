/*
Create a function called _if which takes 3 arguments: a value bool and 2 functions (which do not take any parameters): func1 and func2

When bool is truthy, func1 should be called, otherwise call the func2.

Example:
void the_true() { printf("true"); }
void the_false() { printf("false"); }
_if(true, the_true, the_false);
// Logs "true" to the console

https://www.codewars.com/kata/54147087d5c2ebe4f1000805/train/c
*/

#include <stdbool.h>

void _if(bool value, void (*func1)(), void (*func2)())
{
  if (value) {
    func1();
  } else {
    func2();
  }
}