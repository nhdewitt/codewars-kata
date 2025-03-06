"""
You are given a secret message you need to decipher. Here are the things you need to know to decipher it:

For each word:

the second and the last letter is switched (e.g. Hello becomes Holle)
the first letter is replaced by its character code (e.g. H becomes 72)
there are no special characters used, only letters and spaces
words are separated by a single space
there are no leading or trailing spaces
Examples

'72olle 103doo 100ya' --> 'Hello good day'
'82yade 115te 103o'   --> 'Ready set go'

https://www.codewars.com/kata/581e014b55f2c52bb00000f8/train/python
"""

def decipher_this(s):
    decipher = []
    for word in s.split():
        num_str = ""
        i = 0
        while i < len(word) and word[i].isdigit():
            num_str += word[i]
            i += 1
        first = chr(int(num_str))
        rest = list(word[i:])
        if len(rest) > 1:
            rest[0], rest[-1] = rest[-1], rest[0]
        decipher.append(first + "".join(rest))
    
    return " ".join(decipher)