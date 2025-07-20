"""
Imagine a circle. To encode the word codewars, we could split the circle into 8 parts (as codewars has 8 letters):

Then add the letters in a clockwise direction:Then remove the circle:
If we read the result from left to right, we get csordaew.

Decoding is the same process in reverse. If we decode csordaew, we get codewars.

Examples:
encode "codewars" -> "csordaew"
decode "csordaew" -> "codewars"
encode "white" -> "wehti"
decode "wehti" -> "white"


https://www.codewars.com/kata/634d0723075de3f97a9eb604/train/python
"""

def encode(s:str) -> str:
    mid = len(s) // 2
    left, right = s[:mid], s[mid:][::-1]
    max_len = max(len(left), len(right))
    
    encoded = []
    for i in range(max_len):
        if i < len(left):
            encoded.append(left[i])
        if i < len(right):
            encoded.append(right[i])
    return "".join(encoded)
    
    
def decode(s:str) -> str:
    return s[0::2] + s[1::2][::-1]