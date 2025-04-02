"""
Complete the method that takes a sequence of objects with two keys each: country or state, and capital. Keys may be symbols or strings.

The method should return an array of sentences declaring the state or country and its capital.

Examples
[{'state': 'Maine', 'capital': 'Augusta'}] --> ["The capital of Maine is Augusta"]
[{'country' : 'Spain', 'capital' : 'Madrid'}] --> ["The capital of Spain is Madrid"]
[{"state" : 'Maine', 'capital': 'Augusta'}, {'country': 'Spain', "capital" : "Madrid"}] --> ["The capital of Maine is Augusta", "The capital of Spain is Madrid"]


https://www.codewars.com/kata/53573877d5493b4d6e00050c/train/python
"""

def capital(capitals):
    strings = []
    for capital in capitals:
        if "state" in capital.keys():
            strings.append(f"The capital of {capital['state']} is {capital['capital']}")
        else:
            strings.append(f"The capital of {capital['country']} is {capital['capital']}")
    
    return strings