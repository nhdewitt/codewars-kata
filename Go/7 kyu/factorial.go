/*
Your task is to write function factorial.

https://en.wikipedia.org/wiki/Factorial

https://www.codewars.com/kata/57a049e253ba33ac5e000212/train/go
*/

package kata

func Factorial(n int) int {
  prod := 1
  for i := n; i > 0; i-- {
    prod *= i
  }
  return prod
}