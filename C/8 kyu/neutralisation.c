/*
Given two strings comprised of + and -, return a new string which shows how the two strings interact in the following way:

When positives and positives interact, they remain positive.
When negatives and negatives interact, they remain negative.
But when negatives and positives interact, they become neutral, and are shown as the number 0.
Worked Example
("+-+", "+--") ➞ "+-0"
# Compare the first characters of each string, then the next in turn.
# "+" against a "+" returns another "+".
# "-" against a "-" returns another "-".
# "+" against a "-" returns "0".
# Return the string of characters.
Examples
("--++--", "++--++") ➞ "000000"

("-+-+-+", "-+-+-+") ➞ "-+-+-+"

("-++-", "-+-+") ➞ "-+00"
Notes
The two strings will be the same length.


https://www.codewars.com/kata/65128732b5aff40032a3d8f0/train/c
*/

void neutralize (const char *s1, const char *s2, char *s3)
{
  const char *p = s1;
  const char *q = s2;
  char *r = s3;
  
  while (*p && *q) {
    if (*p == '+' && *q == '+')
      *r = '+';
    else if (*p == '-' && *q == '-')
      *r = '-';
    else
      *r = '0';
    p++;
    q++;
    r++;
  }
  *r = '\0';
}