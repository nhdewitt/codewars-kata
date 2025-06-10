/*
If you have completed the Tribonacci sequence kata, you would know by now that mister Fibonacci has at least a bigger brother. If not, give it a quick look to get how things work.

Well, time to expand the family a little more: think of a Quadribonacci starting with a signature of 4 elements and each following element is the sum of the 4 previous, a Pentabonacci (well Cinquebonacci would probably sound a bit more italian, but it would also sound really awful) with a signature of 5 elements and each following element is the sum of the 5 previous, and so on.

Well, guess what? You have to build a Xbonacci function that takes a signature of X elements - and remember each next element is the sum of the last X elements - and returns the first n elements of the so seeded sequence.

xbonacci {1,1,1,1} 10 = {1,1,1,1,4,7,13,25,49,94}
xbonacci {0,0,0,0,1} 10 = {0,0,0,0,1,1,2,4,8,16}
xbonacci {1,0,0,0,0,0,1} 10 = {1,0,0,0,0,0,1,2,3,6}
xbonacci {1,1} produces the Fibonacci sequence

https://www.codewars.com/kata/556e0fccc392c527f20000c5/train/go
*/

package kata

func Sum(arr []int) int {												// helper to sum the elements of an array
  var total int
  for _, a := range arr {
    total += a
  }
  return total
}

func Xbonacci(signature []int, n int) []int {
  if n == 0 {
    return []int{}
  }
  if n <= len(signature) {												// if n <= len(signature), we already have the sequence, we just return that portion of signature
    return signature[:n]
  }
  sequence := make([]int, 0)
  sequence = append(sequence, signature...)								// if we need to calculate, first append the signature to the sequence
  for i := len(signature); i < n; i++ {
    sequence = append(sequence, Sum(sequence[i-len(signature):i]))		// then, while the size of sequence is less than n, append the sum of the last X elements to the sequence
  }
  return sequence
}