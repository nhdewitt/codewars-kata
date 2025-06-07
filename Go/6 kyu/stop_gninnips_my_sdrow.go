/*
Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples:

"Hey fellow warriors"  --> "Hey wollef sroirraw" 
"This is a test        --> "This is a test" 
"This is another test" --> "This is rehtona test"

https://www.codewars.com/kata/5264d2b162488dc400000001/train/go
*/

package kata

import "strings"

func SpinWords(str string) string {
  splitStr := strings.Fields(str)								// split on whitespace
  rev := func(s string) string {								// anonymous function to reverse a string
    r := []rune(s)
    for i, j := 0, len(r)-1; i < len(r)/2; i, j = i+1, j-1 {
      r[i], r[j] = r[j], r[i]
    }
    return string(r)
  }
  for i, split := range splitStr {
    if len(split) >= 5 {										// only need to reverse strings longer than 4
      splitStr[i] = rev(split)
    }
  }
  return strings.Join(splitStr, " ")							// rejoin with whitespace
}