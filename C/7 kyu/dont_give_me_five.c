/*
Don't give me five!
In this kata you get the start number and the end number of a region and should return the count of all numbers except numbers with a 5 in it. The start and the end number are both inclusive!

Examples:

1,9 -> 1,2,3,4,6,7,8,9 -> Result 8
4,17 -> 4,6,7,8,9,10,11,12,13,14,16,17 -> Result 12
The result may contain fives. ;-)
The start number will always be smaller than the end number. Both numbers can be also negative!

I'm very curious for your solutions and the way you solve it. Maybe someone of you will find an easy pure mathematics solution.

Have fun coding it and please don't forget to vote and rank this kata! :-)

I have also created other katas. Take a look if you enjoyed this kata!

https://www.codewars.com/kata/5813d19765d81c592200001a/train/c
*/

#include <stdbool.h>

bool contains_five(int n)
{
  if (n < 0)  n = -n;
  
  while (n > 0)
  {
    int digit = n % 10;
    if (digit == 5)   return true;
    n /= 10;
  }
  return false;
}

int dontGiveMeFive(int start, int end)
{
  int count = 0;
  
  for (int i = start; i <= end; i++)
    if (!contains_five(i))  count++;
  
  return count;
}