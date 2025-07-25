/*
This is the simple version of Shortest Code series. If you need some challenges, please try the challenge version.

Task:
Find out "B"(Bug) in a lot of "A"(Apple).

There will always be one bug in apple, not need to consider the situation that without bug or more than one bugs.

input: string Array apple

output: Location of "B", [x,y]


https://www.codewars.com/kata/56fe97b3cc08ca00e4000dc9/train/c
*/

#include <stddef.h>

typedef struct { size_t i, j; } coords;

coords bug_in_apple(size_t m, size_t n, const char apple[m][n]) {
  size_t p, q;
  for (p = 0; p < m; p++)
    for (q = 0; q < n; q++)
      if (apple[p][q] == 'B')
        return (coords){p, q};
  return (coords){p, q};
}