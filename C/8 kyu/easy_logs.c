/*
Given a logarithm base X and two values A and B, return a sum of logratihms with the base X: 
log
⁡
X
A
+
log
⁡
X
B
log 
X
​
 A+log 
X
​
 B.


https://www.codewars.com/kata/5b68c7029756802aa2000176/train/c
*/

#import <math.h>

double log_base(double x, double base) {
  return log(x) / log(base);
}

double easy_logs(double x, double a, double b) {
  return log_base(a, x) + log_base(b, x);
}