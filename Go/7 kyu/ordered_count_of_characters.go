/*
Count the number of occurrences of each character and return it as a (list of tuples) in order of appearance. For empty output return (an empty list).

Consult the solution set-up for the exact data structure implementation depending on your language.

Example:

OrderedCount("abracadabra") == []Tuple{Tuple{'a', 5}, Tuple{'b', 2}, Tuple{'r', 2}, Tuple{'c', 1}, Tuple{'d', 1}}

// Where
type Tuple struct {
    Char  rune
    Count int
}

https://www.codewars.com/kata/57a6633153ba33189e000074/train/go
*/

package orderedcount

// Use the preloaded Tuple struct as return type
// type Tuple struct {
//	Char  rune
//	Count int
// }

func OrderedCount(text string) []Tuple {
  histogram := make(map[rune]int)
  for _, r := range text {
    histogram[r]++
  }
  res := make([]Tuple, 0, len(histogram))
  seenSet := make(map[rune]struct{})
  for _, r := range text {
    if _, ok := seenSet[r]; !ok {
      res = append(res, Tuple{r, histogram[r]})
      seenSet[r] = struct{}{}
    }
  }
  return res
}