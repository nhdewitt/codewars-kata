/*
Task
Your task is to write a function which returns the n-th term of the following series, which is the sum of the first n terms of the sequence (n is the input parameter).

S
e
r
i
e
s
:
1
+
1
4
+
1
7
+
1
10
+
1
13
+
1
16
+
…
Series:1+ 
4
1
​
 + 
7
1
​
 + 
10
1
​
 + 
13
1
​
 + 
16
1
​
 +…
You will need to figure out the rule of the series to complete this.

Rules
You need to round the answer to 2 decimal places and return it as String.

If the given value is 0 then it should return "0.00".

You will only be given Natural Numbers as arguments.

Examples (Input --> Output)
n
1 --> 1 --> "1.00"
2 --> 1 + 1/4 --> "1.25"
5 --> 1 + 1/4 + 1/7 + 1/10 + 1/13 --> "1.57"


https://www.codewars.com/kata/555eded1ad94b00403000071/train/c
*/

#include <stdlib.h>
#include <stdio.h>

char *series_sum(size_t n)
{
  float sum = 0.0f;
  
  for (size_t i = 0; i < n; i++)
    sum += 1 / (((float) (i) * 3) + 1.0);
    
  int len = snprintf(NULL, 0, "%.2f", sum);
  if (len < 0)    return NULL;
  
  char *out = malloc(len + 1);
  if (!out)       return NULL;
  
  snprintf(out, len + 1, "%.2f", sum);
  return out;
}