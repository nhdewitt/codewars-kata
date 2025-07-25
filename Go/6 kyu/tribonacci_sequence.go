/*
Well met with Fibonacci bigger brother, AKA Tribonacci.

As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers of the sequence to generate the next. And, worse part of it, regrettably I won't get to hear non-native Italian speakers trying to pronounce it :(

So, if we are to start our Tribonacci sequence with [1, 1, 1] as a starting input (AKA signature), we have this sequence:

[1, 1 ,1, 3, 5, 9, 17, 31, ...]
But what if we started with [0, 0, 1] as a signature? As starting with [0, 1] instead of [1, 1] basically shifts the common Fibonacci sequence by once place, you may be tempted to think that we would get the same sequence shifted by 2 places, but that is not the case and we would get:

[0, 0, 1, 1, 2, 4, 7, 13, 24, ...]
Well, you may have guessed it by now, but to be clear: you need to create a fibonacci function that given a signature array/list, returns the first n elements - signature included of the so seeded sequence.

Signature will always contain 3 numbers; n will always be a non-negative number; if n == 0, then return an empty array (except in C return NULL) and be ready for anything else which is not clearly specified ;)

If you enjoyed this kata more advanced and generalized version of it can be found in the Xbonacci kata

[Personal thanks to Professor Jim Fowler on Coursera for his awesome classes that I really recommend to any math enthusiast and for showing me this mathematical curiosity too with his usual contagious passion :)]

https://www.codewars.com/kata/556deca17c58da83c00002db/train/go
*/

package kata

func Tribonacci(signature [3]float64, n int) []float64 {
  output := make([]float64, 0)
  if n == 0 {															// edge cases: n=0, return nil; n=1, return signature[0]; n=2, return signature[0], signature[1]
    return []float64{}
  }
  if n == 1 {
    return []float64{signature[0]}
  } else if n == 2 {
    return []float64{signature[0], signature[1]}
  }
  for _, sig := range signature {										// append the signature to the start of the output
    output = append(output, sig)
  }
  for i := 2; i < n-1; i++ {
    output = append(output, (output[i] + output[i-1] + output[i-2]))	// shift the window for each iter, adding the previous three
  }
  return output
}