"""
You are given a string of words (x), for each word within the string you need to turn the word 'inside out'. By this I mean the internal letters will move out, and the external letters move toward the centre.

If the word is even length, all letters will move. If the length is odd, you are expected to leave the 'middle' letter of the word where it is.

An example should clarify:

'taxi' would become 'atix' 'taxis' would become 'atxsi'

https://www.codewars.com/kata/57ebdf1c2d45a0ecd7002cd5/train/python
"""

def inside_out(st):
    s = st.split(" ")
    inside_out = []
    for w in s:
        if len(w) < 4:                                                              # len(3) or less, nothing changes
            inside_out.append(w)
            continue
        slice = len(w) // 2
        if len(w) % 2 == 0:
            inside_out.append(w[:slice][::-1] + w[slice:][::-1])                    # even length, slice in half and reverse each slice
        else:
            inside_out.append(w[:slice][::-1] + w[slice] + w[slice + 1:][::-1])     # odd length, slice in half, reverse each slice, insert the middle char
    
    return " ".join(inside_out)