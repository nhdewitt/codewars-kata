/*
Given two numbers and an arithmetic operator (the name of it, as a string), return the result of the two numbers having that operator used on them.

a and b will both be positive integers, and a will always be the first number in the operation, and b always the second.

The four operators are "add", "subtract", "divide", "multiply".

A few examples:(Input1, Input2, Input3 --> Output)

5, 2, "add"      --> 7
5, 2, "subtract" --> 3
5, 2, "multiply" --> 10
5, 2, "divide"   --> 2.5
Try to do it without using if statements!


https://www.codewars.com/kata/583f158ea20cfcbeb400000a/train/c
*/

double arithmetic(double a, double b, const char* operator) {
  switch (operator[0]) {
  case 'a':   return a + b;
  case 's':   return a - b;
  case 'm':   return a * b;
  case 'd':   return a / b;
  }
}