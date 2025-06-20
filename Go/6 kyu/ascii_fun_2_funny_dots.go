/*
Funny Dots
You will get two integers n (width) and m (height) and your task is to draw the following pattern. Each line is seperated with a newline (\n)

Both integers are equal or greater than 1; no need to check for invalid parameters.

Examples

                                            +---+---+---+
             +---+                          | o | o | o |
dot(1, 1) => | o |            dot(3, 2) =>  +---+---+---+            
             +---+                          | o | o | o |
                                            +---+---+---+

https://www.codewars.com/kata/59098c39d8d24d12b6000020/train/go
*/

package kata

import "strings"

func Dot(n, m int) string {
  var sb strings.Builder
  sb.Grow(m*(8*n + 4) + (4*n + 1))
  
  for j := 0; j < m; j++ {
    sb.WriteString(strings.Repeat("+---", n))
    sb.WriteString("+\n")
    sb.WriteString(strings.Repeat("| o ", n))
    sb.WriteString("|\n")
  }
  sb.WriteString(strings.Repeat("+---", n))
  sb.WriteString("+")
  
  return sb.String()
}
