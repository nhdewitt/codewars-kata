/*
Write a function that returns the smallest distance between two factors of a number. The input will always be a number greater than one.

Example:

13013 has factors: [ 1, 7, 11, 13, 77, 91, 143, 169, 1001, 1183, 1859, 13013]

Hence the answer will be 2 (=13-11)

https://www.codewars.com/kata/59b8614a5227dd64dc000008/train/go
*/

package kata

import "sort"

func Factors(n int) []int {				// generate factors up to sqrt(n), sort and return
  factors := make([]int, 0)
  for i := 1; i * i <= n; i++ {
    if n % i == 0 {
      factors = append(factors, i)
      if i != n/i {
        factors = append(factors, n/i)
      }
    }
  }
  sort.Ints(factors)
  return factors
}

func MinDistance(n int) int {
  distance := n - 1
  factors := Factors(n)
  if len(factors) == 2 { return distance }	// if there are only two factors, it's prime, so the difference is n-1
  for i := 0; i < len(factors)-1; i++ {
    d := factors[i+1] - factors[i]			// iterate through the slice, comparing diffs and updating distance if lower
    if d < distance {
      distance = d
      if d <= 2 {							// can short-circuit here as there won't be a difference smaller than 2 if one has already been seen (i.e. 11, 13 or 3, 5)
        break
      }
    }
  }
  return distance
}