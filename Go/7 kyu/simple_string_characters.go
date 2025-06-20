/*
In this Kata, you will be given a string and your task will be to return a list of ints detailing the count of uppercase letters, lowercase, numbers and special characters (everything else), as follows.

The order is: uppercase letters, lowercase letters, numbers and special characters.

"*'&ABCDabcde12345" --> [ 4, 5, 5, 3 ]
More examples in the test cases.

Good luck!

https://www.codewars.com/kata/5a29a0898f27f2d9c9000058/train/go
*/

package kata

import "unicode"

func Solve(s string) []int {
  hashMap := map[string]int{
    "uppercase": 0,
    "lowercase": 0,
    "numbers":   0,
    "special":   0,
  }
  
  for _, r := range s {
    if unicode.IsUpper(r) {
      hashMap["uppercase"]++
    } else if unicode.IsLower(r) {
      hashMap["lowercase"]++
    } else if unicode.IsDigit(r) {
      hashMap["numbers"]++
    } else {
      hashMap["special"]++
    }
  }
  
  return []int{hashMap["uppercase"], hashMap["lowercase"], hashMap["numbers"], hashMap["special"]}
}