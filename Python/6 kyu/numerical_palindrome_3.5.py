"""
A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward. Examples of numerical palindromes are: 2332, 110011, 54322345

For a given number num, write a function which returns an array of all the numerical palindromes contained within each number. The array should be sorted in ascending order and any duplicates should be removed.

In this kata, single digit numbers and numbers which start or end with zeros (such as 010 and 00) are NOT considered valid numerical palindromes.

If num contains no valid palindromes, return "No palindromes found". Otherwise, return "Not valid" if the input is not an integer or is less than 0.

Examples
1221      -->  [22, 1221]
34322122  -->  [22, 212, 343, 22122]
1001331   -->  [33, 1001, 1331]
1294      -->  "No palindromes found"
"1221"    -->  "Not valid"

https://www.codewars.com/kata/58e2708f9bd67fee17000080/train/python
"""

def palindrome(num):
    if not isinstance(num, int) or num < 0:             # Two invalid cases
        return "Not valid"
    if num < 10:                                        # n must be > 9
        return "No palindromes found"
    seen = set()                                        # avoid repeats
    st_num = str(num)
    n = len(st_num)
    for i in range(n - 1):
        if st_num[i] == "0":                            # palindrome can't start with 0
            continue
        for j in range(i + 2, n + 1):
            if st_num[i:j] == st_num[i:j][::-1]:
                seen.add(int(st_num[i:j]))
    if not seen:
        return "No palindromes found"
    return sorted(seen)