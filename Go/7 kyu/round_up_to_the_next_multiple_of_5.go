/*
Given an integer as input, can you round it to the next (meaning, "greater than or equal") multiple of 5?

Examples:

input:    output:
0    ->   0
2    ->   5
3    ->   5
12   ->   15
21   ->   25
30   ->   30
-2   ->   0
-5   ->   -5
etc.
Input may be any positive or negative integer (including 0).

You can assume that all inputs are valid integers.

https://www.codewars.com/kata/55d1d6d5955ec6365400006d/train/go
*/

package kata

func RoundToNext5(n int) int {
  r := (n % 5)
  if r < 0  {  r += 5  }
  if r == 0 { return n }
  return (5 - r + n)
}