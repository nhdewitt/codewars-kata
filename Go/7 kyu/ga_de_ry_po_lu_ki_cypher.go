/*
Introduction
The GADERYPOLUKI is a simple substitution cypher used in scouting to encrypt messages. The encryption is based on short, easy to remember key. The key is written as paired letters, which are in the cipher simple replacement.

The most frequently used key is "GA-DE-RY-PO-LU-KI".

 G => A
 g => a
 a => g
 A => G
 D => E
  etc.
The letters, which are not on the list of substitutes, stays in the encrypted text without changes.

Task
Your task is to help scouts to encrypt and decrypt thier messages. Write the Encode and Decode functions.

Input/Output
The input string consists of lowercase and uperrcase characters and white . The substitution has to be case-sensitive.

Example
 Encode("ABCD")          // => GBCE 
 Encode("Ala has a cat") // => Gug hgs g cgt 
 Encode("gaderypoluki")  // => agedyropulik
 Decode("Gug hgs g cgt") // => Ala has a cat 
 Decode("agedyropulik")  // => gaderypoluki
 Decode("GBCE")          // => ABCD

https://www.codewars.com/kata/592a6ad46d6c5a62b600003f/train/go
*/

package kata

import "strings"

const (
  decode = "GDRPLKgdrplkAEYOUIaeyoui"
  encode = "AEYOUIaeyouiGDRPLKgdrplk"
)

var (
  decMap = make(map[rune]rune, len(encode))
  encMap = make(map[rune]rune, len(decode))
)

func init() {
  for i, d := range decode {
    e := rune(encode[i])
    decMap[e] = d
    encMap[d] = e
  }
}

func Decode(str string) string {
  var sb strings.Builder
  for _, r := range str {
    if mapped, ok := decMap[r]; ok {
      sb.WriteRune(mapped)
    } else {
      sb.WriteRune(r)
    }
  }
  return sb.String()
}

func Encode(str string) string {
  var sb strings.Builder
  for _, r := range str {
    if mapped, ok := encMap[r]; ok {
      sb.WriteRune(mapped)
    } else {
      sb.WriteRune(r)
    }
  }
  return sb.String()
}