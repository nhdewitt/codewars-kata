/*
You are given two arrays a1 and a2 of strings. Each string is composed with letters from a to z. Let x be any string in the first array and y be any string in the second array.

Find max(abs(length(x) − length(y)))

If a1 and/or a2 are empty return -1 in each language except in Haskell (F#) where you will return Nothing (None).

Example:
a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
mxdiflg(a1, a2) --> 13
Bash note:
input : 2 strings with substrings separated by ,
output: number as a string

https://www.codewars.com/kata/5663f5305102699bad000056/train/c
*/

#include <stddef.h>
#include <string.h>
#include <stdint.h>

int mxdiflg(
    const char *const arr_1[], size_t len_1, 
    const char *const arr_2[], size_t len_2
)
{
    if (len_1 == 0 || len_2 == 0)   return -1;
    size_t shortest_1 = SIZE_MAX, longest_1 = 0;
    size_t shortest_2 = SIZE_MAX, longest_2 = 0;
    
    for (size_t i = 0; i < len_1; i++)
    {
      size_t len = strlen(arr_1[i]);
      if (len < shortest_1)    shortest_1 = len;
      if (len > longest_1)     longest_1  = len;
    }
    
    for (size_t i = 0; i < len_2; i++)
    {
      size_t len = strlen(arr_2[i]);
      if (len < shortest_2)    shortest_2 = len;
      if (len > longest_2)     longest_2  = len;
    }
    
    int check_if_1_gr = longest_1 - shortest_2;
    int check_if_2_gr = longest_2 - shortest_1;
    
    return (check_if_1_gr > check_if_2_gr) ?
            check_if_1_gr :
            check_if_2_gr;
}