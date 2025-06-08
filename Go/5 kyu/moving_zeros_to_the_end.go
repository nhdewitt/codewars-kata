/*
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

MoveZeros([]int{1, 2, 0, 1, 0, 1, 0, 3, 0, 1}) // returns []int{ 1, 2, 1, 1, 3, 1, 0, 0, 0, 0 }

https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/go
*/

package kata

func MoveZeros(arr []int) []int {
  i, j, l := 0, 0, len(arr)				// two pointers
  for i < l {
    if arr[i] == 0 {					// if pointer i == 0, only increment i
      i++
    } else if i == j {					// if both are pointing to the same and i is not 0, increment both
      i++
      j++
    } else {
      arr[j] = arr[i]					// swap j and i, set i to 0, increment both
      arr[i] = 0
      i++
      j++
    }
  }
  return arr
}