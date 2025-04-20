"""
Introduction
The GADERYPOLUKI is a simple substitution cypher used in scouting to encrypt messages. The encryption is based on short, easy to remember key. The key is written as paired letters, which are in the cipher simple replacement.

The most frequently used key is "GA-DE-RY-PO-LU-KI".

 g => a
 a => g
 d => e
 e => d
  etc.
The letters, which are not on the list of substitutes, stay in the encrypted text without changes.

Other keys often used by Scouts:

PO-LI-TY-KA-RE-NU
KA-CE-MI-NU-TO-WY
KO-NI-EC-MA-TU-RY
ZA-RE-WY-BU-HO-KI
BA-WO-LE-TY-KI-JU
RE-GU-LA-MI-NO-WY
Task
Our scouts had a party yesterday, and they had too much milk and cookies. As a result, all of them forgot the key. Your task is to help scouts to find the key that they used for encryption. Fortunately, they have some messages that are already encoded.

Input
The function accepts two arrays.

The messages string array consists of lowercase characters and whitespace characters. The strings on the messages array are scout's messages before encryption.

The secrets string array consists of lowercase characters and whitespace characters.

The strings on the secrets array are scout's messages after encryption.

Output
The returned string should consist of lowercase characters only. The pairs of substitutions should be ordered by the first letter of substitution. The letters in each pair should be in alphabetical order.

ga => incorrect output (error: g is after a )
ag => correct output  
deag => incorrect output  (error: de is after ag)
agde => correct output  
Example
string[] messages = { "dance on the table", "hide my beers", "scouts rocks" };
string[] secretes = { "egncd pn thd tgbud" ,"hked mr bddys" ,"scplts ypcis" };
FindTheKey(messages, secretes);   //=> agdeikluopry

https://www.codewars.com/kata/592bdf59912f2209710000e9/train/python
"""

def find_the_key(messages, secrets):
    zipped = list(zip((c for c in "".join(messages)), (c for c in "".join(secrets))))       # merge the two together as tuples
    seen = set()                                                                            # set() seen to avoid unneccesary work
    code = []
    for z in zipped:
        if z[0] not in seen and z[1] not in seen:
            if z[0] != z[1]:
                code.append(f"{z[0]}{z[1]}")                                                # if the two characters are different, they are part of the code
            seen.add(z[0])
            seen.add(z[1])
    
    code = ["".join(sorted(c)) for c in code]                                               # sort each pair alphabetically
    
    return "".join(sorted(code))                                                            # return the code as a single string sorted alphabetically by pairs