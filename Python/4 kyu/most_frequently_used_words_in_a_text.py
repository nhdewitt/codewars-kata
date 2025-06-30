"""
Write a function that, given a string of text (possibly with punctuation and line-breaks), returns an array of the top-3 most occurring words, in descending order of the number of occurrences.

Assumptions:
A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII.
Apostrophes can appear at the start, middle or end of a word ('abc, abc', 'abc', ab'c are all valid)
Any other characters (e.g. #, \, / , . ...) are not part of a word and should be treated as whitespace.
Matches should be case-insensitive, and the words in the result should be lowercased.
Ties may be broken arbitrarily.
If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty array if a text contains no words.
Examples:
"In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."

--> ["a", "of", "on"]


"e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"

--> ["e", "ddd", "aa"]


"  //wont won't won't"

--> ["won't", "wont"]
Bonus points (not really, but just for fun):
Avoid creating an array whose memory footprint is roughly as big as the input text.
Avoid sorting the entire array of unique words.

https://www.codewars.com/kata/51e056fe544cf36c410000fb/train/python
"""

import re
from collections import Counter

def top_3_words(text):
    text = text.lower()                                                 # normalize to lowercase
    pattern = r"[^A-Za-z0-9']+|(?<![A-Za-z0-9])'(?![A-Za-z0-9])"        # regex to remove non-alphanumerics
    cleaned = re.sub(pattern, " ", text)                                # replace with whitespace
    cleaned = re.sub(r"\s+", " ", cleaned).strip()                      # collapse whitespace and remove leading/trailing whitespace
    c = Counter(cleaned.split())                                        # word frequencies
    top_3 = c.most_common(3)                                            # top 3 as tuple
    return [x[0] for x in top_3]                                        # return as list (already sorted from c.most_common(3))