/*
The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 
Notes
Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!

https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/go
*/

package kata

import "strings"

func DuplicateEncode(word string) string {
  charFreq := map[rune]int{}
  for _, r := range strings.ToLower(word) {
    charFreq[r]++
  }
  var sb strings.Builder
  for _, r := range strings.ToLower(word) {
    if charFreq[r] > 1 {
      sb.WriteString(")")
    } else {
      sb.WriteString("(")
    }
  }
  return sb.String()
}