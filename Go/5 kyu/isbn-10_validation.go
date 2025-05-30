/*
ISBN-10 identifiers are ten digits long. The first nine characters are digits 0-9. The last digit can be 0-9 or X, to indicate a value of 10.

An ISBN-10 number is valid if the sum of the digits multiplied by their position modulo 11 equals zero.

For example:

ISBN     : 1 1 1 2 2 2 3 3 3  9
position : 1 2 3 4 5 6 7 8 9 10
This is a valid ISBN, because:

(1*1 + 1*2 + 1*3 + 2*4 + 2*5 + 2*6 + 3*7 + 3*8 + 3*9 + 9*10) % 11 = 0
Examples
1112223339   -->  true
111222333    -->  false
1112223339X  -->  false
1234554321   -->  true
1234512345   -->  false
048665088X   -->  true
X123456788   -->  false

https://www.codewars.com/kata/51fc12de24a9d8cb0e000001/train/go
*/

package kata

import (
  "strconv"
  "strings"
  )

func ValidISBN10(isbn string) bool {
  var checksum int
  if len(isbn) != 10 {							// short-circuit on invalid length
    return false
  }
  for i, n := range isbn[:len(isbn)-1] {		// everything up to last character must be a digit, short-circuit on invalid character
    j, ok := strconv.Atoi(string(n))
    if ok != nil {
      return false
    }
    checksum += j * (10 - i)					// multiply each digit by its position (10 - i)
  }
  last := string(isbn[len(isbn)-1])
  if strings.ToUpper(last) == "X"  {			// last character can be 'X' or 'x' or digit
    checksum += 10
  } else {
    j, ok := strconv.Atoi(string(last))
    if ok != nil {
      return false
    }
    checksum += j
  }
  return checksum % 11 == 0						// if all characters are valid, checksum must still be divisible by 11 to be true		
}