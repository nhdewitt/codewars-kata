/*
Your Task
Given an array of Boolean values and a logical operator, return a Boolean result based on sequentially applying the operator to the values in the array.

Examples
booleans = [True, True, False], operator = "AND"
True AND True -> True
True AND False -> False
return False
booleans = [True, True, False], operator = "OR"
True OR True -> True
True OR False -> True
return True
booleans = [True, True, False], operator = "XOR"
True XOR True -> False
False XOR False -> False
return False
Input
an array of Boolean values (1 <= array_length <= 50)
a string specifying a logical operator: "AND", "OR", "XOR"
Output
A Boolean value (True or False).

https://www.codewars.com/kata/57096af70dad013aa200007b/train/c
*/

#include <stdbool.h>
#include <stddef.h>

enum Operator { AND, XOR, OR };

bool logical_calculator (size_t len, const bool booleans[len], enum Operator operator)
{
  bool result = booleans[0];
  for (size_t i = 1; i < len; i++)
  {
    bool next_bool = booleans[i];
    switch (operator) {
        case 0:
        result = result && next_bool;
        break;
        case 1:
        result = (result == next_bool) ? false : true;
        break;
        case 2:
        result = result || next_bool;
    }
  }
  return result;
}