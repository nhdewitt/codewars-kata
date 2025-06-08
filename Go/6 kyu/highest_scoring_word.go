/*
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

For example, the score of abad is 8 (1 + 2 + 1 + 4).

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.

https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/go
*/

package kata

import "strings"

func High(s string) string {
  charScores := make(map[rune]int)
  for r, i := 'a', 1; r <= 'z'; r, i = r+1, i+1 {
    charScores[r] = i
  }
  var highestScore int
  idx := 0
  words := strings.Fields(s)
  for i, word := range words {
    sum := 0
    for _, r := range word {
      sum += charScores[r]
    }
    if sum > highestScore {
      highestScore = sum
      idx = i
    }
  }
  return words[idx]
}