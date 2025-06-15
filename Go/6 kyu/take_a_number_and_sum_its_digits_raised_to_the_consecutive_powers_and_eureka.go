/*
The number 
89
89 is the first integer with more than one digit that fulfills the property partially introduced in the title of this kata. What's the use of saying "Eureka"? Because this sum gives the same number: 
89
=
8
1
+
9
2
89=8 
1
 +9 
2
 

The next number in having this property is 
135
135:

See this property again: 
135
=
1
1
+
3
2
+
5
3
135=1 
1
 +3 
2
 +5 
3
 

Task
We need a function to collect these numbers, that may receive two integers 
a
a, 
b
b that defines the range 
[
a
,
b
]
[a,b] (inclusive) and outputs a list of the sorted numbers in the range that fulfills the property described above.

Examples
Let's see some cases (input -> output):

1, 10  --> [1, 2, 3, 4, 5, 6, 7, 8, 9]
1, 100 --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
If there are no numbers of this kind in the range 
[
a
,
b
]
[a,b] the function should output an empty list.

90, 100 --> []
Enjoy it!!

https://www.codewars.com/kata/5626b561280a42ecc50000d1/train/go
*/

package kata

import "strconv"

func intPow(base, exp uint64) uint64 {
  var result uint64 = 1
  for i := uint64(0); i < exp; i++ {
    result *= base
  }
  return result
}

func IsEureka(n uint64) bool {
  s := strconv.FormatUint(n, 10)
  var sum uint64 = 0
  for i, r := range s {
    d := uint64(r - '0')
    sum += intPow(d, uint64(i+1))
  }
  return sum == n
}

func SumDigPow(a, b uint64) []uint64 {
  eureka := make([]uint64, 0)
  for i := a; i <= b; i++ {
    if IsEureka(i) {
      eureka = append(eureka, i)
    }
  }
  return eureka
}