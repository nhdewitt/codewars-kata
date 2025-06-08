/*
Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

Examples
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""

https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/go
*/

package kata

import (
  "strings"
  "regexp"
  "strconv"
  )

func Order(sentence string) string {
  words := strings.Fields(sentence)
  ordered := make([]string, len(words))			// split words, make an output slice the size of the number of words
  re := regexp.MustCompile(`-?\d+`)				// regex to match a single digit
  for _, word := range words {
    digit := re.Find([]byte(word))				// for each word, pull out the digit with regex and convert to int
    idx, _ := strconv.Atoi(string(digit))
    ordered[idx-1] = word						// idx-1 - original string is 1-indexed
  }
  return strings.Join(ordered, " ")
}