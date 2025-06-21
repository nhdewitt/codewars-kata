/*
MAQE Challenge - MAQE Bot
MAQE has built a robot called MAQE Bot which walks in 2-dimensional plane (X, Y coordinate). It can only turn left or right, and walk straight. It also knows of its current position (X, Y) as well as its direction (North, East, West and South). In order to command MAQE Bot to walk, it must be input with a walking command. The walking command can be represented with a string consisting of three alphabets R, L and W followed by a positive integer N to indicate the distance of how many positions it has to walk which can be explained as follows:

R: Turn 90 degree to the right of MAQE Bot (clockwise)
L: Turn 90 degree to the left of MAQE Bot (counterclockwise)
WN: Walk straight for N point(s) where N can be any positive integers. For example, W1 means walking straight for 1 point.
Initial Conditions:
MAQE Bot starts at the position (X, Y) of (0, 0).
MAQE Bot is facing up North.
Example:
The walking code of RW15RW1 means:

MAQE Bot starts at (0, 0) facing up North.
MAQE Bot turns right (facing East) and walk straight 15 positions.
MAQE Bot turns another right (now facing South) and walk straight 1 position.
Your task is to implement the function Move. Which accepts an argument as an input string of the walking code with directions and prints out the result of the last position (X, Y) of MAQE Bot and its last facing direction (North, East, West or South).

Note that the output is case-sensitive.

A sample of testing your function/API with the input of RW15RW1:

Move("RW15RW1") = "X= 15 Y= -1 Direction= South"
Sample of Test Data:
W5RW5RW2RW1R
RRW11RLLW19RRW12LW1
LLW100W50RW200W10
LLLLLW99RRRRRW88LLLRL
W55555RW555555W444444W1

I/O
Input is guaranteed to be valid this time for this version.
X and Y are guaranteed to fit within the int data type range without overflow.
Easy, right?

Enjoy it!

Cheers,

📝 Copyright reference to the primary source of the challenge design:
💡 https://maqe.github.io/maqe-bot.html

https://www.codewars.com/kata/676b24db88a34f2e69a08ad3/train/go
*/

package maqebot

import (
  "fmt"
  "strconv"
  "unicode"
)

type MAQEBot struct {
  X           int
  Y           int
  Direction   Direction
}

type Direction int

const (
  North Direction = iota
  East
  South
  West
)

func (d Direction) normalized() Direction {
  n := int(d) % 4
  if n < 0 {
    n += 4
  }
  return Direction(n)
}

func (d Direction) String() string {
  switch d.normalized() {
  case North:   return "North"
  case East:    return "East"
  case South:   return "South"
  case West:    return "West"
  }
  return ""
}

func (m *MAQEBot) Turn(direction string) {
  switch direction {
  case "R":
    m.Direction = (m.Direction + 1).normalized()
  case "L":
    m.Direction = (m.Direction - 1).normalized()
  }
}

func (m *MAQEBot) Walk(distance int) {
  switch m.Direction.normalized() {
  case North:
    m.Y += distance
  case East:
    m.X += distance
  case South:
    m.Y -= distance
  case West:
    m.X -= distance
  }
}

func Move(command string) string {
  mb := MAQEBot{
    X: 0,
    Y: 0,
    Direction: 0,
  }
  
  rs := []rune(command)
  
  for i := 0; i < len(rs); i++ {
    r := rs[i]
    switch {
    case r == 'R':
      mb.Turn("R")
    case r == 'L':
      mb.Turn("L")
    case r == 'W':
      j := i + 1
      for j < len(rs) && unicode.IsDigit(rs[j]) {
        j++
      }
      if j > i+1 {
        if distance, err := strconv.Atoi(string(rs[i+1:j])); err == nil {
          mb.Walk(distance)
          i = j - 1
        }
      }
      
    default:
      continue
    }
  }
  return fmt.Sprintf("X= %d Y= %d Direction= %s", mb.X, mb.Y, mb.Direction)
}