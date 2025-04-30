"""
Step 1: Create a function called encode() to replace all the lowercase vowels in a given string with numbers according to the following pattern:

a -> 1
e -> 2
i -> 3
o -> 4
u -> 5
For example, encode("hello") would return "h2ll4". There is no need to worry about uppercase vowels in this kata.

Step 2: Now create a function called decode() to turn the numbers back into vowels according to the same pattern shown above.

For example, decode("h3 th2r2") would return "hi there".

For the sake of simplicity, you can assume that any numbers passed into the function will correspond to vowels.

https://www.codewars.com/kata/53697be005f803751e0015aa
"""

vowel_code = {
    'a': "1",
    'e': "2",
    'i': "3",
    'o': "4",
    'u': "5"
}

translation_table = str.maketrans(vowel_code)
reverse_trans = str.maketrans({v: k for k, v in translation_table.items()})


def encode(st):
    return st.translate(translation_table)
    
def decode(st):
    return st.translate(reverse_trans)