"""
You know how sometimes you write the the same word twice in a sentence, but then don't notice that it happened? For example, you've been distracted for a second. Did you notice that "the" is doubled in the first sentence of this description?

As as aS you can see, it's not easy to spot those errors, especially if words differ in case, like "as" at the beginning of this sentence.

Write a function that counts the number of sections repeating the same word (case insensitive). The occurence of two or more equal words next after each other counts as one.

Examples
"dog cat"                  -->  0
"dog DOG cat"              -->  1
"apple dog cat"            -->  0
"pineapple apple dog cat"  -->  0
"apple apple dog cat"      -->  1
"apple dog apple dog cat"  -->  0
"dog dog DOG dog dog dog"  -->  1
"dog dog dog dog cat cat"  -->  2
"cat cat dog dog cat cat"  -->  3

https://www.codewars.com/kata/5245a9138ca049e9a10007b8/train/python
"""

def count_adjacent_pairs(st):
    seen = list()                                       # can't use a set as words can repeat
    s = st.lower().split()
    for i in range(-1, -len(s), -1):
        print(s[i - 1])
        if s[i] == s[i - 1]:
            if len(seen) > 0 and seen[-1] == s[i]:      # skip IndexError for first check of seen
                continue
            seen.append(s[i])

    return len(seen)                                    # length of seen is the number of repeating words