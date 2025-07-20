/*
Each exclamation mark's weight is 2; each question mark's weight is 3. Putting two strings left and right on the balance - are they balanced?

If the left side is more heavy, return "Left"; if the right side is more heavy, return "Right"; if they are balanced, return "Balance".

Examples
"!!", "??"     -->  "Right"
"!??", "?!!"   -->  "Left"
"!?!!", "?!?"  -->  "Left"
"!!???!????", "??!!?!!!!!!!"  -->  "Balance"

https://www.codewars.com/kata/57fb44a12b53146fe1000136/train/c
*/

enum Outcome {
    Balance, Left, Right
};

enum Outcome balance(const char *left, const char *right) {
  int weight = 0;
  while (*left)
  {
    if (*left == '!')
      weight += 2;
    else if (*left == '?')
      weight += 3;
    *left++;
  }
  while (*right)
  {
    if (*right == '!')
      weight -= 2;
    else if (*right == '?')
      weight -= 3;
    *right++;
  }

  if     (weight == 0) return Balance;
  else if (weight < 0) return Right;
                       return Left;
}