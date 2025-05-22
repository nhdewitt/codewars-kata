/*
Strong number is a number with the sum of the factorial of its digits is equal to the number itself.

For example, 145 is strong, because 1! + 4! + 5! = 1 + 24 + 120 = 145.

Task
Given a positive number, find if it is strong or not, and return either "STRONG!!!!" or "Not Strong !!".

Examples
1 is a strong number, because 1! = 1, so return "STRONG!!!!".
123 is not a strong number, because 1! + 2! + 3! = 9 is not equal to 123, so return "Not Strong !!".
145 is a strong number, because 1! + 4! + 5! = 1 + 24 + 120 = 145, so return "STRONG!!!!".
150 is not a strong number, because 1! + 5! + 0! = 122 is not equal to 150, so return "Not Strong !!".


https://www.codewars.com/kata/5a4d303f880385399b000001/train/go
*/

package kata

func Strong(n int) string {
  var fact = [10]int{1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880}   // 0! - 9! (check by digit)
  m := n
  sum := 0
  for m > 0 {
    d := m % 10
    sum += fact[d]
    if sum > n {
      return "Not Strong !!"
    }
    m /= 10
  }
  if sum == n {
    return "STRONG!!!!"
  }
  return "Not Strong !!"
}