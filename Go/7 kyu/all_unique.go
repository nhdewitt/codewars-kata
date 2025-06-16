/*
Write a program to determine if a string contains only unique characters. Return true if it does and false otherwise.

The string may contain any of the 128 ASCII characters. Characters are case-sensitive, e.g. 'a' and 'A' are considered different characters.

https://www.codewars.com/kata/553e8b195b853c6db4000048/train/go
*/

package kata

func HasUniqueChar (str string) bool {
  charSet := make(map[rune]bool)
  for _, r := range str {
    if _, ok := charSet[r]; ok {
      return false
    }
    charSet[r] = true
  }
  return true
}