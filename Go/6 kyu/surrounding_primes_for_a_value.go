/*
The result should be output in a list like the following:

prime_bef_aft(n) == [befPrime, aftPrime]
If n is a prime number it will give two primes, n will not be included in the result.

Let's see some cases:

prime_bef_aft(100) == [97, 101]

prime_bef_aft(97) == [89, 101]

prime_bef_aft(101) == [97, 103]
Range for the random tests: 1000 <= n <= 200000

(The extreme and special case n = 2 will not be considered for the tests. Thanks Blind4Basics)

Happy coding!!

https://www.codewars.com/kata/560b8d7106ede725dd0000e2/train/go
*/

package kata

import (
  "math"
  "sort"
)

type Sieve struct {								// Sieve struct will hold all primes
  max           int
  isComposite   []bool
  primes        []int
}

func NewSieve(max int) *Sieve {					// construct the sieve up to max
  s := &Sieve{
    max:          max,
    isComposite:  make([]bool, max+1),
  }
  limit := int(math.Sqrt(float64(max)))
  
  for i := 2; i <= limit; i++ {
    if s.isComposite[i] {
      continue
    }
    for j := i * i; j <= max; j += i {
      s.isComposite[j] = true
    }
  }
  
  s.primes = make([]int, 0, max/int(math.Log(float64(max))))
  for i := 2; i <= max; i++ {
    if !s.isComposite[i] {
      s.primes = append(s.primes, i)
    }
  }
  return s
}

func (s *Sieve) IsPrime(n int) bool {
  return !s.isComposite[n]
}

func (s *Sieve) Neighbors(n int) [2]int {					// binary search to find the nearest primes on each side
  idx := sort.SearchInts(s.primes, n)
  lower, upper := 0, 0
  if idx > 0 && s.primes[idx-1] < n {
    lower = s.primes[idx-1]
  }
  if idx < len(s.primes) {									// need to distinguish between when n is prime (return idx+1) and when it is not (return idx)
    switch {
    case s.primes[idx] == n:
      upper = s.primes[idx+1]
    case s.primes[idx] > n:
      upper = s.primes[idx]
    }
  }
  return [2]int{lower, upper}
}

func PrimeBefAft(n int) [2]int {
  s := NewSieve(200_000)
  return s.Neighbors(n)
}