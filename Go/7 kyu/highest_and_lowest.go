/*
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Examples
HighAndLow("1 2 3 4 5") // return "5 1"
HighAndLow("1 2 -3 4 5") // return "5 -3"
HighAndLow("1 9 3 4 -5") // return "9 -5"
Notes
All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.

https://www.codewars.com/kata/554b4ac871d6813a03000035/train/go
*/

package kata

import (
  "strings"
  "math"
  "strconv"
  "fmt"
)

func HighAndLow(in string) string {
  high := math.Inf(-1)
  low := math.Inf(1)
  split := strings.Fields(in)
  for _, spl := range split {
    s, _ := strconv.Atoi(spl)
    if float64(s) > high {
      high = float64(s)
    }
    if float64(s) < low {
      low = float64(s)
    }
  }
  return fmt.Sprintf("%d %d", int(high), int(low))
}