/*
In this Kata, you will be given an array of strings and your task is to remove all consecutive duplicate letters from each string in the array.

For example:

dup(["abracadabra","allottee","assessee"]) = ["abracadabra","alote","asese"].

dup(["kelless","keenness"]) = ["keles","kenes"].

Strings will be lowercase only, no spaces. See test cases for more examples.

Good luck!


https://www.codewars.com/kata/59f08f89a5e129c543000069/train/go
*/

package kata

import "strings"

func Dup(arr []string) []string {
  res := make([]string, len(arr))		// output slice is same length as arr
  
  for i, a := range arr {
    var sb strings.Builder
    sb.Grow(len(a))						// grow each inner strings.Builder to the length of a (although will probably be smaller with removed chars, it won't be larger)
    var last rune						// keep track of last seen
    for _, r := range a {
      if r != last {					// iterate through string, if it doesn't match, write it to the sb and set new last, otherwise nop
        sb.WriteRune(r)
        last = r
      }
    }
    res[i] = sb.String()				// write each string to the res array for return
  }
  return res
}