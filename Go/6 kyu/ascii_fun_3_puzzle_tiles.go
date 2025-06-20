/*
Because my other two parts of the serie were pretty well received I decided to do another part.

Puzzle Tiles
You will get two Integer n(width) and m (height) and your task is to draw following pattern. Each line is seperated with '\n'.

Both integers are equal or greater than 1. No need to check for invalid parameters.
There are no whitespaces at the end of each line.
For example, for width = 4 and height = 3, you should draw the following pattern:

   _( )__ _( )__ _( )__ _( )__
 _|     _|     _|     _|     _|
(_   _ (_   _ (_   _ (_   _ (_
 |__( )_|__( )_|__( )_|__( )_|
 |_     |_     |_     |_     |_
  _) _   _) _   _) _   _) _   _)
 |__( )_|__( )_|__( )_|__( )_|
 _|     _|     _|     _|     _|
(_   _ (_   _ (_   _ (_   _ (_
 |__( )_|__( )_|__( )_|__( )_|
                                      
For more informations take a look in the test cases!

https://www.codewars.com/kata/5947d86e07693bcf000000c4/train/go
*/

package kata

import "strings"

func PuzzleTiles(n, m int) string {
  top := "_( )__"
  topTiles := make([]string, n)
  for i := range topTiles {
    topTiles[i] = top
  }
  
  topLine := "   " + strings.Join(topTiles, " ")
  
  even := strings.Join([]string{
    topLine,
    " _|" + strings.Repeat("     _|", n),
    "(_" + strings.Repeat("   _ (_", n),
    " |" + strings.Repeat("__( )_|", n),
  }, "\n")
  odd := strings.Join([]string{
    " |_" + strings.Repeat("     |_", n),
    "  _)" + strings.Repeat(" _   _)", n),
    " |" + strings.Repeat("__( )_|", n),
  }, "\n")
  
  evenLines := strings.Split(even, "\n")
  oddLines := strings.Split(odd, "\n")
  
  var res []string
  
 for i := 0; i < m; i++ {
   if i%2 == 0 {
     if i == 0 {
       res = append(res, evenLines...)
     } else {
       res = append(res, evenLines[1:]...)
     }
   } else {
     res = append(res, oddLines...)
   }
 }
  
  return strings.Join(res, "\n")
}