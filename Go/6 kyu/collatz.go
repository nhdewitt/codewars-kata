/*
Preface
A collatz sequence, starting with a positive integern, is found by repeatedly applying the following function to n until n == 1 :

f
(
n
)
=
{
n
/
2
,
 if 
n
 is even
3
n
+
1
,
 if 
n
 is odd
f(n)={ 
n/2, if n is even
3n+1, if n is odd
​
 

A more detailed description of the collatz conjecture may be found on Wikipedia.

The Problem
Create a function collatz that returns a collatz sequence string starting with the positive integer argument passed into the function, in the following form:

"X0->X1->...->XN"

Where Xi is each iteration of the sequence and N is the length of the sequence.

Sample Input
Input: 4
Output: "4->2->1"

Input: 3
Output: "3->10->5->16->8->4->2->1"
Don't worry about invalid input. Arguments passed into the function are guaranteed to be valid integers >= 1.

https://www.codewars.com/kata/5286b2e162056fd0cb000c20/train/go
*/

package kata

import (
  "strings"
  "strconv"
)

func Collatz(n int) string {
  if n == 1 {
    return "1"
  }
  sequence := []string{strconv.Itoa(n)}
  for n > 1 {
    if n % 2 == 0 {
      n /= 2
    } else {
      n = (3 * n) + 1
    }
    sequence = append(sequence, strconv.Itoa(n))
  }
  return strings.Join(sequence, "->")
}