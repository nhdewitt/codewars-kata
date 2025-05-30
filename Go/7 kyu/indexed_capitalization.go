/*
Given a string and an array of integers representing indices, capitalize all letters at the given indices.

For example:

capitalize("abcdef",[1,2,5]) = "aBCdeF"
capitalize("abcdef",[1,2,5,100]) = "aBCdeF". There is no index 100.
The input will be a lowercase string with no spaces and an array of digits.

Good luck!

Be sure to also try:

Alternate capitalization

String array revisal

https://www.codewars.com/kata/59cfc09a86a6fdf6df0000f1/train/go
*/

package kata

import "unicode"

func Capitalize(st string, arr []int) string {
  runes := []rune(st)
  for _, i := range arr {
    if i >= len(runes) {
      continue
    }
    runes[i] = unicode.ToUpper(runes[i])
  }
  return string(runes)
}