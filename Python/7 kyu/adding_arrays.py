"""
Create a function that takes an array of letters, and combines them into words in a sentence.

The array will be formatted as so:

[
  ['J','L','L','M'],
  ['u','i','i','a'],
  ['s','v','f','n'],
  ['t','e','e','']
]
The function should combine all the 0th indexed letters of each sub-array to create the word Just, all the 1st indexed letters of each sub-array to create the word Live, etc.

If a word is shorter than the maximum length, the remaining positions in the sub-array will contain empty strings (e.g., the last element in the last sub-array).

Examples:

[
  ['J','L','L','M'],
  ['u','i','i','a'],
  ['s','v','f','n'],
  ['t','e','e','']
] // => "Just Live Life Man"

[ 
  [ 'T', 'M', 'i', 't', 'p', 'o', 't', 'c' ],
  [ 'h', 'i', 's', 'h', 'o', 'f', 'h', 'e' ],
  [ 'e', 't', '', 'e', 'w', '', 'e', 'l' ],
  [ '', 'o', '', '', 'e', '', '', 'l' ],
  [ '', 'c', '', '', 'r', '', '', '' ],
  [ '', 'h', '', '', 'h', '', '', '' ],
  [ '', 'o', '', '', 'o', '', '', '' ],
  [ '', 'n', '', '', 'u', '', '', '' ],
  [ '', 'd', '', '', 's', '', '', '' ],
  [ '', 'r', '', '', 'e', '', '', '' ],
  [ '', 'i', '', '', '', '', '', '' ],
  [ '', 'a', '', '', '', '', '', '' ]
] // => "The Mitochondria is the powerhouse of the cell"

https://www.codewars.com/kata/59778cb1b061e877c50000cc/train/python
"""

def arr_adder(arr):
    output = []
    for j in range(len(arr[0])):
        inner = []
        for i in range(len(arr)):
            inner.append(arr[i][j])
        output.append("".join(inner))
    return " ".join(output)