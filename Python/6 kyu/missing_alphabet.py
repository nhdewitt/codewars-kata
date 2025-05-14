"""
In this Kata you have to create a function,named insertMissingLetters,that takes in a string and outputs the same string processed in a particular way.

The function should insert only after the first occurrence of each character of the input string, all the alphabet letters that:

-are NOT in the original string
-come after the letter of the string you are processing

Each added letter should be in uppercase, the letters of the original string will always be in lowercase.

Example:

input: "holly"

missing letters: "a,b,c,d,e,f,g,i,j,k,m,n,p,q,r,s,t,u,v,w,x,z"

output: "hIJKMNPQRSTUVWXZoPQRSTUVWXZlMNPQRSTUVWXZlyZ"

You don't need to validate input, the input string will always contain a certain amount of lowercase letters (min 1 / max 50).

https://www.codewars.com/kata/5ad1e412cc2be1dbfb000016/train/python
"""

from string import ascii_lowercase

def insert_missing_letters(st):
    missing = sorted(list(set(s.upper() for s in ascii_lowercase if s not in st)))      # keep track of letters not in st alphabetically
    output = ""
    seen = set()                                                                        # keep track of letters in st already processed
    for s in st:
        if s in seen:
            output += s                                                                 # if we've already seen s, just append it
        else:
            output += f"{s}{''.join(list(m for m in missing if m > s.upper()))}"        # append the list of letters > s after s
            seen.add(s)                                                                 # add s to seen so we don't process it twice
    return output