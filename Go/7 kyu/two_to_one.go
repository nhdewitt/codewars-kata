/*
Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string (alphabetical ascending), the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

https://www.codewars.com/kata/5656b6906de340bd1b0000ac/train/go
*/

package kata

import "strings"

func TwoToOne(s1 string, s2 string) string {
  letterSet := make(map[rune]struct{})
  var sb strings.Builder
  
  for _, r := range s1 {
    letterSet[r] = struct{}{}
  }
  
  for _, r := range s2 {
    letterSet[r] = struct{}{}
  }
  
  for i := 'a'; i <= 'z'; i++ {
    if _, ok := letterSet[i]; !ok {
      continue
    }
    sb.WriteRune(i)
  }
  return sb.String()
}