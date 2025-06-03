/*
1.  The input string will always consist of lowercase letters and spaces, but may be empty, in which case you must return an empty array. 2.  If the character in the string is whitespace then pass over it as if it was an empty seat

Examples
"hello" => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
" s p a c e s " => [ " S p a c e s ", " s P a c e s ", " s p A c e s ", " s p a C e s ", " s p a c E s ", " s p a c e S "]
Good luck and enjoy!

https://www.codewars.com/kata/58f5c63f1e26ecda7e000029/train/go
*/

package kata

import "strings"

func wave(words string) []string {
  output := []string{}
  for i := 0; i < len(words); i++ {
    inner := ""
    if string(words[i]) == " " {
      continue
    }
    inner += strings.ToLower(words[:i]) + strings.ToUpper(string(words[i])) + strings.ToLower(words[i+1:])
    output = append(output, inner)
  }
  return output
}