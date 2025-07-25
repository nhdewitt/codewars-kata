/*
Complete the function that takes two integers (a, b, where a < b) and return an array of all integers between the input parameters, including them.

For example:

a = 1
b = 4
--> [1, 2, 3, 4]

https://www.codewars.com/kata/55ecd718f46fba02e5000029/train/c
*/

void between(int a, int b, int *integers) {
  for (int i = 0, j = a; j <= b; i++, j++)
      integers[i] = j;
}