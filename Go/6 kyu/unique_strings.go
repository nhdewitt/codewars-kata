/*
Given a string that contains only letters, you have to find out the number of unique strings (including the string itself) that can be produced by re-arranging the letters of the string. Strings are case insensitive.

HINT: Generating all the unique strings and calling length on that isn't a great solution for this problem. It can be done a lot faster...

Examples
uniqcount("AB") = 2      # "AB", "BA"
uniqcount("ABC") = 6     # "ABC", "ACB", "BAC", "BCA", "CAB", "CBA"
uniqcount("ABA") = 3     # "AAB", "ABA", "BAA"
uniqcount("ABBb") = 4    # "ABBB", "BABB", "BBAB", "BBBA"
uniqcount("AbcD") = 24   # "ABCD", etc.

https://www.codewars.com/kata/586c7cd3b98de02ef60001ab/train/go
*/

package kata


import (
  "math/big"
  "strings"
)

func fact(n int64) *big.Int {
  res := big.NewInt(1)
  for i := int64(2); i <= n; i++ {
    res.Mul(res, big.NewInt(i))
  }
  return res
}

func UniqCount(s string) *big.Int {
  s = strings.ToLower(s)								// case-insensitive
  hashMap := make(map[rune]int)
  
  for _, r := range s {									// looking for more than one of characters
    hashMap[r]++
  }
  
  total := int64(len(s))
  numerator := fact(total)
  
  denominator := big.NewInt(1)
  for _, count := range hashMap {
    if count > 1 {
      denominator.Mul(denominator, fact(int64(count)))
    }
  }
  
  return numerator.Div(numerator, denominator)			// nPr = n! / (n-r)!
}