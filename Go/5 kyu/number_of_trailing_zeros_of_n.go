/*
Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 * 2 * 3 *  ... * N

Be careful 1000! has 2568 digits...

For more info, see: http://mathworld.wolfram.com/Factorial.html

Examples
N	Product	N factorial	Trailing zeros
6	1*2*3*4*5*6	720	1
12	1*2*3*4*5*6*7*8*9*10*11*12	479001600	2
Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros.

https://www.codewars.com/kata/52f787eb172a8b4ae1000a34/train/go
*/

package kata

import "math"

func Zeros(n int) int {
  zeros := 0.0
  divisor := 5
  for divisor <= n {
    zeros += math.Floor(float64(n) / float64(divisor))
    divisor *= 5
  }
  return int(zeros)
}