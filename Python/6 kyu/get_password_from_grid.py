"""
In this kata you are expected to recover a scattered password in a (m x n) grid (you'll be given directions of all password pieces in the array)

The array will contain pieces of the password to be recovered, you'll get directions on how to get all the the pieces, your initial position in the array will be the character "x".

Heres what the array looks like

[
  ["p", "x", "m"],
  ["a", "$", "$"],
  ["k", "i", "t"]
]
The given directions would consist of [left, right, up, down] and [leftT, rightT, upT, downT], the former would be used to move around the grid while the latter would be used when you have a password to that direction of you.( E.g if you are in a position and the move to make is leftT it means theres a password to the left of you, so take the value and move there)

So in the 2d array example above, you will be given the directions ["lefT", "downT", "rightT", "rightT"], making for the word "pa$$".

Remember you initial position is the character "x".

So you write the function getPassword(grid, directions) that uses the directions to get a password in the grid.

Another example.

grid = [
  ["a", "x", "c"],
  ["g", "l", "t"],
  ["o", "v", "e"]
];

directions = ["downT", "down", "leftT", "rightT", "rightT", "upT"]

getPassword(grid, directions) // => "lovet"
Once again, Your initial position is the character "x", so from the position of "x" you follow the directions given and get all pieces in the grid.


https://www.codewars.com/kata/58f6e7e455d7597dcc000045/train/python
"""

def get_password(grid, directions):
    password = []
    deltas = [(-1, 0), (1, 0), (0, -1), (0, 1)]     # U, D, L, R
    
    for row, i in enumerate(grid):
        for col, v in enumerate(grid[row]):
            if grid[row][col] == "x":
                x, y = row, col
                break
    
    for direction in directions:
        match direction:
            case d if d.startswith("up"):
                dx, dy = deltas[0]
            case d if d.startswith("down"):
                dx, dy = deltas[1]
            case d if d.startswith("left"):
                dx, dy = deltas[2]
            case d if d.startswith("right"):
                dx, dy = deltas[3]
        x += dx
        y += dy
        if direction.endswith("T"):
            password.append(grid[x][y])
    
    return "".join(password)