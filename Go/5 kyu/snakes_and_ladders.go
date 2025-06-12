/*
Introduction
Snakes and Ladders is an ancient Indian board game regarded today as a worldwide classic. It is played between two or more players on a gameboard having numbered, gridded squares. A number of "ladders" and "snakes" are pictured on the board, each connecting two specific board squares. (Source Wikipedia)

Task
Your task is to make a simple class called SnakesLadders. The test cases will call the method play(die1, die2) independantly of the state of the game or the player turn. The variables die1 and die2 are the die thrown in a turn and are both integers between 1 and 6. The player will move the sum of die1 and die2.
The Board

Rules
1.  There are two players and both start off the board on square 0.

2.  Player 1 starts and alternates with player 2.

3.  You follow the numbers up the board in order 1=>100

4.  If the value of both die are the same then that player will have another go.

5.  Climb up ladders. The ladders on the game board allow you to move upwards and get ahead faster. If you land exactly on a square that shows an image of the bottom of a ladder, then you may move the player all the way up to the square at the top of the ladder. (even if you roll a double).

6.  Slide down snakes. Snakes move you back on the board because you have to slide down them. If you land exactly at the top of a snake, slide move the player all the way to the square at the bottom of the snake or chute. (even if you roll a double).

7.  Land exactly on the last square to win. The first person to reach the highest square on the board wins. But there's a twist! If you roll too high, your player "bounces" off the last square and moves back. You can only win by rolling the exact number needed to land on the last square. For example, if you are on square 98 and roll a five, move your game piece to 100 (two moves), then "bounce" back to 99, 98, 97 (three, four then five moves.)

8.  If the Player rolled a double and lands on the finish square “100” without any remaining moves then the Player wins the game and does not have to roll again.
Returns
Return Player n Wins!. Where n is winning player that has landed on square 100 without any remainding moves left.

Return Game over! if a player has won and another player tries to play.

Otherwise return Player n is on square x. Where n is the current player and x is the sqaure they are currently on.
Good luck and enjoy!

https://www.codewars.com/kata/587136ba2eefcb92a9000027/train/go
*/

package kata

import "fmt"

const (
  Player1 = 1
  Player2 = 2
  WinningSquare = 100
) // constants for Player1/Player2 to map board positions

var ladders = map[int]int{
  2: 38, 7: 14, 8: 31, 15: 26, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 78: 98, 87: 94, 
} // ladder space -> new square

var snakes  = map[int]int{
  16: 6, 46: 25, 49: 11, 62: 19, 64: 60, 74: 53, 89: 68, 92: 88, 95: 75, 99: 80,
} // snake space <- new square

// SnakesLadders - Stucture that game is played on
type SnakesLadders struct {
  playerPositions   map[int]int
  currentPlayer     int
  gameOver          bool
}

// NewGame - Method that starts a new game for the SnakesLadders struct
func (sl *SnakesLadders) NewGame() {
  sl.playerPositions = map[int]int{
    Player1: 0,
    Player2: 0,
  }
  sl.currentPlayer = Player1
  sl.gameOver = false
}

// Play - Method that makes turn givem a doce roll from die1 and die2 for the SnakesLadders struct
// Player that dice is for should automatically be determined based on rules
func (sl *SnakesLadders) Play(die1, die2 int) string {
  if sl.gameOver {
    return "Game over!"
  }
  
  roll := die1 + die2
  isDoubles := die1 == die2

  result := sl.movePlayer(roll)
  
  if !isDoubles && !sl.gameOver {
    sl.switchPlayer()
  }
  return result
}

// movePlayer - gets current position, calculates roll, checks if player is on winning square
func (sl *SnakesLadders) movePlayer(roll int) string {
  currentPos := sl.playerPositions[sl.currentPlayer]
  newPos := sl.calculateNewPosition(currentPos, roll)
  
  if newPos == WinningSquare {
    sl.gameOver = true
    sl.playerPositions[sl.currentPlayer] = WinningSquare
    return fmt.Sprintf("Player %d Wins!", sl.currentPlayer)
  }
  
  finalPos := sl.applySnakesAndLadders(newPos)
  sl.playerPositions[sl.currentPlayer] = finalPos
  
  return fmt.Sprintf("Player %d is on square %d", sl.currentPlayer, finalPos)
}

// calculateNewPosition - move player based on roll, checking to see if
// roll has overshot the winning square, in which case the player moves back
func (sl *SnakesLadders) calculateNewPosition(currentPos, roll int) int {
  newPos := currentPos + roll
  
  if newPos > WinningSquare {
    overshoot := newPos - WinningSquare
    return WinningSquare - overshoot
  }
  
  return newPos
}

// applySnakesAndLadders - check to see if the player has landed on a snake
// (in which case they move backwards) or a ladder (in which case they move
// forwards)
func (sl *SnakesLadders) applySnakesAndLadders(position int) int {
  if snakeEnd, hasSnake := snakes[position]; hasSnake {
    return snakeEnd
  }
  
  if ladderEnd, hasLadder := ladders[position]; hasLadder {
    return ladderEnd
  }
  
  return position
}

// switchPlayer - switch players - only runs if !gameOver and !isDoubles
func (sl *SnakesLadders) switchPlayer() {
  if sl.currentPlayer == Player1 {
    sl.currentPlayer = Player2
  } else {
    sl.currentPlayer = Player1
  }
}