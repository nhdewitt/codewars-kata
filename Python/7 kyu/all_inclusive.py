"""
Input:

a string strng
an array of strings arr
Output of function contain_all_rots(strng, arr) (or containAllRots or contain-all-rots):

a boolean true if all rotations of strng are included in arr
false otherwise
Examples:
contain_all_rots(
  "bsjq", ["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"]) -> true

contain_all_rots(
  "Ajylvpy", ["Ajylvpy", "ylvpyAj", "jylvpyA", "lvpyAjy", "pyAjylv", "vpyAjyl", "ipywee"]) -> false)
Note:
Though not correct in a mathematical sense

we will consider that there are no rotations of strng == ""
and for any array arr: contain_all_rots("", arr) --> true

https://www.codewars.com/kata/5700c9acc1555755be00027e/train/python
"""

def contain_all_rots(strng, arr):
    sorts = ["".join(sorted(a)) for a in arr]
    return len(strng) == sorts.count("".join(sorted(strng))) if strng[0:len(strng) // 2] != strng[len(strng) // 2:] else len(strng) // 2 == sorts.count("".join(sorted(strng)))