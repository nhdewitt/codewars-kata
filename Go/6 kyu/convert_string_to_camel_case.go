/*
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"

https://www.codewars.com/kata/517abf86da9663f1d2000003/train/go
*/

package kata

import (
  "strings"
  "unicode"
  )

func ToCamelCase(s string) string {
  if s == "" {
    return ""
  }
  
  replacer := strings.NewReplacer("_", " ", "-", " ")
  s = replacer.Replace(s)

  split := strings.Fields(s)
  output := split[0]
  
  for _, w := range split[1:] {
    if w == "" {
      continue
    }
    w = strings.ToLower(w)
    r := []rune(w)
    r[0] = unicode.ToUpper(r[0])
    output += string(r)
  }
  return output
}