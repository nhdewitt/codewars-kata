/*
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

If you want to know more: http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)

Example: (input --> output)

"ATTGC" --> "TAACG"
"GTAT" --> "CATA"


https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/c
*/

#include <stdlib.h>
#include <string.h>

char *dna_strand(const char *dna)
{
  size_t len = strlen(dna);
  char *dst = malloc(len + 1);
  if (!dst)   return NULL;
  size_t i = 0;
  
  while (*dna) {
    switch (*dna++) {
    case 'A':   dst[i++] = 'T'; break;
    case 'T':   dst[i++] = 'A'; break;
    case 'C':   dst[i++] = 'G'; break;
    case 'G':   dst[i++] = 'C'; break;
    }
  }
  dst[i++] = '\0';
  
  return dst;
}