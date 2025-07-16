/*
You are given an odd-length array of integers, in which all of them are the same, except for one single number.

Complete the method which accepts such an array, and returns that single different number.

The input array will always be valid! (odd-length >= 3)

Examples
[1, 1, 2] ==> 2
[17, 17, 3, 17, 17, 17, 17] ==> 3


https://www.codewars.com/kata/57f609022f4d534f05000024/train/c
*/

#include <stddef.h>

int stray(size_t n, int arr[n]) {
  int res = arr[0];
  int i = 0;
  while (arr[i++] == res) {
    ;
  }
  
  if (i == 2) {
    return (arr[2] == res) ? arr[1] : res;
  }
  
  return arr[i-1];
}