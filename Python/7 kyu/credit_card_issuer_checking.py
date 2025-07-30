"""
Given a credit card number we can determine who the issuer/vendor is with a few basic knowns.

Complete the function get_issuer() that will use the values shown below to determine the card issuer for a given card number. If the number cannot be matched then the function should return the string Unknown.

| Card Type  | Begins With          | Number Length |
|------------|----------------------|---------------|
| AMEX       | 34 or 37             | 15            |
| Discover   | 6011                 | 16            |
| Mastercard | 51, 52, 53, 54 or 55 | 16            |
| VISA       | 4                    | 13 or 16      |
Examples
get_issuer(4111111111111111) == "VISA"
get_issuer(4111111111111) == "VISA"
get_issuer(4012888888881881) == "VISA"
get_issuer(378282246310005) == "AMEX"
get_issuer(6011111111111117) == "Discover"
get_issuer(5105105105105100) == "Mastercard"
get_issuer(5105105105105106) == "Mastercard"
get_issuer(9111111111111111) == "Unknown"


https://www.codewars.com/kata/5701e43f86306a615c001868/train/python
"""

def get_issuer(number):
    number = str(number)
    match number[0]:
        case "3":
            return "AMEX" if ((number[1] == "4" or number[1] == "7") and len(number) == 15) else "Unknown"
        case "6":
            return "Discover" if (number[:4] == "6011" and len(number) == 16) else "Unknown"
        case "5":
            return "Mastercard" if (number[1] in {'1','2','3','4','5'} and len(number) == 16) else "Unknown"
        case "4":
            return "VISA" if (len(number) == 13 or len(number) == 16) else "Unknown"
        case _:
            return "Unknown"