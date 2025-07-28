/*
Write a function that given, an array arr, returns an array containing at each index i the amount of numbers that are smaller than arr[i] to the right.

For example:

* Input [5, 4, 3, 2, 1] => Output [4, 3, 2, 1, 0]
* Input [1, 2, 0] => Output [1, 1, 0]
If you've completed this one and you feel like testing your performance tuning of this same kata, head over to the much tougher version How many are smaller than me II?


https://www.codewars.com/kata/56a1c074f87bc2201200002e/train/go
*/

package kata

func Smaller(arr []int) []int {
  res := make([]int, len(arr))
  for i, a := range arr {
    innerCount := 0
    for _, b := range arr[i+1:] {
      if a > b {
        innerCount++
      }
    }
    res[i] = innerCount
  }
  return res
}