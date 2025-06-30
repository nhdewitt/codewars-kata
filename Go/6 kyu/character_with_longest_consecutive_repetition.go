/*
For a given string s find the character c (or C) with longest consecutive repetition and return:

type Result struct {
    C rune // character
    L int  // count
}
where l (or L) is the length of the repetition. If there are two or more characters with the same l return the first in order of appearance.

For empty string return:

Result{}
Happy coding! :)


https://www.codewars.com/kata/586d6cefbcc21eed7a001155/train/go
*/

package kata

func LongestRepetition(text string) Result {
  runes := []rune(text)
  if len(runes) == 0 {
    return Result{}
  }
  
  res := Result{runes[0], 1}
  currentCount := 1
  
  for i := 1; i < len(runes); i++ {
    if runes[i] == runes[i-1] {
      currentCount++
    } else {
      currentCount = 1
    }
    
    if currentCount > res.L {
      res.C, res.L = runes[i], currentCount
    }
  }
  
  return res
}