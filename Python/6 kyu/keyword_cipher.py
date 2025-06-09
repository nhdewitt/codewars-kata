"""
Third day at your new cryptoanalyst job and you come across your toughest assignment yet. Your job is to implement a simple keyword cipher. A keyword cipher is a type of monoalphabetic substitution where two parameters are provided as such (string, keyword). The string is encrypted by taking the keyword, dropping any letters that appear more than once. The rest of the letters of the alphabet that aren't used are then appended to the end of the keyword.

For example, if your string was "hello" and your keyword was "wednesday", your encryption key would be 'wednsaybcfghijklmopqrtuvxz'.

To encrypt 'hello' you'd substitute as follows,

              abcdefghijklmnopqrstuvwxyz
  hello ==>   |||||||||||||||||||||||||| ==> bshhk
              wednsaybcfghijklmopqrtuvxz
hello encrypts into bshhk with the keyword wednesday. This cipher also uses lower case letters only.

Good Luck.

https://www.codewars.com/kata/57241cafef90082e270012d8/train/python
"""

from collections import Counter
from string import ascii_lowercase

def keyword_cipher(msg, keyword):
    freq = Counter(keyword)
    key = []
    for k in keyword:
        if k in freq and k not in key:                              # set won't keep the order that is needed, so need to make sure k is not already in key
            key.append(k)
    key.extend(list(a for a in ascii_lowercase if a not in key))    # extend the remainder of the alphabet
    key = "".join(key)
    cipher = str.maketrans(ascii_lowercase, key)                    # create cipher string and return the translation
    
    return msg.lower().translate(cipher)