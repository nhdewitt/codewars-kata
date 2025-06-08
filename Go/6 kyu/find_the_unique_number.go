/*
There is an array with some numbers. All numbers are equal except for one. Try to find it!

findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.

https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/go
*/

package kata

func FindUniq(arr []float32) float32 { 
  same := arr[0]
  if arr[0] != arr[1] {					// if 0 != 1, the unique number is in the first three elements, no need to check the rest
    if arr[0] != arr[2] {
      return same
    }
    return arr[1]
  }
  for _, i := range arr[2:] {			// iterate through the rest of the slice until the unique number is found
    if i != same {
      return i
    }
  }
  return 0
}