/*
1, 246, 2, 123, 3, 82, 6, 41 are the divisors of number 246.

Squaring these divisors we get: 1, 60516, 4, 15129, 9, 6724, 36, 1681.

The sum of these squares is 84100 which is 290 * 290.

Task
Find all integers between m and n (m and n are integers with 1 <= m <= n) such that the sum of their squared divisors is itself a square.

We will return an array of subarrays or of tuples (in C an array of Pair) or a string.

The subarrays (or tuples or Pairs) will have two elements: first the number the squared divisors of which is a square and then the sum of the squared divisors.

Example:
m =  1, n = 250 --> [[1, 1], [42, 2500], [246, 84100]]
m = 42, n = 250 --> [[42, 2500], [246, 84100]]
The form of the examples may change according to the language, see "Sample Tests".

Note
In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing whitespace: you can use dynamically allocated character strings.

https://www.codewars.com/kata/55aa075506463dac6600010d/train/go
*/

package kata

import "math"

func ListSquared(m, n int)  [][]int {
  pairs := make([][]int, 0)
  for i := m; i <= n; i++ {
    j := GetDivisorsAndSquare(i)
    if isPerfectSquare(j) {
      pairs = append(pairs, []int{i, j})
    }
  }
  return pairs
}

func isPerfectSquare(n int) bool {
  root := int(math.Sqrt(float64(n)))
  return (root * root) == n
}

func GetDivisorsAndSquare(x int) int {
  total := 0
  limit := int(math.Sqrt(float64(x)))
  for i := 1; i <= limit; i++ {
    if x % i == 0 {
      total += i * i
      if i != x / i {
        total += (x / i) * (x / i)
      }
    }
  }
  return total
}