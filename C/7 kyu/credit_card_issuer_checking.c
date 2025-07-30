/*
Given a credit card number we can determine who the issuer/vendor is with a few basic knowns.

Complete the function getIssuer() that will use the values shown below to determine the card issuer for a given card number. If the number cannot be matched then the function should return the string Unknown.

| Card Type  | Begins With          | Number Length |
|------------|----------------------|---------------|
| AMEX       | 34 or 37             | 15            |
| Discover   | 6011                 | 16            |
| Mastercard | 51, 52, 53, 54 or 55 | 16            |
| VISA       | 4                    | 13 or 16      |
NASM and C/C++ note: The return value is not freed.

Examples
getIssuer(4111111111111111) == "VISA"
getIssuer(4111111111111) == "VISA"
getIssuer(4012888888881881) == "VISA"
getIssuer(378282246310005) == "AMEX"
getIssuer(6011111111111117) == "Discover"
getIssuer(5105105105105100) == "Mastercard"
getIssuer(5105105105105106) == "Mastercard"
getIssuer(9111111111111111) == "Unknown"


https://www.codewars.com/kata/5701e43f86306a615c001868/train/c
*/

#include <stdio.h>
#include <string.h>

const char *getIssuer(const long number)
{
  const char *providers[5] = {"AMEX", "Discover", "Mastercard", "VISA", "Unknown"};
  char num[20];
  snprintf(num, sizeof(num), "%ld", number);
  
  size_t len = strlen(num);
  
  if (len < 13 || len > 16) return providers[4];
  
  switch (len) {
      case 13:
        return (num[0] == '4') ? providers[3] : providers[4];
      case 15:
        return (strncmp(num, "34", 2) == 0 || strncmp(num, "37", 2) == 0) ? providers[0] : providers[4];
      case 16:
        if (num[0] == '4')  return providers[3];
        if (strncmp(num, "6011", 4) == 0) return providers[1];
        if (num[0] == '5' && num[1] >= '1' && num[1] <= '5')  return providers[2];
        return providers[4];
      default:
        return providers[4];
  }
  
  return providers[4];
}