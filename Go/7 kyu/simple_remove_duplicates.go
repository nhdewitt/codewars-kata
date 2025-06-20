/*
Remove the duplicates from a list of integers, keeping the last ( rightmost ) occurrence of each element.

Example:
For input: [3, 4, 4, 3, 6, 3]

remove the 3 at index 0
remove the 4 at index 1
remove the 3 at index 3
Expected output: [4, 6, 3]

More examples can be found in the test cases.

Good luck!

https://www.codewars.com/kata/5ba38ba180824a86850000f7/train/go
*/

package kata 

func Solve(arr []int) []int {
  numberCount := make(map[int]int)
  for _, a := range arr {
    numberCount[a]++
  }
  res := make([]int, 0, len(numberCount))
  for _, a := range arr {
    if numberCount[a] > 1 {
      numberCount[a]--
    } else {
      res = append(res, a)
    }
  }
  return res
}