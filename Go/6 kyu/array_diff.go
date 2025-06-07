/*
Implement a function that computes the difference between two lists. The function should remove all occurrences of elements from the first list (a) that are present in the second list (b). The order of elements in the first list should be preserved in the result.

Examples
If a = [1, 2] and b = [1], the result should be [2].

If a = [1, 2, 2, 2, 3] and b = [2], the result should be [1, 3].

https://www.codewars.com/kata/523f5d21c841566fde000009/train/go
*/

package kata

func ArrayDiff(a, b []int) []int {
  seen := make(map[int]struct{})			// set to track elements in b
  output := make([]int, 0)					// final output
  for _, second := range b {
    seen[second] = struct{}{}				// track each element in b that is seen
  }
  for _, first := range a {
    if _, ok := seen[first]; !ok {
      output = append(output, first)		// if not in seen, can append to output
    }
  }
  return output
}