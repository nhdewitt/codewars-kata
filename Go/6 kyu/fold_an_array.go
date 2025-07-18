/*
In this kata you have to write a method that folds a given array of integers by the middle x-times.

An example says more than thousand words:

Fold 1-times:
[1,2,3,4,5] -> [6,6,3]

A little visualization (NOT for the algorithm but for the idea of folding):

 Step 1         Step 2        Step 3       Step 4       Step5
                     5/           5|         5\          
                    4/            4|          4\      
1 2 3 4 5      1 2 3/         1 2 3|       1 2 3\       6 6 3
----*----      ----*          ----*        ----*        ----*


Fold 2-times:
[1,2,3,4,5] -> [9,6]
As you see, if the count of numbers is odd, the middle number will stay. Otherwise the fold-point is between the middle-numbers, so all numbers would be added in a way.

The array will always contain numbers and will never be null. The parameter runs will always be a positive integer greater than 0 and says how many runs of folding your method has to do.

If an array with one element is folded, it stays as the same array.

The input array should not be modified!

Have fun coding it and please don't forget to vote and rank this kata! :-)

I have created other katas. Have a look if you like coding and challenges.

https://www.codewars.com/kata/57ea70aa5500adfe8a000110/train/go
*/

package kata

func FoldArray(arr []int, runs int) []int {
  for run := 0; run < runs; run++ {						// fold needs to run "runs" times
    l := len(arr)
    res := make([]int, (l+1)/2)							// allocate new slice of length+1/2 (handles even or odd slices)
    for i, j := 0, l-1; i <= j; i, j = i+1, j-1 {		// pointer i starts at the front, pointer j starts at the back
      if i == j {										// if i == j, it's odd, keep the mid-point value as is as there is nothing to add to it
        res[i] = arr[i]
      } else {
        res[i] = arr[i] + arr[j]						// otherwise, add the two values together
      }
    }
    arr = res											// new array for next iteration or return if done
  }
  return arr
}