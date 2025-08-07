/*
This kata is a harder version of this kata: https://www.codewars.com/kata/5727bb0fe81185ae62000ae3

If you haven't done it yet, you should do that one first before doing this one.

You are given a string of letters that you need to type out. In the string there is a special function: [backspace]. Once you encounter a [backspace] , you delete the character right before it. If there is nothing to backspace , just carry on. Return the final string .

e.g. oopp[backspace]s return oops (delete the p)

Walkthrough:

o
oo
oop
oopp
oop [backspace]
oops

e.g. ooppp[backspace][backspace]s return oops (delete both p's)

Walkthrough:

o
oo
oop
oopp
ooppp
oopp [backspace]
oop [backspace]
oops

e.g. a[backspace][backspace]ooppp[backspace][backspace]s return oops

Walkthrough:

a
[nothing]
[nothing]
o
oo
oop
oopp
ooppp
oopp [backspace]
oop [backspace]
oops

But there's a twist! [backspace][backspace][backspace] can appear as [backspace]*3 or even [backspace]*2[backspace]

Basically, [backspace][backspace] ... [backspace] n times can appear as [backspace]*n (n can even be 1, but not less than 1 ([backspace]*0 will not occur))

e.g. a[backspace]*2oopppp[backspace]*2[backspace]s return oops

Walkthrough:

a
[nothing] [backspace]*2
o
oo
oop
oopp
ooppp
oopppp
oopp [backspace]*2
oop [backspace]
oops

To make it easier, only letters, spaces. and the [backspace] function will be in the initial string.

Good luck!


https://www.codewars.com/kata/62b3e38df90eac002c7a983f/train/go
*/

package kata

import (
  "regexp"
  "strconv"
  "strings"
)

var sub = regexp.MustCompile(`#\*([0-9]+)`)

func Solve(s string) string {
  s = strings.ReplaceAll(s, "[backspace]", "#")
  res := sub.ReplaceAllStringFunc(s, func(m string) string {
    parts := sub.FindStringSubmatch(m)
    n, err := strconv.Atoi(parts[1])
    if err != nil {
      return m
    }
    return strings.Repeat("#", n)
  })
  
  out := make([]rune, 0, len(res))
  for _, r := range res {
    if r == '#' {
      if len(out) > 0 {
        out = out[:len(out) - 1]
      }
    } else {
      out = append(out, r)
    }
  }
  return string(out)
}