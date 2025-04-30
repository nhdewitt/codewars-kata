"""
Emotional Sort ( ︶︿︶)
You'll have to create a function that will return an array of emotions sorted. It has two parameters, the first parameter called will expect an array of emotions where an emotion will be one of the following:

:D -> Super Happy
:) -> Happy
:| -> Normal
:( -> Sad
T_T -> Super Sad
Example of the array:[ "T_T", ":D", ":|", ":)", ":(" ]

And the second parameter will expect a boolean. If this parameter is true then the order of the emotions will be descending (from Super Happy to Super Sad) if it's false then it will be ascending (from Super Sad to Super Happy)

Example if order is true with the above array: [ ":D", ":)", ":|", ":(", "T_T" ]

Super Happy -> Happy -> Normal -> Sad -> Super Sad
If order is false: [ "T_T", ":(", ":|", ":)", ":D" ]

Super Sad -> Sad -> Normal -> Happy -> Super Happy
Example:

array: [":D", ":|", ":)", ":(", ":D"]
order: true 
should return [ ":D", ":D", ":)", ":|", ":(" ]

array: [":D", ":|", ":)", ":(", ":D"]
order: false
should return [ ":(", ":|", ":)", ":D", ":D" ]
More in test cases!

Notes:

The array could be empty, in that case return the same empty array ¯\_( ツ )_/¯
All emotions will be valid
Enjoy! (づ｡◕‿‿◕｡)づ

https://www.codewars.com/kata/5a86073fb17101e453000258/train/python
"""

EMOT_TABLE = {
    ':D': 5,
    ':)': 4,
    ':|': 3,
    ':(': 2,
    'T_T': 1
}

def sort_emotions(arr, order):
    return sorted(arr, key=EMOT_TABLE.get, reverse=order)       # grab dict keys from list, sort by dict values, reverse=True/False based on order argument