/*
You've just discovered a square (NxN) field and you notice a warning sign. The sign states that there's a single bomb in the 2D grid-like field in front of you.

Write a function that accepts a 2D array, and returns the location of the mine. The mine is represented as the integer 1 in the 2D array. Areas in the 2D array that are not the mine will be represented as 0s.

The location returned should be an array (Tuple<int, int> in C#, RAX:RDX in NASM) where the first element is the row index, and the second element is the column index of the bomb location (both should be 0 based). All 2D arrays passed into your function will be a square (NxN), and there will only be one mine in the array.

Examples (Input --> Output)
[ [1, 0, 0], [0, 0, 0], [0, 0, 0] ] --> [0, 0]

[ [0, 0, 0], [0, 1, 0], [0, 0, 0] ] --> [1, 1]

[ [0, 0, 0], [0, 0, 0], [0, 1, 0] ] --> [2, 1]

https://www.codewars.com/kata/528d9adf0e03778b9e00067e/train/c
*/

#include <stdlib.h>

// return a heap-allocated array of 2 elements

size_t *mine_location(size_t n, const int field[n][n]) {
  size_t i, j;
  for (i = 0; i < n; i++)
    for (j = 0; j < n; j++)
      if (field[i][j] == 1)
      {
        size_t *res;
        res = malloc(2 * sizeof(size_t));
        if (!res)   return NULL;
        res[0] = i;
        res[1] = j;
        return res;
      }
}