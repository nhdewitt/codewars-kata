/*
Complete the method which returns the number which is most frequent in the given input array. If there is a tie for most frequent number, return the largest number among them.

Note: no empty arrays will be given.

Examples
[12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
[12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
[12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3

https://www.codewars.com/kata/5420fc9bb5b2c7fd57000004/train/go
*/

package kata

func HighestRank(nums []int) int {
  numFreq := make(map[int]int)
  
  for _, num := range nums {
    numFreq[num]++
  }
  
  highest, count := 0, 0
  for k, v := range numFreq {
    if v >= count {
      if v > count || (v == count && k > highest) {
        highest, count = k, v
      }
    }
  }
  return highest
}