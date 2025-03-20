"""
To participate in a prize draw each one gives his/her firstname.

Each letter of a firstname has a value which is its rank in the English alphabet. A and a have rank 1, B and b rank 2 and so on.

The length of the firstname is added to the sum of these ranks hence a number som.

An array of random weights is linked to the firstnames and each som is multiplied by its corresponding weight to get what they call a winning number.

Example:
names: "COLIN,AMANDBA,AMANDAB,CAROL,PauL,JOSEPH"
weights: [1, 4, 4, 5, 2, 1]

PauL -> som = length of firstname + 16 + 1 + 21 + 12 = 4 + 50 -> 54
The *weight* associated with PauL is 2 so PauL's *winning number* is 54 * 2 = 108.
Now one can sort the firstnames in decreasing order of the winning numbers. When two people have the same winning number sort them alphabetically by their firstnames.

Task:
parameters: st a string of firstnames, we an array of weights, n a rank

return: the firstname of the participant whose rank is n (ranks are numbered from 1)

Example:
names: "COLIN,AMANDBA,AMANDAB,CAROL,PauL,JOSEPH"
weights: [1, 4, 4, 5, 2, 1]
n: 4

The function should return: "PauL"
Notes:
The weight array is at least as long as the number of names, it may be longer.

If st is empty return "No participants".

If n is greater than the number of participants then return "Not enough participants".

See Examples Test Cases for more examples.

https://www.codewars.com/kata/5616868c81a0f281e500005c/train/python
"""

def name_sum(name):
    total = 0
    for n in name.lower():
        total += ord(n) - 96
    
    return total

def rank(st, we, n):
    if len(st) == 0:
        return "No participants"
    name_dict = {}
    winner = []
    names = st.lower().split(",")
    if n > len(names):
        return "Not enough participants"
    for i, name in enumerate(names):
        name_dict[name] = name_dict.get(n, 0) + (len(name) + name_sum(name)) * we[i]
    for k, v in name_dict.items():
        winner.append((k, v))
        
    return [name[0].capitalize() for name in sorted(winner, key=lambda item: (-item[1], item[0]))][n - 1]