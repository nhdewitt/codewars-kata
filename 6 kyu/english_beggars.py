"""
Born a misinterpretation of this kata, your task here is pretty simple: given an array of values and an amount of beggars, you are supposed to return an array with the sum of what each beggar brings home, assuming they all take regular turns, from the first to the last.

For example: [1,2,3,4,5] for 2 beggars will return a result of [9,6], as the first one takes [1,3,5], the second collects [2,4].

The same array with 3 beggars would have in turn have produced a better out come for the second beggar: [5,7,3], as they will respectively take [1,4], [2,5] and [3].

Also note that not all beggars have to take the same amount of "offers", meaning that the length of the array is not necessarily a multiple of n; length can be even shorter, in which case the last beggars will of course take nothing (0).

Note: in case you don't get why this kata is about English beggars, then you are not familiar on how religiously queues are taken in the kingdom ;)

Note 2: do not modify the input array.

https://www.codewars.com/kata/59590976838112bfea0000fa/train/python
"""

def beggars(values, n):
    if n == 0:
        return []
    if n == 1:
        return [sum(values)]
    if len(values) < n:
        take_home = []
        for i, v in enumerate(values):
            take_home.append(v)
        for i in range(n - len(values)):
            take_home.append(0)
        return take_home
    else:
        take_home = []
        for x in range(n):
            inner_list = []
            take_home.append(inner_list)
        print(take_home)
        j = 0
        while j < len(values) - 1:
            for i, v in enumerate(values):
                take_home[i % n].append(v)
                j += 1

    return [sum(inner) for inner in take_home]