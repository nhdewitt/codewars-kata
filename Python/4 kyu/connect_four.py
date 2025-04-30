"""
Connect Four
Take a look at wiki description of Connect Four game:

Wiki Connect Four

The grid is 6 row by 7 columns, those being named from A to G.

You will receive a list of strings showing the order of the pieces which dropped in columns:

  pieces_position_list = ["A_Red",
                          "B_Yellow",
                          "A_Red",
                          "B_Yellow",
                          "A_Red",
                          "B_Yellow",
                          "G_Red",
                          "B_Yellow"]
The list may contain up to 42 moves and shows the order the players are playing.

The first player who connects four items of the same color is the winner.

You should return "Yellow", "Red" or "Draw" accordingly.

https://www.codewars.com/kata/56882731514ec3ec3d000009/train/python
"""

def who_is_winner(pieces_position_list):
    # initialize board
    board = {(i, k): None for i in range(1, 8) for k in range(1, 7)}

            
    for piece in pieces_position_list:
        col, color = piece.split("_")
        col = ord(col) - 64
        for row in range(1, 7):                  # drop piece
            if not board[(col, row)]:
                board[(col, row)] = color
                # check down
                if all(board.get((col, r)) == color for r in range(row, row - 4, -1)):
                    return color
                # check diagonally
                for k in range(-3, 1):
                    if all(board.get((col + k + i, row + k + i)) == color for i in range(4)):
                        return color
                    if all(board.get((col + k + i, row - k - i)) == color for i in range(4)):
                        return color
                # check across
                for i in range(col - 3, col + 1):
                    if all(board.get((i + c, row)) == color for c in range(4)):
                        return color
                break
                
    return "Draw"