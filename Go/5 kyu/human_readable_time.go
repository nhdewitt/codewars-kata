/*
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.

https://www.codewars.com/kata/52685f7382004e774f0001f7/train/go
*/

package kata

import "fmt"

func HumanReadableTime(seconds int) string {
  h := seconds / 3600
  m := (seconds % 3600) / 60
  s := seconds % 3600 % 60
  return fmt.Sprintf("%02d:%02d:%02d", h, m, s)
}