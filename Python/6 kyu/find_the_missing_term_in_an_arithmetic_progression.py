"""
An Arithmetic Progression is defined as one in which there is a constant difference between the consecutive terms of a given series of numbers. You are provided with consecutive elements of an Arithmetic Progression. There is however one hitch: exactly one term from the original series is missing from the set of numbers which have been given to you. The rest of the given series is the same as the original AP. Find the missing term.

You have to write a function that receives a list, list size will always be at least 3 numbers. The missing term will never be the first or last one.

Example
find_missing([1, 3, 5, 9, 11]) == 7
PS: This is a sample question of the facebook engineer challenge on interviewstreet. I found it quite fun to solve on paper using math, derive the algo that way. Have fun!

https://www.codewars.com/kata/52de553ebb55d1fca3000371/train/python
"""

def find_missing(sequence):
    delta = (sequence[-1] - sequence[0]) // len(sequence)   # missing term is never first or last,
                                                            # so you can subtract the last element from the first and floor divide
                                                            # by the length of the given sequence to find the constant difference
    for i, _ in enumerate(sequence):
        if sequence[i + 1] - sequence[i] != delta:          # find the two elements that don't match the constant, add the constant to this element
                                                            # to find the missing term
            return sequence[i] + delta