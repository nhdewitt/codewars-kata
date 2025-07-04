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

https://www.codewars.com/kata/583f158ea20cfcbeb400000a/train/go
*/

package kata

func Arithmetic(a int, b int, operator string) int{
  lambdas := map[string]func(int, int) int{
    "add": func(x, y int) int { return x + y },
    "subtract": func(x, y int) int { return x - y },
    "multiply": func(x, y int) int { return x * y },
    "divide": func(x, y int) int { return x / y },
  }
  return lambdas[operator](a, b)
}