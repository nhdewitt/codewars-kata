/*
Everyone knows passphrases. One can choose passphrases from poems, songs, movies names and so on but frequently they can be guessed due to common cultural references. You can get your passphrases stronger by different means. One is the following:

choose a text in capital letters including or not digits and non alphabetic characters,

shift each letter by a given number but the transformed letter must be a letter (circular shift),
replace each digit by its complement to 9,
keep such as non alphabetic and non digit characters,
downcase each letter in odd position, upcase each letter in even position (the first character is in position 0),
reverse the whole result.
Example:
your text: "BORN IN 2015!", shift 1

1 + 2 + 3 -> "CPSO JO 7984!"

4 "CpSo jO 7984!"

5 "!4897 Oj oSpC"

With longer passphrases it's better to have a small and easy program. Would you write it?

https://en.wikipedia.org/wiki/Passphrase

https://www.codewars.com/kata/559536379512a64472000053/train/go
*/

package kata

import (
  "strings"
  "unicode"
)

// ReverseString returns the reverse of a string
func ReverseString(s string) string {
  r := []rune(s)
  for i, j := 0, len(r)-1; i < len(r)/2; i, j = i+1, j-1 {
    r[i], r[j] = r[j], r[i]
  }
  return string(r)
}

// PlayPass: rotates a letter by n, replaces each digit by its complement,
// ignores non-alpha and non-numeric characters, shifts each letter in an odd
// index to lowercase, shifts each letter in an even index to uppercase, and returns
// this string reversed
func PlayPass(s string, n int) string {    
  numComplements := map[rune]rune{
    '0': '9', '1': '8', '2': '7', '3': '6', '4': '5', '5': '4', '6': '3', '7': '2', '8': '1', '9': '0',
  }
  alphaLower := "abcdefghijklmnopqrstuvwxyz"
  alphaUpper := strings.ToUpper(alphaLower)
  rotLower := alphaLower[n:] + alphaLower[:n]				// used to map the rotated alphabet to rot-x
  rotUpper := alphaUpper[n:] + alphaUpper[:n]
  
  transTable := make(map[rune]rune, 52)						// used to translate each character
  for i, r := range alphaLower {
    transTable[r] = rune(rotLower[i])
    transTable[rune(alphaUpper[i])] = rune(rotUpper[i])
  }
  
  var sb strings.Builder
  sb.Grow(len(s))
  
  for i, r := range s {
    if mapped, ok := transTable[r]; ok {					// first see if the rune is in the translation table
      if i % 2 == 0 {
        sb.WriteRune(unicode.ToUpper(mapped))				// if so, check the index to see the desired case
      } else {
        sb.WriteRune(unicode.ToLower(mapped))
      }
      
    } else if numCheck, ok2 := numComplements[r]; ok2 {		// if not in the translation table, check the number complements
      sb.WriteRune(numCheck)
    } else {
      sb.WriteRune(r)										// if neither, just append the original rune
    }
  }
  return ReverseString(sb.String())							// run through ReverseString() before returning
}