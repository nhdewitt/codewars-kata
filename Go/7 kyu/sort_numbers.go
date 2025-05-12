/*
Finish the solution so that it sorts the passed in array of numbers. If the function passes in an empty array or null/nil value then it should return an empty array.

For example:

solution(c(1, 2, 3, 10, 5)) # should return c(1, 2, 3, 5, 10)
solution(NULL)              # should return NULL

https://www.codewars.com/kata/5174a4c0f2769dd8b1000003/train/go
*/

package kata

import "sort"

func SortNumbers(numbers []int) []int {
  sort.Slice(numbers, func(i, j int) bool {
    return numbers[i] < numbers[j]
  })
  return numbers
}