/*
Build Tower
Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:

[
  "  *  ",
  " *** ", 
  "*****"
]
And a tower with 6 floors looks like this:

[
  "     *     ", 
  "    ***    ", 
  "   *****   ", 
  "  *******  ", 
  " ********* ", 
  "***********"
]

https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/go
*/

package kata

import "strings"


func TowerBuilder(nFloors int) []string {
  output := make([]string, 0)
  a := 1
  n := nFloors - 1
  for i := nFloors - 1; i > -1; i-- {
    var sb strings.Builder
    total := 2*n + a
    sb.Grow(total)
    sb.WriteString(strings.Repeat(" ", n))
    sb.WriteString(strings.Repeat("*", a))
    sb.WriteString(strings.Repeat(" ", n))
    output = append(output, sb.String())
    a += 2
    n--
  }
  return output
}