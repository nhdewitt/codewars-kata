/*
In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. For example: 5! = 5 * 4 * 3 * 2 * 1 = 120. By convention the value of 0! is 1.

Write a function to calculate factorial for a given input. If input is below 0 or above 12 throw an exception of type ArgumentOutOfRangeException (C#) or IllegalArgumentException (Java) or RangeException (PHP) or throw a RangeError (JavaScript) or ValueError (Python) or return -1 (C).

More details about factorial can be found here.

https://www.codewars.com/kata/54ff0d1f355cfd20e60001fc/train/c
*/

int factorial(int n) {
  if (n < 0 || n > 12)    return -1;
  int prod = 1;
  while (n > 1)
    prod *= n--;
  return prod;
}

/*
Your task is to write function factorial.

https://en.wikipedia.org/wiki/Factorial

https://www.codewars.com/kata/57a049e253ba33ac5e000212/train/c
*/

unsigned __int128 factorial(unsigned n)
{
  unsigned __int128 prod = 1;
  while (n > 0)
  {
    prod *= n;
    n--;
  }
  return prod;
}