/*
You will get an odd integer n (n >= 3) and your task is to draw an X. The lines are separated by newlines (\n).

Use the following characters: '■' and '□' (Ruby, Crystal and PHP: 'o' and ' ').

Examples
                                     ■□□□■
            ■□■                      □■□■□
  x(3) =>   □■□             x(5) =>  □□■□□
            ■□■                      □■□■□
                                     ■□□□■

*/

package kata

import "strings"

func X(n int) string {
  var sb strings.Builder
  sb.Grow(n*(n+1))				// n*(n+1) for NxN grid with newline at the end
  
  midPoint := (n/2)				// calculate midpoint, split the loop between the two halves to deal with one white square on the middle line
  
  for i := 0; i < midPoint; i++ {
    sb.WriteString(strings.Repeat("□", i) + "■" + strings.Repeat("□", (n-2 - (2*i))) + "■" + strings.Repeat("□", i) + "\n")	// outer black squares gradually grow and inner black squares gradually shrink by 2 each iteration
  }
  
  sb.WriteString(strings.Repeat("□", midPoint) + "■" + strings.Repeat("□", midPoint) + "\n")
  
  for i := midPoint-1; i >= 0; i-- {
    sb.WriteString(strings.Repeat("□", i) + "■" + strings.Repeat("□", (n-2 - (2*i))) + "■" + strings.Repeat("□", i) + "\n")
  }
  
  return strings.TrimRight(sb.String(), "\n")
}