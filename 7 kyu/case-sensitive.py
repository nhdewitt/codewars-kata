"""
Your task is very simple. Given an input string s, case_sensitive(s), check whether all letters are lowercase or not. Return True/False and a list of all the entries that are not lowercase in order of their appearance in s.

For example, case_sensitive('codewars') returns [True, []], but case_sensitive('codeWaRs') returns [False, ['W', 'R']].

Goodluck :)

https://www.codewars.com/kata/5a805631ba1bb55b0c0000b8/train/python
"""

def case_sensitive(s):
    return [s == "".join(s.lower()), [c for c in s if c.isupper()]]