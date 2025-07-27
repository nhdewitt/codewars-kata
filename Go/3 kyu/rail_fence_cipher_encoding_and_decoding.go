/*
Create two functions to encode and then decode a string using the Rail Fence Cipher. This cipher is used to encode a string by placing each character successively in a diagonal along a set of "rails". First start off moving diagonally and down. When you reach the bottom, reverse direction and move diagonally and up until you reach the top rail. Continue until you reach the end of the string. Each "rail" is then read left to right to derive the encoded string.

For example, the string "WEAREDISCOVEREDFLEEATONCE" could be represented in a three rail system as follows:

W       E       C       R       L       T       E
  E   R   D   S   O   E   E   F   E   A   O   C  
    A       I       V       D       E       N    
The encoded string would be:

WECRLTEERDSOEEFEAOCAIVDEN
Write a function/method that takes 2 arguments, a string and the number of rails, and returns the ENCODED string.

Write a second function/method that takes 2 arguments, an encoded string and the number of rails, and returns the DECODED string.

For both encoding and decoding, assume number of rails >= 2 and that passing an empty string will return an empty string.

Note that the example above excludes the punctuation and spaces just for simplicity. There are, however, tests that include punctuation. Don't filter out punctuation as they are a part of the string.


https://www.codewars.com/kata/58c5577d61aefcf3ff000081/train/go
*/

package kata

import "strings"

func Encode(s string,n int) string {
  encodedStrings := make([][]rune, n)
  
  runes := []rune(s)
  if n <= 1 || n >= len(s) {
    return s
  }
  
  j := 0
  step := 1
  
  for _, r := range runes {
    encodedStrings[j] = append(encodedStrings[j], r)    
    j += step
    if j == 0 || j == n - 1 {
      step = -step
    }
  }
  
  var sb strings.Builder
  sb.Grow(len(runes))
  
  for _, row := range encodedStrings {
    sb.WriteString(string(row))
  }
  
  return sb.String()
}

func Decode(s string,n int) string {
  decodedStrings := make([][]rune, n)
  
  runes := []rune(s)
  rowCounts := make([]int, n)
  if n <= 1 || n >= len(s) {
    return s
  }
  
  j := 0
  step := 1
  
  for range runes {
    rowCounts[j]++
    j += step
    if j == 0 || j == n - 1 {
      step = -step
    }
  }
  
  idx := 0
  for i := 0; i < n; i++ {
    decodedStrings[i] = runes[idx:idx + rowCounts[i]]
    idx += rowCounts[i]
  }
  
  j = 0
  step = 1
  rowPositions := make([]int, n)
  
  var sb strings.Builder
  sb.Grow(len(runes))
  
  for range runes {
    sb.WriteRune(decodedStrings[j][rowPositions[j]])
    rowPositions[j]++
    
    j += step
    if j == 0 || j == n - 1 {
      step = -step
    }
  }
  return sb.String()
}