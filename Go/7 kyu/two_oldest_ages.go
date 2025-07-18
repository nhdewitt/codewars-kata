/*
The two oldest ages function/method needs to be completed. It should take an array of numbers as its argument and return the two highest numbers within the array. The returned value should be an array in the format [second oldest age,  oldest age].

The order of the numbers passed in could be any order. The array will always include at least 2 items. If there are two or more oldest age, then return both of them in array format.

For example (Input --> Output):

[1, 2, 10, 8] --> [8, 10]
[1, 5, 87, 45, 8, 8] --> [45, 87]
[1, 3, 10, 0]) --> [3, 10]

https://www.codewars.com/kata/511f11d355fe575d2c000001/train/go
*/

package kata

func TwoOldestAges(ages []int) [2]int {
  res := [2]int{0, 0}
  
  for _, v := range ages {
    if v > res[1] {
      res[0] = res[1]
      res[1] = v
    } else if v > res[0] {
      res[0] = v
    }
  }
  
  return res
}