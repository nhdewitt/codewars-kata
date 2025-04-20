"""
Introduction
The GADERYPOLUKI is a simple substitution cypher used in scouting to encrypt messages. The encryption is based on short, easy to remember key. The key is written as paired letters, which are in the cipher simple replacement.

The most frequently used key is "GA-DE-RY-PO-LU-KI".

 G => A
 g => a
 a => g
 A => G
 D => E
  etc.
The letters, which are not on the list of substitutes, stays in the encrypted text without changes.

Other keys often used by Scouts:

PO-LI-TY-KA-RE-NU
KA-CE-MI-NU-TO-WY
KO-NI-EC-MA-TU-RY
ZA-RE-WY-BU-HO-KI
BA-WO-LE-TY-KI-JU
RE-GU-LA-MI-NO-WY
Task
Your task is to help scouts to encrypt and decrypt thier messages. Write the Encode and Decode functions.

Input/Output
The function should have two parameters.
The message input string consists of lowercase and uperrcase characters and whitespace character.
The key input string consists of only lowercase characters.
The substitution has to be case-sensitive.

Example
 Encode("ABCD", "agedyropulik");             // => GBCE 
 Encode("Ala has a cat", "gaderypoluki");    // => Gug hgs g cgt 
 Decode("Dkucr pu yhr ykbir","politykarenu") // => Dance on the table
 Decode("Hmdr nge brres","regulaminowy")  // => Hide our beers
 
 https://www.codewars.com/kata/592b7b16281da94068000107/train/python
 """

def encode(message, _key):
    enc, dec = [], []
    for i in range(0, len(_key), 2):                                # split the key in groups of two, mirror the chars to the encoding and decoding list
        enc.append(f"{_key[i]}{_key[i].upper()}")
        enc.append(f"{_key[i + 1]}{_key[i + 1].upper()}")
        dec.append(f"{_key[i + 1]}{_key[i + 1].upper()}")
        dec.append(f"{_key[i]}{_key[i].upper()}")
        
    code = str.maketrans("".join(dec), "".join(enc))                # join into strings for the maketrans, use to decrypt/encrypt
    
    return message.translate(code)
    
def decode(message, _key):
    return encode(message, _key)