/*
Your task is to find the first element of an array that is not consecutive.

By not consecutive we mean not exactly 1 larger than the previous element of the array.

E.g. If we have an array [1,2,3,4,6,7,8] then 1 then 2 then 3 then 4 are all consecutive but 6 is not, so that's the first non-consecutive number.

If a non consecutive number is found then return true and set the passed in pointer to the number found.

If the whole array is consecutive then return false.

The array will always have at least 2 elements1 and all elements will be numbers. The numbers will also all be unique and in ascending order. The numbers could be positive or negative and the first non-consecutive could be either too!

1 Can you write a solution that will return false for both [] and [ x ] (an empty array and one with a single number) though? (This is an empty array and one with a single number and is not tested for, but you can write your own example test. )


https://www.codewars.com/kata/58f8a3a27a5c28d92e000144/train/c
*/

// For c the function should return `false` if no non consecutive numbers are found
// It should return `true` if one is found and the pointer arg `first` set to the value

#include <stdbool.h>
#include <stdio.h>

bool firstNonConsecutive (const int arr[/* length */], int length, int *first) {
  int j = arr[0];
  for (int i = 1; i < length; i++) {
    if (++j != arr[i]) {
      *first = arr[i++];
      return true;
    }
  }
  *first = -1;
  return false;
}