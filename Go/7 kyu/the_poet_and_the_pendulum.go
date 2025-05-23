/*
Scenario
the rhythm of beautiful musical notes is drawing a Pendulum

Beautiful musical notes are the Numbers

Task
Given an array/list [] of n integers , Arrange them in a way similar to the to-and-fro movement of a Pendulum

The Smallest element of the list of integers , must come in center position of array/list.

The Higher than smallest , goes to the right .
The Next higher number goes to the left of minimum number and So on , in a to-and-fro manner similar to that of a Pendulum.

!alt

Notes
Array/list size is at least 3 .

In Even array size , The minimum element should be moved to (n-1)/2 index (considering that indexes start from 0)

Repetition of numbers in the array/list could occur , So (duplications are included when Arranging).

Input >> Output Examples:
pendulum ([6, 6, 8 ,5 ,10]) ==> [10, 6, 5, 6, 8]
Explanation:
Since , 5 is the The Smallest element of the list of integers , came in The center position of array/list

The Higher than smallest is 6 goes to the right of 5 .

The Next higher number goes to the left of minimum number and So on .

Remember , Duplications are included when Arranging , Don't Delete Them .

pendulum ([-9, -2, -10, -6]) ==> [-6, -10, -9, -2]
Explanation:
Since , -10 is the The Smallest element of the list of integers , came in The center position of array/list

The Higher than smallest is -9 goes to the right of it .

The Next higher number goes to the left of -10 , and So on .

Remeber , In Even array size , The minimum element moved to (n-1)/2 index (considering that indexes start from 0) .

pendulum ([11, -16, -18, 13, -11, -12, 3, 18]) ==> [13, 3, -12, -18, -16, -11, 11, 18]
Explanation:
Since , -18 is the The Smallest element of the list of integers , came in The center position of array/list

The Higher than smallest is -16 goes to the right of it .

The Next higher number goes to the left of -18 , and So on .

Remember , In Even array size , The minimum element moved to (n-1)/2 index (considering that indexes start from 0) .

Tune Your Code , There are 200 Assertions , 60.000 element For Each .

https://www.codewars.com/kata/5bd776533a7e2720c40000e5/train/go
*/

package kata

import "sort"

func Pendulum(values []int) []int {
  output := []int{}
  // delta for first range determinant on len(values) being even/odd
  delta := 1
  if len(values) % 2 == 0 { delta = 2 }
  // anonymous function to sort the initial slice ascending
  sort.Slice(values, func(i, j int) bool {
    return values[i] < values[j]
  })
  // first iteration, start at the largest value - delta, append every other value
  for i := len(values) - delta; i > -1; i -= 2 {
    output = append(output, values[i])
  }
  // second iteration, start at the 2nd value, append every other value
  for i := 1; i < len(values); i += 2 {
    output = append(output, values[i])
  }
  
  return output
}