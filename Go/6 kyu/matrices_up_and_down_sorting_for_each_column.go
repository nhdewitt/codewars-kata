/*
You are given a matrix M, of positive and negative integers. It should be sorted in an up and down column way, starting always with the lowest element placed at the top left position finishing with the highest depending on n value: at the bottom right position if the number of columns,n, is odd, or placed at the top right, if n is even.

E.g.:

M = [[-20, -4, -1],
     [  1,  4,  7], 
     [  8, 10, 12]]
     
M_ = [[-20, 7, 8],
      [-4, 4, 10],
      [-1, 1, 12]]
In order to be more understandable we show the directions of the sorting for the new matrix with arrows:

source: imgur.com

Create the function up_down_col_sort() that receives a matrix as an argument and may do this kind of sorting.

Your function will be tested with square or rectangular matrices of m rows and n columns Features of the random tests:

Number of tests = 120
10 <= m <= 200
10 <= n <= 200
-1000 <= M[i,j] <= 1000
The kata is available at Python 2, Typescript, Javascript and Ruby at the moment. Translations into another languages will be released soon.

https://www.codewars.com/kata/590b8d5cee471472f40000aa/train/go
*/

package kata

import "sort"

func UpDownColSort(matrix [][]int) [][]int {
  rows, cols := len(matrix), len(matrix[0])
  nums := make([]int, 0, rows * cols)			// slice to hold all the values of the matrix for sorting
  for _, row := range matrix {
    for _, v := range row {
      nums = append(nums, v)
    }
  }
  sort.Ints(nums)
  output := make([][]int, rows)					// output size capacity rows filled with slices of capacity cols
  for i := range output {
    output[i] = make([]int, cols)
  }
  idx := 0										// track where we are at in the nums slice
  for col := 0; col < cols; col++ {				// iterate column by column
    if col % 2 == 0 {							// two separate conditions: even index, go down; odd index, go up
      for row := 0; row < rows; row++ {
        output[row][col] = nums[idx]
        idx++
      }
    } else {
      for row := rows - 1; row >= 0; row-- {
        output[row][col] = nums[idx]
        idx++
      }
    }
  }
  return output
}