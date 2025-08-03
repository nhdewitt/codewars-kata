/*
Write a function that accepts two square matrices (N x N two dimensional arrays), and return the sum of the two. Both matrices being passed into the function will be of size N x N (square), containing only integers.

How to sum two matrices:

Take each cell [n][m] from the first matrix, and add it with the same [n][m] cell from the second matrix. This will be cell [n][m] of the solution matrix. (Except for C where solution matrix will be a 1d pseudo-multidimensional array).

Visualization:

|1 2 3|     |2 2 1|     |1+2 2+2 3+1|     |3 4 4|
|3 2 1|  +  |3 2 3|  =  |3+3 2+2 1+3|  =  |6 4 4|
|1 1 1|     |1 1 3|     |1+1 1+1 1+3|     |2 2 4|
Example
matrixAddition(
  [ [1, 2, 3],
    [3, 2, 1],
    [1, 1, 1] ],
//      +
  [ [2, 2, 1],
    [3, 2, 3],
    [1, 1, 3] ] )

// returns:
  [ [3, 4, 4],
    [6, 4, 4],
    [2, 2, 4] ]

https://www.codewars.com/kata/526233aefd4764272800036f/train/c
*/

#include <stdlib.h>

int *matrix_addition(size_t n, const int matrix_a[n][n], const int matrix_b[n][n])
{
  int* res = malloc((n * n) * sizeof(int));
  
  for (size_t i = 0; i < n; i++) {
    for (size_t j = 0; j < n; j++) {
      res[i * n + j] = matrix_a[i][j] + matrix_b[i][j];
    }
  }
  
  return res;
}