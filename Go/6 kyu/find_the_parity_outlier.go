/*
You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)

https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/go
*/

package kata

func abs(i int) int {							// avoid type conversion from math.Abs
  if i < 0 {
    return -i
  }
  return i
}

func FindOutlier(integers []int) int {
  check := 0
  for _, integer := range integers[:3] {		// only need to check the first three to determine parity
    check += abs(integer) % 2					// abs to avoid negatives if integer < 0
  }
  if check > 1 {								// check > 1 means we're looking for the only even number
    for _, integer := range integers {
      if abs(integer) % 2 == 0 {
        return integer
      }
    }
  } else {
    for _, integer := range integers {			// check <= 1 means we're looking for the only odd number
      if abs(integer) % 2 != 0 {
        return integer
      }
    }
  }
  return 0
}