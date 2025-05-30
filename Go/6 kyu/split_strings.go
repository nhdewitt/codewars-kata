/*
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']

https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/train/go
*/

package kata

func Solution(str string) []string {
  output := []string{}
  if len(str) % 2 != 0 {
    for i := 0; i < len(str) - 1; i += 2 {
      output = append(output, str[i:i+2])
    }
    output = append(output, str[len(str)-1:] + "_")
  } else {
    for i := 0; i < len(str); i += 2 {
      output = append(output, str[i:i+2])
    }
  }
  return output
}