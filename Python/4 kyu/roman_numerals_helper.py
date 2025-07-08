"""
Write two functions that convert a roman numeral to and from an integer value. Multiple roman numeral values will be tested for each function.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals:

1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC
2008 is written as 2000=MM, 8=VIII; or MMVIII
1666 uses each Roman symbol in descending order: MDCLXVI.
Input range : 1 <= n < 4000

In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").

Examples
to roman:
2000 -> "MM"
1666 -> "MDCLXVI"
  86 -> "LXXXVI"
   1 -> "I"

from roman:
"MM"      -> 2000
"MDCLXVI" -> 1666
"LXXXVI"  ->   86
"I"       ->    1
Help
+--------+-------+
| Symbol | Value |
+--------+-------+
|    M   |  1000 |
|   CM   |   900 |
|    D   |   500 |
|   CD   |   400 |
|    C   |   100 |
|   XC   |    90 |
|    L   |    50 |
|   XL   |    40 |
|    X   |    10 |
|   IX   |     9 |
|    V   |     5 |
|   IV   |     4 |
|    I   |     1 |
+--------+-------+

https://www.codewars.com/kata/51b66044bce5799a7f000003/train/python
"""

class RomanNumerals:
    numeral_map = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
                   (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"),
                   (5, "V"), (4, "IV"), (1, "I")]
    roman_hash = {sym: val for val, sym in numeral_map}
    
    @staticmethod
    def to_roman(val : int) -> str:
        if val < 1 or val >= 4000:
            raise ValueError("number must be between 1 and 3999")
        res = []
        for (v, sym) in RomanNumerals.numeral_map:
            count, val = divmod(val, v)
            res.append(sym * count)
        
        return "".join(res)

    @staticmethod
    def from_roman(roman_num : str) -> int:
        res, i, n = 0, 0, len(roman_num)
        while i < n:
            if i + 1 < n and roman_num[i:i + 2] in RomanNumerals.roman_hash:
                res += RomanNumerals.roman_hash[roman_num[i:i + 2]]
                i += 2
            else:
                res += RomanNumerals.roman_hash[roman_num[i]]
                i += 1

        return res