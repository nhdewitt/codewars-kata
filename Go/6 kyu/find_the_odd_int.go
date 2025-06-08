/*
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).

https://www.codewars.com/kata/54da5a58ea159efa38000836/train/go
*/

package kata

func FindOdd(seq []int) int {
  if len(seq) == 1 {				// if count=1, the only element is the answer
    return seq[0]
  }
  freqMap := make(map[int]int)
  for _, s := range seq {
    freqMap[s]++					// frequency count map of each integer and number of appearances
  }
  for k, v := range freqMap {
    if v % 2 != 0 {
      return k						// return the one that's odd
    }
  }
  return 0
}