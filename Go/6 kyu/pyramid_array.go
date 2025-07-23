/*
Write a function that given an integer n >= 0, returns an array of n ascending length subarrays, all filled with 1s.

0 => [ ]
1 => [ [1] ]
2 => [ [1], [1, 1] ]
3 => [ [1], [1, 1], [1, 1, 1] ]


https://www.codewars.com/kata/515f51d438015969f7000013/train/go
*/

package kata

func Pyramid(n int) [][]int {
  if n <= 0 {
    return [][]int{}
  }
  
  res := make([][]int, n)
  for i := 0; i < n; i++ {
    row := make([]int, i + 1)
    for j := range row {
      row[j] = 1
    }
    res[i] = row
  }
  return res
}