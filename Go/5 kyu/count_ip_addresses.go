/*
Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).

All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.

Examples
* With input "10.0.0.0", "10.0.0.50"  => return   50 
* With input "10.0.0.0", "10.0.1.0"   => return  256 
* With input "20.0.0.10", "20.0.1.0"  => return  246

https://www.codewars.com/kata/526989a41034285187000de4/train/go
*/

package kata

import (
  "strings"
  "strconv"
  )

func IpsBetween(start, end string) int {
  startIP := strings.Split(start, ".")
  endIP := strings.Split(end, ".")
  
  var sum int
  for i, shift := range[]uint{24, 16, 8, 0} {
    s, _ := strconv.Atoi(startIP[i])
    e, _ := strconv.Atoi(endIP[i])
    
    sum += (e - s) << shift
  }
  return sum
}