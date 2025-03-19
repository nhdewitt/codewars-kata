"""
You receive the name of a city as a string, and you need to return a string that shows how many times each letter shows up in the string by using asterisks (*).

For example:

"Chicago"  -->  "c:**,h:*,i:*,a:*,g:*,o:*"
As you can see, the letter c is shown only once, but with 2 asterisks.

The return string should include only the letters (not the dashes, spaces, apostrophes, etc). There should be no spaces in the output, and the different letters are separated by a comma (,) as seen in the example above.

Note that the return string must list the letters in order of their first appearance in the original string.

More examples:

"Bangkok"    -->  "b:*,a:*,n:*,g:*,k:**,o:*"
"Las Vegas"  -->  "l:*,a:**,s:**,v:*,e:*,g:*"
Have fun! ;)

https://www.codewars.com/kata/5b358a1e228d316283001892/train/python
"""

def get_strings(city):
    counts = {}
    string = []
    for c in city.lower():
        if c != " ":
            counts[c] = counts.get(c, 0) + 1
    seen = set()
    for c in city.lower():
        if c not in seen and c != " ":
            seen.add(c)
            string.append(f"{c}:{'*' * counts[c]}")
    
    return ",".join(string)