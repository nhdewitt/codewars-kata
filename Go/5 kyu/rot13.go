/*
How can you tell an extrovert from an introvert at NSA?
Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it?
According to Wikipedia, ROT13 is frequently used to obfuscate jokes on USENET.

For this task you're only supposed to substitute characters. Not spaces, punctuation, numbers, etc.

Test examples:

"EBG13 rknzcyr." -> "ROT13 example."

"This is my first ROT13 excercise!" -> "Guvf vf zl svefg EBG13 rkprepvfr!"

https://www.codewars.com/kata/52223df9e8f98c7aa7000062/train/go
*/

package kata

import "strings"

func Rot13(msg string) string {
  alphaLower := "abcdefghijklmnopqrstuvwxyz"
  alphaUpper := strings.ToUpper(alphaLower)
  rotLower := alphaLower[13:] + alphaLower[:13]
  rotUpper := alphaUpper[13:] + alphaUpper[:13]
  
  transTable := make(map[rune]rune, 52)
  for i, r := range alphaLower {
    transTable[r] = rune(rotLower[i])
    transTable[rune(alphaUpper[i])] = rune(rotUpper[i])
  }
  
  var sb strings.Builder
  sb.Grow(len(msg))
  
  for _, r := range msg {
    if mapped, ok := transTable[r]; ok {
      sb.WriteRune(mapped)
    } else {
      sb.WriteRune(r)
    }
  }
  return sb.String()
}