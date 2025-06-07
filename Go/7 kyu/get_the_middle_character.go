/*
You are going to be given a non-empty string. Your job is to return the middle character(s) of the string.

If the string's length is odd, return the middle character.
If the string's length is even, return the middle 2 characters.
Examples:
"test" --> "es"
"testing" --> "t"
"middle" --> "dd"
"A" --> "A"

https://www.codewars.com/kata/56747fd5cb988479af000028/train/go
*/

package kata

func GetMiddle(s string) string {
  l := []rune(s)
  mid := len(l) / 2
  if len(l) % 2 == 0 {
    return s[mid-1:mid+1]
  }
  return string(s[mid])
}