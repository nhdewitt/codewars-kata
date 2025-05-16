/*
This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.

https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/go
*/

package kata

import "strings"

func Accum(s string) string {
  output := ""
  for i:=0;i<len(s);i++ {
    c := string(s[i])
    output += string(strings.ToUpper(c))
    for j:=1;j<=i;j++ {
      output += strings.ToLower(c)
    }
    if i != len(s) - 1 { output += string('-') }
  }
  return output
}